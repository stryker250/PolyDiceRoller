#!/usr/bin/env python3
# Copyright 2018 - RaptorRant
#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Dice:
    def __init__(self, **kwargs):
        if 'DiceType' in kwargs:
            self._DiceType = kwargs['DiceType']
        if 'DiceAmount' in kwargs:
            self._DiceAmount = kwargs['DiceAmount']
        if 'DiceHist' in kwargs:
            self._DiceHist = kwargs['DiceHist']
        if 'Name' in kwargs:
            self._Name = kwargs['Name']

    def DiceType(self, t=None):
        if t: self._DiceType = t
        try: return self._DiceType
        except AttributeError:
            return None

    def DiceAmount(self, d=None):
        if d: self._DiceAmount = d
        try: return self._DiceAmount
        except AttributeError: return None

    def DiceHist(self, h=None):
        if h: self._DiceHist = h
        try: return self._DiceHist
        except AttributeError: return None
    
    def Name(self, nm=None):
        if nm: self._Name = nm
        try: return self._Name
        except AttributeError: return 'Not Someone'

class DicePool(Dice):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def PassTheDice(self):
        print(self.Name())
        DiceCount=str()
        ResultList=dict()
        with open('Saves/History.txt','a+') as varHistWrite:
            pass
        with open('Saves/History.txt','r') as varHistWrite:
            for n, res in enumerate(varHistWrite, 1):
                ResultList[n] = ResultList.get(n, []) + [res.rstrip()]
        with open('DiceStore/DiceMainC.txt','a+') as WritetoFile:
            pass
        with open('DiceStore/DiceMainC.txt','r+') as WritetoFile:
            for l in WritetoFile:
                DiceCount=l
        Dicelist = [int(x) for x in DiceCount.split()]
        DiceC = [int(x) for x in Dicelist[0::2]]
        DiceS = [int(x) for x in Dicelist[1::2]]
        a0 = DicePool(DiceAmount=DiceC, DiceType=DiceS, DiceHist=ResultList)
        return a0
    
    def StoreDiceToRoll(self):
        while True:
            try:
                #  takes an input such as 1d12 and replaces the d with a space and then splits the 1 and 2 in to a dicecount and dice size
                Dicelist = [int(x) for x in input(f"Enter details of roll: ").replace('d', ' ').split()]
                lengthcheck =len(Dicelist)
                if not lengthcheck%2: # Checks that list length is an even number
                    with open('DiceStore/DiceMainC.txt','a+') as WritetoFile:
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
        with open('DiceStore/DiceMainC.txt','w'): pass

    def ClearHistory(self):
            with open('Saves/History.txt','w+'): pass

class WorkTheDice:
    def RollTheDice(self):
        print(f'{self.Name()} is')
        names = self.Name()
        self = DicePool.PassTheDice(self)
        from random import randint
        RollPass = []
       # global SetCount #  Sets the SetCount to the Global Variable (Starts as 1)
        import datetime
        date=str(datetime.datetime.today().strftime('%Y/%m/%d----%H:%M:%S'))
        for dCount, dType in zip(self.DiceAmount(), self.DiceType()):#  sets the function variables for the amount of rolls and dice size from DiceAmount and DiceType from Class Dice()
                if RollPass:
                    pass
                else: 
                    with open('Saves/History.txt','a+') as varHistWrite:
                        print(f'{date} {names}',end=" ", file=varHistWrite)
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
                            with open('Saves/History.txt','a+') as varHistWrite:
                                print(f'{dType} {count} {RollValue}',end=" ", file=varHistWrite)
                        count += 1
                #SetCount+=1
        if RollPass:
                with open('Saves/History.txt','a') as varHistWrite:
                    print(f'',file=varHistWrite)

# class displaying(Dice):
#     def print_dice_pool(self):
#         print(f'The d{self.DiceType()} is Rolled "{self.DiceAmount()}" times by {self.Name()}"')

def main():
    # a1= DicePool(Name='Llew') # Reminder code as I want to pass a player name. 
    # WorkTheDice.RollTheDice(a1)
    while True:
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1: Add Dice to Rolling Pool')
        print('2: View Rolling Pool')
        print('3: View Roll History')
        print('4: Roll them baby!')
        print('5: Clear Dice Pool')
        print('6: Clear roll history')
        print('9: Exit')

        x = input('Choice: ')
        if x == '1':
            print()
            input('Press Enter to Continue')
        elif x == '2':
            print()
            input('Press Enter to Continue')
        elif x == '3':
            print()
            input('Press Enter to Continue')
        elif x == '4':
            print()
            player_name=input('Enter the name of the Character Rolling: ')
            a1= DicePool(Name=player_name)
            WorkTheDice.RollTheDice(a1)
            input('Press Enter to Continue')
        elif x == '5':
            print()
            print('Dice Pool cleared....')
            input('Press Enter to Continue')
        elif x == '6':
            print()
            print('Dice History cleared....')
            input('Press Enter to Continue')
        elif x == '9':
            print()
            break
        else:
            print()
            print('Please choose a valid option')
            print()
            
    

if __name__ == '__main__': main()