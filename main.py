# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import math


def input_y_co_ordinate():
    y = float(input("Faka ipoyint ka Y  :"))
    return y


def input_x_co_ordinates():
    x = float(input("Faka ipoyint ka X  :"))
    return x


def input_point_name():
    name = input("Faka igama lepoyint :")
    return name


def input_radius():
    radius = float(input("Faka iradiyasi"))
    return radius


def perimeter(r):
    perimeter = 2*3.14*r
    return perimeter


def area(a):
    area = 3.14*a*2
    return area


def checking(x, y, rad):
    x_origin = 0
    y_origin = 0
    distance = math.sqrt((x-x_origin)**2+(y-y_origin)**2)
    if distance > rad:
        point = "ngaphandle kwesekile"
    else:
        point = "ngaphakathi kwesekile"
    return point


def results(origin_y, origin_x, name, perimeter, area, check):
    print("Iperimitha yalesekile ngu  :", perimeter,"meters")
    print(" ieriya yalesekile ngu  :", area,"meters")
    print("le point",name,(origin_x,origin_y), check)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    y = input_y_co_ordinate()
    x = input_x_co_ordinates()
    name = input_point_name()
    rad = input_radius()
    perimeter = perimeter(rad)
    area = area(rad)
    check = checking(x, y, rad)
    results(x, y, name, perimeter,area, check)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
