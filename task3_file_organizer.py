
# task3_file_organizer.py
import os
import shutil

def organize_directory(target_dir):
    """Sorts files in the given directory into subfolders based on extension."""
    
    # Dictionary mapping folder names to their allowed file extensions
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.csv'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Audio': ['.mp3', '.wav'],
        'Archives': ['.zip', '.rar', '.tar']
    }

    # Check if the user-provided directory actually exists
    if not os.path.exists(target_dir):
        print(f"\n❌ Error: The directory '{target_dir}' does not exist.")
        return

    print(f"\n📂 Scanning directory: {target_dir}\n")
    print("-" * 40)

    files_moved = 0

    # Loop through every item in the directory
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)

        # Skip if it is already a folder; we only want to move files
        if os.path.isdir(file_path):
            continue

        # Extract the file extension (e.g., '.jpg') and make it lowercase
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # Variable to track if we found a match in our dictionary
        moved = False

        # Check which category the file belongs to
        for folder_name, extensions_list in file_types.items():
            if extension in extensions_list:
                # Create the category folder if it doesn't exist yet
                folder_path = os.path.join(target_dir, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Move the file into the category folder
                new_file_path = os.path.join(folder_path, filename)
                shutil.move(file_path, new_file_path)
                print(f"✅ Moved: {filename}  -->  {folder_name}/")
                moved = True
                files_moved += 1
                break

        # If the file extension wasn't in our list, put it in an 'Others' folder
        if not moved and extension != "":
            folder_path = os.path.join(target_dir, 'Others')
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            new_file_path = os.path.join(folder_path, filename)
            shutil.move(file_path, new_file_path)
            print(f"✅ Moved: {filename}  -->  Others/")
            files_moved += 1

    print("-" * 40)
    print(f"🎉 Organization Complete! Successfully moved {files_moved} files.")

if __name__ == "__main__":
    print("=" * 40)
    print("🤖 SMART FILE ORGANIZER")
    print("=" * 40)
    
    # Take input from the user
    folder_to_organize = input("Enter the full path of the folder to organize:\n> ")
    
    # Run the function
    organize_directory(folder_to_organize)
