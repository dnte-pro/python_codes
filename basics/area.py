pi = 3.14159

def area_of_circle(radius):

    return pi * radius**2
r= int(input("Enter the radius of the circle: "))
area = area_of_circle(r)
print("The area of the circle with radius", r, "is", area)