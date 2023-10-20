
#/////////////////////////////////////////////////
'''
 Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength. 

●       Implement a Python function called check_password_strength that takes a password string as input.
●       The function should check the password against the following criteria:
○       Minimum length: The password should be at least 8 characters long.
○       Contains both uppercase and lowercase letters.
○       Contains at least one digit (0-9).
○       Contains at least one special character (e.g., !, @, #, $, %).
●       The function should return a boolean value indicating whether the password meets the criteria.
●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.
●       Provide appropriate feedback to the user based on the strength of the password. 
'''
#////////////////////////////////////////////////////////////////

class password :

    

    def check_password_strength (self) :

        '''
        This functions checks given input of password satisfies the all
        the required security criteria for a strong password and
        accordingly checks and provides the feedback to user about provided
        password  acceptance, if not the missing guidance.

        Here function is designed to use the sets intersection function
        to see the commonality w.r.to all upper / lower cases / numbers and special character
        pool and finding out the input string have those elements.

        #1 min password char length of 8 check
        #2 atleast one upper case char
        #3 atleast one lower case char
        #4 atleast one number
        #5 atleast on special chat

        if all the above checks are meet, function returns "true" else "false"

        '''

        pwd_input = input ("Please enter the password: ->")
        charUpper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        charLower = ["a","b","c","e","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        num = ["0","1","2","3","4","5","6","7","8","9"]
        splChar = ["~","!","@","#","$","%","^","&","*","(",")","_","?","<",">","/","{","}"]

        set_pwdinput = set (pwd_input)
        set_charUpper = set (charUpper)
        set_charLower = set (charLower)
        set_num = set (num)
        set_splChar = set (splChar)

        if len(pwd_input) >= 8 :

            value = "true"

            if set_pwdinput.intersection(set_charUpper) :
                pass
            
            else :
                print ("password must have at least a Upper case letter")
                value = "false"
            
            if set_pwdinput.intersection(set_charLower) :
                pass
            
            else :
                print ("password must have at least a Lower case letter")
                value = "false"
            
            if set_pwdinput.intersection(set_num) :
                pass
            
            
            else :
                print ("password must have atleast a digit")
                value = "false"
            
            if set_pwdinput.intersection(set_splChar) :
                pass

            elif set_pwdinput.intersection(set_charUpper) and set_pwdinput.intersection(set_charLower) and set_pwdinput.intersection(set_num) and set_pwdinput.intersection(set_splChar) :

                value = "true"

            
            else :
                print ("password must have atleast a Special Character")
                value = "false"
            
            
        else :

            print ("Password length should be minimum 8 characters, Hence this Password not accepted !!")
            print ("Please try again !!")
            value = "false"

        
        return value

# object Initation to trigger the pwd check function    
  
checkpwd_case1 = password ()

result = checkpwd_case1.check_password_strength()



if  (result == "true") :
    print ("Given Password is Perfectly Met the password criteria")

else :

    print("Given Password is Doesn't met the password criteria")

#//////////////////////////////////////////////////////////////////////////////////
'''
Q2. As a DevOps engineer, it is crucial to monitor the health and performance of servers. Write a Python program to monitor the health of the CPU. Few pointers to be noted:

●       The program should continuously monitor the CPU usage of the local machine.
●       If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message should be displayed.
●       The program should run indefinitely until interrupted.
●       The program should include appropriate error handling to handle exceptions that may arise during the monitoring process.

Hint:

●       The psutil library in Python can be used to retrieve system information, including CPU usage. You can install it using pip install psutil.
●       Use the psutil.cpu_percent() method to get the current CPU usage as a percentage.

Expected Output:

Monitoring CPU usage...

Alert! CPU usage exceeds threshold: 85%

Alert! CPU usage exceeds threshold: 90%

... (continues until interrupted)
'''
#/////////////////////////////////////////////////////////////////////////////
import psutil,time


class cpuHealthMonitor :

    def cpuUsageMonitor (self) :

        '''

        Here, function "cpuUsageMonitor" put on for continuos monitoring of the
        CPU usage , in  a while loop , where it keeps checking the cpu usage percent.
        if it exceeds 80, user will get alert message.
        If required, program run can be intrrupted through a keyboard (ctrl+c).

        '''

        print ("Monitoring CPU usage...")

        while True :

            try :
                          
                CPU_Usage = psutil.cpu_percent (10)
                

                if CPU_Usage >= 80.0 :
                    print (f" *** Alert !! :: CPU Usage is Exceeding its threshold @ {CPU_Usage} % ")
            
            except KeyboardInterrupt:

                time.sleep (1)

     
# Object Initation to trigger the CPU usage function 

localcpucheck = cpuHealthMonitor ()

localcpucheck.cpuUsageMonitor ()

#////////////////////////////////////////////////////////////////////////////////////
'''
Q4. In DevOps, performing regular backups of important files is crucial:

●       Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.
●       The script should copy all files from the source directory to the destination directory.
●       Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the file name to ensure uniqueness.
●       Handle errors gracefully, such as when the source directory or destination directory does not exist.
 

Sample Command:
python backup.py /path/to/source /path/to/destination

By running the script with the appropriate source and destination directories, it should create backups of the files in the source directory, ensuring unique file names in the destination directory.
'''
#////////////////////////////////////////////////////////////////////////////////////////////
import os,sys,shutil


class backUpData :

    
    def backUpExecute (self) :

        '''
         both source dir path for backup to be taken
         and destination dir path for backup to be done,
         will be given as input arguments at the execution of python file.

         In this function, backUpExecute will verify both paths
         and execute backup using the shutil.copytree with
         all exceptions handlings and confirmatios.

        '''


        path_to_source = sys.argv[1]
        path_to_desitnation = sys.argv[2]


        if os.path.isdir (path_to_source) :
            print ("Source path verified")
        
        else :

            print ("Issue in source path")

        if os.path.isdir (path_to_desitnation) :
            print ("Destination path verified")
        
        else :

            print ("Issue in Destination path")    


        try :
            
            if os.path.isdir (path_to_source) :
                shutil.copytree (path_to_source, path_to_desitnation,copy_function = shutil.copy)
            
                print ("backup is in process !!")
            
            if os.path.isdir (path_to_desitnation) :

                print ("backup successful")
            
            
            else :

                print ("Issue with Directory paths of Source and destinations")
            


        except shutil.Error :

            print ("shutil.error occurred, backup Failed !!")

# Object Initation to trigger the backupexecution function 

backup1 = backUpData ()

backup1.backUpExecute ()


#script usage -
#<python.exe> backup.py <source_dir> <destination_dir>
#C:/Python311/python.exe c:/my_learning_2023_24/devops_HeVi/Module_1_Step_Flask_Python/
#graded_assignment_python/Question_4_backup/backup.py "C:\xyz" "C:\to_my_backup\20oct2023"
#where desintation Dir, "c:\to_my_backup" Directory exists,
#where 20Oct2023 sub directory will be created dynamically throuhg shutil.copytree 

#/////////////////////////////////////////////////////////////////////////////////////////

 


