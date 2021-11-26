import sys
import pandas as pd
import numpy as np
from collections import deque


def find_connected_cells(file,
                         x_coordinate,
                         y_coordinate,
                         upper_limit,
                         lower_limit,
                         ):
    """
    Finds all connected cells within a numerical grid data set in a csv file
    format, starting from a single point using an upper and lower limit. A
    breadth first search algorithm is adopted to achieve this. A basic command
    line visulisation is used to display the connected cells in the grid.


    :param file: The file path of a CSV file

    :type file: str

    :param x_coordinate: The column of the starting point in data_set starting
    from 0

    :type x_coordinate: int

    :param y_coordinate: The row of the starting point in the data_set starting
    from 0

    :type y_coordinate: int

    :param upper_limt: upper value limit for a cell to be considered
    as a connected cell relative to the center cell

    :type upper_limit: numerical - int or float

    :param lower_limit: lower value limit for a cell to be considered
    as a connected cell relative to the center cell

    :type lower_limit: numerical - int or float

    :raises ValueError: If either x_coordinate or y_coordinate cannot be casted
    into type int

    :raises ValueError: If either x_coordinate or y_coordinate are greater than
    grid_width or grid_height, respectively

    :raises ValueError: If either lower_limit or upper_limit cannot be casted
    into type float

    :return connected_cells: A set of all the coordinates of the connected cells
    as tuples, in the from (x, y)

    :rtype connected_cells: set
    """
    data_set = read_data_set(file)

    grid_width, grid_height = get_grid_width_height(data_set)

    try:
        x_coordinate = int(x_coordinate)
        y_coordinate = int(y_coordinate)
    except:
        raise ValueError("x_coordinate and y_coordinate must be the type int")

    if x_coordinate > grid_width or y_coordinate > grid_height:
        raise ValueError(
            "x_coordinate and y_coordinate must be within data_set index bounds")

    try:
        lower_limit = float(lower_limit)
        upper_limit = float(upper_limit)
    except:
        raise ValueError("upper_limit and lower_limit must be a number")

    connected_cells = set([(x_coordinate, y_coordinate)])

    # queue for iterating through each connected cell
    queue = deque([(x_coordinate, y_coordinate)])

    while queue:
        x, y = queue.popleft()
        neighbours = []

        # add all neighbouring cells including diagonally of current cell to
        # neighbours considering if either x or y coordinates are on the edge of
        # the grid
        if x < grid_width:
            # right cell
            neighbours.append((x + 1, y))
            if y > 0:
                # top right diagonal cell
                neighbours.append((x + 1, y - 1))
            if y < grid_height:
                # bottom right diagonal cell
                neighbours.append((x + 1, y + 1))
        if x > 0:
            neighbours.append((x - 1, y))
            if y > 0:
                # top left diagonal cell
                neighbours.append((x - 1, y - 1))
            if y < grid_height:
                # bottom left diagonal cell
                neighbours.append((x - 1, y + 1))
        if y < grid_height:
            # bottom cell
            neighbours.append((x, y + 1))
        if y > 0:
            # top cell
            neighbours.append((x, y - 1))

        for coordinates_tuple in neighbours:
            if (
                coordinates_tuple not in connected_cells
                and coordinates_tuple not in connected_cells
                and (data_set[x][y] - lower_limit)
                <= data_set[coordinates_tuple[0]][coordinates_tuple[1]]
                <= (data_set[x][y] + upper_limit)
            ):
                connected_cells.add(coordinates_tuple)
                queue.append(coordinates_tuple)

    # Showing user loaded data set as a DataFrame, target cell and connected
    # cells
    # REMOVE FOLLOWING LINES IF VISUALISATION IS NOT REQUIRED
    print(data_set)

    print("Loaded data set")
    input("Press Enter to continue...")

    data_set_coordinate = data_set.copy()
    data_set_coordinate.iloc[y_coordinate, x_coordinate] = str(
        data_set_coordinate.iloc[y_coordinate, x_coordinate]) + "X"

    print(data_set_coordinate)
    data_set_coordinate[x_coordinate][y_coordinate]

    print("Target cell marked with X")
    input("Press Enter to continue...")
    data_set_neighbours = data_set_coordinate.copy()

    for (x, y) in connected_cells:
        data_set_neighbours.iloc[y, x] = "*" + \
            str(data_set_neighbours.iloc[y, x]) + "*"
    print(data_set_neighbours)

    print("Connected cells circumfixed by *")
    input("Press Enter to exit...")

    return connected_cells


def read_data_set(file):
    """
    Reads a comma-separated values (CSV) file of numbers into a DataFrame.


    :param file: The file path of a CSV file

    :type file: str

    :raises ValueError: If file is not a str

    :raises ValueError: The parameter file does not locate a valid CSV - empty,
    incorrect file location, contains non-numbers

    :return df: The file data as a DataFrame object

    :rtype df: pandas.core.frame.DataFrame
    """
    if type(file) is not str:
        raise ValueError("The parameter file must be a str")

    try:
        df = pd.read_csv(file, header=None, dtype=np.float64)
    except:
        raise ValueError(
            "The parameter file must be the location of a non-empty CSV file containing only numbers")

    return df


def get_grid_width_height(data_set):
    """
    Returns the dimensions of a DataFrame object as width and height.


    :param data_set: A DataFrame object

    :type data_set: pandas.core.frame.DataFrame

    :raises ValueError: If data_set is not a DataFrame object

    :return width: The number of columns in data_set

    :rtype width: int

    :return height: The number of rows in data_set

    :rtype height: int
    """
    if type(data_set) is not pd.core.frame.DataFrame:
        raise ValueError(
            "The paratemer data_set must be a pandas.core.frame.DataFrame")

    width = data_set.shape[1] - 1
    height = data_set.shape[0] - 1
    return width, height


if __name__ == "__main__":
    if len(sys.argv) != 6:
        help(find_connected_cells)
        raise ValueError(
            "The program uses the find_connected_cells() function and was run with the incorrect"
            " number of arguments. \n See an example running this program with the correct"
            " number of arguments below: \n python3 ./main.py ./num_grid_test.csv 3 1 3 3"
        )

    find_connected_cells(sys.argv[1], sys.argv[2],
                         sys.argv[3], sys.argv[4], sys.argv[5])
