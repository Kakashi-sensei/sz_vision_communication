import zipfile
import os

# Specify the directory containing the zipped folders
zip_dir = 'C:\\Users\\timothy\\OneDrive\\Documents\\SZ_Scarpe_plan\\temp\\'  # Use double backslashes for Windows paths
# Specify the directory where you want to extract the contents
extract_dir = 'C:\\Users\\timothy\\OneDrive\\Documents\\SZ_Scarpe_plan\\temp\\'  # Use double backslashes for Windows paths

# Ensure the extract directory exists
os.makedirs(extract_dir, exist_ok=True)

# Check if the zip directory exists
if not os.path.exists(zip_dir):
    print(f"The directory {zip_dir} does not exist.")
else:
    # Loop through all files in the zip directory
    for filename in os.listdir(zip_dir):
        if filename.endswith('.zip'):
            try:
                # Construct full file path
                file_path = os.path.join(zip_dir, filename)
                # Create a ZipFile object
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    # Extract all the contents into the specified directory
                    zip_ref.extractall(extract_dir)
                    print(f'Extracted {filename}')
            except zipfile.BadZipFile:
                print(f'Error: {filename} is not a zip file or it is corrupted.')
            except Exception as e:
                print(f'Error extracting {filename}: {e}')

print('Extraction process completed.')
