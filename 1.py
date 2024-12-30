import os
import shutil
import sys

def clear_directory(directory):
    """Deletes all files and subdirectories inside the given directory."""
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
        print(f"All files in {directory} have been deleted.")
    except Exception as e:
        print(f"Error while deleting files: {e}")

def display_warning():
    """Display warnings before proceeding with the file deletion."""
    print("Warning: This application will delete files on your system.")
    print("It will delete all files in the specified directory, except for certain important system files.")
    print("Please make sure you have backups of important data.")
    response = input("Do you wish to proceed? Type 'YES' to continue: ").strip().upper()
    
    if response != 'YES':
        print("Operation aborted.")
        sys.exit(1)
    
    print("Warning: The files will be deleted permanently.")
    response = input("Are you absolutely sure? Type 'YES' to proceed: ").strip().upper()
    
    if response != 'YES':
        print("Operation aborted.")
        sys.exit(1)

def main():
    # WARNING: Make sure you only run this with directories that are intended to be cleaned up
    directory_to_clean = input("Enter the directory you want to clean up (e.g., C:/Users/YourName/Downloads): ").strip()
    
    # Display warnings
    display_warning()

    # Proceed to clear the directory
    if os.path.exists(directory_to_clean):
        clear_directory(directory_to_clean)
    else:
        print("The specified directory does not exist.")
        sys.exit(1)

if __name__ == "__main__":
    main()
