#!/usr/bin/env python3
# Copyright 2019 RaptorRants

#  Global Variables
DiceMainS = [] #  Global variable used to keep DiceSize state while not cleared
DiceMainC = [] #  Global variable used to keep DiceCount state while not cleared
RollHistory = [] #  Global variable used to keep Dthe history of rolls
SetCount = 1 #  used to itterate the set counts while roll history is not cleared



#  Innitiates Dice variable details such as Dice Size, Amount of Dice and the history of the dice
class Dice:
    def __init__(self, **kwargs):
        if 'DiceType' in kwargs:
            self._DiceType = kwargs['DiceType']
        if 'DiceAmount' in kwargs:
            self._DiceAmount = kwargs['DiceAmount']
        if 'DiceHist' in kwargs:
            self._DiceHist = kwargs['DiceHist']

    def DiceType(self, t=None):
        if t:
            self._DiceType = t
        try:
            return self._DiceType
        except AttributeError:
            return None

    def DiceAmount(self, d=None):
        if d:
            self._DiceAmount = d
        try:
            return self._DiceAmount
        except AttributeError:
            return None

    def DiceHist(self, h=None):
        if h:
            self._DiceHist = h
        try:
            return self._DiceHist
        except AttributeError:
            return None

#  Various functions that handle / modify the Dice Pool. 
class DicePool(Dice):#  Innitiates Dice class to DicePool to allow use of the variables
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def StoreDiceToRoll(self):
        UniqueCount = 'Y'
        print("Provide your die rolls in format diecount diesize (Example: 2 12 is 2d12)")
        count = 1
        while UniqueCount == 'Y' or UniqueCount == 'y':
            while True:
                try:
                    var2, var1 = [int(x) for x in input(f"Enter details of roll {count}: ").split()]  # var1 and var2 will be passed as DieType nad DieSize. This value is swopped in this line to capture rolls before size but will be passed as Size/Rolls later to ensure the first variable is passed to dict as a unique key
                except ValueError:
                    print('Invalid dice selection. Try again')
                    continue
                else:
                    break
            
            DiceMainS.append(var1)  # adds var1 to DiceMainS list
            DiceMainC.append(var2)  # adds var2 to DiceMainC list
            UniqueCount = input('Add another set? Y / N: ')
            count += 1
            if UniqueCount == 'N' or UniqueCount == 'n':
                    break
        else:
            print('invalid option selected. Rolling dice selected so far')
        print()

    def print_pool(self):
        for i, v in zip(self.DiceAmount(), self.DiceType()):
            print(f'{i}d{v}')

    def print_history(self):
        for i, v, c, x in self.DiceHist():
            print(f'Set{x}: d{i}, roll {c}: {v}')

    def ClearDicePool(self):
            del DiceMainC[:]
            del DiceMainS[:]
            print('Cleared the Dice Pool. You have no dice assigned. History will be kept.')

    def ClearHistory(self):
            del RollHistory[:]
            print('Cleared the Roll History.')


#  Action to Roll stored Dice
def RollTheDice(o):
                global SetCount #  Sets the SetCount to the Global Variable (Starts as 1)
                from random import randint
                for dCount, dType in zip(o.DiceAmount(), o.DiceType()):#  sets the function variables for the amount of rolls and dice size from DiceAmount and DiceType from Class Dice()
                        print(f'Rolling for {dCount}d{dType}')
                        count = 1
                        #total = 0
                        while dCount >= count:
                                RollValue = randint(1, dType)
                                print(f'Roll {count} : {RollValue}')
                                varHist = [dType, RollValue, count, SetCount]
                                RollHistory.append(varHist)
                                count += 1
                        print()
                SetCount += 1 #  Increases Setcount by 1 when the roll is finished to increase the value of the next set count. 


#  Call this to pass Dice details and set their types as per class - Dice().
#  When adding an argument here ensure to initiate it in Dice() as well. 
def PassingList():
    a0 = DicePool(DiceAmount=DiceMainC, DiceType=DiceMainS, DiceHist=RollHistory)
    return a0




