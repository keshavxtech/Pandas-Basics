import pandas as pd

df = pd.read_csv("students.csv")

print("First 5 rows:")
print(df.head())

print("\nInfo:")
print(df.info())

print("\nStatistics:")
print(df.describe())

print("\nShape:", df.shape)
print("Columns:", df.columns)
