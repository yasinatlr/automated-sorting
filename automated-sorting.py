import os
import shutil

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def move_file(file_path, destination_directory):
    # Ensure destination directory exists
    ensure_directory_exists(destination_directory)
    shutil.move(file_path, destination_directory)

def assign_file_to_folder_based_on_extension(file_path, file_extension_mapping, default_folder, destination_directory):
    file_extension = os.path.splitext(file_path)[1].lower()
    destination_folder = file_extension_mapping.get(file_extension, default_folder)
    destination_path = os.path.join(destination_directory, destination_folder)
    print(f"Destination path: {destination_path}")
    move_file(file_path, destination_path)

def organize_files_into_folders(source_directory, destination_directory):
    file_extension_mapping = {
        ".pdf": "Documents", ".docx": "Documents", ".txt": "Documents", ".pptx": "Documents", ".xlsx": "Documents", ".csv": "Documents",
        ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images", ".bmp": "Images", ".tiff": "Images",
        ".mp4": "Videos", ".mov": "Videos", ".avi": "Videos", ".mkv": "Videos", ".flv": "Videos", ".wmv": "Videos",
        ".mp3": "Music", ".wav": "Music", ".aac": "Music", ".flac": "Music", ".ogg": "Music", ".wma": "Music",
        ".zip": "Archives", ".rar": "Archives", ".tar": "Archives", ".gz": "Archives", ".7z": "Archives"
    }
    folders_to_create = set(file_extension_mapping.values()) | {"Others"}

    if not os.path.exists(source_directory):
        print(f"Source directory {source_directory} not found.")
        return

    for folder in folders_to_create:
        ensure_directory_exists(os.path.join(destination_directory, folder))

    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)
        if os.path.isfile(file_path):
            try:
                assign_file_to_folder_based_on_extension(
                    file_path,
                    file_extension_mapping,
                    "Others",
                    destination_directory
                )
            except Exception as e:
                print(f"Error moving {filename}: {e}")

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"{os.path.basename(file_path)} has been deleted.")
    except Exception as e:
        print(f"Error deleting {os.path.basename(file_path)}: {e}")

def delete_all_files(files, folder_path):
    for file in files:
        file_path = os.path.join(folder_path, file)
        delete_file(file_path)
    print("All files have been deleted.")

def get_user_choice(file):
    print(f"File: {file}")
    return input("Do you want to delete this file? (yes/no/all): ").strip().lower()

def handle_file_deletion(file, folder_path):
    file_path = os.path.join(folder_path, file)
    delete_file(file_path)

def review_and_optionally_delete_files(folder_path):
    print(f"Reviewing files in {folder_path}")
    files = os.listdir(folder_path)
    if not files:
        print("No files to review.")
        return
    
    for file in files:
        user_choice = get_user_choice(file)
        if user_choice == "all":  # If user selects 'all' after some iterations
            delete_all_files(files, folder_path)
            break
        elif user_choice == "yes":
            handle_file_deletion(file, folder_path)
            files.remove(file)
        elif user_choice == "no":
            files.remove(file)

if __name__ == "__main__":
    # NOTE: Ensure that inputs are sanitized properly to avoid security risks.
    source_directory_path = input("Enter the source directory path: ").strip()
    destination_directory_path = input("Enter the destination directory path: ").strip()
    organize_files_into_folders(source_directory_path, destination_directory_path)
    print("Files have been organized.")

    others_folder_path = os.path.join(destination_directory_path, "Others")
    review_and_optionally_delete_files(others_folder_path)
