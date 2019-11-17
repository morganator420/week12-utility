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
    
################################################
########   Function 3 : UpdateString   #########
################################################

def UpdateString(in_string,letter,index):
    my_list = []
    for i in range(0,len(in_string)):
        my_list.append(in_string[i])
    my_list[index] = letter
    word = ''.join([str(char) for char in my_list])
    PrintOutput(word)
