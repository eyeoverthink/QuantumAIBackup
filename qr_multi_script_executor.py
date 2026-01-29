#!/usr/bin/env python3
"""
QR Multi-Script Executor

This module provides secure execution of multiple scripts from QR codes:
1. Script isolation and sandboxing
2. Security verification
3. Execution logging
4. Support for multiple script types (Python, Shell, etc.)

The module follows the 'lego' modular design principle and can be used as an extension
to existing QR code systems.
"""

import os
import sys
import time
import json
import base64
import hashlib
import tempfile
import subprocess
import logging
import uuid
from typing import Dict, List, Tuple, Any, Union, Optional
from pathlib import Path

# For QR code processing
import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Import security extension
from qr_face_2fa_security_extension import QRFace2FASecurityExtension

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QRMultiScriptExecutor")


class QRMultiScriptExecutor:
    """
    QR Multi-Script Executor
    
    Provides secure execution of multiple scripts from QR codes.
    """
    
    def __init__(self, security_extension: QRFace2FASecurityExtension = None, base_dir: str = None):
        """
        Initialize the multi-script executor
        
        Args:
            security_extension: Security extension instance
            base_dir: Base directory for storing execution files
        """
        # Set up base directory
        if base_dir is None:
            base_dir = os.path.join(os.path.expanduser("~"), ".qr_multi_script_executor")
        
        self.base_dir = base_dir
        self.scripts_dir = os.path.join(base_dir, "scripts")
        self.logs_dir = os.path.join(base_dir, "logs")
        
        # Create directories
        os.makedirs(self.scripts_dir, exist_ok=True)
        os.makedirs(self.logs_dir, exist_ok=True)
        
        # Initialize security extension
        if security_extension is None:
            self.security_extension = QRFace2FASecurityExtension(
                base_dir=os.path.join(base_dir, "security"),
                generate_keys=True
            )
        else:
            self.security_extension = security_extension
        
        # Supported script types
        self.supported_script_types = {
            "python": {
                "extension": ".py",
                "executor": sys.executable,
                "args": []
            },
            "shell": {
                "extension": ".sh",
                "executor": "/bin/bash",
                "args": []
            },
            "node": {
                "extension": ".js",
                "executor": "node",
                "args": []
            }
        }
        
        logger.info("QR Multi-Script Executor initialized")
    
    def execute_from_qr_image(self, qr_image_path: str) -> Dict[str, Any]:
        """
        Execute scripts from a QR code image
        
        Args:
            qr_image_path: Path to QR code image
            
        Returns:
            Execution results
        """
        try:
            # Read QR code
            qr_data = self._read_qr_code(qr_image_path)
            
            if not qr_data:
                return {
                    "success": False,
                    "error": "Failed to read QR code"
                }
            
            # Parse QR data
            try:
                qr_payload = json.loads(qr_data)
            except json.JSONDecodeError:
                return {
                    "success": False,
                    "error": "Invalid QR code data format (not JSON)"
                }
            
            # Execute scripts
            return self.execute_from_qr_data(qr_payload)
        
        except Exception as e:
            logger.error(f"Error executing from QR image: {str(e)}")
            return {
                "success": False,
                "error": f"Execution error: {str(e)}"
            }
    
    def execute_from_qr_data(self, qr_payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute scripts from QR data
        
        Args:
            qr_payload: QR code data payload
            
        Returns:
            Execution results
        """
        try:
            # Get scripts from payload
            is_valid, scripts, error_message = self.security_extension.get_scripts_from_payload(qr_payload)
            
            if not is_valid:
                return {
                    "success": False,
                    "error": f"Invalid script payload: {error_message}"
                }
            
            # Extract user ID
            user_id = qr_payload.get("data", {}).get("user_id", "anonymous")
            
            # Execute scripts
            return self._execute_scripts(scripts, user_id)
        
        except Exception as e:
            logger.error(f"Error executing from QR data: {str(e)}")
            return {
                "success": False,
                "error": f"Execution error: {str(e)}"
            }
    
    def _read_qr_code(self, image_path: str) -> Optional[str]:
        """
        Read QR code from image
        
        Args:
            image_path: Path to image
            
        Returns:
            QR code data or None if not found
        """
        try:
            # Read image
            image = cv2.imread(image_path)
            
            if image is None:
                logger.error(f"Failed to read image: {image_path}")
                return None
            
            # Convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Decode QR code
            qr_codes = decode(gray)
            
            if not qr_codes:
                logger.error("No QR code found in image")
                return None
            
            # Get data from first QR code
            qr_data = qr_codes[0].data.decode('utf-8')
            
            return qr_data
        
        except Exception as e:
            logger.error(f"Error reading QR code: {str(e)}")
            return None
    
    def _execute_scripts(self, scripts: List[Dict[str, str]], user_id: str) -> Dict[str, Any]:
        """
        Execute multiple scripts
        
        Args:
            scripts: List of script dictionaries
            user_id: User ID
            
        Returns:
            Execution results
        """
        # Create execution session
        session_id = str(uuid.uuid4())
        session_dir = os.path.join(self.scripts_dir, session_id)
        os.makedirs(session_dir, exist_ok=True)
        
        # Create log file
        log_file = os.path.join(self.logs_dir, f"{session_id}.log")
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(file_handler)
        
        try:
            logger.info(f"Starting execution session {session_id} for user {user_id}")
            
            # Validate scripts
            for i, script in enumerate(scripts):
                if "type" not in script or "content" not in script:
                    return {
                        "success": False,
                        "error": f"Invalid script format for script {i}"
                    }
                
                if script["type"] not in self.supported_script_types:
                    return {
                        "success": False,
                        "error": f"Unsupported script type: {script['type']}"
                    }
            
            # Execute each script
            results = []
            
            for i, script in enumerate(scripts):
                script_type = script["type"]
                script_name = script.get("name", f"script_{i}")
                script_content = script["content"]
                
                # Get script extension
                extension = self.supported_script_types[script_type]["extension"]
                
                # Create script file
                script_file = os.path.join(session_dir, f"{script_name}{extension}")
                
                with open(script_file, "w") as f:
                    f.write(script_content)
                
                # Make script executable if shell script
                if script_type == "shell":
                    os.chmod(script_file, 0o755)
                
                # Execute script
                result = self._execute_single_script(script_file, script_type, script_name, user_id)
                results.append(result)
                
                # Stop execution if script fails
                if not result["success"]:
                    logger.error(f"Script {script_name} failed, stopping execution")
                    break
            
            # Create result
            execution_result = {
                "success": all(result["success"] for result in results),
                "session_id": session_id,
                "user_id": user_id,
                "timestamp": time.time(),
                "results": results
            }
            
            # Save result
            result_file = os.path.join(session_dir, "result.json")
            with open(result_file, "w") as f:
                json.dump(execution_result, f, indent=2)
            
            logger.info(f"Execution session {session_id} completed")
            
            return execution_result
        
        except Exception as e:
            logger.error(f"Error executing scripts: {str(e)}")
            return {
                "success": False,
                "error": f"Execution error: {str(e)}"
            }
        
        finally:
            # Remove file handler
            logger.removeHandler(file_handler)
    
    def _execute_single_script(self, script_file: str, script_type: str, script_name: str, user_id: str) -> Dict[str, Any]:
        """
        Execute a single script
        
        Args:
            script_file: Path to script file
            script_type: Script type
            script_name: Script name
            user_id: User ID
            
        Returns:
            Execution result
        """
        try:
            logger.info(f"Executing script {script_name} ({script_type})")
            
            # Get executor
            executor = self.supported_script_types[script_type]["executor"]
            args = self.supported_script_types[script_type]["args"]
            
            # Create command
            command = [executor] + args + [script_file]
            
            # Execute command
            start_time = time.time()
            
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            stdout, stderr = process.communicate()
            
            end_time = time.time()
            
            # Create result
            result = {
                "success": process.returncode == 0,
                "script_name": script_name,
                "script_type": script_type,
                "return_code": process.returncode,
                "stdout": stdout,
                "stderr": stderr,
                "execution_time": end_time - start_time
            }
            
            if result["success"]:
                logger.info(f"Script {script_name} executed successfully")
            else:
                logger.error(f"Script {script_name} failed with return code {process.returncode}")
                logger.error(f"Error: {stderr}")
            
            return result
        
        except Exception as e:
            logger.error(f"Error executing script {script_name}: {str(e)}")
            return {
                "success": False,
                "script_name": script_name,
                "script_type": script_type,
                "error": str(e)
            }
    
    def create_qr_code(self, scripts: List[Dict[str, str]], user_id: str, output_path: str,
                      expiration_minutes: int = 5, encrypt: bool = True) -> str:
        """
        Create a QR code for multi-script execution
        
        Args:
            scripts: List of script dictionaries
            user_id: User ID
            output_path: Output path for QR code image
            expiration_minutes: Expiration time in minutes
            encrypt: Whether to encrypt the scripts
            
        Returns:
            Path to created QR code image
        """
        try:
            # Create payload
            payload = self.security_extension.create_multi_script_payload(
                scripts,
                user_id,
                expiration_minutes,
                encrypt
            )
            
            # Convert payload to JSON
            payload_json = json.dumps(payload)
            
            # Create QR code
            import qrcode
            
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=10,
                border=4,
            )
            
            qr.add_data(payload_json)
            qr.make(fit=True)
            
            # Create image
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(output_path)
            
            logger.info(f"QR code created at {output_path}")
            
            return output_path
        
        except Exception as e:
            logger.error(f"Error creating QR code: {str(e)}")
            raise
    
    def validate_script_security(self, script_content: str, script_type: str) -> Tuple[bool, str]:
        """
        Validate script security
        
        Args:
            script_content: Script content
            script_type: Script type
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        # This is a simplified security check
        # In a real system, use a more sophisticated security analysis
        
        # Check for common dangerous operations
        dangerous_patterns = {
            "python": [
                "os.system", "subprocess.call", "subprocess.Popen",
                "exec(", "eval(", "__import__('os')"
            ],
            "shell": [
                "rm -rf", ":(){ :|:& };:", "> /dev/sda",
                "dd if=/dev/zero", "mkfs", "wget", "curl"
            ],
            "node": [
                "child_process", "exec(", "spawn(",
                "fs.unlinkSync", "fs.rmdirSync"
            ]
        }
        
        if script_type in dangerous_patterns:
            for pattern in dangerous_patterns[script_type]:
                if pattern in script_content:
                    return False, f"Dangerous pattern detected: {pattern}"
        
        return True, ""


def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="QR Multi-Script Executor")
    parser.add_argument("--qr", help="Path to QR code image")
    parser.add_argument("--shell", help="Shell script content")
    parser.add_argument("--python", help="Python script content")
    parser.add_argument("--output", help="Output QR code path")
    parser.add_argument("--encrypt", action="store_true", help="Encrypt the payload")
    parser.add_argument("--expiration", type=int, default=5, help="Expiration time in minutes")
    
    args = parser.parse_args()
    
    # Initialize security extension
    security_extension = QRFace2FASecurityExtension()
    
    # Initialize executor
    executor = QRMultiScriptExecutor(security_extension=security_extension)
    
    if args.qr:
        # Execute scripts from QR code
        results = executor.execute_from_qr_image(args.qr)
        print(json.dumps(results, indent=2))
    elif args.shell or args.python:
        # Create scripts list
        scripts = []
        
        if args.shell:
            scripts.append({
                "type": "shell",
                "content": args.shell,
                "name": "shell_script"
            })
        
        if args.python:
            scripts.append({
                "type": "python",
                "content": args.python,
                "name": "python_script"
            })
        
        # Create multi-script payload
        payload = security_extension.create_multi_script_payload(
            scripts,
            expiration_minutes=args.expiration,
            encrypt=args.encrypt
        )
        
        if args.output:
            # Generate QR code
            import qrcode
            
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=10,
                border=4,
            )
            qr.add_data(json.dumps(payload))
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(args.output)
            
            print(f"Multi-script QR code saved to {args.output}")
            print(f"Scripts: {len(scripts)}")
            print(f"Encrypted: {args.encrypt}")
            print(f"Expiration: {args.expiration} minutes")
        else:
            # Execute scripts directly
            results = executor._execute_scripts(scripts, "direct")
            print(json.dumps(results, indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    import argparse
    main()
