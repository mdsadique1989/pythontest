import pandas as pd

# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# reading 1 csv file from the website
df_Premier21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')

# renaming column names
df_Premier21.rename(columns={'FTHG': 'Home_goals', 'FTAG': 'Away_goals'}, inplace=True)


# Save the DataFrame to an Excel file after renaming columns
df_Premier21.to_excel(excel_writer='table_data.xlsx', index=False)

# Save the DataFrame to an Excel file after renaming columns
df_Premier21.to_csv('table_data.csv', index=False)