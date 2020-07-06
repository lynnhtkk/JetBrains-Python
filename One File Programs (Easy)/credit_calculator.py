import math

action = input('What do you want to calculate?\n'\
    'type "n" - for count of months,\n'\
    'type "a" - for annuity monthly payment,\n'\
    'type "p" - for credit principal:\n')

if action == 'n':
    credit_principal = float(input('Enter credit principal: '))
    monthly_payment = float(input('Enter monthly payment: '))
    credit_interest = float(input('Enter credit interest: '))
    credit_interest = credit_interest / (12 * 100)
    periods = math.ceil(math.log( monthly_payment / (monthly_payment - credit_interest * credit_principal),credit_interest + 1))
    years = int(periods // 12)
    months = math.ceil(periods % 12)
    if years == 0:
        if months == 1:
            print(f'You need {months} month to repay this credit!')
        else:
            print(f'You need {months} months to repay this credit!')
    elif years == 1:
        if months == 0:
            print(f'You need {years} year to repay this credit!')
        elif months == 1:
            print(f'You need {years} year {months} month to repay this credit!')
        else:
            print(f'You need {years} year {months} months to repay this credit!')
    else:
        if months == 0:
            print(f'You need {years} years to repay this credit!')
        elif months == 1:
            print(f'You need {years} years {months} month to repay this credit!')
        else:
            print(f'You need {years} years {months} months to repay this credit!')
elif action == 'a':
    credit_principal = float(input('Enter credit principal: '))
    periods = float(input('Enter count of periods: '))
    credit_interest = float(input('Enter credit interest: '))
    credit_interest = credit_interest / (12 * 100)
    monthly_payment = credit_principal * (credit_interest * (1 + credit_interest) ** periods) / ((1 + credit_interest) ** periods - 1)
    print(f'Your annuity payment = {math.ceil(monthly_payment)}!')
else:
    monthly_payment = float(input('Enter monthly payment: '))
    periods = float(input('Enter count of periods: '))
    credit_interest = float(input('Enter credit interest: '))
    credit_interest = credit_interest / (12 * 100)
    credit_principal = monthly_payment * ((1  + credit_interest) ** periods - 1) / (credit_interest * (1 + credit_interest) ** periods)
    print(f'Your credit principal = {round(credit_principal)}')