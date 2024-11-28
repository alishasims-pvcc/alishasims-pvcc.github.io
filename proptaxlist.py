# Name: Alisha Sims
# Program Purpose use lists to find the personal property tax for vehicles
#   in Charlottesville and produces a report which displays all data and the total tax due
#   for six months
#
# Personal property tax in Charlottesville:
#       -- 4.20% per year
#       -- Paid every six months
# Personal Property Tax Relief (PPTR):
#       -- Eligibility: Vehicles used for personal use only
#       -- Tax relief rate is 33%

import datetime

############## define tax rates ###############
PPT_RATE = .042  
RELIEF_RATE = .33  

############## create list data ###############
vehicle = ["2019 Volvo ",
           "2018 Toyota",
           "2022 Kia   ",
           "2020 Ford  ",
           "2023 Honda ",
           "2019 Lexus "]

vehicle_value = [13000, 10200, 17000, 21000, 28000, 16700]

pptr_eligible = ["Y", "Y", "N", "Y", "N", "Y"]

owner_name = ["Brand, Debra      ",
              "Smith, Carter     ",
              "Johnson, Bradley  ",
              "Garcia, Jennifer  ",
              "Henderson, Leticia",
              "White, Danielle   "]

ppt_owed = []

num_vehicles = len(vehicle)
total = 0


################## define program functions ################

def main():
    perform_calculations()
    display_results()

def perform_calculations():
    global total, ppt_owed

    for i in range(num_vehicles):
        tax_due = (vehicle_value[i] * PPT_RATE) / 2

        if pptr_eligible[i].upper() == "Y":
            tax_due *= (1 - RELIEF_RATE)

        ppt_owed.append(tax_due)

        total += tax_due

def display_results():
    line = ("-----------------------------------------------------------------------------")
    tab = '\t'
    dt_full = str(datetime.datetime.now())
    dt_short = dt_full[0:16]

    print(line)
    print("************************* Personal Property Tax Report ************************")
    print("                           Charlottesville, Virginia")

    print("\n\t\tRUN DATE/TIME: " + dt_short)
    print("\nNAME" + tab + tab + tab + "VEHICLE" + tab + tab + "VALUE" + tab + tab + "RELIEF" + tab + "TAX DUE")
    print(line)

    for i in range(num_vehicles):
        relief = pptr_eligible[i]
        tax_due = "{:,.2f}".format(ppt_owed[i])
        value = "{:,.2f}".format(vehicle_value[i])
        print(f"{owner_name[i]}\t{vehicle[i]}\t{value}\t{relief}\t{tax_due}")

    print(line)
    print(f"*********************************** TOTAL TAX DUE: \t{total:,.2f}".format(total))

main()
