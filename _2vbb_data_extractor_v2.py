path_directory = '/Users/didarsedghi/Desktop/Work/McGill/U4 (2024-2025)/U4 Fall/PHYS-459D1 Research Thesis/Code/test_file.txt'

"""This function takes in a directory input and an integer (column) input.
It takes the elements of the directory and puts in an array matrix. It
takes the column integer and outputs desired column of data."""

def data_extractor_00(directory, column):
    """
    directory = path to file
    column = desired column 
    """

    matrix = []
    with open(directory, "r") as doc:
        for line in doc:
            element = line.split()
            matrix.append(element)
    
    column_data = []
    print(f"Column {column + 1}: ")

    for index in range(1, len(matrix)):
        column_data.append(float(matrix[index][column]))
    for index in range(len(column_data)):
        print(column_data[index])
    
    return "Data extracted successfully."


print("\n", data_extractor_00(path_directory, 2), "\n")

    