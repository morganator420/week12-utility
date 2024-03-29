#https://github.com/morganator420/week12-utility.git
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

################################################
########   Function 6 : Union          #########
################################################

def Union(list1,list2):
    newlist = []
    check = 'Y'
    value = "["
    for i in list1:
        for j in list2:
            if i == j:
                check = 'O'
        if check == 'O':
            check = 'Y'
            value = i
            continue
        else:
           newlist.append(i)
    if value != "[":
        newlist.append(value)
    for i in list2:
        for j in list1:
            if i == j:
                value2 = i
                check = 'O'
        if check == 'O':
            check = 'Y'
            continue
        else:
           newlist.append(i)
    return newlist

################################################
########   Function 7 : Intersection   #########
################################################

def Intersection(list1,list2):
    newlist = []
    for i in list1:
        for j in list2:
            if i == j:
                newlist.append(i)
    return newlist

################################################
########   Function 8 : NotIn          #########
################################################

def NotIn(list1,list2):
    newlist = []
    for i in list1:
        for j in list2:
            if i != j:
                continue
            else:
                newlist.append(i)
    checklist = []
    for i in range(0,len(list1)):
        for j in range(0,len(newlist)):
            if list1[i] == newlist[j]:
                checklist.append(i)
    checklist.append(0)
    for i in range(0,len(checklist) - 1):
        list1.pop(checklist[i])
        checklist[i+1] -= 1

    return list1

players = ["Mary", "Cody", "Joe", "Jill", "Xai", "Bodo"]               
players2 = ["Melvin", "Martian", "Baka", "Xai", "Cody"]
scores = [5, 8, 10, 6, 10, 4, 10]     
print("OUTPUT", NotIn(players2, players))


    
