import operator

def readInFile(fileName):
    # reads in txt file of Grimm's tales
    # makes list wordList of every word sequentially without punctuation
    # returns wordList
    file = open(fileName)
    fileList = []
    wordList = []
    for line in file:
        fileList.append(line.strip().split())
        # print(line.strip().split())

    #get rid of punctuation for easier comparison
    for line in fileList:
        for elem in line:
            elem = elem.strip("'")
            elem = elem.strip(":")
            elem = elem.strip(";")
            elem = elem.strip(".")
            elem = elem.strip(",")
            elem = elem.strip("?")
            elem = elem.strip("!")
            elem = elem.strip("'")
            elem = elem.strip("’")
            elem = elem.strip(",")
            elem = elem.strip("!")
            elem = elem.strip("'")
            elem = elem.strip(".")
            elem = elem.strip("?")
            elem = elem.strip("‘")
            # print(elem)
            wordList.append(elem)
    return wordList
    # for elem in wordList:
    # print(elem)

def makingNounLists(femaleNounList, maleNounList, genderNeutralNounList):
    # takes female, male, and gender neutral noun lists as defined in main
    # makes one nounList (so we have separate options or one combined option)
    nounList = []
    for word in femaleNounList:
        nounList.append(word)
    for word in maleNounList:
        nounList.append(word)
    for word in genderNeutralNounList:
        nounList.append(word)
    return nounList

def makeAdjCorpus(adjFileName):
    # reads in file of adjectives
    # for each adjective, gets rid of number and dot, makes lower case
    # then if no number there, adds adj
    # if there's a 1, adds version of adjective that also work (-er, -est, etc, according to letters in word)
    # if it has a 2 or 3 just don't add that word
    # we tried added the noun-adjectives (with 2s)
    # but our program, looking only for an exact word,
    # identified nouns which cause confusion
    # returns a set of all of these commonly used adjectives
    adjFile = open(adjFileName)
    adjSet = set()
    for elem in adjFile:
        dex = elem.find(".")
        elem = (elem[dex + 1:]).strip().lower()
        # print(elem.split())
        if len(elem.split()) == 1:
            # print(elem)
            adjSet.add(elem)
        else:
            if elem.split()[1] == '1':
                adjSet.add(elem.split()[0])
                #this one didn't follow suit--assuming some others didn't and here is an issue with our method
                if elem.split()[0] == 'wet':
                    adjSet.add("wettest")
                    adjSet.add("wetter")
                elif elem.split()[0][-1] == 'y':
                    adjSet.add(elem.split()[0][0:-1] + "ier")
                    adjSet.add(elem.split()[0][0:-1] + "iest")
                elif elem.split()[0][-1] == 'e':
                    adjSet.add(elem.split()[0] + "r")
                    adjSet.add(elem.split()[0] + "st")
                else:
                    adjSet.add(elem.split()[0] + "er")
                    adjSet.add(elem.split()[0] + "est")
            if elem.split()[1] == '2':
                # adjSet.add(elem.split()[0])
                # print((elem[0:dex2-1]).strip(" "))
                pass
            if elem.split()[1] == '3':
                #adjSet.add(elem.split()[0])
                pass
                # print((elem[0:dex3-1]).strip(" "))
    return adjSet

def compileDictionary(wordList, nounList, adjSet):
    # makes a fictionary, goes through wordlist
    # for each word, checks if there's a dictionary of that word
    # if not, initializes one. Then goes 2 back from word and 1 up from word
    # checks if words there are in the adjective set
    # if so, it adds them to the dictionary for that word
    # either by upping the value at that adjective's key, or adding that key
    #
    # returns dictionary of dictionaries where the keys of the first are nouns,
    # and the values are dictionaries where the keys are adjectives
    # and the values are counts of that adjective for that noun.
    d = {}
    for i in range(0, 2):
        # just for first two word where we cannot go back 2,
        # so we check the word after the noun (and one more for wiggle-room) for adjectives
        word = wordList[i]
        if word in nounList:
            if word not in d:
                d[word] = {}
            for j in range(0, 2):
                if wordList[i + j] in adjSet:
                    if wordList[i + j] not in d[word]:
                        d[word][wordList[i + j]] = 0
                    d[word][wordList[i + j]] += 1

    for i in range(2, len(wordList) - 1):
        # For words where index errors will not be a problem as we can go 2 back and one forward
        word = wordList[i]
        if word in nounList:
            if word not in d:
                d[word] = {}
            for j in range(-2, 1):
                if wordList[i + j] in adjSet:
                    if wordList[i + j] not in d[word]:
                        d[word][wordList[i + j]] = 0
                    d[word][wordList[i + j]] += 1

    # for the last word since we cannot check the word in front of it
    # one word so don't need a for loop but in place from playing around with numbers,
    # plus keeps things parallel
    for i in range(len(wordList) - 1, len(wordList)):
        word = wordList[i]
        if word in nounList:
            if word not in d:
                d[word] = {}
            for j in range(-2, 0):
                if wordList[i + j] in adjSet:
                    if wordList[i + j] not in d[word]:
                        d[word][wordList[i + j]] = 0
                    d[word][wordList[i + j]] += 1
    return d

if __name__ == '__main__':

    femaleNounList = ["woman", "queen's", "wife", "mother", "princess", "gretel", "woman" "daughter", "queen", "girl",
                      "bride", "youth", "servant", "lady", "friend", "maid", "sister", "witch", "elsie", "fairy",
                      "maiden", "rapunzel", "grandmother", "princesses", "girls", "catherine", "enchantress", "mrs",
                      "daughters", "mother's", "sisters"]
    maleNounList = ["dwarf", "dwarfs", "king", "man", "father", "son", "hans", "king's", "boy", "prince", "master",
                    "husband", "hansel", "soldier", "brothers", "brother", "huntsman", "men", "fisherman", "fellow",
                    "huntsmen", "father's", "shepherd", "doctor", "giants", "sultan", "god", "robbers", "countryman",
                    "gardener", "merchant", "thieves", "thief", "mayor", "princes", "bridegroom"]
    genderNeutralNounList = ["child", "children", "peasant", "people", "wretch", "guest", "servants", "kids"]

    wordList = readInFile("grimms.txt")
    adjSet = makeAdjCorpus("adjFile.txt")

    # make dictionary with all words,
    # sort the adjectives in each noun dictionary by count to see most frequent first
    nounList = makingNounLists(femaleNounList, maleNounList, genderNeutralNounList)
    d = compileDictionary(wordList, nounList, adjSet)
    sortedDict = {}
    for noun in d:
        dictOfNouns = d[noun]
        #print(dictOfNouns)
        sortedDictOfNouns = sorted(dictOfNouns.items(), key=operator.itemgetter(1), reverse=True)
        sortedDict[noun] = sortedDictOfNouns
    #for key, value in sortedDict.items():
        #print(key, value)

    # make same dictionary but with male words (pass in empty lists for other parameters)
    nounList = makingNounLists([], maleNounList, [])
    d = compileDictionary(wordList, nounList, adjSet)
    sortedDict = {}
    for noun in d:
        dictOfNouns = d[noun]
        # print(dictOfNouns)
        sortedDictOfNouns = sorted(dictOfNouns.items(), key=operator.itemgetter(1), reverse=True)
        sortedDict[noun] = sortedDictOfNouns
    #for key, value in sortedDict.items():
        #print(key, value)

    # make same dictionary but with female words (pass in empty lists for other parameters)
    nounList = makingNounLists(femaleNounList, [], [])
    d = compileDictionary(wordList, nounList, adjSet)
    sortedDict = {}
    for noun in d:
        dictOfNouns = d[noun]
        # print(dictOfNouns)
        sortedDictOfNouns = sorted(dictOfNouns.items(), key=operator.itemgetter(1), reverse=True)
        sortedDict[noun] = sortedDictOfNouns
    for key, value in sortedDict.items():
        print(key, value)

    # make same dictionary but with gender neutral words (pass in empty lists for other parameters)
    nounList = makingNounLists([], [], genderNeutralNounList)
    d = compileDictionary(wordList, nounList, adjSet)
    sortedDict = {}
    for noun in d:
        dictOfNouns = d[noun]
        # print(dictOfNouns)
        sortedDictOfNouns = sorted(dictOfNouns.items(), key=operator.itemgetter(1), reverse=True)
        sortedDict[noun] = sortedDictOfNouns
    #for key, value in sortedDict.items():
        #print(key, value)

    # The separate prints for each male, female, gender neutral, and general noun list
    # can be un-commented out to look at the dictionaries created for each respectively
    # (the for key, value.. print(key, value) just need be uncommented)
    # That way we can see the adjectives associated with a particularly "gendered" word
    # Which gives us interesting insight