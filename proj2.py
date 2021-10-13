import mysql.connector
from mysql.connector import errorcode
import os
from decouple import config
import sys
# print(config('USER'))
# print(config('PASSWORD'))
# print(config('HOST'))
# print(config('DATABASE'))


try:
    # Start connection to database using env file
    cnx = mysql.connector.connect(user=config('USER'), password=config('PASSWORD'), host=config('HOST'))
    # initialize cursor for doing sql queries or mysql commands
    cursor = cnx.cursor()
    # use cs given database and show tables within it
    # can be commented out if desired for testing
    cursor.execute("USE " + config('DATABASE'))
    cursor.execute("SHOW TABLES")
# exception catcher for any errors
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
    exit()
# else if used if there are no exceptions that mean the connection is open
else:
    print("Connection Open")
  
# main function where selection of project questions occur
def main():
    # test connection and see tables
    # print(cursor)
    # for x in cursor:
    #     print(x) 
    
    # arguement list
    args = sys.argv
    argsLength = len(args)
    print(argsLength)
    
    # ensure first arguement is a question number else give message and close connection
    try:
        qno = int(args[1])
        # ensure number is a valid question number else give message and close connection
        if(qno >= 1 and qno <= 8):
            # print arguments for testing
            print(args)
            # list of question numbers to call associated function.
            # Any with a parameter are checked to make sure user inputted correctly
            # Var names are given for better readability of arguments
            if(argsLength > 2 and qno == 1):
                streetName = args[2]
                qno1(streetName)
                
            elif(argsLength > 2 and qno == 2):
                schedSystem = args[2]
                qno2(schedSystem)
                
            elif(qno == 3):
                qno3()
                
            elif(argsLength > 2 and qno == 4):
                phoneNo = args[2]
                qno4(phoneNo)
                
            elif(qno == 5):
                qno5()
                
            elif(argsLength > 2 and qno == 6):
                modelNo = args[2]
                qno6(modelNo)
                
            elif(qno == 7):
                qno7()
                
            elif(qno == 8):
                qno8()
                
            else:
                closeConnection("Second arguement needed for question " + str(qno) + ".")
                return
        else:
            closeConnection("First arguement is not a valid question number.")
            return
    except:
        closeConnection("First arguement is not a number.")
        return
        
    # close connection when program finishes
    cnx.close();
    print('Connection Closed')

# function to close connection with a message
def closeConnection (msg):
    cnx.close()
    print(msg)
    print('Connection Closed')

# Question 1 function
# Find the sites that are on a given street (i.e., the address contains the street name 
# (case insensitive)). Show the detailed information of each site. To get the answer of this question, 
# the command to run is python proj.py 1 <param_street_name> (for Python)
def qno1 (streetName):
    print("logic for qno1")

# Question 2 function
# Find the digital displays with a given scheduler system. Show their serial nos, model 
# nos, and the names of technical supports who specialize their models. The scheduler system 
# should be a parameter input through the main program. To get the answer of this question, the 
# command to run is python proj.py 2 <param_schedular_system> (for Python)
def qno2 (schedSystem):
    print("logic for qno2")
    
# Question 3 function
# List the distinct names of all salesmen and the number of salesmen with that name. 
# The output should be in the ascending order of the salesmen name. If multiple salesmen have the 
# same name, show all the attribute values for those salesmen. For instance, if the Salesman 
# relation contains the following 4 records 
# (1, ’Peter’, ’M’), (2, Mary, ’F’), (3, ’John’, ’M’), (4, Mary, ’F’). 
# The output should be: 
# Name cnt 
# ------------------
# John 1 
# Mary 2 (2,Mary,’F’),(4,Mary,’F’)
# Peter 1
# To get the answer of this question, the command to run is python proj.py 3 (for python)
def qno3 ():
    print("logic for qno3")

# Question 4 function
# Find the clients with a given phone no. The phone no should be a parameter input 
# through the main program. To get the answer of this question, the command to run is python proj.py 4 <param_phone_no> (for Python)
def qno4 (phoneNo):
    print("logic for qno4")
    
# Question 5 function
# Find the total working hours of each administrator. Display the administrators’ 
# employee ids, names, and total working hours in ascending order of the total working hours. To 
# get the answer of this question, the command to run is
def qno5 ():
    print("logic for qno5")
    
# Question 6 function    
# Find the technical supports that specialize a specified model. Display the names of 
# those technical supports. The specified model no should be a parameter input through the main 
# program. To get the answer of this question, the command to run is python proj.py 6 <param_model_no> (for Python)
def qno6 (modelNo):
    print("logic for qno6")
 
# Question 7 function
# Order the salesmen with descending order of their average commission rates. Display 
# each salesman’s name and the average commission rate. To get the answer of this question, the 
# command to run is python proj.py 7 (for Python)
def qno7 ():
    print("logic for qno7")
    
# Question 8 function
# Calculate the number of administrators, salesmen, and technical supports. Display the 
# results in the following format. 
# Role cnt 
# ------------------
# Administrator 10 
# Salesmen 40 
# Technicians 20 
# To get the answer of this question, the command to run is python proj.py 8 (for Python)
def qno8 ():
    print("logic for qno8")

# calls main
if __name__=="__main__":
    main()