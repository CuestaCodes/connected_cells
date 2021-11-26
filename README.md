# connected_cells

The Program
-------------
This is an implementation of a breadth first search algorithm in order to find all connected cells within a 2D numerical matrix in the format
of a .csv file.

It uses a user-defined starting coordinate within the matrix as the beginnning target cell - the first connected cell.

All neighbouring cells (adjacent and diagonal) are checked to see if they are within the range of a user-defined upper limit and lower limit
relative to the target cell. If so, the cell added to the set of connected cells. For example, if the target cell has a value of 5 and the 
upper limit and lower limit is set to 1, a neighbouring cell has to have a value within 4 - 6 to be considered a connected cell.

Each newly added connected cell are individually considered as the new target cell. The process repeats until all connected cells have
had their neighbouring cells check and there are no more new connected cells.

A basic command line visualisation is used to display the connected cells in the input. Even though this program is optimised for large data sets,
the visualisation is only useful for small datasets and the corresponding code should be removed if the dataset is much bigger than the example
num_grid_test.csv provided.

How To Use This
---------------
The main.py program needs to be run with all the arugments of the find_connected_cells() function in the format, 
"python3 ./main.py csv_file_location x_starting_coordinate y_starting_coordinate upper_limit lower_limit"

Example,
```
❯ python3 ./main.py ./num_grid_test.csv 3 1 3 3
```

Two bash scripts can also be run from the command line. Running auto.sh will run the above example, whereas running interactive.sh
will prompt the user for the arugments.

Example,
```
❯bash interactive.sh
Location of .csv: ./num_grid_test.csv
Row number of target cell: 3
Column number of target cell: 1
Upper limit: 3
Lower limit: 3
```


Credits
-------
Thanks go to to starkmatt for [their repo](https://github.com/starkmatt/bash-py-wrapper) to create the bash scripts used.
