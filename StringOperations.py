

inputlist = list(input("\nEnter String:").split())

numberWords = 0
for i in inputlist:
    numberWords += 1



def findLongWord():
    
    recordWord = ""
    recordCount = 0

    for word in inputlist:
        letterCount = 0
        for letter in word:
            letterCount += 1
        
        if letterCount > recordCount:
            recordWord = word
            recordCount = letterCount
        elif letterCount == recordCount:
            recordWord = recordWord + ", " + word
    
    print(recordWord)



def characterOccurrence():

    character = str(input("Enter character to check occurence for:"))
    characterCount = 0

    for word in inputlist:
        for letter in word:
            if letter == character:
                characterCount += 1

    print(characterCount)



def palindromeChecker():

    characterList = []

    for word in inputlist:
        for letter in word:
            characterList.append(letter)

    if characterList == characterList[::-1]:
        print("Given string is Palindrome")

    else:
        print("Given string is not Palindrome")



def Indexer():
    substr = str(input("Enter word to find index for:"))
    wordnumber = -1
    for word in inputlist:
        wordnumber += 1
        if word == substr:
            print("[", wordnumber, "]:", substr)
            break



def eachWordOccurrence():

    noDuplicateList = []

    for word in inputlist:
        if word not in noDuplicateList:
            noDuplicateList.append(word)

    for word1 in noDuplicateList:
        wordCount = 0
        for word2 in inputlist:
            if word1 == word2:
                wordCount += 1

        print(word1,":",wordCount)



def menu():
    print('''
    =============================================================
    1] Show word with longest length
    2] Find the frequency of occurrence of particular character
    3] Check whether given string is palindrome or not
    4] Show index of first occurrence of a particular word
    5] Show frequency of occurrence of each word
    =============================================================
    ''')

    switch = int(input("Select the operation to be performed:"))

    if switch == 1:
        print("\n The longest word is:")
        findLongWord()
        exitMenu()

    elif switch == 2:
        print("\n")
        characterOccurrence()
        exitMenu()

    elif switch == 3:
        print("\n")
        palindromeChecker()
        exitMenu()

    elif switch == 4:
        print("\n")
        Indexer()
        exitMenu()

    elif switch == 5:
        print("\n")
        eachWordOccurrence()
        exitMenu()

    else:
        print("Please make a valid selection :)")
        print("Returning back to menu....")



def exitMenu():
    print('''
    ==========================
    1] Go back to main menu
    2] Exit
    ==========================
    ''')
    switch2 = int(input("Select:"))

    if switch2 == 1:
        menu()

    elif switch2 == 2:
        exit()

    else:
        print("Please make a valid selection :)")
        exitMenu()


menu()
