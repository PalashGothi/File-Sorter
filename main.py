import os
import shutil

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def move_and_rename_file(src_path, dest_path, new_name):
    _, file_extension = os.path.splitext(src_path)
    dest_file_path = os.path.join(dest_path, new_name + file_extension)
    shutil.move(src_path, dest_file_path)

def sort_files(src_directory, dest_directory, name_format):
    file_types = {
        "documents": [".pdf", ".docx", ".txt"],
        "images": [".jpg", ".jpeg", ".png", ".gif"],
        "videos": [".mp4", ".avi", ".mov"],
        "music": [".mp3", ".wav"],
        "archives": [".zip", ".rar", ".tar", ".gz"],
        # Add more types as needed
    }
    
    create_directory(dest_directory)
    
    for file_type, extensions in file_types.items():
        type_directory = os.path.join(dest_directory, file_type)
        create_directory(type_directory)
        
        for filename in os.listdir(src_directory):
            file_path = os.path.join(src_directory, filename)
            if os.path.isfile(file_path):
                _, file_extension = os.path.splitext(filename)
                if file_extension.lower() in extensions:
                    new_name = name_format.format(
                        original_name=os.path.splitext(filename)[0],
                        file_type=file_type,
                        extension=file_extension.replace(".", "")
                    )
                    move_and_rename_file(file_path, type_directory, new_name)

if __name__ == "__main__":
    src_directory = input("Enter the source directory: ")
    dest_directory = input("Enter the destination directory: ")
    name_format = input("Enter the new naming format (use {original_name}, {file_type}, {extension}): ")

    sort_files(src_directory, dest_directory, name_format)
