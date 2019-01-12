#!/usr/bin/env python3
# Copyright 2019 RaptorRants

#  This was for inputing dice but only accepted dice in format x x instead of x'd'x
# print(DiceMainC)
        # UniqueCount = 'Y'
        # print("Provide your die rolls in format diecount dies1ize (Example: 2 12 is 2d12)")
        # count = 1
        # while UniqueCount == 'Y' or UniqueCount == 'y':
        #     while True:
        #         try:
        #             var2, var1 = [int(x) for x in input(f"Enter details of roll {count}: ").split()]  # var1 and var2 will be passed as DieType nad DieSize. This value is swopped in this line to capture rolls before size but will be passed as Size/Rolls later to ensure the first variable is passed to dict as a unique key
        #         except ValueError:
        #             print('Invalid dice selection. Try again')
        #             continue
        #         else:
        #             break
        #     print(var1)
        #     print(var2)
        #     DiceMainS.append(var1)  # adds var1 to DiceMainS list
        #     DiceMainC.append(var2)  # adds var2 to DiceMainC list
        #     print(DiceMainS)
        #     print(DiceMainC)
        #     UniqueCount = input('Add another set? Y / N: ')
        #     count += 1
        #     if UniqueCount == 'N' or UniqueCount == 'n':
        #             break
        # else:
        #     print('invalid option selected. Rolling dice selected so far')
        # print()




#def print_history(self):

        #  way 1
        # for key, group in groupby(self.DiceHist(), key=itemgetter(1)):
        #     print()
        #     print(f'Starting with set {key}:')
        #     print()
        #     for item in group:
        #         unpack_item0 =[item[0]]
        #         for a, b, c in unpack_item0:
        #             print(f'd{a} roll {c} result: {b}')
        #  way 2
        # count = 1
        # for Result, Set in self.DiceHist(): 
        #     Display_Results =[ [x, v] for x, v  in self.DiceHist() if v == count] 
        #     if len(Display_Results) != 0:
        #         print()
        #         print(f'Set {count}')
        #         for Results, Set in Display_Results:
        #             finalout = [Results]
        #             for a,b,c in finalout:
        #                 print(f'd{a}, roll {c} :{b}')
        #         print()
        #         count += 1
        #     else:
        #         break

        #  Way 3
        # ResultList = dict()
        # for res, n in self.DiceHist():
        #     ResultList[n] = ResultList.get(n, []) + [res]

        # for k, v in ResultList.items():
        #     print()
        #     print(f'Results of Set {k}:')
        #     Results = v
        #     for a,b,c in Results:
        #         print(f'd{a}, roll{c} = {b}')
        #     print()


        # with open('Actions/DiceMainC.txt','a+') as WritetoFile, open('Actions/DiceMainS.txt','a+') as WritetoFile2:
        #                     for i in var1: 
        #                         WritetoFile.write(str(i))
        #                         WritetoFile.write(' ')
        #                     for i in var2: 
        #                         WritetoFile2.write(str(i))
        #                         WritetoFile2.write(' ')