# Name: Alisha Sims
# Prog Purpose: Read in a list of customers and display a report that will
#   increase the amount they owe by 10% is payment is late
#   DATA FILE is .csv (comma seperated values)
#       Four data fields: last name, first name, amount owed, days payment is late

infile = "customer_data_file.csv"

cust_in_data_block_list = []
cust = []

LATE_FEE_RATE = .10
grand_total = 0

def main():
    read_in_cust_file()
    perform_calculations()
    display_cust_report()

def read_in_cust_file():
    global cust

    #read ALL the lines in the file into one big list
    with open(infile, "r") as cust_data_file:
        cust_in_data_block_list = cust_data_file.readlines()

    #split the data into a list of individual customer lists
    for i in cust_in_data_block_list:
        cust.append([item.strip() for item in i.split(",")])
        
    cust_data_file.close()


def perform_calculations():
    global grand_total

    for i in range(len(cust)):
        amt_owed = float(cust[i][2])
        days_late = int(cust[i][3])

        if days_late > 0:
            late_fee = amt_owed * LATE_FEE_RATE
        else:
            late_fee = 0

        amt_owed += late_fee
        grand_total += amt_owed
        cust[i][2] = amt_owed

def display_cust_report():

    currency_format = '${:,.2f}'
    line = "----------------------------------"
    tab = "\t"

    print(line)
    print("***** CUSTOMER BALANCE REPORT ******")
    print(" NAME\t\t\tNEW AMOUNT OWED")
    print(line)

    for i in range(len(cust)):
        print(f"{cust[i][1]} {cust[i][0]}{tab}${cust[i][2]:,.2f}")
        
    print(line)
    print ("GRAND TOTAL: \t${:,.2f}".format(grand_total))

main()
