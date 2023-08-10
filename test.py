import pandas as pd

def create_and_print_dataframe(columns, data):
    df = pd.DataFrame(data, columns=columns)

    for i in range(len(df)):
        row = df.iloc[i]
        row_values = ' '.join(f"{column}{row[column]}" for column in columns)
        print(row_values)

# Define column labels
columns = ['g', 'x', 'y', 'z', 'e', 'f']

# Create a sample data dictionary with numerical values
data = {
    'g': [1, 2, 3, 4, 5],
    'x': [6, 7, 8, 9, 10],
    'y': [11, 12, 13, 14, 15],
    'z': [16, 17, 18, 19, 20],
    'e': [21, 22, 23, 24, 25],
    'f': [26, 27, 28, 29, 30]
}

# Call the function to create and print the DataFrame
create_and_print_dataframe(columns, data)
