#A function to load emails from a file
def load(user_information):
    x = {}
    return x

# Open a file
user_information = open("contacts.txt" , "w")
# Call the load function
I = load(user_information)

# A function to print a new line
def line():
    print("\n")

# A function to look up a person's email address
def lookup():
    n = input("Enter a name:")
    if(n in I.keys()):
        print("Name: " , n)
        print("Email: ", I[n])
        line()
    else:
        print("The Specified name was not found")
        line()

# A function to add a new name and email address
def add():
    n = input("Enter a name:")
    e = input("Enter email address:")
    if(n in I.keys()):
        print("The name already exists")
        line()
    else:
        I[n] = e
        print("Name and address have been added")
        line()

# A function to change an email address
def change():
    n = input("Enter a name: ")
    if(n in I):
        e = input("Enter email address ")
        I[n] = e
        print("Information Updated")
        line()
    else:
        print("The Specified name was not found")
        line()

# A function to delete a name and email address
def delete():
    n = input("Enter a name: ")
    if(n in I):
        del(I[n])
        print("Information Deleted")
        line()
    else:
        print("The name is not in the database")
        line()

#A function to save emails in a file
def quit():
    user_information.write("Name     &     Email\n")
    for l in I:
        key = l
        value = I[key]
        user_information.write("{0}     {1:>20}    \n".format(key,value))
    print("Information Saved")

# A function to display a menu
def menu():
    print("Menu")
    print("---------------------------------")
    print("1.Look up an email address")
    print("2.Add a new name and email address")
    print("3.Chage an existing email address")
    print("4.Delete a name and email address")
    print("5.Quit the program")


# A function for the main part of the program
def main():
    done = False
    while(done == False):
        menu()
        line()
        C = input("Enter your choice: ")
        C = int(C)

        if(C == 1):
            lookup()
        elif(C == 2):
            add()
        elif(C == 3):
            change()
        elif(C == 4):
            delete()
        elif(C == 5):
            quit()
            done = True
            
# call main function 
main()

#close file
user_information.close()
