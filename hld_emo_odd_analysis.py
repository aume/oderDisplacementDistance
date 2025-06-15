import pandas as pd

# Import the thorogood_dist function from a module named 'thorogood_dist_algorithm'.
from order_displacement_distance import order_displacement_dist

def read_csv_sort_list(filename, order_by):
    """
    Reads a CSV file, extracts 'File' and a specified 'order_by' column,
    sorts the data by the 'order_by' column, and returns 'File' column as a list.

    Args:
        filename (str): The path to the CSV file.
        order_by (str): The name of the column to sort the data by.

    Returns:
        list: A list of values from the 'File' column, sorted according to 'order_by'.
    """
    # Read the CSV file into a pandas DataFrame, selecting only the 'File'
    # and the column specified by 'order_by'. This improves efficiency by
    # not loading unnecessary columns.
    df = pd.read_csv(filename, usecols=['File', order_by])

    # Sort the DataFrame based on the values in the 'order_by' column.
    # This rearranges the rows of the DataFrame, and consequently the 'File'
    # column, according to the order of the specified column.
    df = df.sort_values(by=order_by)

    # Convert the 'File' column of the sorted DataFrame into a Python list
    # and return it. This list will be used as one of the inputs for the
    # thorogood_dist function.
    return df['File'].tolist()

# Example usage with pre-defined lists, as present in your original script.
# These lines demonstrate how thorogood_dist works with direct list inputs.
a2 = ['apple', 'banana', 'orange', 'grape']
b2 = ['banana', 'apple', 'grape', 'orange']
print(f"List A: {a2}")
print(f"List B: {b2}")
# Calculate and print the normalized displacement distance between a2 and b2.
print(f"Normalized Displacement Distance: {order_displacement_dist(a2, b2)}")

print("-" * 30)

# The following lines demonstrate reading data from CSV files, sorting it,
# and then applying the order_displacement_dist function to compare these lists.

# Read the 'expert' list by loading 'Desolate.csv' and sorting by the 'Value' column.
expert = read_csv_sort_list('./MiniCorpus/CSVFiles/Desolate.csv', 'Value')
# Read the 'emo' list by loading 'emo_predicted_hld.csv' and sorting by the 'desolate' column.
emo = read_csv_sort_list('./MiniCorpus/emo_predicted_hld.csv', 'desolate')
# Read the 'hld' list by loading 'hld_desolate.csv' and sorting by the 'Value' column.
hld = read_csv_sort_list('./MiniCorpus/hld_desolate.csv', 'Value')
# Read the 'rand' list by loading 'random_chaotic.csv' and sorting by the 'Value' column.
rand = read_csv_sort_list('./MiniCorpus/random_chaotic.csv', 'Value')


# Calculate and print the normalized displacement distance between the 'expert' list
# and the 'emo' predicted list. 
print(f"Normalized Displacement Distance EMO: {order_displacement_dist(expert, emo)}")
# Calculate and print the normalized displacement distance between the 'expert' list
# and the 'hld' list. 
print(f"Normalized Displacement Distance HLD: {order_displacement_dist(expert, hld)}")
