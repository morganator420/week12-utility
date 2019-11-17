#Morgan Stoner
#CSCI 102 - Section E
#Week 12 - Part A

################################################
########   Function 1 : PrintOutput    #########
################################################

def PrintOutput(input_string):
    print("OUTPUT",input_string)

################################################
########   Function 2 : LoadFile       #########
################################################

def LoadFile(file_name):
    myJournal = open(file_name)
    contents = myJournal.readlines()
    myJournal.close()
    return contents
    

