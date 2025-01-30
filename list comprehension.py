start= int(input("Enter the starting number: "))
end= int(input("Enter the ending number: "))

def odd_even(s,e):
    
    even= [i for i in range(s,e+1) if i % 2==0]
    odd = [i for i in range(s,e+1) if (i % 2==0) == False ]
        
    print(f"The even numbers are: {even}")
    print(f"The odd numbers are: {odd}")
    
odd_even(start,end)
print()
print()
print()

#===============================================================

fruits= ["apple", "banana", "coconut", "durian", "fuji apples", "grapes"]
print(fruits)
capital= []

for x in fruits:
    
    p= x.capitalize
    (capital.append(p))
    
print(str(capital))


        