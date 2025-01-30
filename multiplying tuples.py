
a= (4 , 3 , 2 , 2 , -1 , 18)
b= (2, 4, 8, 8, 3, 2, 9)

tup3= []
def multiply(tup1, tup2):

    for i in range (0, len(tup1)):
        p= tup1[i] * tup2[i]
        
        tup3.append(p)
    
multiply(a, b)
print(tup3)



