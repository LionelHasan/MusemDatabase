# Arts Museum Database

### Description
The Arts Museum Database is a group final project created for "ENSF 300 Software Engineering Practices for Data Management". This project is a terminal-based application that uses Python to interface with a database created using MySQL. Depending on the role of the user (guest, data-entry, or admin) different permissions and options will be provided to query and manipulate data.

This repository contains a project information pdf file, an SQL file, and two Python files. The project information pdf contains information regarding task distribution among group members, software notes/installations, user login information, the enhanced entity relationship diagram (EERD), database design decisions/assumptions, and the relational diagram. The SQL file script is used to initialize and create the database. The Python file titled "ArtsMuseumInterface.py" contains the full Python script created by the entire group. The Python file titled "ArtsMuseumInterface - Liam Mah.py" contains code that only Liam Mah wrote (in addition to the SQL script file).

### Installation and Use
To run the application created in this repository, please follow the following steps:
1. Run the "ARTMUSEUM.sql" script in an SQL application (such as MySQL Workbench) to initialize the database
2. Install Python (if not already installed)
3. Import "ArtsMuseumInterface.py" into an IDE
4. Install 'maskpass' in the virtual environment via "pip install maskpass"
5. Install 'MySQL Connector' in the virtual environment via "python -m pip install mysql-connector-python"
6. Run the script

Usernames and passwords are required to test the data entry and admin roles. Below are the credentials for each role. Note that the user can also use the username "root" and the localhost password to sign into these roles.

#### Admin Information
- Username: db_admin
- Password: "adminpass"

#### Data Entry Information
- Username: data_entry
- Password: dataentrypass

### Credits
This project was created as a group final project for "ENSF 300 Software Engineering Practices for Data Management" under the Department of Electrical and Software Engineering at the University of Calgary. The project was created by: Liam Mah, Theodore Hoang, Eric Mei, and Lionel Hasan.
