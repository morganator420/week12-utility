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

################################################
########   Function 4 : FindWordCount  #########
################################################

def FindWordCount(my_list,in_string):
    total = 0
    for i in range(0,len(my_list)):
        if my_list[i] == in_string:
            total += 1
    return total

################################################
########   Function 5 : FindWordCount  #########
################################################

def ScoreFinder(players,scores,in_string):
    string = in_string.lower()
    check = 'O'
    for i in range(0,len(players)):
        check1 = players[i].lower()
        if check1 == string:
            check = check1
            index = i
    if check == 'O':
        PrintOutput("player not found")
        return
    else:
        score = scores[index]
        output = in_string + " got a score of " + str(score)
        PrintOutput(output)


