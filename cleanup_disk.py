import os
import shutil
import sys

def get_size(path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                total += os.path.getsize(fp)
            except:
                pass
    return total

def human_size(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} TB"

# Directories to clean up (adjust as needed)
temp_dirs = [
    os.path.join(os.path.expanduser("~"), "CascadeProjects/QuantumAI/deep_learning/checkpoints"),
    os.path.join(os.path.expanduser("~"), "CascadeProjects/QuantumAI/deep_learning/evolution_history"),
    os.path.join(os.path.expanduser("~"), "CascadeProjects/QuantumAI/brain_metrics"),
    os.path.join(os.path.expanduser("~"), "CascadeProjects/QuantumAI/brain_states"),
    os.path.join(os.path.expanduser("~"), "CascadeProjects/QuantumAI/agent_data")
]

# Check disk space
try:
    total, used, free = shutil.disk_usage("/")
    print(f"Total disk space: {human_size(total)}")
    print(f"Used disk space: {human_size(used)}")
    print(f"Free disk space: {human_size(free)}")
    print(f"Disk usage: {used / total:.1%}")
except:
    print("Could not get disk usage information")

# Report sizes before cleanup
print("\nDirectory sizes before cleanup:")
for directory in temp_dirs:
    if os.path.exists(directory):
        size = get_size(directory)
        print(f"{directory}: {human_size(size)}")
    else:
        print(f"{directory}: does not exist")

# Clean up directories
print("\nCleaning up directories...")
total_freed = 0
for directory in temp_dirs:
    if os.path.exists(directory):
        size_before = get_size(directory)
        try:
            # Remove all files in the directory but keep the directory itself
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            
            size_after = get_size(directory)
            freed = size_before - size_after
            total_freed += freed
            print(f"Cleaned {directory}: freed {human_size(freed)}")
        except Exception as e:
            print(f"Error cleaning {directory}: {e}")
    else:
        print(f"Skipped {directory}: does not exist")

print(f"\nTotal space freed: {human_size(total_freed)}")

# Check disk space after cleanup
try:
    total, used, free = shutil.disk_usage("/")
    print(f"Free disk space now: {human_size(free)}")
    print(f"Disk usage now: {used / total:.1%}")
except:
    print("Could not get disk usage information")

print("\nCleanup completed. You should now have enough space to restore your files.")
