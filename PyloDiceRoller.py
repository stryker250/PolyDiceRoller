#!/usr/bin/env python3
# Copyright 2018 - RaptorRants
from Actions.DiceWorking import DicePool, RollTheDice, PassingList
import os

def Menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1: Add Dice to Rolling Pool')
        print('2: View Rolling Pool')
        print('3: Roll them baby!')
        print('4: View Roll History')
        print('5: Clear Dice Pool')
        print('6: Clear roll history')
        print('9: Exit')

        x = input('Choice: ')
        if x == '1':
            print()
            DicePool.StoreDiceToRoll(PassingList())
            input('Press Enter to Continue')
        elif x == '2':
            print()
            DicePool.print_pool(PassingList())
            input('Press Enter to Continue')
        elif x == '3':
            print()
            RollTheDice(PassingList())
            input('Press Enter to Continue')
        elif x == '4':
            print()
            DicePool.print_history(PassingList())
            input('Press Enter to Continue')
        elif x == '5':
            print()
            DicePool.ClearDicePool(True)
            input('Press Enter to Continue')
        elif x == '6':
            print()
            DicePool.ClearHistory(True)
            input('Press Enter to Continue')
        elif x == '9':
            print()
            break
        else:
            print()
            print('Please choose a valid option')
            print()

if __name__ == "__main__": Menu()