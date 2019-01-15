#!/usr/bin/env python3
# Copyright 2018 - RaptorRant

class Dice:
    def __init__(self, **kwargs):
        if 'DiceType' in kwargs:
            self._DiceType = kwargs['DiceType']
        if 'DiceAmount' in kwargs:
            self._DiceAmount = kwargs['DiceAmount']
        if 'PlayerName' in kwargs:
            self._PlayerName = kwargs['PlayerName']

    def DiceType(self, t=None):
        if t: self._DiceType = t
        try: return self._DiceType
        except AttributeError:
            return None

    def DiceAmount(self, d=None):
        if d: self._DiceAmount = d
        try: return self._DiceAmount
        except AttributeError: return None
    
    def PlayerName(self, nm=None):
        if nm: self._PlayerName = nm
        try: return self._PlayerName
        except AttributeError: return 'UnspecifiedUser'

def PassingDice(*args):
    """
        This function reads data from various files, 
        splits it in to their respective variables and passes
        the info to the class/function that needs it. 
    """
    DiceCount=[]
    with open('DiceStore/DicePool.txt','r+') as WritetoFile:
        for l in WritetoFile:
            DiceCount=l
        if DiceCount:
            Dicelist = [int(x) for x in DiceCount.split()]
            DiceC = [int(x) for x in Dicelist[0::2]]
            DiceS = [int(x) for x in Dicelist[1::2]]
            returnType= Dice(DiceType = DiceS, DiceAmount = DiceC)
            return returnType
        else:
            returnType=Dice(DiceType=None)
        
    #DiceT = (self.DiceType())
    #DiceA = (self.DiceAmount())

class DicePool:
    DicePoolSet = PassingDice(True)
    def RollTheDice(self, a):
        from random import randint
        import datetime
        RollPass=[]
        
        if not a.DicePoolSet:
            print('Please add Dice to your pool to roll them.')
        else:
            for dCount, dType in zip(a.DicePoolSet.DiceAmount(), a.DicePoolSet.DiceType()):
                if RollPass: # if RollPass has data it does not append a new date
                    pass
                else: #if RollPass has no data then it sets a date to the beginning of the line for the roll
                    setDate = DiceStorage()
                    setDate.storeHistory(a= 0, b=1)
                print(f'Rolling for {dCount}d{dType}')
                count = 1
                while dCount >= count:
                        RollValue = randint(1, dType)
                        print(f'Roll {count} : {RollValue}')
                        RollPass.append(f'{dType},{count},{RollValue}')
                        if RollPass:
                            PassToHistory=DiceStorage(DiceType=dType, DiceAmount=count)
                            PassToHistory.storeHistory(RollValue, b=2)
                        count += 1
        if RollPass: #if RollPass has data, it sets a new line after the roll details have finished writing to file.
            newLine = DiceStorage()
            newLine.storeHistory(a= 0, b=3)
        return RollPass #returns the value of rollpass to the function so it can be read by the display functions to show the results. 
        

class DiceStorage(Dice):

    def storeDicePool(self):
        pass

    def storeHistory(self, a, b):
        import datetime
        date=str(datetime.datetime.today().strftime('%Y/%m/%d----%H:%M:%S'))
        dType=self.DiceType()
        count= self.DiceAmount()
        RollValue=a
        with open('Saves/History.txt','r+'):
            pass
        if b == 1:
            with open('Saves/History.txt','a+') as varHistWrite:
                            print(f'{date}',end=" ", file=varHistWrite)
        elif b == 2:
            with open('Saves/History.txt','a+') as varHistWrite:
                print(f'{dType} {count} {RollValue}',end=" ", file=varHistWrite)
        elif b == 3:
            with open('Saves/History.txt','a') as varHistWrite:
                print(f'',file=varHistWrite)
        
        # with open('Saves/History.txt','a') as varHistWrite:
        #             print(f'',file=varHistWrite)

class DisplayDice:

    def displayDicePool(self):

        pass
    def displayHistory(self):
        pass



def main():
    while True:
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1: Add Dice to Rolling Pool')
        print('2: View Rolling Pool')
        print('3: Roll them baby!')
        print('4: View Roll History')
        print('5: Clear Dice Pool')
        print('6: Clear roll history')
        print('9: Exit')

        x = input('Enter the menu number you require: ')
        if x == '1':
            print()
        elif x == '2':
            print()
        elif x == '3':
            print()
            a1=DicePool()
            a1.RollTheDice(a1)
            input('press enter')
        elif x == '4':
            print()
        elif x == '5':
            print()
        elif x == '6':
            print()
        elif x == '9':
            print()
            break
        else:
            print()
            print('Please choose a valid option')
            input('Press Enter')

    
    pass
    

if __name__ == '__main__': main()
