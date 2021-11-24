import typer
import pandas as pd
import numpy as np
from collections import deque

app = typer.Typer()


@app.command()
def find_connected_cells(file,
                         x_coordinate,
                         y_coordinate,
                         upper_limit,
                         lower_limit,
                         ):
    """
    Finds all connected cells within a numerical grid data set in a csv file
    format, starting from a single point using an upper and lower limit.


    :param file: The file path of a CSV file

    :type file: str

    :param x_coordinate: The column of the starting point in data_set

    :type x_coordinate: int

    :param y_coordinate: The row of the starting point in the data_set

    :type y_coordinate: int

    :param upper_limt: upper value limit for a cell to be considered
    as a connected cell

    :type upper_limit: float or int

    :param lower_limit: lower value limit for a cell to be considered
    as a connected cell

    :type lower_limit: float or int

    :return connected_cells: A set of all the coordinates of the connected cells
    as tuples, in the from (x, y)

    :rtype connected_cells: set
    """
    data_set = read_data_set(file)

    grid_width, grid_height = get_grid_width_height(data_set)

    check_x_y_coordinates(x_coordinate, y_coordinate, grid_width, grid_height)

    connected_cells = set([(x_coordinate, y_coordinate)])

    # queue for iterating through each connected cell
    queue = deque([(x_coordinate, y_coordinate)])

    while queue:
        x, y = queue.popleft()
        neighbours = []

        # add all neighbouring cells of current cell to neighbours considering
        # if either x or y coordinates are on the edge of the grid
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
                and lower_limit
                <= data_set[coordinates_tuple[0]][coordinates_tuple[1]]
                <= upper_limit
            ):
                connected_cells.add(coordinates_tuple)
                queue.append(coordinates_tuple)

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


def check_x_y_coordinates(x_coordinate, y_coordinate, grid_width, grid_height):
    """
    Checks that the parameters x_coordinate and y_coordinate are the type int
    and that they are within the bounds of a grid_width and grid_height,
    respectively by raisng ValueErrors if otherwise.


    :param x_coordinate: value to be checked

    :type x_coordinate: int

    :param y_coordinate: value to be checked

    :type y_coordinate: int

    :param grid_width: maximum value of x_coordinate

    :type grid_width: int

    :param grid_height: maximum value of y_coordinate

    :type grid_height: int

    :raises ValueError: If either x_coordinate or y_coordinate are not type int

    :raises ValueError: If either x_coordinate or y_coordinate are greater than
    grid_width or grid_height, respectively

    :return: None

    :rtype: NoneType
    """
    if type(x_coordinate) is not int or type(y_coordinate) is not int:
        raise ValueError("x_coordinate and y_coordinate must be the type int")

    if x_coordinate > grid_width or y_coordinate > grid_height:
        raise ValueError(
            "x_coordinate and y_coordinate must be within data_set index bounds")


if __name__ == "__main__":
    app()
