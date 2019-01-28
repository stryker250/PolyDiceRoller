#!/usr/bin/env python3
# Copyright 2018 - RaptorRants
from Actions.DiceWorking import DicePool, WorkTheDice
import os

def main():
    try:
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
                DicePool.StoreDiceToRoll(DicePool.PassingList(x))
                input('Press Enter to Continue')
            elif x == '2':
                print()
                WorkTheDice.print_pool(DicePool.PassingList(x))
                input('Press Enter to Continue')
            elif x == '3':
                print()
                WorkTheDice.RollTheDice(DicePool.PassingList(x))
                input('Press Enter to Continue')
            elif x == '4':
                print()
                WorkTheDice.print_history(DicePool.PassingList(x))
                input('Press Enter to Continue')
            elif x == '5':
                print()
                DicePool.ClearDicePool(True)
                print('Dice Pool cleared....')
                input('Press Enter to Continue')
            elif x == '6':
                print()
                DicePool.ClearHistory(True)
                print('Dice History cleared....')
                input('Press Enter to Continue')
            elif x == '9':
                print()
                DicePool.ClearDicePool(True)
                break
            else:
                print()
                print('Please choose a valid option')
                print()
    except KeyboardInterrupt:
        print('\nExiting ...')

if __name__ == "__main__":
    main()
