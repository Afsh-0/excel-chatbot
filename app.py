#to read and analyze excel 
import pandas as pd

file_path = "data/Humanitarian_Data.xlsx"

excel_file = pd.ExcelFile(file_path)

print(excel_file.sheet_names)

"""after this if we run python app.py in terminal, we will see names of all sheet"""

#to read excel sheets
population = pd.read_excel(file_path, sheet_name="Population")

print("\nPopulation data:")
print(population.head())
print("\nColumns:")  #to explore all columns
print(population.columns.tolist())

calculations = {
    "sum": "sum",
    "total": "sum",
    "average": "mean",
    "avg": "mean",
    "mean": "mean",
    "maximum": "max",
    "max": "max",
    "highest": "max",
    "minimum": "min",
    "min": "min",
    "lowest": "min",
    "count": "count"
}

question = input("\nAsk a question: ").lower()

selected_column = None

for column in population.columns:
    if column.lower() in question:
        selected_column = column
        break

print("Selected column:", selected_column)

#calculation
"""total_refugees = population["Refugees"].sum()

print("\nTotal refugees:", total_refugees)"""