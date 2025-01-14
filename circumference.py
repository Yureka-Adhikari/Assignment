r= float(input("Enter the radius of the circle: "))
def calc(radius):
    c= (2 * radius) * 3.141592653589793238462643383279502884197
    return c
    
circumference= calc(r)
    
print(f"The circumference of the circle with the radius {r} is {circumference}")