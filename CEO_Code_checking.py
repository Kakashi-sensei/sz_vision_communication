import pandas as pd

# File paths
input_file_path = r'C:\Users\timothy\OneDrive\Documents\temp\CEO_Code_Checking.csv'
output_file_path = r'C:\Users\timothy\OneDrive\Documents\temp\CEO_Code_Checking_output.csv'

# Read the input CSV file with a different encoding
df = pd.read_csv(input_file_path, encoding='latin1')

# Find CEO Names with multiple unique CEO Codes
incorrect_coding_cases = df.groupby('CEO Name')['CEO_Code'].nunique()
incorrect_coding_cases = incorrect_coding_cases[incorrect_coding_cases > 1].index

# Filter the original DataFrame to get the incorrect coding cases
incorrect_coding_df = df[df['CEO Name'].isin(incorrect_coding_cases)]

# Save the incorrect coding cases to a new CSV file
incorrect_coding_df.to_csv(output_file_path, index=False)

print(f"Incorrect coding cases have been saved to {output_file_path}")

