# Write circle_calc() function that takes radius of a circle as an input from
# user and then it calculates and returns area, circumference and diameter. You should
# get these values in your main program by calling circle_calc function and  then print them
import math
def circle_calc(radius):
    circle_area = round( math.pi*(radius**2) ,2)#pi r2
    circle_circumference = round (2 * math.pi * radius ,2)
    circle_diameter = round( 2 *radius ,2)
    return circle_area , circle_diameter , circle_circumference

if __name__ == "__main__":
    radius = input("Enter the radius of the circle: ")
    radius = float(radius)
    circle_area, circle_diameter, circle_circumference = circle_calc(radius)
    print(f"The area of the circle is {circle_area} and its diameter is {circle_diameter}"
          f" and its circumference is {circle_circumference}")
