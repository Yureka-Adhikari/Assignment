def square_of_numbers(start, end):
    p = start
    even = []
    odd = []
    square = []
    
    while p <= end:
        r = p**2  
        square.append(r)
              
        if p % 2 == 0: 
            even.append(r)
        else:
            odd.append(r)
        p = p+1
        
    print(f"The numbers when squared: {square}")
    print(f"The even numbers when squared: {even}")
    print(f"The odd numbers when squared: {odd}")
    
 

s= int(input("Enter the starting number: "))
e= int(input("Enter the ending number: "))

square_of_numbers(s,e)