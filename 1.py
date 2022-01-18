
print("please inter an item")
shopping_list = []
b = 1
while b == 1:
    a = input ()
    if a == "QUIT": 
        b = 0
    else:
        shopping_list = shopping_list + [a]
        print("Please insert the next item ")
    

print(shopping_list)