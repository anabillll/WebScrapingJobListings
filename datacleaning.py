import pandas as pd
import re
import os

# Define the file paths
raw_file_path = 'E:/Job Listings Project/glassdoor_job_listings.xlsx'
cleaned_file_path = 'E:/Job Listings Project/glassdoor_job_listings_cleaned.xlsx'

# Create directories if they do not exist
os.makedirs(os.path.dirname(cleaned_file_path), exist_ok=True)

# Load the raw data
df = pd.read_excel(raw_file_path)

# Step 1: Remove newline characters from the 'Company' column
df['Company'] = df['Company'].str.replace('\n', ' ')

# Step 2: Extract ratings from the 'Company' column and create a new 'Rating' column
df['Rating'] = df['Company'].str.extract(r'(\d\.\d)', expand=False)
df['Company'] = df['Company'].str.replace(r'\s*\d\.\d\s*', '', regex=True)

# Step 3: Standardize the 'Salary' column
def parse_salary(salary):
    if pd.isna(salary):
        return None
    salary = salary.replace(',', '')
    if 'Per hour' in salary:
        match = re.search(r'(\d+(?:\.\d+)?)', salary)
        if match:
            return float(match.group(1)) * 40 * 52
    elif 'Per year' in salary or 'Employer Est.' in salary or 'Glassdoor Est.' in salary:
        match = re.findall(r'\d+(?:\.\d+)?', salary)
        if match:
            return sum([float(x) for x in match]) / len(match)
    return None

df['Salary'] = df['Salary'].apply(parse_salary)

# Step 4: Handle missing or 'N/A' values
df.fillna({'Title': 'N/A', 'Company': 'N/A', 'Location': 'N/A', 'Salary': 0, 'Rating': 0}, inplace=True)

# Save the cleaned data to a new Excel file
df.to_excel(cleaned_file_path, index=False)

print("Data cleaning complete. Cleaned data saved to:", cleaned_file_path)
