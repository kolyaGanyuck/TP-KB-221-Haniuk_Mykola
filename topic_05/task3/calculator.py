from operations import calculator_if
from operations import genIntValue
from operations import get_operation


def main():       
        value1 = genIntValue("Enter the first integer (x): ")

        value2 = genIntValue("Enter the second integer (y): ")
    
        operation = get_operation()
    
        print(calculator_if(value1, value2, operation))

while True:
    main()
    continue_calculation = input("Do you want to continue calculating? (yes/no): ")
    if continue_calculation.lower() != "yes":
        break



