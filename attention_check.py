import pandas as pd
import os
import re

# Define the file path and the list of CSV files
file_path = 'C:/Users/timothy/OneDrive/Documents/temp/'
csv_files = [
    "Day_10_LVC_Afternoon_Survey_June_28_2024_23_12.csv", "Day_3_LVC_Midday_Survey_June_28_2024_22_58.csv",
    "Day_7_LVC_Evening_Survey_June_28_2024_23_08.csv", "Day_10_LVC_Evening_Survey_June_28_2024_23_13.csv",
    "Day_4_LVC_Afternoon_Survey_June_28_2024_23_01.csv", "Day_7_LVC_Midday_Survey_June_28_2024_23_08.csv",
    "Day_10_LVC_Midday_Survey_June_28_2024_23_13.csv", "Day_4_LVC_Evening_Survey_June_28_2024_23_02.csv",
    "Day_8_LVC_Afternoon_Survey_June_28_2024_23_09.csv", "Day_1_LVC_Afternoon_Survey_June_28_2024_22_53.csv",
    "Day_4_LVC_Midday_Survey_June_28_2024_23_02.csv", "Day_8_LVC_Evening_Survey_June_28_2024_22_02.csv",
    "Day_1_LVC_Evening_Survey_June_28_2024_22_54.csv", "Day_5_LVC_Afternoon_Survey_June_28_2024_23_03.csv",
    "Day_8_LVC_Evening_Survey_June_28_2024_23_10.csv", "Day_1_LVC_Midday_Survey_June_28_2024_21_59.csv",
    "Day_5_LVC_Evening_Survey_June_28_2024_23_04.csv", "Day_8_LVC_Midday_Survey_June_28_2024_23_10.csv",
    "Day_2_LVC_Afternoon_Survey_June_28_2024_22_56.csv", "Day_5_LVC_Midday_Survey_June_28_2024_23_04.csv",
    "Day_9_LVC_Afternoon_Survey_June_28_2024_23_11.csv", "Day_2_LVC_Evening_Survey_June_28_2024_22_57.csv",
    "Day_6_LVC_Afternoon_Survey_June_28_2024_23_05.csv", "Day_9_LVC_Evening_Survey_June_28_2024_23_11.csv",
    "Day_2_LVC_Midday_Survey_June_28_2024_22_56.csv", "Day_6_LVC_Evening_Survey_June_28_2024_23_05.csv",
    "Day_9_LVC_Midday_Survey_June_28_2024_23_12.csv", "Day_3_LVC_Afternoon_Survey_June_28_2024_22_59.csv",
    "Day_6_LVC_Midday_Survey_June_28_2024_23_06.csv", "Day_3_LVC_Evening_Survey_June_28_2024_22_59.csv",
    "Day_7_LVC_Afternoon_Survey_June_28_2024_23_07.csv"
]

# Define the keyword
keyword = "To ensure that you are paying attention"

# Function to check each CSV file
def check_csv_files(file_path, csv_files, keyword):
    incorrect_responses = []
    
    for csv_file in csv_files:
        full_path = os.path.join(file_path, csv_file)
        
        # Read the CSV file, skip the first and third rows, and use the second row as header
        df = pd.read_csv(full_path, skiprows=[0, 2])
        
        # Find the column with the keyword and extract the correct value
        keyword_column = None
        correct_value = None
        for column in df.columns:
            if keyword in column:
                keyword_column = column
                match = re.search(r'".*"', column)
                if match:
                    correct_value = match.group(0).strip('"').lower()
                break
        
        if keyword_column and correct_value:
            # Check each row for the correct value
            for index, row in df.iterrows():
                value = row[keyword_column]
                if not (isinstance(value, str) and value.strip('"').lower() == correct_value):
                    incorrect_responses.append({'Response ID': row['Response ID'], 'File Name': csv_file})
    
    return incorrect_responses

# Get the incorrect responses
incorrect_responses = check_csv_files(file_path, csv_files, keyword)

# Create a DataFrame for the incorrect responses
incorrect_responses_df = pd.DataFrame(incorrect_responses)

# Save the incorrect responses to a CSV file
output_file = os.path.join(file_path, 'incorrect_responses.csv')
incorrect_responses_df.to_csv(output_file, index=False)

print(f"Incorrect responses saved to {output_file}")
