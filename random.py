schools = ["AAAA", "BBBB", "CCCC", "DDDD"]

medals = [4, 6, 1, 3]

answer = "Y"

while answer == "Y":

    choice = int(input("Enter the school name (input -1 to view all data): "))


    while (choice < 1 and choice != -1) or choice > 4:
        print("Invalid choice. Enter school name 1-4")
        choice = int(input("Enter the school name: "))



    if choice == -1:
        print("")
        for i in range(0, 4):
            print(f"School number: {i + 1} School name: {schools[i]} Number of medals: {medals[i]} ")
    else:
        choice -= 1
        medals[choice] = medals[choice] + 1
        print(medals)

    
    print("\nDo you want to enter another school name? 'Y' or 'N'")
    answer = input()