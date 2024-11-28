# Name: Alisha Sims
# Prog Purpose: This program calculates personal property taxes for 6 months
#   personal property tax rate: 4.40% per year
#   tax relief: 30%
#   assessed value: $5525

import datetime

############## define global variables ##############
TAX_RATE = 0.044  
TAX_RELIEF = 0.3  
ASSESSED_VALUE = 5525

############## define program functions ##############
def main():
    more_cars = True

    while more_cars:
        is_eligible = get_user_data()
        total_due, relief_amount, annual_total = perform_calculations(is_eligible)
        display_results(total_due, relief_amount, annual_total)

        yesno = input("\nWould you like to calculate tax for another vehicle (Y or N)? ")
        if yesno.upper() == "N":
            more_cars = False
            print("\nThank you!")

def get_user_data():
    while True:
        try:
            choice = int(input("\nIs your vehicle eligible for tax relief? (1 for YES, 2 for NO): "))
            if choice == 1:
                return True
            elif choice == 2:
                return False
            else:
                print("Invalid choice. Please enter 1 for YES or 2 for NO.")
        except ValueError:
            print("Invalid input. Please enter a valid number (1 or 2).")

def perform_calculations(is_eligible):
    annual_tax = ASSESSED_VALUE * TAX_RATE
    if is_eligible:
        relief_amount = annual_tax * TAX_RELIEF
        total_due = (annual_tax - relief_amount) / 2  
    else:
        relief_amount = 0
        total_due = annual_tax / 2
    return total_due, relief_amount, annual_tax

def display_results(total_due, relief_amount, annual_total):
    currency = '8,.2f'
    full_date = str(datetime.datetime.now())
    line = ('------------------------------')
    
    print(line)
    print('**** PERSONAL PROPERTY TAX BILL ****')
    print('Please Pay in a Timely Manner')
    print(full_date)
    print(line)
    print('Assessed Value       $ ' + format(ASSESSED_VALUE,currency))
    print('Relief Amount        $ ' + format(relief_amount,currency))
    print('Full Annual Amount   $ ' + format(annual_total,currency))
    print(line)
    print('Total Due            $ ' + format(total_due,currency))
    print(line)

########## call on main program to execute ###########
main()
