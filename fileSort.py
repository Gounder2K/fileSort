import os
import shutil
import time

desktop_path = os.path.expanduser("~/Desktop")

def organize_files():
    # Get a list of all files on the desktop
    files = [f for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f))]

    # Get the current time
    current_time = time.time()

    # Create folders for different file types
    for file in files:
        file_path = os.path.join(desktop_path, file)

        # Check the creation time of the file
        file_creation_time = os.path.getctime(file_path)

        # Check if 30 minutes have passed since the file was created
        if current_time - file_creation_time >= 1800:
            file_extension = file.split(".")[-1].lower()
            
            # Exclude hidden files (those starting with a dot)
            if file_extension and not file.startswith("."):
                folder_path = os.path.join(desktop_path, file_extension)

                # Check if the folder already exists, if not, create it
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Move the file to its corresponding folder
                shutil.move(file_path, os.path.join(folder_path, file))

if __name__ == "__main__":
    organize_files()
    print("Files on your desktop have been sorted.")