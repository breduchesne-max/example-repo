#========The beginning of the class==========
class Shoe:
    '''Represents a shoe with attributes for country, code, product, cost, and quantity.'''

    def __init__(self, country, code, product, cost, quantity):
        '''Initialize a new Shoe instance with casted data types.'''
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        '''Return the cost of the shoe.'''
        return self.cost
    def get_quantity(self):
        '''Return the quantity of the shoe.'''
        return self.quantity
        '''returns a string representation of the Shoe instance, including all its attributes.'''
            
    def __str__(self):
        '''Return a string representation of the Shoe instance.'''
        return (f"Country: {self.country}, Code: {self.code}, Product: {self.product}, "
                f"Cost: {self.cost}, Quantity: {self.quantity}")

shoes_list = []



#==========Functions outside the class==============
def read_shoes_data():
    '''Load shoe data from inventory.txt and populates the global shoes_list.
    Skips the file header row. Identifies if a file is missing 
    or has wrong lines.
    """'''
    try:
        with open("inventory.txt", "r") as file:
            next(file, None)
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    shoe = Shoe(*parts)
                    shoes_list.append(shoe)
    except FileNotFoundError:
        print("The file inventory.txt was not found.")
    except Exception as e :
        print(f"An error occurred: {e}")

def capture_shoes():
    '''Prompt the user to input shoe details and add a new Shoe instance to shoes_list and inventory.txt.'''


    country = input("Enter the country of the shoe: ")
    code = input("Enter the code of the shoe: ")
    product = input("Enter the product name of the shoe: ")
    cost = input("Enter the cost of the shoe: ")
    quantity = input("Enter the quantity of the shoe: ")
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(new_shoe)
    with open("inventory.txt", "a") as file:
        '''Append the new shoe details to the inventory.txt file in a comma-separated format.'''
        file.write(f"\n{country},{code},{product},{cost},{quantity}\n")


def view_all():
    '''Display all shoes in the shoes_list.'''

    for shoe in shoes_list:
        '''Print the string representation of each Shoe instance in shoes_list.'''
        print(shoe)


def re_stock():
    '''Identify the shoe with the lowest quantity and prompt the user to restock it. Updates both the in-memory list and the inventory.txt file.'''
    if not shoes_list:
        print("No shoes available to restock.")
        return

    lowest_quantity_shoe = min(shoes_list, key=lambda shoe: shoe.get_quantity())
    print(f"The shoe with the lowest quantity is: {lowest_quantity_shoe}")

    confirm = input("Would you like to restock this shoe? (yes/no): ").strip().lower()
    if confirm not in ("yes", "y"):
        print("Restock cancelled.")
        return

    restock_amount = input("Enter the amount to restock: ")
    try:
        lowest_quantity_shoe.quantity += int(restock_amount)
        print(f"Quantity updated in memory. New quantity: {lowest_quantity_shoe.quantity}")

        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoes_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

        print("Inventory file successfully updated.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the restock amount.")
    except Exception as e:
        print(f"An error occurred while saving to the file: {e}")


def search_shoe():
    '''Search for a shoe by its code and display its details.'''
    code = input("Enter the shoe code to search: ")
    for shoe in shoes_list:
        if shoe.code == code:
            print(shoe)
            return  

    print("Shoe not found.")
    '''prints if shoe is not found in the list'''

def value_per_item():
    '''Calculate and display the total value of each shoe in the inventory.'''
    for shoe in shoes_list:
        total_value = shoe.get_cost() * shoe.get_quantity()
        print(f"Product: {shoe.product}, Total Value: {total_value}")

def highest_qty():
    '''Identify and display the shoe with the highest quantity in the inventory.'''
    if not shoes_list:
        print("No shoes available.")
        return
    highest_quantity_shoe = max(shoes_list, key=lambda shoe: shoe.get_quantity())
    print(f"The shoe with the highest quantity is: {highest_quantity_shoe}")


#==========Main Menu=============
def menu():
    '''Display the main menu and handle user input to perform various inventory operations.'''
    read_shoes_data()
    while True:
        print("\nMenu:")
        print("1. Read Shoe Data")
        print("2. Capture new Shoes")
        print("3. View All Shoes")
        print("4. Restock Shoe")
        print("5. Search for a Shoe")
        print("6. Value Per Item")
        print("7. Highest Quantity Shoe")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            read_shoes_data()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            view_all()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            search_shoe()
        elif choice == "6":
            value_per_item()
        elif choice == "7":
            highest_qty()
        elif choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()



'''Pathways have been removed and corrected to just have invetory.txt
Indentation errors have been corrected and the code has been 
refactored to be more efficient and readable. 
I have added a note in the re_stock function to indicate 
where the corrections have been made'''
