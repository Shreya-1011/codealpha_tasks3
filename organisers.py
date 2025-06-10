import os
import shutil

# Folder to organize
folder = "C:/Users/DELL/Downloads"

# File categories
types = {
    'Images': ['.png', '.jpg', '.jpeg'],
    'Docs': ['.pdf', '.docx', '.txt', '.pptx'],
    'Music': ['.mp3'],
    'Videos': ['.mp4'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Executables': ['.exe', '.msi', '.jar'],
    'Code': ['.py', '.cpp', '.java', '.js', '.html', '.css']
}

total_files = 0
moved_files = 0
already_organized = 0

# Organize files
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    print(f"Checking: {file}")

    if os.path.isdir(file_path):
        continue

    total_files += 1
    _, ext = os.path.splitext(file)
    ext = ext.lower()

    moved = False
    for category, ext_list in types.items():
        if ext in ext_list:
            category_path = os.path.join(folder, category)
            os.makedirs(category_path, exist_ok=True)
            shutil.move(file_path, os.path.join(category_path, file))
            print(f"Moved {file} to {category}")
            moved_files += 1
            moved = True
            break

    if not moved:
        others_path = os.path.join(folder, "Others")
        os.makedirs(others_path, exist_ok=True)
        shutil.move(file_path, os.path.join(others_path, file))
        print(f"Moved {file} to Others")
        moved_files += 1

print("\n--- Summary ---")
print(f"Total files checked: {total_files}")
print(f"Files moved: {moved_files}")
print(f"Already organized folders skipped.")
