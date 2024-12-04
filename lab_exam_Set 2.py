import pandas as pd
import os

# Paths to the input and output files
input_file = r"C:\Users\kanik\OneDrive\Desktop\Exam\AQI_Data (1).csv"
output_file = r"C:\Users\kanik\OneDrive\Desktop\Exam\result.csv"

# Check if input file exists
if not os.path.exists(input_file):
    print(f"Error: Input file not found at {input_file}")
else:
    # Load the CSV file into a DataFrame
    data = pd.read_csv(input_file)

    # Display the column names for verification
    print("Columns in the dataset:", data.columns)

    # Rename columns
    data.rename(columns={
        'AQI': 'AIR Quality Index',
        'PM2.5': 'Particulate Matter 2.5',
        'PM10': 'Particulate Matter 10',
        'city': 'location'
    }, inplace=True)

    # Replace "unknown" with "not available" in the "location" column
    if 'location' in data.columns:
        data['location'] = data['location'].replace('unknown', 'not available')
    else:
        print("Warning: 'location' column not found in the dataset.")

    # Display the updated dataset
    print(data.head())

    # Save the updated DataFrame to a new CSV file
    try:
        data.to_csv(output_file, index=False)
        print(f"Updated dataset saved to: {output_file}")
    except Exception as e:
        print(f"Error while saving the output file: {e}")


