import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

response = requests.get('https://www.freetestapi.com/api/v1/cats')
print(response.status_code)
data=(response.json())

if isinstance(data, list) and data:
    # Get the column names
    headers = data[0].keys()
    # Get the column names
    rows = [item.values() for item in data]  
else:
    print(f"Unexpected data format {response.json()}")
    exit()
output_file = "output.csv"
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Get the column names
    writer.writerow(headers)  
    # Get the column names
    writer.writerows(rows)    
print(f"Data successfully saved to {output_file}")
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write the headers
    writer.writerows(rows)    # Write the rows

print(f"Data successfully saved to {output_file}")

# Step 1: Load the CSV file
csv_file = "output.csv"
df = pd.read_csv(csv_file)

# Step 2: Initial Exploration
print("First 5 rows of the data:")
print(df.head())

print("\nData Info:")
print(df.info()) 

print("\nSummary Statistics:")
print(df.describe())  
# Step 3: Handling Missing Values

print("\nMissing values per column:")
print(df.isnull().sum())  


# Step 4: Check for Duplicates
print("\nNumber of duplicate rows:", df.duplicated().sum())

# Step 5: Data Distribution (Visualization)


#Correlation heatmap
# Check for numeric columns
numeric_df = df.select_dtypes(include='number')

if not numeric_df.empty:
    # Compute correlation matrix
    correlation_matrix = numeric_df.corr()
    print("Correlation Matrix:")
    print(correlation_matrix)
    
    # Plot heatmap
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()
else:
    print("No numeric columns available for correlation heatmap.")

