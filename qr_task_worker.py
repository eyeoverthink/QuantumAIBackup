import cv2
from qreader import QReader
import json
import time
import sys
import io
from contextlib import redirect_stdout

# Initialize QReader (and the detector model it uses)
# This might download model weights on first run if not already cached.
print("Initializing QReader...")
try:
    qreader_instance = QReader()
    print("QReader initialized successfully.")
except Exception as e:
    print(f"Error initializing QReader: {e}")
    print("Please ensure all dependencies for qreader are installed correctly.")
    sys.exit(1)

processed_task_ids = set() # To avoid re-processing tasks seen multiple times
MAX_PROCESSED_IDS = 100 # Limit the size of the set

def execute_script_and_capture_output(script_content, task_inputs):
    """Executes the script in a controlled environment and captures its stdout."""
    output_capture = io.StringIO()
    try:
        # Prepare a restricted global scope if needed, for now, just task_inputs
        # For safety, __builtins__ can be restricted further in a real system
        exec_globals = {"task_inputs": task_inputs, "__builtins__": __builtins__}
        with redirect_stdout(output_capture):
            exec(script_content, exec_globals)
        script_output = output_capture.getvalue()
        return script_output, None # Output, No error
    except Exception as e:
        script_output = output_capture.getvalue()
        return script_output, e # Output (if any before error), Error object
    finally:
        output_capture.close()

def process_frame(frame):
    """Processes a single video frame to detect, decode, and execute QR code tasks."""
    try:
        decoded_texts = qreader_instance.decode(image=frame)

        if decoded_texts:
            for text_content in decoded_texts:
                if text_content is None: continue
                try:
                    task_data = json.loads(text_content)
                    task_id = task_data.get("task_id")

                    if task_id and task_id not in processed_task_ids:
                        print(f"\n[+] New task found: {task_id}")
                        script_to_execute = task_data.get("script")
                        task_inputs = task_data.get("input_data", {})

                        if not script_to_execute:
                            print(f"   Task {task_id}: No script found. Skipping.")
                            continue

                        print(f"   Executing script for task {task_id}...")
                        script_output, error = execute_script_and_capture_output(script_to_execute, task_inputs)
                        
                        print(f"--- Script Output (Task {task_id}) ---")
                        if script_output:
                            print(script_output.strip()) 
                        else:
                            print("(No output from script)")
                        print(f"--- End Script Output (Task {task_id}) ---")

                        if error:
                            print(f"   Error during script execution (Task {task_id}): {error}")
                        else:
                            print(f"   Task {task_id} executed successfully.")
                        
                        processed_task_ids.add(task_id)
                        if len(processed_task_ids) > MAX_PROCESSED_IDS:
                            processed_task_ids.pop() # Simple way to keep the set from growing indefinitely

                    elif task_id and task_id in processed_task_ids:
                        # This task has been seen and processed recently
                        pass 

                except json.JSONDecodeError:
                    # Not a task QR or malformed JSON. 
                    # print(f"QR content not valid JSON: {text_content[:60]}...") 
                    pass 
                except Exception as e:
                    print(f"Error processing decoded QR content: {e}")
    except Exception as e:
        # This catches errors from qreader_instance.decode or other frame processing logic
        # print(f"Error processing frame with QReader: {e}")
        pass

if __name__ == "__main__":
    print("QR Task Worker started (MacAlpha - with camera).")
    print("Point this machine's webcam at a QR code displayed by the Issuer (iMac).")
    
    cap = cv2.VideoCapture(0) # 0 is usually the default webcam
    if not cap.isOpened():
        print("CRITICAL ERROR: Could not open webcam. Please check camera permissions and drivers.")
        sys.exit(1)

    print("Webcam opened successfully. Scanning for QR codes...")
    print("Press 'q' in the OpenCV window (if shown) or Ctrl+C in terminal to quit.")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Can't receive frame (stream end?). Exiting ...")
                time.sleep(0.5)
                continue # Or break, depending on desired behavior

            process_frame(frame)

            # Optional: Display the camera feed for aiming/debugging
            # To enable, uncomment the next line. Ensure you have a GUI environment.
            # cv2.imshow('QR Task Worker - MacAlpha Camera Feed', frame)

            # Check for 'q' key press to quit (if cv2.imshow is used)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #    print("Quit signal received.")
            #    break
            
            time.sleep(0.1) # Polling interval for QR codes

    except KeyboardInterrupt:
        print("\nKeyboard interrupt received. Shutting down...")
    finally:
        print("Releasing webcam and cleaning up...")
        cap.release()
        cv2.destroyAllWindows() # Only if cv2.imshow was used
        print("Worker node stopped.")
