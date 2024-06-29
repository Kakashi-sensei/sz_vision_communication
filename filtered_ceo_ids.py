import pandas as pd

# File paths
input_file_path = 'C:/Users/timothy/OneDrive/Documents/temp/CEO_personality_ratings.csv'
output_file_path = 'C:/Users/timothy/OneDrive/Documents/temp/filtered_ceo_ids.csv'

# List of CEO_IDs to check
ceo_id_list = [243014, 241110, 243003, 243004, 243005, 243011, 243012, 243013, 248090]

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file_path)

# Filter the DataFrame for rows where CEO_ID is in the specified list
filtered_df = df[df['CEO_ID'].isin(ceo_id_list)]

# Save the results to a new CSV file
filtered_df.to_csv(output_file_path, index=False)

print(f"Filtered cases saved to {output_file_path}")
