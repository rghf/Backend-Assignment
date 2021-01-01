import threading 
#threading is imported in order to run multiple threads (tasks, function calls) at the same time
from threading import*
import time

dict={} #'dict' is the dictionary where we will store the data on which we will perform CRD operations.


# CRD first one C i.e. Create operation
def rcreate(key,value,timeout=0):
    if key in dict:
        print("error-message: value already present") #error message displays
    else:
        if(key.isalpha()):  # isalpha() method as we need to deal with string so it'll return True if all the characters are alphabet letters (a-z)
            if len(dict)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file storing data size is less than 1GB and JSON object value is capped at 16KB.
                if timeout==0: # to check the limit of max time for calling a function or running a command
                    m=[value,timeout]
                else:
                    m=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    dict[key]=m
            else:
                print("error-message: Memory limit size exceeded!! ")#error message displays
        else:
            print("error-messge: Invalid name of key!! It must contain only alphabets, no special characters or numbers !!!!!")#error message displays

#CRD second one R for read operation            
def rread(key):
    if key not in dict:
        print("error: key not exists in database. Retry with a valid key") #error message displays
    else:
        current_time=dict[key]
        if current_time[1]!=0:
            if time.time()<current_time[1]: #comparing the current time with expiry time to check if key is available for Read operations.
                JSONstring=str(key)+":"+str(current_time[0]) #returning the value in the format of JasonObject 
                return JSONstring
            else:
                print("error-message: Time-to-Live of",key,"has been expired") #error message displays
        else:
            JSONstring=str(key)+":"+str(current_time[0])
            return JSONstring

#CRD third one D for delete operation

def rdelete(key):
    if key not in dict:
        print("error-message: given key does not exist in database. Please enter a valid key") #error message displays
    else:
        current_time=dict[key]
        if current_time[1]!=0:
            if time.time()<current_time[1]: #comparing the current time with expiry time to check if key is available for Delete operations.
                del dict[key]
                print("key is successfully deleted") # if yes then display the message of successful deletion
            else:
                print("error-message: Time-To-Live of",key,"has been expired") #error message displays
        else:
            del dict[key]
            print("Successful deleteion of the key !!!!")

