path_directory = '/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Fall/PHYS-459D1 Research Thesis/Code/test_file.txt'

"""
The extractor function will take in input a directory file made up of
columns of data. It will also take an integer value corresponding to
a column one wishes to manipulate. It processes the directory file 
and extracts the desired column data and prints out all the values
related to that column.
"""

def data_extractor_00(directory, column):
    """
    directory = path to file
    column = desired column (integer) 
    """

    matrix = [] # Empty matrix where all the data is stored.
    with open(directory, "r") as doc:
        for line in doc:
            element = line.split()
            matrix.append(element) # Sorts data into an empty matrix.
    
    column_data = [] # Empty column array where desired data is stored.
    print(f"Column {column + 1}: ") # We start at column 0 due to indexing.

    # Turns string data into float values and prints data.
    for index in range(1, len(matrix)):
        column_data.append(float(matrix[index][column]))
    for index in range(len(column_data)):
        print(column_data[index])
    
    return "Data extracted successfully."


print("\n", data_extractor_00(path_directory, 1), "\n")

