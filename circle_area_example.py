from math import pi


def circle_area(radius):
    if radius < 0:
        raise ValueError("The radius cannot be negative.")
    return pi * (radius ** 2)


# Testing circle_area function
"""
radius_test_values = [2, 0, -3, 2 + 5j, True, "radius"]
message = "Area of circle with r = {radius} is {area}."

for r in radius_test_values:
    A = circle_area(r)
    print(message.format(radius=r, area=A))
"""