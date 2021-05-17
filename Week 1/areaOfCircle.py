import math


def main():
    area_Circle()


def area_Circle():
    radius_circle = int(input("Enter radius of circle:"))
    area = math.pi * radius_circle * radius_circle
    print("area of the circle is:", area)
    return area


main()