import pandas as pd

# File paths
input_file_path = 'C:/Users/timothy/OneDrive/Documents/temp/CEO_personality_ratings.csv'
output_file_path = 'C:/Users/timothy/OneDrive/Documents/temp/checked_repeat.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file_path)

# Group by CEO_ID and filter groups where Durationinseconds has duplicates
duplicates = df[df.duplicated(['CEO_ID', 'Durationinseconds'], keep=False)]

# Save the results to a new CSV file
duplicates.to_csv(output_file_path, index=False)

print(f"Checked repeat cases saved to {output_file_path}")
