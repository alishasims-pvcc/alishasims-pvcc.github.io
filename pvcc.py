# Name: Alisha Sims
# Prog Purpose: This program computes PVCC college tuition & fees based on number of credits
#   PVCC Fee Rates are from https://www.pvcc.edu/tuition-and-fees

import datetime

# define tuition & fee rates
RATE_TUITION_IN = 164.40
RATE_TUITION_OUT = 353.00
RATE_CAPITAL_FEE = 26.00
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# define global variables
inout = 1  # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarship_amt = 0
tuition = 0
inst_fee = 0
cap_fee = 0
act_fee = 0
total = 0
balance = 0

# create output file
outfile = "pvccweb.html"

def main():
    open_outfile()
    more = True
    
    while more:
        get_user_data()
        perform_calculations()
        create_output_file()

        yesno = input("\nWould you like to calculate tuition and fees for another student? (Y/N): ")
        if yesno.lower() == "n":
            more = False
            print(f'\n** Open this file in a browser window to see your results: {outfile}')
    
    close_outfile()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html><head><title>PVCC Tuition</title>\n')
    f.write('<style>td { text-align: right; }</style></head>\n')
    f.write('<body style="background-color: #985b45; background-image: url(wp-pvcc.png); color: #000000;">\n')

def close_outfile():
    f.write('</body></html>')
    f.close()

def get_user_data():
    global inout, numcredits, scholarship_amt
    print('**** PIEDMONT VIRGINIA COMM COLLEGE Tuition & Fees ****')
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarship_amt = int(input("Scholarship amount received: "))

def perform_calculations():
    global tuition, inst_fee, cap_fee, act_fee, total, balance

    if inout == 1:
        tuition = numcredits * RATE_TUITION_IN
        cap_fee = 0
    else:
        tuition = numcredits * RATE_TUITION_OUT
        cap_fee = numcredits * RATE_CAPITAL_FEE

    inst_fee = numcredits * RATE_INSTITUTION_FEE
    act_fee = numcredits * RATE_ACTIVITY_FEE
    total = tuition + cap_fee + inst_fee + act_fee
    balance = total - scholarship_amt

def create_output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan="3">'

    f.write('\n<table border="3" style="background-color: #FFFFFF; font-family: arial; margin: auto;">\n')
    f.write(f'{colsp}<h2>PIEDMONT VIRGINIA COMM COLLEGE</h2></td></tr>\n')
    f.write(f'{colsp}**** PVCC TUITION and FEES REPORT ****</td></tr>\n')

    f.write(f'{tr}Tuition{endtd}{numcredits}{endtd}{tuition:{currency}}{endtr}')
    f.write(f'{tr}Capital Fee{endtd}{cap_fee}{endtd}{cap_fee:{currency}}{endtr}')
    f.write(f'{tr}Institution Fee{endtd}{inst_fee}{endtd}{inst_fee:{currency}}{endtr}')
    f.write(f'{tr}Activity Fee{endtd}{act_fee}{endtd}{act_fee:{currency}}{endtr}')
    
    f.write(f'{tr}Total{endtd}{endtd}{total:{currency}}{endtr}')
    f.write(f'{tr}Scholarship Amount{endtd}{endtd}{scholarship_amt:{currency}}{endtr}')
    f.write(f'{tr}Balance{endtd}{endtd}{balance:{currency}}{endtr}')

    f.write(f'{colsp}Date/Time: {day_time}{endtr}')
    f.write('</table><br />')

# call on main program to execute
main()
