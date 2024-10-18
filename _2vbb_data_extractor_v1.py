

file_path = "/Users/didarsedghi/Desktop/TRIUMFresearch/emax4_data_from_eval.txt"

"""
The extractor function will split each row into a line. These lines will be turned into
list of string elements. An empty 'matrix' list will then be used to append all these new
lists into it, creating a 2D array. The first element matrix[0] is of no interest since it's
only the header of the .txt data file. So we loop over matrix[index][...] where second bracket
defines interested column of choice.
"""

def data_extractor_00(directory, column):
    """
    directory = path to data file.
    column = the desired column wanted.
    """

    matrix = []

    with open(directory, "r") as doc:
        for line in doc:
            element = line.split()
            matrix.append(element)
    column_data = []
    for index in range(1, len(matrix)):
        column_data.append(float(matrix[index][column]))
    for index in range(len(column_data)):
        print(column_data[index])
    return "Data successfully extracted!"
print(data_extractor_00(file_path, 1))

