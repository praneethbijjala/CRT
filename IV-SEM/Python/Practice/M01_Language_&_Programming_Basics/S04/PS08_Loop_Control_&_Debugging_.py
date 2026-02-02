
'''
pdb commands:
1)
Docstring for IV-SEM.Python.Practice.M01_Language_&_Programming_Basics.S04.PS08_Loop_Control_&_Debugging_
'''


try:
    a=int(input("Enter a number: "))
    print(10/a)
except ZeroDivisionError:
    print("Can not divisible by Zero")
except ValueError:
    print("Invalid input.")
    