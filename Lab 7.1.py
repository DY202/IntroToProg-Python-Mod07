# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# Deborah Yenubari, 3.4.21, Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
lstTable = []
file = "AppData.txt"
strID = ""
strName = ""
objFile = "AppData.data"
objFileData = []


# Processing -------------------------------------- #
lstHeader = ["ID", "NAME"]
print(lstHeader[0], lstHeader[1], sep=" ")
lstRow = ["1", "James Madison"]
print(lstRow[0], lstRow[1], sep=",")


def display_current_data(lstTable):
    lstTable.append(lstHeader)
    lstTable.append(lstRow)
    print(lstTable)


def save_data_to_file(lstTable, file):
    file = open("AppData.txt", "a")
    for lstRow in lstTable:
        file.write(lstRow[0] + "," + lstRow[1] + "\n")
    file.close()
    return lstTable
    # except IOError:
    #     print("Error: Can't find file!")
    # else:
    #     print("Data saved in text file, 'AppData.txt'!")
    # file = open("AppData.txt", "a")
    # for lstRow in lstTable:
    #     file.write(lstRow[0] + "," + lstRow[1] + "\n")
    # file.close()
    # return lstTable


def read_data_from_file(file, lstTable):
    file = open("AppData.txt", "r")
    fileData = file.read().splitlines()
    for line in file:
        print(fileData[0].strip() + "," + fileData[1].strip() + "\n")
    print(fileData)
    file.close()


# Get ID and NAME From user, then store it in a list object

def add_new_data(strID, strName):
    try:
        strID = input("Enter an ID: ")
        if strID <= "0":
            raise ValueError
    except ValueError:
        print("Please enter a number above zero")
    finally:
        strID = input("Enter an ID: ")
    try:
        strName = input("Enter a Name: ")
        for char in strName:
            if char in strName == "!":
                raise ValueError
            elif char == "#":
                raise ValueError
            elif char == "@":
                raise ValueError
            elif char == "%":
                raise ValueError
            elif char == "$":
                raise ValueError
            elif char == "%":
                raise ValueError
            elif char == "&":
                raise ValueError
            elif char == "*":
                raise ValueError
    except ValueError:
        print("Please note symbols are not allowed")
    finally:
        strName = input("Enter a Name: ")
    lstRow = [strID, strName]
    lstTable.append(lstRow)
    print("\n")
    print(lstTable)

    # #  print("Type in your ID and Name: ")
    # strID = input("Enter an ID: ")
    # strName = input("Enter a Name: ")
    # lstRow = [strID, strName]
    # lstTable.append(lstRow)
    # print("\n")
    # print(lstTable)
    #

def save_data_to_binary_file(lstTable, objFile):
    objFile = open("AppData.data", "ab")
    pickle.dump(lstTable, objFile)
    objFile.close()


def read_data_from_binary_file(objFileData, lstTable):
    objFile = open("AppData.data", "rb")
    objFileData = pickle.load(objFile)  # read all data from the file at once
    print(objFileData)
    objFile.close()


# Presentation ------------------------------------ #

#  Main Script


intChoice = True

while True:
    print("""
    Please choose an option:
    1. Display Current Data
    2. Save Data to File
    3. Read Data from File 
    4. Add New Data
    5. Save List to Binary File
    6. Read from Binary File to List
    """)
    # Step 2
    # Add a new item to the List(Table) each time the user makes that choice
    intChoice = input("Enter 1, 2, 3, 4, 5, 6 or exit: ")

    if intChoice == "1":
        print("Your Current Data is: ")
        display_current_data(lstTable)
    elif intChoice == "2":
        answer = input("Would you like to Save your Data to file? Yes or No:")
        if answer.lower() == "yes":
            print("Data saved to file, 'AppData.txt'!")
            save_data_to_file(lstTable, file)
    elif intChoice == "3":
        print("Here is the current Data from the file, 'AppData.txt': ")
        read_data_from_file(file,lstTable)
    elif intChoice == "4":
        print("Type in your ID and Name: ")
        add_new_data(strID, strName)
    elif intChoice == "5":
        print("Data saved to Binary File, 'AppData.data!")
        save_data_to_binary_file(lstTable, objFile)
    elif intChoice == "6":
        print("Showing pickled Data from Binary File, 'AppData.data': ")
        read_data_from_binary_file(objFileData, lstTable)
    else:
        break