import os
import shutil

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"]
}

def organize_folder(path):
    if not os.path.exists(path):
        print("❌ Folder does not exist")
        return

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            moved = False

            for folder, extensions in file_types.items():
                if ext in extensions:
                    folder_path = os.path.join(path, folder)

                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    shutil.move(file_path, os.path.join(folder_path, file))
                    print(f"Moved: {file} → {folder}")
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(path, "Others")
                if not os.path.exists(other_path):
                    os.makedirs(other_path)

                shutil.move(file_path, os.path.join(other_path, file))
                print(f"Moved: {file} → Others")

# Take user input
folder = input("Enter folder path: ")

organize_folder(folder)

print("✅ Files organized successfully!")