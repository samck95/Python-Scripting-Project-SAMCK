import os
import shutil

def copy_game_files(src_directory, dest_directory):
    # Check if the source directory exists
    if not os.path.exists(src_directory):
        print(f"Source directory '{src_directory}' does not exist.")
        return
    
    # Create the destination directory if it does not exist
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    # Walk through the source directory
    for root, dirs, files in os.walk(src_directory):
        for file in files:
            if file == 'game':
                # Construct the full file path
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_directory, file)
                
                # Copy the file to the destination directory
                shutil.copy(src_file_path, dest_file_path)
                print(f"Copied '{src_file_path}' to '{dest_file_path}'")

# Define the source and destination directories
src_directory = 'dev'
dest_directory = 'copied_games'

# Call the function to copy the files
copy_game_files(src_directory, dest_directory)

#

