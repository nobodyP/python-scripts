import os
import sys

def rename_txt_to_lab(folder_path):
    try:
        # Check if the provided path is a directory
        if not os.path.isdir(folder_path):
            raise FileNotFoundError("The specified path is not a directory.")

        # Loop through all files in the directory
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # Check if the file is a .txt file
            if os.path.isfile(file_path) and filename.lower().endswith('.txt'):
                # Create the new file path with .lab extension
                new_file_path = os.path.join(folder_path, filename[:-4] + '.lab')

                # Rename the file
                os.rename(file_path, new_file_path)
                print(f'Renamed: {filename} to {filename[:-4]}.lab')

        print('Renaming completed successfully.')

    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == "__main__":
    # Check if a folder path is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
    else:
        folder_path = sys.argv[1]
        rename_txt_to_lab(folder_path)
