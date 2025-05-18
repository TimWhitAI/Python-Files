'''You are tasked with creating a simple inventory management system for a market. The system should allow users
 to add, update, view, and remove items from the inventory. Each item in the inventory will have a name, price,
 quantity, and category.
Functionality:
Add Item: Create a function add_item that allows users to add a new item to the inventory. Users should input the name,
 price, quantity, and category of the item.

Update Item: Implement a function update_item that allows users to update the details of an existing item in the inventory.
Users should be able to update the price, quantity, and category of the item.

View Inventory: Develop a function view_inventory that displays all items in the inventory along with their details (name,
 price, quantity, and category).

Remove Item: Create a function remove_item that allows users to remove an item from the inventory based on its name.

Search by Category: Implement a function search_by_category that allows users to search for items in the inventory based
on their category. The function should display all items belonging to the specified category.

Project Structure:
Define a list inventory to store the items in the market inventory. Each item should be represented as a dictionary with
keys for name, price, quantity, and category.
Implement the functions add_item, update_item, view_inventory, remove_item, and search_by_category to manage the inventory.
Create a main loop to interact with the user. The loop should prompt the user to choose from various options such as adding,
 updating, viewing, removing items, or searching by category'''
#create the initial inventory dictionary
inventory = {
    "laptop": {
        "price": 1200.00,
        "quantity": 10,
        "Category": "XYZ"
        },
    "mouse": {
        "quantity": 50,
        "price": 25.00,
        "Category": "ABC"
        },
    "keyboard": {
        "quantity": 30,
        "price": 75.00,
        "Category": "ABC"
        }
}
# define the functions
def printInv(prtInv):
  print(prtInv)
def addItem(name,price,quantity,category):
  inventory.update ({name: {"price": price, "quantity": quantity, "category": category}})
def updateItem(name, price, quantity, category):
    if inventory.get(name,"Not Found") == "Not Found":
      print("The item is not in the inventory.")
    else:
      inventory.update ({name: {"price": price, "quantity": quantity, "category": category}})
      print("Changes have been made.")
def deleteitem(name):
  try:
    del inventory[name]
    print(inventory)
  except:
    print("Item not found")
def find_items(data, value, Cat):
    for id, info in inventory.items():
        found = False
        for key in info:
            if key == Cat and info[key] == value:
                print("\nProduct:", id)
                value1 = inventory[id]['price']
                print("Price: ", value1)
                value2 = inventory[id]['quantity']
                print("Quantity: ", value2)
                print(key + ':', info[key])
                found = True
    if found == False:
        print("Category not found")


#Create the interface to allow users to perform multiple functions entering a 6 to exit program

x = 1
option = 0
while True:
  try:
    option = int(input("Please select from the follow options. Enter 1 to view Inventory. Enter 2 to add new item. Enter 3 to update an item. Enter 4 to remove an item. Enter 5 to search by category. Enter 6 to exit program: "))
    if 1 <= option <= 6:
      if option == 1:
        # Call function and print the results
        printInv(inventory)
      elif option == 2: #Call function to add new inventory
        input_name = input("Please enter name of product: ")
        input_price = float(input("Please enter price of product: "))
        input_quantity = int(input("Please enter quantity of product: "))
        input_Cat = input("Please enter category of product: ")
        addItem(input_name, input_price, input_quantity, input_Cat)
      elif option == 3: #Call functions to update inventory
        input_name = input("Please enter name of product: ")
        input_price = float(input("Please enter price of product: "))
        input_quantity = int(input("Please enter quantity of product: "))
        input_Cat = input("Please enter category of product: ")
        updateItem(input_name, input_price, input_quantity, input_Cat)
      elif option == 4: #Call function to remove inventory
        input_name = input("Please enter name of product to be deleted: ")
        deleteitem(input_name)
      elif option == 5:#Call function to search for product by
         input_Category = input("Please enter the category you wish to search: ")
         x = "Category"
         find_items(inventory,input_Category,x)
      elif option == 6: #Option will exit program by leaving loop
        break
    else:
      print("Number out of range. Try again.") #Error message displayed if entries not between 1 and 5
  except ValueError:
    print("Invalid input. Please enter an integer.") #error message displayed if entry not numeric










