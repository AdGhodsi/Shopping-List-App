
#create shopping list
shopping_list = []

#instructions
def guide():
    print("""
        In order to finish the list, please type 'Quit'
        In order to see the existing items, please type 'SHOW'
        To see this guide, please type 'HELP'
        """)
#show all the items
def show():
   
    for i in shopping_list:
        print(i)

#add new item t list
def add_to_list():
    
    shopping_list.append(new_item)
   
    print("the last item is {}. The list now has {} items".format(new_item, len(shopping_list)))

#strat
guide()
print("please insert an item")
while True:

    new_item = input (">")
    
    if new_item == "SHOW":
       show()
        
    elif new_item == "HELP":
       guide()
       continue

    elif  new_item == "QUIT":
        print("Your list includes the following items:")
        show()
        break
   
    else:
        add_to_list()
   
