#!/usr/bin/env python3
# Copyright 2019 RaptorRants
from itertools import groupby
from operator import itemgetter

#  Global Variables
RollHistory = [] #  Global variable used to keep Dthe history of rolls
# RollHistory data format: [DiceType, Roll Result, The Roll Count (ie roll 1 / roll 2 etc), the set count (ie: Roll set 1 would be the first dice or die rolled)]
SetCount = 0 #  used to itterate the set counts while roll history is not cleared


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
        #multiple dice
        while True:
            try:
                #  takes an input such as 1d12 and replaces the d with a space and then splits the 1 and 2 in to a dicecount and dice size
                Dicelist = [int(x) for x in input(f"Enter details of roll: ").replace('d', ' ').split()]
                lengthcheck =len(Dicelist)
                if not lengthcheck%2: #  if the amount of items in the list being passed is divisible by 0 then append the data, else throw away, try again
                    with open('Actions/DiceMainC.txt','a+') as WritetoFile:
                        for i in Dicelist: 
                            WritetoFile.write(str(i))
                            WritetoFile.write(' ')                  
                else: 
                    print('You seem to have left a value off of one of your rolls')
                    continue
            except ValueError:
                print('Oops, try it in the standard naming format. Example: 1d12.')
                print('if you wish you may exclude the d so that it is 1 12')
                continue
            else:
                break

    def print_pool(self):
        for i, v in zip(self.DiceAmount(), self.DiceType()):
            print(f'{i}d{v}')

    def print_history(self):
        #  Way 3
        ResultList = dict()
        for res, n in self.DiceHist():
            ResultList[n] = ResultList.get(n, []) + [res]

        for k, v in ResultList.items():
            print()
            print(f'Results of Set {k}:')
            Results = v
            for a,b,c in Results:
                print(f'd{a}, roll{c} = {b}')
            print()

    def ClearDicePool(self):
            with open('Actions/DiceMainC.txt','w'): pass
            print('Cleared the Dice Pool. You have no dice assigned. History will be kept.')

    def ClearHistory(self):
            del RollHistory[:]
            with open('Actions/History.txt','w+'): pass
            global SetCount
            SetCount = 0
            print('Cleared the Roll History.')


#  Action to Roll stored Dice
def RollTheDice(o):
    RollPass = []
    global SetCount #  Sets the SetCount to the Global Variable (Starts as 1)
    from random import randint
    for dCount, dType in zip(o.DiceAmount(), o.DiceType()):#  sets the function variables for the amount of rolls and dice size from DiceAmount and DiceType from Class Dice()
            print(f'Rolling for {dCount}d{dType}')
            count = 1
            #total = 0
            while dCount >= count:
                    RollValue = randint(1, dType)
                    print(f'Roll {count} : {RollValue}')
                    varHist = ([dType, RollValue, count], SetCount+1)
                    # with open('Actions/History.txt','a+') as varHistWrite:
                    #     print(f'{SetCount+1}:{dType},{RollValue},{count}', file=varHistWrite)
                    RollHistory.append(varHist)
                    RollPass.append(f'{SetCount+1}:{dType},{count},{RollValue}')
                    count += 1
    if RollPass:
        with open('Actions/History.txt','a+') as varHistWrite:
                print(f'{RollPass}', file=varHistWrite)
                print()
                RollPass=[]
                SetCount += 1 #  Increases Setcount by 1 when the roll is finished to increase the value of the next set count. 


#  Call this to pass Dice details and set their types as per class - Dice().
#  When adding an argument here ensure to initiate it in Dice() as well. 
def PassingList():
    DiceCount=str()
    with open('Actions/DiceMainC.txt','a+') as WritetoFile:
        pass
    with open('Actions/DiceMainC.txt','r+') as WritetoFile:
        for l in WritetoFile:
            DiceCount=l
    Dicelist = [int(x) for x in DiceCount.split()]
    DiceC = [int(x) for x in Dicelist[0::2]]
    DiceS = [int(x) for x in Dicelist[1::2]]
    a0 = DicePool(DiceAmount=DiceC, DiceType=DiceS, DiceHist=RollHistory)
    return a0
