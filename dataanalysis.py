import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Book1.csv")
   

# Display the first 5 rows of the data
print(df.head())

# Describe the statistical data of numerical columns
print(df.describe())

# Find the sum of missing values
mv = df.isnull().sum()
print("Missing values in each column:\n", mv)

# Average of the 'Age' column
if "Age" in df.columns:
    avg = df["Age"].mean()
    print("Average of Age:", avg)
else:
    print("Column 'Age' not found in the dataset.")

# Count unique values in 'Age'
if "Age" in df.columns:
    uv = df["Age"].nunique()
    print(f"Unique values in Age: {uv}")

# Filter data where Department is Engineering
if "Department" in df.columns:
    eng_emp = df[df["Department"] == "Engineering"]
    print("Employees in Engineering Department:\n", eng_emp)

# Find employees with maximum and minimum salaries
if "Salary" in df.columns:
    max_salary = df["Salary"].max()
    max_salary_emp = df[df['Salary'] == max_salary]
    print("Employee(s) with maximum salary:\n", max_salary_emp)

    min_salary = df["Salary"].min()
    min_salary_emp = df[df['Salary'] == min_salary]
    print("Employee(s) with minimum salary:\n", min_salary_emp)

# Count frequency of each value in 'Department'
if "Department" in df.columns:
    dep_count = df["Department"].value_counts()
    print("Number of employees in each department:\n", dep_count)

# Sort employees by age
if "Age" in df.columns:
    sort = df.sort_values(by="Age", ascending=False)
    print("Employees sorted from senior to junior:\n", sort)

# Add a new column for experience level
if "Age" in df.columns:
    df["Experience"] = df["Age"].apply(lambda x: 'Senior' if x >= 30 else 'Junior')
    print("Data with 'Experience' column:\n", df)

# DATA VISUALIZATION
if "Department" in df.columns:
    # Pie chart for department distribution
    plt.figure(figsize=(8, 6))
    plt.pie(dep_count, labels=dep_count.index, autopct='%1.1f%%', startangle=140)
    plt.title("Department Distribution")
    plt.show()
else:
    print("Column 'Department' not found for visualization.")
