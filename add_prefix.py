import os
import sys

def add_prefix_to_files(folder_path, prefix):
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            new_name = f"{prefix}{filename}"
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
            print(f"Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python add_prefix.py <folder_path> <prefix>")
    else:
        folder_path = sys.argv[1]
        prefix = sys.argv[2]
        add_prefix_to_files(folder_path, prefix)
