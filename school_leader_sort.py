import os
import glob
import re

# Set the folder path
folder_path = r"C:\Users\timothy\OneDrive\Documents\temp"

# Iterate over each file in the folder
for file_path in glob.glob(os.path.join(folder_path, "*.csv")):
    # Get the base name of the file (filename without the directory)
    base_name = os.path.basename(file_path)
    
    # Extract the "Day X" part (e.g., Day 5)
    day_match = re.search(r"Day\s(\d+)", base_name)
    if day_match:
        day_number = day_match.group(1)
    else:
        continue  # If no day is found, skip renaming this file
    
    # Extract "Leader Evening" or any other leader-related part
    leader_match = re.search(r"Leader\s(\w+)", base_name)
    if leader_match:
        leader_part = leader_match.group(1)
    else:
        continue  # Skip if no matching leader part is found
    
    # Construct the new name as Leader_Evening_D5.csv
    new_name = f"Leader_{leader_part}_D{day_number}.csv"
    
    # Construct the full path for the new file name
    new_file_path = os.path.join(folder_path, new_name)
    
    # If the file with the new name already exists, append a number to make it unique
    counter = 1
    while os.path.exists(new_file_path):
        new_file_path = os.path.join(folder_path, f"Leader_{leader_part}_D{day_number}_{counter}.csv")
        counter += 1
    
    # Rename the file
    os.rename(file_path, new_file_path)

print("Renaming complete.")

