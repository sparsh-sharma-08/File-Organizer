import os
import shutil

# Define a dictionary to map file types to categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".webm", ".mpg", ".wmv"],
    "Documents": [".pdf", ".docx", ".xlsx", ".pptx", ".txt", ".csv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Programs": [".exe", ".apk", ".bat", ".sh", ".msi"],
}

def organize_files(directory):
    try:
        # List all files in the given directory
        all_files = os.listdir(directory)
        
        # Iterate through each file in the directory
        for file in all_files:
            # Get the full path of the file
            file_path = os.path.join(directory, file)
            
            # Skip directories
            if os.path.isdir(file_path):
                continue

            # Find the file extension and categorize
            file_extension = os.path.splitext(file)[1].lower()

            # Check each category and move files accordingly
            for category, extensions in file_types.items():
                if file_extension in extensions:
                    # Create the folder if it doesn't exist
                    folder_path = os.path.join(directory, category)
                    os.makedirs(folder_path, exist_ok=True)

                    # Move the file into the respective folder
                    shutil.move(file_path, os.path.join(folder_path, file))
                    print(f"Moved {file} to {category}")
                    break  # Stop once the file is moved

    except Exception as e:
        print(f"Error: {e}")

# Specify the directory you want to organize
directory_to_organize = "F:\Projects\File_organizer"  
organize_files(directory_to_organize)
