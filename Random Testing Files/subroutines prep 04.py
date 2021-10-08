
# MULTIPLES


# def multipes(times, start, end, name):
#     print(f"Hello {name}... here is your times table")
#     for i in range(start, end + 1):
#         print(f"{times} x {i} = {times * i}")
        

# name, times, start, end = input("What is your name? "), int(input("Enter times table number ")), int(input("Enter the start number ")), int(input("Enter the end number "))

# multipes(times, start, end, name)



########################################################################

# PASSWORD CHANGER

# password = input("Enter password: ")

# while len(password) < 6 or len(password) > 8:
#     print("Password must be between 6 and 8 chars long!")
#     password = input("Enter password: ")

# password2 = input("Enter password again: ")

# while password != password2:
#     print("Error: Passwords do not match!")
#     password2 = input("Enter password again: ")

# print("Password change completed!")





###############################################################################

# CAR PARK SPACES

# from os import name, system

# def clear():
#     if name == 'nt':
#         _ = system('cls')



# run = "Y"
    

# class grid():

#     def __init__(self):
#         self.grid = [

#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],

#             ]

#     def print_grid(self):
#         for row in self.grid:
#             print (" ".join(row))

#     def add_car(self, position1, position2, reg):
#         self.grid[position1-1][position2 -1] = reg.upper()
#         self.print_grid()

    
#     def clear_grid(self):
#         self.grid = [

#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],
#             ["empty", "empty", "empty", "empty", "empty", "empty"],

#             ]

#     def remove_car(self, reg):
#         found, row, column = self.find_index(reg.upper())
#         if found:
#             self.grid[row][column] = "empty"
#             self.print_grid()
#             return True
#         else:
#             return False

#     def find_index(self, reg):
#         row = 0
#         for a in self.grid:
#             if reg.upper() in a:
#                 column = a.index(reg.upper())
#                 return True, row, column
#             row += 1
#         return False
                
    
#     def check_car(self, position1, position2):
#         if self.grid[position1-1][position2 -1] == "empty":
#             return False
#         else:
#             return True

# grid = grid()


# while run == "Y":
#     leave = False
#     choice = "no choice"
#     clear()
#     while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
#         clear()
#         print("1. Reset all spaces to 'empty'")
#         print("2. Park a car")
#         print("3. Remove a car")
#         print("4. Display grid")
#         print("5. Exit")

#         choice = int(input("\nChoose your option: "))
    
#     if choice == 1:
#         clear()
#         grid.clear_grid()
#         grid.print_grid()
#         print("\nThe grid has now been cleared!")
#         input("\nPress Enter to continue... ")
#     elif choice == 2:
#         clear()
#         checked_for_car = False

#         while not checked_for_car:
#             clear()
#             grid.print_grid()
#             row = int(input("\nEnter the row number (1 - 10): "))

#             while row < 1 or row > 10:
#                 clear()
#                 row = int(input("Enter the row number (1 - 10): "))
            
#             column = int(input("Enter the column number (1 - 6) "))

#             while column < 1 or column > 6:
#                 clear()
#                 print(f"You have selected a row number of {row}")
#                 column = int(input("\nNow enter the column number (1 - 6): "))  
                
#             if grid.check_car(row, column):
#                 print("There is already a car parked here! Please choose another bay!")
#                 input("\nPress Enter to continue... ")
#             else:
#                 checked_for_car = True
        
#         clear()


#         reg = input("What is the reg number of the vehicle you want to park?: ")
#         while grid.find_index(reg):
#             clear()
#             print(f"A vehicle of reg number {reg.upper()} is already in the grid! ")
#             reg = input("What is the reg number of the vehicle you want to park?: (enter '1' to go back to main menu) ")
            
#             if reg == "1":
#                 leave = True
#                 break

#         clear()

#         if leave == False:
#             grid.add_car(row, column, reg)
#             print("\nCar is now added to the grid!")
#             input("\nPress Enter to continue... ")
#         else: 
#             pass


#     elif choice == 3:
#         clear()
#         grid.print_grid()
#         reg = input("\nWhat is the reg number of the vehicle you want to remove?: ")
#         while not grid.find_index(reg):
#             clear()
#             grid.print_grid()
#             print(f"A vehicle of reg number {reg.upper()} is not in the grid!")
#             reg = input("What is the reg number of the vehicle you want to remove?: (enter '1' to go back to main menu) ")
            
#             if reg == "1":
#                 leave = True
#                 break
#         if leave == False:
#             clear()
#             if grid.remove_car(reg):
#                 print("\nCar is now removed from the grid!")
#                 input("\nPress Enter to continue... ")
#             else:
#                 break
#         else: 
#             pass
#     elif choice == 4:
#         clear()
#         grid.print_grid()
#         input("\nPress Enter to continue... ")
#     else:
#         clear()
#         print("Program terminating")
#         input("\nPress Enter to continue... ")
#         run = "N"

    




