import pandas as pd

tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)#Season_1_(1989%E2%80%9390)')

# Check the number of tables found
print(len(tables))

# Set number of rows and columns to display
pd.set_option('display.max_rows', 10)  # Show up to 10 rows
pd.set_option('display.max_columns', 10)  # Show up to 10 column

# Print the index table
print(tables[1])

# Assuming you want to save the second table (index 1) to a CSV file
# tables[1].to_csv('table_data.csv', index=False)

# Assuming you want to save the second table (index 1) to an Excel file
tables[1].to_excel('table_data.xlsx', index=False)
