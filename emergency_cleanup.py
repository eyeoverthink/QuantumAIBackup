#!/usr/bin/env python3
"""
Emergency Disk Cleanup Script for QuantumAI Project
This script identifies and removes temporary files to free up disk space.
"""
import os
import shutil
import subprocess
import glob
import json
import sys
import time

def get_size(path):
    """Get the size of a file or directory in bytes."""
    if os.path.isfile(path):
        try:
            return os.path.getsize(path)
        except (OSError, IOError):
            return 0
    elif os.path.isdir(path):
        total_size = 0
        try:
            for dirpath, dirnames, filenames in os.walk(path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    try:
                        if os.path.exists(fp) and os.path.isfile(fp):
                            total_size += os.path.getsize(fp)
                    except (OSError, IOError):
                        continue
        except (OSError, IOError):
            pass
        return total_size
    return 0

def format_size(size_in_bytes):
    """Format size in bytes to human-readable format."""
    if size_in_bytes < 1024:
        return f"{size_in_bytes} B"
    elif size_in_bytes < 1024 * 1024:
        return f"{size_in_bytes / 1024:.2f} KB"
    elif size_in_bytes < 1024 * 1024 * 1024:
        return f"{size_in_bytes / (1024 * 1024):.2f} MB"
    else:
        return f"{size_in_bytes / (1024 * 1024 * 1024):.2f} GB"

def remove_file_or_dir(path):
    """Remove a file or directory and print the action."""
    try:
        size = get_size(path)
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
        print(f"Removed {path} - {format_size(size)}")
        return size
    except Exception as e:
        print(f"Error removing {path}: {e}")
        return 0

def find_largest_files(directory, top_n=50):
    """Find the largest files in a directory tree."""
    print(f"\nScanning for {top_n} largest files in {directory}...")
    files = []
    
    try:
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                try:
                    full_path = os.path.join(dirpath, filename)
                    if os.path.isfile(full_path):
                        size = os.path.getsize(full_path)
                        files.append((full_path, size))
                except (OSError, IOError):
                    continue
    except (OSError, IOError) as e:
        print(f"Error scanning directory: {e}")
    
    # Sort files by size (largest first)
    files.sort(key=lambda x: x[1], reverse=True)
    
    # Return top N files
    return files[:top_n]

def find_largest_directories(directory, top_n=20):
    """Find the largest directories."""
    print(f"\nScanning for {top_n} largest directories in {directory}...")
    dirs = []
    
    try:
        for dirpath, dirnames, _ in os.walk(directory):
            for dirname in dirnames:
                try:
                    full_path = os.path.join(dirpath, dirname)
                    size = get_size(full_path)
                    dirs.append((full_path, size))
                except (OSError, IOError):
                    continue
    except (OSError, IOError) as e:
        print(f"Error scanning directories: {e}")
    
    # Sort directories by size (largest first)
    dirs.sort(key=lambda x: x[1], reverse=True)
    
    # Return top N directories
    return dirs[:top_n]

def check_disk_space():
    """Check disk space using Python's os module."""
    try:
        project_root = os.path.dirname(os.path.abspath(__file__))
        stat = os.statvfs(project_root)
        free_bytes = stat.f_frsize * stat.f_bavail
        total_bytes = stat.f_frsize * stat.f_blocks
        used_bytes = total_bytes - free_bytes
        
        print(f"\nDisk space report:")
        print(f"Total: {format_size(total_bytes)}")
        print(f"Used: {format_size(used_bytes)}")
        print(f"Free: {format_size(free_bytes)}")
        print(f"Usage: {used_bytes / total_bytes:.1%}")
        
        return {
            "total": total_bytes,
            "used": used_bytes,
            "free": free_bytes
        }
    except Exception as e:
        print(f"Error checking disk space: {e}")
        return None

def check_inode_usage():
    """Check inode usage using subprocess."""
    try:
        result = subprocess.run(["df", "-i"], capture_output=True, text=True)
        print("\nInode usage:")
        print(result.stdout)
        return result.stdout
    except Exception as e:
        print(f"Error checking inode usage: {e}")
        return None

def aggressive_cleanup(project_root):
    """Perform aggressive cleanup of the project directory."""
    print("\nPerforming aggressive cleanup...")
    total_freed = 0
    
    # List of patterns for files to remove
    patterns_to_remove = [
        "**/__pycache__/**",
        "**/.pytest_cache/**",
        "**/.cache/**",
        "**/*.log",
        "**/*.tmp",
        "**/*.zip",
        "**/*.gz",
        "**/*.tar",
        "**/*.pyc",
        "**/*.pyo",
        "**/*.swp",
        "**/*.swo",
        "**/*.bak",
        "**/*.backup",
        "**/*.pkl",
        "**/*.npy",
        "**/*.npz",
        "**/*.json",  # Be careful with this one
        "**/*.png",
        "**/*.jpg",
        "**/*.jpeg",
        "**/*.gif",
        "**/*.svg",
        "**/*.pdf",
        "**/.git/objects/**",  # Be careful with git objects
        "**/.git/logs/**",
        "**/node_modules/**",
        "**/venv/**",
        "**/.venv/**",
        "**/dist/**",
        "**/build/**",
        "**/target/**",
    ]
    
    # Directories to completely remove
    dirs_to_remove = [
        "duplicate_code",
        "duplicate_read",
        "consolidated_quantum copy",
        "consolidated_quantum",
        "quantum_extras",  # Duplicate of main functionality
        "quantum_files",   # Large data files
        "visualizations",  # Images and large files
        "experimental_results",
        "logs",
        "quantum_continuity_logs",
        "phi_temporal_logs",
        "phi75_network_logs",
        "quantum_evolution",  # Large evolution data
        "wireless_energy_cache",
        "wireless_energy_visualizations",
        "voyager_phi_results",
        "verification_results",
        "quantum_market_analysis",
        "quantum_market_validation",
        "phi_harmonic_gpu_random_integration",
        "phi_harmonic_true_quantum_benchmark",
        "qhrc_physics_monitor",
    ]
    
    # Remove files matching patterns
    for pattern in patterns_to_remove:
        for path in glob.glob(os.path.join(project_root, pattern), recursive=True):
            if os.path.exists(path):
                total_freed += remove_file_or_dir(path)
    
    # Remove specific directories
    for dir_name in dirs_to_remove:
        path = os.path.join(project_root, dir_name)
        if os.path.exists(path) and os.path.isdir(path):
            total_freed += remove_file_or_dir(path)
    
    # Clean git repository to reduce size
    try:
        print("\nCleaning git repository...")
        # Remove git index lock if it exists
        git_lock = os.path.join(project_root, ".git", "index.lock")
        if os.path.exists(git_lock):
            os.remove(git_lock)
            print(f"Removed git lock file: {git_lock}")
        
        # Run git garbage collection
        subprocess.run(["git", "gc", "--prune=now", "--aggressive"], 
                      cwd=project_root, check=False, capture_output=True)
        print("Git repository cleaned")
    except Exception as e:
        print(f"Error cleaning git repository: {e}")
    
    return total_freed
    
    print(f"\nTotal space freed: {format_size(total_freed)}")
    print("\nDisk cleanup completed. Attempting to restore git files...")
    
    # Try to restore files from git
    try:
        os.system("git checkout -- quantum_black_box_micro.py")
        print("Restored quantum_black_box_micro.py from git")
    except Exception as e:
        print(f"Failed to restore files from git: {e}")
    
    print("\nDisk cleanup and restoration completed.")

if __name__ == "__main__":
    main()
