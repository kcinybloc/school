## Title: Sphere.py
## 
## Author:   Student
##
## Course:  INFO-2820 
##
## Description: This program calculates various attributes
## of a sphere based on user input of the radius. 

## required modules 

import math

## create the "sphere" class and define attributes

class sphere:
    def __init__(self, sphere_radius):
        self.sphere_radius = sphere_radius
        self.sphere_diameter = sphere_radius * 2
        self.sphere_circumfrence = sphere_radius * 2 * math.pi
        self.sphere_surf_area = (4 * math.pi * sphere_radius ** 2)
        self.sphere_volume = ((4/3) * math.pi * sphere_radius ** 3)

## collect radius from the user

given_radius = float(input("Please enter the radius of the sphere: "))

## make a sphere! 

sphere_one = sphere(given_radius)

## format the results into a user 
## friendly ouput

result_string = '''
For a sphere of the given radius {radius} the following is true:\n
The Diameter is: {diameter} 
The Circumference is: {circumference} 
The Surface area is:{surf_area} 
The Volume is: {volume} 
'''
result_string = result_string.format(radius = sphere_one.sphere_radius,
                                    diameter = sphere_one.sphere_diameter,
                                    circumference = sphere_one.sphere_circumfrence,
                                    surf_area = sphere_one.sphere_surf_area,
                                    volume = sphere_one.sphere_volume)

## give the output to the user

print(result_string)