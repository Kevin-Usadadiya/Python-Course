# 1 can of paint can cover 5 square meters of wall
import math
height = int(input("Enter height of wall : "))
width = int(input("Enter width of wall: "))
def paint_wall(height, width):
    coverage = 5;
    number_of_cans = math.ceil((height * width) / coverage);
    print(f'You have to buy {number_of_cans} cans of paint to paint the wall')

paint_wall(height,width)