import operator

def readInFile(fileName):
    file = open(fileName)
    fileList = []
    wordList = []
    for line in file:
        fileList.append(line.strip().split())
        # print(line.strip().split())

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
    nounList = []
    for word in femaleNounList:
        nounList.append(word)
    for word in maleNounList:
        nounList.append(word)
    for word in genderNeutralNounList:
        nounList.append(word)
    return nounList

def makeAdjCorpus(adjFileName):
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
    d = {}
    for i in range(0, 1):
        word = wordList[i]
        if word in nounList:
            if word not in d:
                d[word] = {}
            for j in range(0, 2):
                if wordList[i + j] in adjSet:
                    if wordList[i + j] not in d[word]:
                        d[word][wordList[i + j]] = 0
                    d[word][wordList[i + j]] += 1

    for i in range(2, len(wordList) - 2):
        word = wordList[i]
        if word in nounList:
            if word not in d:
                d[word] = {}
            for j in range(-2, 1):
                if wordList[i + j] in adjSet:
                    if wordList[i + j] not in d[word]:
                        d[word][wordList[i + j]] = 0
                    d[word][wordList[i + j]] += 1

    for i in range(len(wordList) - 2, len(wordList)):
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

    #make dictionary with all words
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

    # make dictionary with male words
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

    # make dictionary with female words
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

    # make dictionary with gender neutral words
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