# Name: Alisha Sims
# Prog Purpose: This program finds the cost of a meal at Branch Barbeque Buffet
#   Price for an adult meal: $19.95
#   Price for a child meal: $11.95
#   Service fee: 10%
#   Sales tax rate: 6.2%

import datetime

##############  define global variables ############
# define tax rate, service fee, and prices
ADULT_MEAL = 19.95

CHILD_MEAL = 11.95

SALES_TAX_RATE = .062

SERVICE_FEE_RATE = .1

# define global variables
num_adult_meals = 0
num_child_meals = 0
adult_subtotal = 0
child_subtotal = 0
subtotal = 0
service_fee = 0
sales_tax = 0
total = 0


##############  define program functions ################
def main():

    more_meals = True

    while more_meals:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno == "N" or yesno =="n":
            more_meals = False
            print("Thank you for coming to Branch Barbeque Buffet! Enjoy your meal!")

def get_user_data():
    global num_adult_meals
    num_adult_meals = int(input("Number of Adult Meals: "))
    global num_child_meals
    num_child_meals = int(input("Number of Child Meals: "))
                            
def perform_calculations():
    global adult_subtotal, child_subtotal, subtotal, service_fee, sales_tax, total
    adult_subtotal = ADULT_MEAL * num_adult_meals
    child_subtotal = CHILD_MEAL * num_child_meals
    subtotal = adult_subtotal + child_subtotal
    sales_tax = subtotal * SALES_TAX_RATE
    service_fee = subtotal * SERVICE_FEE_RATE
    total = subtotal + sales_tax

def display_results():
    print('------------------------------')
    print('**** Branch Barbeque Buffett ****')
    print('------------------------------')
    print('Adult Meals   $ ' + format(adult_subtotal,'12,.2f'))
    print('Child Meals   $ ' + format(child_subtotal,'12,.2f'))
    print('Service Fee   $ ' + format(service_fee,'12,.2f'))
    print('Sales Tax     $ ' + format(sales_tax,'12,.2f'))
    print('Total         $ ' + format(total,'12,.2f'))
    print('------------------------------')
    print(str(datetime.datetime.now()))
     
##########  call on main program to execute ###########
main()
