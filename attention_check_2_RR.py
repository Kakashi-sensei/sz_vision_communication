import pandas as pd

# Define the file path and file name
file_path = 'C:/Users/timothy/OneDrive/Documents/temp/'
csv_file = 'Wrong_numbing.csv'

# Full path to the CSV file
full_path = file_path + csv_file

# Read the CSV file, skip the first and third rows, and use the second row as header
df = pd.read_csv(full_path, skiprows=[0, 2])

# Define the keywords to filter the columns
keywords = ["unique Prolific ID", "Please click strongly"]

# Filter the columns based on the keywords
filtered_columns = [col for col in df.columns if any(keyword in col for keyword in keywords)]

# Create a new DataFrame with the filtered columns
filtered_df = df[filtered_columns]

# Rename the columns based on the specified rules
new_column_names = {}
for col in filtered_df.columns:
    if "unique Prolific ID" in col:
        new_column_names[col] = "Prolific_ID"
    elif "Please click strongly" in col:
        new_column_names[col] = col.split("Please click")[1].strip()

# Rename the columns in the filtered DataFrame
filtered_df.rename(columns=new_column_names, inplace=True)

# Save the filtered DataFrame to a new CSV file
output_path = file_path + 'check.csv'
filtered_df.to_csv(output_path, index=False)

# Print a message confirming the save
print(f"Filtered columns saved to {output_path}")

