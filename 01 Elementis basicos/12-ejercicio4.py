# exercist four - area and longit of a circle

import math

print("exercis four")

# my version
'''
radio = float(input("Enter radio the circle: "))
area = 3.1314 * radio**2
longitud = 2 * 3.1314 * radio
print(f"the area of circle is {area}")
# format from cut float
print(f"the longitud of circle is {longitud}")
'''

# version correct in python
radio = float(input("Enter radio the circle: "))
area = math.pi * radio**2
longitud = 2 * math.pi * radio
print(f"the area of circle is {area}")
# format from cut float
print(f"the longitud of circle is {longitud:.2f}")
