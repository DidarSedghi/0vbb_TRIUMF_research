"""
For a given generated data list and directory, this function will take the
desired data; sort it and then write it into a file, where the _2vbb_data_extractor
will then exctract the data. The purpose is to move data from compute.canada environment
to local hardware.
"""

def data_sorter(directory, data_list):
    """
    directory = file path to directory where we will put data in
    data_list = generated data list
    """

    line = f"{'Column 1':>4s} {'Column 2':>4s} \n" # Header for columns in file.
    line+= f"{str(data_list[0]):>4s}" # First element is put under first column.

    for index in range(1, len(data_list)):
        if index % 2 == 0:
            line+= f"{str(data_list[index]):>4s}" # If index even, then it goes under 1st column.
        elif index % 2 != 0:
            line+= f"{str(data_list[index]):>9s} \n"
    
    with opne(directory, "w") as doc:
        doc.write(line)
    
    return f"Data written to {directory}."
 