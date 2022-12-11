#FINAL PROJECT SDEV140 (Time tracking and payroll system)

#The project is to develop and implement a new time tracking and payroll system,
#that will allow the staff to log in from anywhere on the network. 
#Each department of the organization is to monitor their staff's time tracking. 
#There will be an option for a manager to correct information once the employee has accepted it. 
#There will also be security for logging in and a manager-level login.  
#This time tracking information will feed into the payroll system.

# TIME TRACKING

# User Login detail (username and password)
# Time punch (clock -in, clock-out)


def check_time (test_time) :
    is_good = (len(test_time) == 4)
    if not is_good :
        print('You must enter exactly four digits for the time')
        return False
    is_good = start_time.isdigit()
    if not is_good :
        print('The time entered must be all digits')
        return False

    test_time = int(test_time)
    is_good =   (0 <= test_time <= 1159)
    if not is_good :
        print('Time must be between 0000 and 1159')
        return False

    return True


print()
PASSWORD = 'sdev140'
while True :
    username = input('Enter username: ')
    if username == '' :
        print('You must enter a non-blank Username')
        continue
    password = str(input('Enter password: '))
    if password != PASSWORD :
        print('You entered the wrong password')
    else :
        break

Employee_name = str(input('Enter full name: first name, Last name '))
print()

# Set Time_punch  = (clock-in/clock-out)
while True :
    start_time = input('clock-in time:')

    if not check_time(start_time) :
        continue
    stop_time = input('clock-out time:')
    if not check_time(stop_time) :
        continue
    else :
        break

print()
# Named constants to represent the base hours and
# the overtime multiplier.

BASE_HRS = 40  # Base hours per week
OT_MULTIPLIER = 1.5  # Overtime multiplier

# Get the hours worked and the hourly pay rate.
number_of_hrs_worked = float(input('Enter total number of hours worked weekly: '))
pay_rate = float(input('Enter the hourly pay rate: '))
overtime_hours = number_of_hrs_worked - BASE_HRS
print()
# Calculate and display the gross pay.

if number_of_hrs_worked > BASE_HRS :

    # Calculate the amount of overtime pay.
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER

    print('*****************************************')
    # Calculate the gross pay.
    gross_pay = BASE_HRS * pay_rate + overtime_pay
else :
    gross_pay = BASE_HRS * pay_rate
print()
Fed = int(gross_pay * 0.04)

state_tax = (gross_pay * 0.012)

county_tax = (gross_pay * 0.007)

Income_Taxes = Fed + state_tax + county_tax

# Other deductions
medical = (gross_pay * 0.023)
dental = (gross_pay * 0.05)
vision = (gross_pay * 0.010)
Deductions = Income_Taxes + medical + dental + vision

Net_pay = gross_pay - Deductions

# Display the paystub.
print("GLOBE INDUSTRIES....It's all about pipe")
print("---------------------------------------------------")
print(f'Paystub for: {Employee_name}\n')
print(f'Login detail is {username}: password is *******')
print(f'You clocked in at {start_time:}am.')
print(f'You clocked out at {stop_time:}pm.')
print(f'Your overtime is {overtime_hours:,.1f} hours.')
print()
print(f'Fed:{Fed:,.2f}\n')
print(f'state tax: {state_tax:,.2f}\n')
print(f'county tax:{county_tax:,.2f}\n')
print(f'Income Taxes: {Income_Taxes:,.2f}\n')
print(f'Deductions: {Deductions:,.2f}\n')
print(f'The gross pay is ${gross_pay:,.2f}.    Your Netpay:${Net_pay:,.2f}')

