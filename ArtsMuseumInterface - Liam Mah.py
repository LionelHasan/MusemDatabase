''' IMPORTANT NOTE: This code was created by Liam Mah for the database interface. Because this was a group project, this file is incomplete on its own. '''

import mysql.connector
import maskpass

def update(cur, cnx): # Data entry user function for updating information.
    while True: # Loops until a valid table name is entered
        print("UPDATE MENU\nPlease enter the name of the table you would like to update/change.")
        print("\nTABLE NAMES:\n- Art_Object\n- Borrowed\n- Permanent_Collection\n- Painting\n- Statue\n- Sculpture\n- Other\n- Collections\n- Artist\n- Created_By\n- Exhibition\n- Shown_During")
        table = input("\nPlease enter the name of the table you would like to update: ").strip().lower()
        if table not in ["art_object", "borrowed", "permanent_collection", "painting", "statue", "sculpture", "other", "collections", "artist", "created_by", "exhibition", "shown_during"]:
            print("The table you selected does not exist in the ORIGINAL database. Would you like to proceed? (Y/N)") # Option added for the case that an additional table is added (that does not already exist in the original database)
            valid = input().upper().strip()
            if valid == "N":
                continue
            elif valid == "Y":
                break
            else:
                print("Invalid input. Please re-enter the table name.\n")
                continue
        break
    
    while True:
        number_of_identifying_attributes = input("Please enter the number of identifying attributes (to identify the tuple you want to change): ")
        if number_of_identifying_attributes.isnumeric(): # Check to ensure that an integer is added. Loops until a valid integer is entered.
            number_of_identifying_attributes = int(number_of_identifying_attributes)
            break
        else:
            print("The value entered is not an integer. Please try again.")
    
    print("Attributes for table {}:".format(table))
    
    try: # Uses an SQL query to retrieve and print the available attributes for the corresponding table.
        cur.execute("select * from {}".format(table))
        attribute_names = cur.column_names
        for attribute in attribute_names:
            print("- {}".format(attribute))
    except: # Exception handling for the case that an invalid table name is entered (resulting in an invalid SQL command).
        print("Error. Could not retrieve attribute names for the table provided.") 

    identifying_attributes = [] # Empty list for the names of the identifying attributes
    identifying_attribute_values = [] # Empty list for the corresponding values of the identifying attributes provided above.
    for i in range(number_of_identifying_attributes): # Loops over user input to gather necessary information to create an SQL query.
        identifying_attribute = input("\nPlease enter the name of an identifying attribute(s): ")
        identifying_attribute_value = input("Please enter the current value for the identifying attribute provided above: ")
        identifying_attributes.append(identifying_attribute)

        is_numeric = identifying_attribute_value.isnumeric()
        if is_numeric == False:
            identifying_attribute_value = "'" + identifying_attribute_value + "'" # Adds necessary apostrophes around non-integer data types. This is required in order to make a valid SQL update command (apostrophes around strings and date datatypes).
        
        identifying_attribute_values.append(identifying_attribute_value)
    
    changing_attribute = input("\nPlease enter the name of the attribute to be changed: ").strip() # Asks for the attribute that is being changed.
    new_value = input("Please enter a new value for the attribute entered above: ") # Asks for the new value of the attribute.

    is_numeric = new_value.isnumeric()
    if is_numeric == False:
        new_value = "'" + new_value + "'" # Adds apostrophes around the new value if it is a string or data datatype. This is required in order to make a valid SQL update command.

    execution_string = "UPDATE " + table + " SET " + changing_attribute + " = " + new_value + " WHERE " + identifying_attributes[0] + " = " + identifying_attribute_values[0] # Creates the baseline string for the SQL command. Note that because strings are mutable in Python, it can be done in this way.
    
    if number_of_identifying_attributes > 1: # Takes into the account of multiple identifying attributes. This completes the execution_string above in order to complete an SQL update command.
        i = 1
        while i < number_of_identifying_attributes:
            execution_string = execution_string + " AND " + identifying_attributes[i] + " = " + identifying_attribute_values[i]
            i = i + 1
    
    try: # Executes the SQL update command.
        cur.execute(execution_string) 
        cnx.commit()
        print("Update on {} was successful.".format(table))
    except mysql.connector.Error: # Exception handling for the case that invalid information is entered and the operation is unsuccessful.
        print("Error. Invalid input(s) given. Update operation was unsuccessful. Please re-enter values.")

def admin(cur, cnx):
    print("Welcome to the Arts Museum! You are currently in admin mode.")
    loop = True
    while loop == True:
        print("\nADMIN MENU\na. Enter an SQL command\nb. Provide an SQL script file\nc. Enter data_entry mode\nd. Quit")
        print("Note: You may add, edit, and block users by entering the proper SQL comamnd. You may also make direct changes to the database via entering an SQL command.")
        choice = input("Please enter the letter corresponding to your choice: ").strip().lower()
        if choice == 'a':   # Enter an SQL command
            command(cur, cnx)
        elif choice == 'b': # Enter an SQL script
            new_script(cur, cnx) # May or may not have to remove cur and cnx as passed values to function (not sure if we need it)
        elif choice == 'c':
            data_entry(cur, cnx)
        elif choice == 'd': # Exiting the selection loop
            print("Exiting database. Thank you!")
            loop = False
        
        else:
            print("Error. Invalid selection.")

def data_entry(cur, cnx):
    print("Welcome to the Arts Museum! You are currently in data entry mode.")
    loop = True
    while loop == True:
        print("\nDATA ENTRY MENU\na. Add/Insert Data\nb. Update/Modify Existing Information\nc. Delete Data\nd. Lookup data\ne. Quit")
        choice = input("Please enter the letter corresponding to your choice: ").strip().lower()
        if choice == 'a': # Add/insert tuples of data
            add(cur, cnx)
        elif choice == 'b': # Update and modify data - Tell user if operation is successful
           update(cur, cnx)
        elif choice == 'c': # Delete tuples of data - Tell user if operation is successful
            delete(cur, cnx)
        elif choice == 'd': # Query for data (same as guest interface)
            search(cur)
        elif choice == 'e': # Exiting the selection loop
            print("Exiting data entry mode. Thank you!")
            loop = False
        else:
            print("Error. Invalid selection.")

def guest(cur):
    print("Welcome to the Arts Museum! You are currently in guest view.")
    loop = True
    while loop == True:
        print("\nGUEST MENU\na. Search for information\nb. Quit")
        choice = input("Please enter the letter corresponding to your choice: ").strip().lower()
        if choice == 'a':
            search(cur)
        elif choice == 'b':
            print("Exiting database. Thank you!")
            loop = False
        else:
            print("Error. Invalid selection.")

def main():
    print("\nARTS MUSEUM DATABASE\n")
    print("MENU - Role Selection:\na. Admin\nb. Data Entry User\nc. Guest") # Prints roles taht you can choose from.
    role_validity = False
    while role_validity == False:
        role_selection = input("Please enter the letter corresponding to your selection: ").strip().lower() # Strips the input of any whitespace and converts any uppercase to lowercase for increased accuracy.
        if role_selection == 'a' or role_selection == 'b' or role_selection == 'c': # Checks that a valid input has been entered.
            role_validity = True
        else:
            print("Error. Invalid role selected. Please re-enter your role.")
    
    if (role_selection == 'a') or (role_selection == 'b'): 
        connection = False
        while connection == False: # Creates loop until a valid connection has been established.
            user_username = input("Please enter your username: ")
            print("Please enter your password: ", end = "")
            user_password = maskpass.askpass(mask = "*") # Hides the localhost (or user) password as it is being entered.
            try: # Uses user information to establish a connection to the SQL database.
                cnx = mysql.connector.connect(
                    host = '127.0.0.1',
                    port = 3306,
                    user = user_username,
                    password = user_password,
                    database = "ARTSMUSEUM")
                if cnx.is_connected(): # Checks that a valid connection has been established before exiting loop.
                    connection = True
            except mysql.connector.Error: # Exception handling for the case that an invalid username or password has not been entered (resulting in an invalid connection).
                print("Invalid username or password. Please re-enter details.")
    
    elif role_selection == 'c': # Creates an SQL connection (with limited permissions) for a guest user without the need of a username or password. This connects to a role created in the SQL script.
        cnx = mysql.connector.connect(
            host = '127.0.0.1',
            port = 3306,
            user = "guest",
            password = None,
            database = "ARTSMUSEUM")
    
    cur = cnx.cursor(buffered = True) # Creates an SQL cursor using the connection previously established.
    cur.execute("use ARTSMUSEUM") # Connects to the ARTSMUSUM database.
    print()

    if role_selection == 'a':
        admin(cur, cnx)
    elif role_selection == 'b':
        data_entry(cur, cnx)
    else:
        guest(cur)
    
    cnx.close() # Closes the connection as the program is exited.

if __name__ == "__main__":
    main()