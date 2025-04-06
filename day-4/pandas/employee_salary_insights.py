import pandas as pd
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah'],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT', 'HR'],
    'Age': [25, 32, 29, 41, 37, 45, 26, 38],
    'Salary': [50000, 70000, 65000, 80000, 75000, 90000, 62000, 85000],
    'Experience': [2, 7, 5, 15, 10, 20, 3, 12]
}
df = pd.DataFrame(data)
print("Average Salary by Department:")
print(df.groupby('Department')['Salary'].mean(), "\n")
print("Highest Paid Employee in Each Department:")
print(df.loc[df.groupby('Department')['Salary'].idxmax()][['Department', 'Employee', 'Salary']], "\n")
print("Experienced & Well-Paid Employees:")
print(df[(df['Experience'] > 5) & (df['Salary'] > 65000)][['Employee', 'Experience', 'Salary']])
