import random
# basic version of story generator
# better one analyzed.

def initialSituation0(charGender, charName, typeOfHero, charType, objPronoun):
    # The setup
    if typeOfHero.lower() == "royal":
        livedIn = "castle"
    else:
        livedIn = "cottage"

    return "There was once a " + charGender + " named " + charName + " the " + charType + " who lived in a " + \
           livedIn + " with " + objPronoun + " family.\n"

def absentations1(charGender, possPronoun):
    # Someone leaves or dies. Usually a parent.
    return "The " + charGender + "'s mom died and and " + possPronoun + "'s dad remarried an awful woman.\n"

def interdiction2(charName, objNoNo, possPronoun):
    # A big rule is set up. Don't touch the spinning wheel. You can't go to the ball. You know the drill.
    return charName + " was told never to touch " + possPronoun + " stepmother's special " + objNoNo + ".\n"

def violation3(charName, objNoNo, pronoun):
    # Someone breaks the big rule. This could be good or bad as seen by the examples above.
    return charName + " was bored and curious one day and found the " + objNoNo + " hiding on a tall shelf.\n" \
           + pronoun + " picked it up and dropped it, but put it back thinking no one saw.\n"

def reconnaissance4():
    # The villain spies on the hero or the hero learns about the villain.
    return "Meanwhile, the stepmother was watching it all happen.\n"

def delivery5(objNoNo):
    # The searching party discovers information.
    return "The stepmother examined the " + objNoNo + " and saw that it was, indeed, broken.\n"

def trickery6(charName, objNoNo):
    # Villain tricks hero.
    return "She then asked " + charName + " to kindly bring her the " + objNoNo + " from the shelf.\n"

def complicity7(charName, objNoNo, pronoun):
    # The hero is forced, tricked or influenced by magic to do something bad. There are bad consequences.
    return charName + " had no other choice but to get " + objNoNo + " and pretend nothing happened.\n" + \
           "When the stepmother asked if " + pronoun + " knew where the " + objNoNo + " is, " + charName + \
           " says " + pronoun + " never saw it.\n"

def villainy8(charName, charType):
    # Baddy McBadson does something really evil, normally stealing the Macguffin or kidnapping the princess.
    return "The stepmother said that she would kill " + charName + " the " + charType + " for her disobedience.\n"

def meditation9(charName, pronoun):
    # The goodies figure out a plan and get ready to set out on their quest.
    return charName + " went to think and realized that " + pronoun + "must leave immediately.\n"

def beginningCounteraction10(charName, possPronoun):
    # The heroes choose to fight back.
    return charName + " vowed to come back and convince " + possPronoun + " father of " + possPronoun + \
           " stepmother's evilness.\n"

def departure11(charName, charType, pronoun):
    #They... depart. Voluntarily or not.
    return charName + " the " + charType + " ran away in the middle of the night that night.\n" + pronoun[0].upper() + \
           pronoun[1:] + " wandered and wandered until finding a magical hut.\n"

def firstDonor12(charName, helper):
    # function of donor - The hero run into a donor or a magic dude. This character can be The Obi-Wan, a mysterious beggar or a "None Shall Pass" kind of character. They may have to pass a test. The hero may have to fight the donor. But on the bright side, the donor may have a magical object to help them on their quest.
    return "Out of the magical hut came a " + helper + " who gave " + charName + " a special feather. As long as " + \
           charName + " had the feather, nothing bad could happen.\n"

'''
def protagonistReaction():
    # The hero outsmarts, outfights or finds a way around the donor's demands. He gets the Macguffin.
def acquisitionOfMagicalAgent():
    # The obi-wan type character. Can be the donor. This character helps the hero on his quest, sometimes willingly, sometimes not.
def transference():
    # The hero is taken to a new place. Physically. Emotionally. Spiritually. Grammatically.
def struggle():
    # Our hero (surprisingly) struggles.
def branding():
    # Our hero for his efforts is marked out as a hero either with a token or with a mark on his body.
def victory():
    # The hero beats the villain with his wits, his special abilities or his brawn.
def liquidation():
    # The goodies all help the hero, and get what they were after.
def theReturn():
    # Guess.
def pursuit():
    # The heroes are chased by the villain, who is going all One-Winged Angel on them.
def rescue():
    # The goodies run for it and escape by placing obstacles in the villain's path.
def unrecognised():
    # The hero comes home and no one knows who he is because...
def unfoundedClaims():
    # Some Il Capitano-Zapp Brannigan-Gilderoy Lockhart character claims he saved the day.
def difficultTask():
    # To prove he's the Hero the Hero must, well prove himself. It can be an ordeal of choice, a riddle or a test of strength.
def solution():
    # The Hero chooses right/guesses right/wins the fight.
def recognition():
    #Everyone realises that the hero is the hero through his special mark, the fact they got the right solution or through simple recognition.
def exposure():
    #The false hero is shown up.
def transfiguration():
    #The hero gets a makeover. Or at least new clothes or a palace.
def punishment():
    #False Hero and Villain (and yes, they can be the same guy) get what's coming to them.
def theWedding():
    # Usually the hero marries the princess or something like that, but the wedding can just be a general celebration from getting crowned to a party.
'''

def composeFunction(lst):
    #Lets user choose which functions to include by inputting list (here we have mostly essential functions and only one option
    ret = ''
    if 0 in lst:
        ret += initialSituation0(charGender, charName, typeOfHero, charType, objPronoun)
    if 1 in lst:
        ret += absentations1(charGender, possPronoun)
    if 2 in lst:
        ret += interdiction2(charName, objNoNo, possPronoun)
    if 3 in lst:
        ret += violation3(charName, objNoNo, pronoun)
    if 4 in lst:
        ret += reconnaissance4()
    if 5 in lst:
        ret += delivery5(objNoNo)
    if 6 in lst:
        ret += trickery6(charName, objNoNo)
    if 7 in lst:
        ret += complicity7(charName, objNoNo, pronoun)
    if 8 in lst:
        ret += villainy8(charName, charType)
    if 9 in lst:
        ret += meditation9(charName, pronoun)
    if 10 in lst:
        ret += beginningCounteraction10(charName, possPronoun)
    if 11 in lst:
        ret += departure11(charName, charType, pronoun)
    if 12 in lst:
        ret += firstDonor12(charName, helper)
    return ret

if __name__ == '__main__':
    # prompts user for inputs to their story
    charGender = input("main character--boy or girl? ")
    if charGender == "boy":
        pronoun = "he"
        objPronoun = "him"
        possPronoun = "his"
    if charGender == "girl":
        pronoun = "she"
        objPronoun = "her"
        possPronoun = "her"
    charName = input("main character's name? ")
    typeOfHero = input("royal or poor ")
    charType = input("favorite adjective? ")
    womanOrCreature = input("1 or 2 ")
    if womanOrCreature == "2":
        helper = input("favorite magical creature? ")
    if womanOrCreature == "1":
        helper = random.choice(["old woman", "witch", "fairy"])
    #badGuy = input("name your bad guy ") Nevermind well just do a stepmother
    objNoNo = input("special object in home? ")
    #lstElems = input("Write any number of numbers from 0-12 with spaces in the middle ")
    #lst = [int(elem) for elem in lstElems.split()]
    # puts all functions into story because story not complex enough to account for different iterations
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(lst)
    print(composeFunction(lst))