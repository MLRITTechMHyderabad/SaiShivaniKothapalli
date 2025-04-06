import pandas as pd

data = {
    'Student': ['John', 'Sara', 'Mike', 'Anna', 'David', 'Emily', 'Chris', 'Sophia'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Marks': [85, 72, 90, 65, 78, 88, 92, 55],
    'Attendance': [92, 80, 95, 70, 85, 90, 97, 60]
}
df = pd.DataFrame(data)
print("Average Marks by Subject:")
print(df.groupby('Subject')['Marks'].mean(), "\n")
print("High Scorers with Low Attendance:")
print(df[(df['Marks'] > 85) & (df['Attendance'] < 90)][['Student', 'Marks', 'Attendance']], "\n")
def grade(m):
    if m >= 90: return 'A'
    elif m >= 80: return 'B'
    elif m >= 70: return 'C'
    else: return 'D'

df['Grade'] = df['Marks'].apply(grade)
print("Data with Grades:")
print(df[['Student', 'Marks', 'Grade']], "\n")
print("Grade Counts:")
print(df['Grade'].value_counts(), "\n")
print("Correlation between Marks and Attendance:")
print(df[['Marks', 'Attendance']].corr())
