# This is my method for testing code and preventing crashes.
# try -- except -- else -- finally

try: # The code in this block is ALWAYS executed
    myVariable = 1
    print(myVariable)
    mystring = "Five"
    print(float(mystring))

except ValueError: # This code will run If there Is an error(exception)
    print("There is an incorrect variable name in your code")
except: 
    print("Something else went wrong")
else: # runs if no errors
    print('Code executed correctly with no exceptions.\n')
finally: # Always runs
    print("I'll be back.\n")        
#except NameError:
#    pass