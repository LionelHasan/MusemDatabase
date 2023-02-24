import mysql.connector
import maskpass

def command(cur, cnx): # Admin function for executing an SQL command.
    command_choice = input("Enter 'a' to execute a query command. Enter 'b' to execute a data base editing command (insert, update, delete, etc.)\nInput: ").strip().lower()
    if command_choice == 'a':
        command_string = input("Please enter your SQL command as you would in the workbench (without the semicolon at the end): ")
        try:
            cur.execute(command_string)
            col_names = cur.column_names
            search_result = cur.fetchall()
            print("Search found",len(search_result)," Entries:\n")
            header_size = len(col_names)
            for i in range(header_size):
                print("{:<20s}".format(col_names[i]),end='')
            print()
            print(20*header_size*'-')
            for row in search_result:
                for val in row:
                    print("{:<20s}".format(str(val)),end='')
                print()
        except:
            print("Error. Invalid SQL command entered. Command unsuccesful.\n")

    elif command_choice == 'b':
        command_string = input("Please input your SQL command as you would in the workbench (without the semicolon at the end): ")
        try:
            cur.execute(command_string)
            cnx.commit()
        except:
            print("Error. Invalid SQL command entered. Command unsuccessful.\n")

    else:
        print("Error. Invalid Selection.\n")


def new_script(cur, cnx):
    # Admin function for executing an SQL script.
    admin_script = input("Please enter the entire file name of the script you would like to run (Cannot be used to return data, scripts can only be ran to manipulate data) ")
    file_o = open(admin_script,'r')
    admin_file = file_o.read()
    commands = admin_file.split(';')

    try:
        i = 0
        while i < len(commands):
            cur.execute(("%s" % (commands[i])))
            cnx.commit()
            i = i + 1 
    except:
        print(("%s" % (admin_file)))
        print("An error has occured")

def search(cur):    # Guest and data entry user function for searching up data via a series of prompts.
    loop = True
    yes_no = ["Y","N"]
    while loop == True:
        x = 20
        try_go = True
        print("\nWhich topic would you like to search for?\na. Art Objects\nb. Artists\nc. Quit")
        choice = input("Please enter the letter corresponding to your choice: ").strip().lower()
        if choice == 'a':
                while(True):
                    print("1. Details on paintings\n2. Details on statues\n3. Details on sculptures\n4. Details on other types of art objects\n5. List of all art objects\n6. Return to search menu")
                    art_object = input("Please select which type of art object you are interested in: ")
                    if art_object == "1":
                        ID = input("Enter the ID number of the painting you are looking for (press enter to view all): ") or None
                        if ID == None:
                            instr = "select* from painting"
                            
                        else:
                            instr = "select* from painting where paint_id_no = %(id)s"
                        break

                    elif art_object == "2":
                        ID = input("Enter the ID number of the statue you are looking for (press enter to view all): ") or None
                        if ID == None:
                            instr = "select* from statue"
                        else:
                            instr = "select* from statue where stat_id_no = %(id)s"
                        break
                        
                    elif art_object == "3":
                        ID = input("Enter the ID number of the sculpture you are looking for (press enter to view all): ") or None
                        if ID == None:
                            instr = "select* from sculpture"
                            
                        else:
                            instr = "select* from sculpture where scul_id_no = %(id)s"
                        break
                        
                    elif art_object == "4":    
                        ID = input("Enter the ID number of the other type of art object you are looking for (press enter to view all): ") or None
                        if ID == None:
                            instr = "select* from other"
                            
                        else:
                            instr = "select* from other where other_id = %(id)s"
                        break
                        
                    elif art_object == "5":
                         ID = input("Enter the ID number of the art_object you are looking for (press enter to view all): ") or None
                         ex_choice = input("Would you like to see which exhibition your art piece(s) were shown? (Y or N): ").upper().strip()
                         if ex_choice not in yes_no:
                            print("Invalid input, please try again\n")
                            continue

                         if ex_choice == "Y":
                            if ID == None:
                                instr = "select ID_NO, COLLECTION_NAME, START_DATE,END_DATE, e.EXHIBITION_NAME from shown_during as s, art_object, exhibition as e where art_id_no = id_no and e.exhibition_name = s.exhibition_name"
                            else:
                                instr = "select ID_NO,COLLECTION_NAME ,START_DATE, END_DATE, e.EXHIBITION_NAME from shown_during as s, art_object, exhibition as e where art_id_no = id_no and e.exhibition_name = s.exhibition_name and id_no = %(id)s"

                         elif ID == None:
                            instr = "select ID_NO, EPOCH, YEAR_MADE, CULTURE_OR_COUNTRY, TITLE from art_object"  
                         else:
                            instr = "select ID_NO, EPOCH, YEAR_MADE,CULTURE_OR_COUNTRY, TITLE from art_object where id_no = %(id)s"
                         break
                    
                    elif art_object == "6":
                        try_go = False 
                        break
                        
                    else:
                        print("Invalid selection, please try again")
                    
        elif choice == 'b':
            while(True):
                ID = input("Please enter the name of the artist you are searching for(press enter to view all) or enter \"a\" to return to search menu: ") or None
                if ID == "a":
                    try_go = False 
                    break
                artist_art = input("Would you like to see the the art pieces these artist(s) created? (Y or N): ").upper().strip()
                if artist_art not in yes_no:
                        print("Invalid input, please try again")
                        continue
                if artist_art == "Y" and ID == None:
                    instr = ("select A.ARTIST_NAME, TITLE FROM ART_OBJECT, CREATED_BY AS A, ARTIST AS B WHERE A.ARTIST_NAME = B.ARTIST_NAME AND A.ART_ID_NO = ID_NO")
                    x = x+5
                    break
                elif artist_art == "Y" and ID != None:
                    instr = ("select A.ARTIST_NAME, TITLE FROM ART_OBJECT, CREATED_BY AS A, ARTIST AS B WHERE A.ARTIST_NAME = B.ARTIST_NAME AND A.ART_ID_NO = ID_NO AND A.ARTIST_NAME = %(id)s")
                    x = x+10
                    break
                elif artist_art == "N":
                    instr = "select ARTIST_NAME"
                    art_descr = input("Would you like to see the artist's artist description? (Y or N): ").upper().strip()
                    if art_descr not in yes_no:
                        print("Invalid input, please try again")
                        continue
                    if art_descr == "Y" and ID == None:
                        instr = "select ARTIST_NAME,MAIN_STYLE,ORIGIN_COUNTRY, ARTIST_DESCRIPTION FROM ARTIST"
                        x = x+10
                        break
                    if art_descr == "Y" and ID != None:
                        instr = "select ARTIST_NAME,MAIN_STYLE,ORIGIN_COUNTRY, ARTIST_DESCRIPTION FROM ARTIST WHERE ARTIST_NAME = %(id)s "
                        x = x+10
                        break
                    art_epoch = input("Would you like to see the artist's epoch? (Y or N): ").upper().strip()
                    if art_epoch == "Y":
                        instr = instr + ", EPOCH"
                    art_country = input("Would you like to see the artist's country of origin? (Y or N): ").upper().strip()
                    if art_country == "Y":
                        instr = instr + ", ORIGIN_COUNTRY"
                    art_born = input("Would you like to see the artist's date of birth? (Y or N): ").upper().strip()
                    if art_born == "Y":
                        instr = instr + ", DATE_BORN"
                    art_die = input("Would you like to see the artist's date of death? (Y or N): ").upper().strip()
                    if art_die == "Y":
                        instr = instr + ", DATE_DIED"
                    if art_die not in yes_no or art_born not in yes_no or art_country not in yes_no or art_epoch not in yes_no:
                        print("Invalid input, please try again")
                        continue
                    if ID != None:
                        instr = instr + " from artist where artist_name = %(id)s" 
                    else:
                        instr = instr + " from artist"
                    x = x+5
                    break

        elif choice == 'c':
            print("Exiting query/search mode.")
            main()
        else:
            print("Error. Invalid selection.")
            continue
        
        if try_go == True:
            try:
                if ID != None:
                    cur.execute(instr,{"id":ID})
                else:
                    cur.execute(instr)

            except:
                print("Please try you input again")
        
            rows = cur.fetchall()
            attr_names = cur.column_names
            print()
            for attr in attr_names:
                print("{:<{x}}".format(attr,x=x),end="")
            for row in rows:
                print()
                for col in row:
                    if col == None:
                        col = "Null"
                    print("{:<{x}}".format(col,x=x),end="")
            print()


def add(cur, cnx): # Data entry user function for inserting a tuple.

    table_choice = input("Please enter the name of the table that you would like to insert a row into: ")
    cur.execute(("select column_name from information_schema.columns where table_schema = 'ARTSMUSEUM' and table_name = '%s' order by ordinal_position") % (table_choice))
    result = cur.fetchall()
    print(("Please enter the following the values for the following attributes in order: \n %s \n") % (','.join(str(tup) for tup in result)))
    i = 0
    attribute_list = []
    while i < len(result):
        attribute_list.append(input("Please enter the value for a single attribute \n"))
        i = i+1
    
    j = 0 
    i = 1
    execution_string = "INSERT into %s VALUES (" % (table_choice)
    while j < len(result):
        execution_string = execution_string  + " " +"'"+ attribute_list[j]+"'"
        if i < len(result):
            execution_string = execution_string + ","
        i = i + 1
        j = j + 1
    execution_string = execution_string + ")"
    try:
        cur.execute(execution_string)
        print("The following command has been executed %s" % (execution_string))
        cnx.commit()
    except: 
        print("an error has occured")
    
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
        if choice == 'a':   # Add/insert tuples of data
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