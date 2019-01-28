#!/usr/bin/env python3
# Copyright 2019 RaptorRants
from itertools import groupby
from operator import itemgetter
from random import randint
import datetime
import os

#  Global Variables
#RollHistory = []  # Global variable used to keep Dthe history of rolls
#  RollHistory data format: [DiceType, Roll Result, The Roll Count (ie roll 1 / roll 2 etc), the set count (ie: Roll set 1 would be the first dice or die rolled)]
#SetCount = 0  # used to itterate the set counts while roll history is not cleared


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

#  Action to Roll stored Dice
class WorkTheDice(Dice):

    def RollTheDice(self):
        RollPass = []
        # global SetCount #  Sets the SetCount to the Global Variable (Starts as 1)

        date=str(datetime.datetime.today().strftime('%Y/%m/%d----%H:%M:%S'))
        for dCount, dType in zip(self.DiceAmount(), self.DiceType()):#  sets the function variables for the amount of rolls and dice size from DiceAmount and DiceType from Class Dice()
            if RollPass:
                pass
            else:
                with open('Actions/History.txt','a+') as varHistWrite:
                    print(f'{date}',end=" ", file=varHistWrite)
            print(f'Rolling for {dCount}d{dType}')
            count = 1
            #total = 0
            while dCount >= count:
                RollValue = randint(1, dType)
                print(f'Roll {count} : {RollValue}')
                # varHist = ([dType, RollValue, count], SetCount+1)
                # RollHistory.append(varHist)
                RollPass.append(f'{dType},{count},{RollValue}')
                if RollPass:
                    with open('Actions/History.txt','a+') as varHistWrite:
                        print(f'{dType} {count} {RollValue}',end=" ", file=varHistWrite)
                count += 1
                #SetCount+=1
        if RollPass:
            with open('Actions/History.txt','a') as varHistWrite:
                print(f'',file=varHistWrite)

    def print_pool(self):
        for i, v in zip(self.DiceAmount(), self.DiceType()):
            print(f'{i}d{v}')

    def print_history(self):
        unpack = dict(self.DiceHist())
        for k, v in unpack.items():
            print(f'set {k}')
            DiceCount = ''.join(str(e) for e in v)
            Dicelist = [x for x in DiceCount.split()]
            DiceS = [x for x in Dicelist[1::3]]
            DiceC = [x for x in Dicelist[2::3]]
            DiceR = [x for x in Dicelist[3::3]]
            DiceD = [Dicelist[0]]
            DiceD = ' '.join(str(i) for i in DiceD)
            print(DiceD)
            for i,v,x in zip(DiceS,DiceC,DiceR):
                print(f'D{i}, Roll {v} = {x}')
            print()

#  Various functions that handle / modify the Dice Pool.
class DicePool(Dice):#  Innitiates Dice class to DicePool to allow use of the variables
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
#  Call this to pass Dice details and set their types as per class - Dice().
#  When adding an argument here ensure to initiate it in Dice() as well.
    def PassingList(self):
        DiceCount=str()
        ResultList=dict()

        if  os.path.exists('Actions/History.txt'):
            with open('Actions/History.txt','r') as varHistWrite:
                for n, res in enumerate(varHistWrite, 1):
                    ResultList[n] = ResultList.get(n, []) + [res.rstrip()]

        if os.path.exists('Actions/DiceMainC.txt'):
            with open('Actions/DiceMainC.txt','r+') as WritetoFile:
                for l in WritetoFile:
                    DiceCount=l
        Dicelist = [int(x) for x in DiceCount.split()]
        DiceC = [int(x) for x in Dicelist[0::2]]
        DiceS = [int(x) for x in Dicelist[1::2]]
        a0 = DicePool(DiceAmount=DiceC, DiceType=DiceS, DiceHist=ResultList)
        return a0

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

    def ClearDicePool(self):
        with open('Actions/DiceMainC.txt','w'): pass

    def ClearHistory(self):
#       del RollHistory[:]
        with open('Actions/History.txt','w+'): pass
#       global SetCount
#       SetCount = 0
