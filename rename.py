import os

def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        new_filename = filename.replace('_csv', '.csv')
        if new_filename != filename:
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f'Renamed: {filename} -> {new_filename}')

# Directory path with the files to rename
directory_path = r'C:\Users\timothy\OneDrive\Documents\temp'
rename_files_in_directory(directory_path)
