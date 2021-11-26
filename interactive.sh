#!/bin/bash
#
# Performs an interactive run of the connected_cells python program

read -p 'Location of .csv: ' file
read -p 'Row number of target cell: ' x_coordinate
read -p 'Column number of target cell: ' y_coordinate
read -p 'Upper limit: ' upper_limit
read -p 'Lower limit: ' lower_limit

python3 ./main.py "$file" "$x_coordinate" "$y_coordinate" "$upper_limit" "$lower_limit"
