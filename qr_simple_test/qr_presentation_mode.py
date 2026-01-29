#!/usr/bin/env python3
"""
QR Presentation Mode - Create and navigate through QR code presentations
By Vaughn Scott

This script allows you to:
1. Create QR codes from Python files
2. Organize them into a presentation sequence
3. Navigate through them like slides
4. Execute each QR code when viewed

Uses the phi-harmonic principles and existing QR task worker.
"""

import os
import sys
import json
import time
import uuid
import argparse
import qrcode
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import cv2
import base64
import zlib
import subprocess
import threading

# Phi (Golden Ratio) constant for phi-harmonic timing
PHI = (1 + np.sqrt(5)) / 2  # Approximately 1.618034

class QRPresentationBuilder:
    """Build and navigate through QR code presentations."""
    
    def __init__(self):
        """Initialize the presentation builder."""
        self.presentation_slides = []
        self.current_slide_index = 0
        self.presentation_name = "Quantum_Phi_Presentation"
        self.output_dir = "qr_presentation_slides"
        self.worker_process = None
        
        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def compress_payload(self, payload):
        """Compress the payload using zlib and base64 encode it."""
        compressed = zlib.compress(payload.encode('utf-8'), 9)  # Max compression
        encoded = base64.b64encode(compressed).decode('utf-8')
        return f"COMPRESSED:{encoded}"
    
    def create_qr_from_file(self, file_path, slide_title=None):
        """Create a QR code from a Python file."""
        if not os.path.exists(file_path):
            print(f"Error: File {file_path} not found.")
            return None
        
        # Read the file
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Create a unique task ID
        task_id = str(uuid.uuid4())
        
        # Get the filename without path
        filename = os.path.basename(file_path)
        
        # Use the filename as slide title if none provided
        if not slide_title:
            slide_title = os.path.splitext(filename)[0]
        
        # Calculate phi-harmonic timing
        phi_time = (time.time() * PHI) % 1.0
        
        # Create task payload
        task_payload = {
            "task_id": task_id,
            "timestamp": time.time(),
            "script": content,
            "input_data": {
                "filename": filename,
                "phi_time": phi_time
            },
            "task_meta": {
                "type": "QR Presentation Slide",
                "title": slide_title,
                "phi_harmonic": phi_time,
                "visual_inversion": False,
                "intensity_profile": {
                    "resonance": 1.0 / (1.0 + abs(phi_time - 0.5)),
                    "complexity": 0.5 + 0.5 * phi_time
                }
            }
        }
        
        # Convert to JSON
        json_payload = json.dumps(task_payload)
        
        # Compress the payload
        compressed_payload = self.compress_payload(json_payload)
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=None,  # Auto-determine version
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(compressed_payload)
        qr.make(fit=True)
        
        # Create QR image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Create slide data
        slide_data = {
            "task_id": task_id,
            "title": slide_title,
            "filename": filename,
            "content": content,
            "phi_time": phi_time,
            "qr_image": img
        }
        
        return slide_data
    
    def add_slide(self, file_path, slide_title=None):
        """Add a slide to the presentation."""
        slide_data = self.create_qr_from_file(file_path, slide_title)
        if slide_data:
            self.presentation_slides.append(slide_data)
            print(f"Added slide: {slide_data['title']}")
            return True
        return False
    
    def save_current_slide(self):
        """Save the current slide as a QR code image."""
        if not self.presentation_slides:
            print("No slides in presentation.")
            return None
        
        slide = self.presentation_slides[self.current_slide_index]
        slide_number = str(self.current_slide_index + 1).zfill(3)
        output_path = os.path.join(self.output_dir, f"slide_{slide_number}_{slide['title']}.png")
        
        slide["qr_image"].save(output_path)
        print(f"Saved slide to {output_path}")
        return output_path
    
    def save_presentation(self):
        """Save all slides in the presentation."""
        if not self.presentation_slides:
            print("No slides in presentation.")
            return
        
        # Create presentation directory
        presentation_dir = os.path.join(self.output_dir, self.presentation_name)
        if not os.path.exists(presentation_dir):
            os.makedirs(presentation_dir)
        
        # Save each slide
        saved_paths = []
        for i, slide in enumerate(self.presentation_slides):
            slide_number = str(i + 1).zfill(3)
            output_path = os.path.join(presentation_dir, f"slide_{slide_number}_{slide['title']}.png")
            slide["qr_image"].save(output_path)
            saved_paths.append(output_path)
        
        # Create presentation metadata
        metadata = {
            "name": self.presentation_name,
            "created": time.time(),
            "phi_harmonic": (time.time() * PHI) % 1.0,
            "slides": [
                {
                    "number": i + 1,
                    "title": slide["title"],
                    "task_id": slide["task_id"],
                    "filename": slide["filename"],
                    "phi_time": slide["phi_time"]
                }
                for i, slide in enumerate(self.presentation_slides)
            ]
        }
        
        # Save metadata
        metadata_path = os.path.join(presentation_dir, "presentation_metadata.json")
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"Saved presentation '{self.presentation_name}' with {len(saved_paths)} slides to {presentation_dir}")
        return presentation_dir
    
    def start_qr_worker(self, qr_path):
        """Start the QR task worker to process the current slide."""
        # Kill any existing worker process
        if self.worker_process and self.worker_process.poll() is None:
            self.worker_process.terminate()
            time.sleep(0.5)
        
        # Start a new worker process
        cmd = [sys.executable, "qr_task_worker_from_file.py", "-f", qr_path]
        self.worker_process = subprocess.Popen(cmd)
    
    def run_gui(self):
        """Run the presentation builder GUI."""
        root = tk.Tk()
        root.title("QR Presentation Mode")
        root.geometry("800x600")
        
        # Main frame
        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title frame
        title_frame = tk.Frame(main_frame)
        title_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(title_frame, text="QR Presentation Mode", font=("Helvetica", 16)).pack(side=tk.LEFT)
        
        # Set presentation name
        def set_name():
            name = simpledialog.askstring("Presentation Name", "Enter presentation name:", 
                                          initialvalue=self.presentation_name)
            if name:
                self.presentation_name = name
                presentation_name_label.config(text=f"Presentation: {self.presentation_name}")
        
        tk.Button(title_frame, text="Set Name", command=set_name).pack(side=tk.RIGHT)
        presentation_name_label = tk.Label(title_frame, text=f"Presentation: {self.presentation_name}")
        presentation_name_label.pack(side=tk.RIGHT, padx=10)
        
        # QR display frame
        qr_frame = tk.Frame(main_frame, bd=2, relief=tk.SUNKEN)
        qr_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        qr_canvas = tk.Canvas(qr_frame, bg="white")
        qr_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Slide info frame
        info_frame = tk.Frame(main_frame)
        info_frame.pack(fill=tk.X, pady=5)
        
        slide_label = tk.Label(info_frame, text="No slides")
        slide_label.pack(side=tk.LEFT)
        
        # Navigation frame
        nav_frame = tk.Frame(main_frame)
        nav_frame.pack(fill=tk.X, pady=5)
        
        # Function to update the display
        def update_display():
            qr_canvas.delete("all")
            if not self.presentation_slides:
                slide_label.config(text="No slides")
                return
            
            slide = self.presentation_slides[self.current_slide_index]
            slide_label.config(text=f"Slide {self.current_slide_index + 1}/{len(self.presentation_slides)}: {slide['title']}")
            
            # Convert PIL Image to PhotoImage
            qr_img = slide["qr_image"]
            photo_img = ImageTk.PhotoImage(qr_img)
            
            # Store reference to prevent garbage collection
            qr_canvas.image = photo_img
            
            # Calculate position to center the image
            canvas_width = qr_canvas.winfo_width()
            canvas_height = qr_canvas.winfo_height()
            img_width, img_height = qr_img.size
            x = (canvas_width - img_width) // 2
            y = (canvas_height - img_height) // 2
            
            # Display the image
            qr_canvas.create_image(x, y, anchor=tk.NW, image=photo_img)
        
        # Function to navigate to previous slide
        def prev_slide():
            if not self.presentation_slides:
                return
            self.current_slide_index = (self.current_slide_index - 1) % len(self.presentation_slides)
            update_display()
        
        # Function to navigate to next slide
        def next_slide():
            if not self.presentation_slides:
                return
            self.current_slide_index = (self.current_slide_index + 1) % len(self.presentation_slides)
            update_display()
        
        # Function to add a slide
        def add_slide_dialog():
            file_path = filedialog.askopenfilename(
                title="Select Python File",
                filetypes=[("Python Files", "*.py"), ("All Files", "*.*")]
            )
            if file_path:
                title = simpledialog.askstring("Slide Title", "Enter slide title:",
                                              initialvalue=os.path.splitext(os.path.basename(file_path))[0])
                if self.add_slide(file_path, title):
                    self.current_slide_index = len(self.presentation_slides) - 1
                    update_display()
        
        # Function to execute the current slide
        def execute_slide():
            if not self.presentation_slides:
                messagebox.showinfo("No Slides", "No slides to execute.")
                return
            
            # Save the current slide
            qr_path = self.save_current_slide()
            if qr_path:
                # Start worker in a separate thread to avoid blocking the GUI
                threading.Thread(target=self.start_qr_worker, args=(qr_path,), daemon=True).start()
                messagebox.showinfo("Executing", f"Executing slide: {self.presentation_slides[self.current_slide_index]['title']}")
        
        # Function to save the presentation
        def save_presentation_dialog():
            if not self.presentation_slides:
                messagebox.showinfo("No Slides", "No slides to save.")
                return
            
            dir_path = self.save_presentation()
            if dir_path:
                messagebox.showinfo("Saved", f"Presentation saved to {dir_path}")
        
        # Navigation buttons
        tk.Button(nav_frame, text="Previous", command=prev_slide).pack(side=tk.LEFT, padx=5)
        tk.Button(nav_frame, text="Next", command=next_slide).pack(side=tk.LEFT, padx=5)
        tk.Button(nav_frame, text="Execute", command=execute_slide).pack(side=tk.LEFT, padx=5)
        tk.Button(nav_frame, text="Add Slide", command=add_slide_dialog).pack(side=tk.LEFT, padx=5)
        tk.Button(nav_frame, text="Save All", command=save_presentation_dialog).pack(side=tk.LEFT, padx=5)
        
        # Update display when canvas is resized
        def on_resize(event):
            update_display()
        
        qr_canvas.bind("<Configure>", on_resize)
        
        # Handle window close
        def on_closing():
            if self.worker_process and self.worker_process.poll() is None:
                self.worker_process.terminate()
            root.destroy()
        
        root.protocol("WM_DELETE_WINDOW", on_closing)
        
        # Start the GUI
        root.mainloop()

def main():
    """Main function to run the QR presentation builder."""
    parser = argparse.ArgumentParser(description="Create and navigate through QR code presentations.")
    parser.add_argument("--file", help="Python file to encode as a QR code")
    parser.add_argument("--title", help="Title for the slide")
    parser.add_argument("--gui", action="store_true", help="Launch the GUI")
    args = parser.parse_args()
    
    builder = QRPresentationBuilder()
    
    if args.file:
        builder.add_slide(args.file, args.title)
        builder.save_current_slide()
    
    if args.gui or not args.file:
        builder.run_gui()

if __name__ == "__main__":
    main()
