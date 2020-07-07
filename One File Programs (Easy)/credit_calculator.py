import argparse
import math
import sys

def diff_payment(P, n, i):
    overpay = 0
    i = i / (12 * 100)
    for m in range(1, n + 1):
        payment = math.ceil((P / n) + i * (P - (P * (m - 1)) / n))
        overpay += payment
        print(f'Month {m}: Paid out {payment}')
    overpay = overpay - P
    print(f'\nOverpayment = {math.ceil(overpay)}')


def ann_payment(P, a, n, i):
    i = i / (12 * 100)
    if P is None:
        P = int(a * ((1  + i) ** n - 1) / (i * (1 + i) ** n))
        print(f'Your credit principal = {P}')
    elif a is None:
        a = math.ceil(P * (i * (1 + i) ** n) / ((1 + i) ** n - 1))
        print(f'Your annuity payment = {a}!')
    else:
        n = math.ceil(math.log( a / (a - i * P),i + 1))
        years = int(n // 12)
        months = math.ceil(n % 12)
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
    overpay = int((a * n) - P)
    print(f'Overpayment = {overpay}')


parser = argparse.ArgumentParser(description='Calculate the Differentiated Payment')
parser.add_argument('--type')
parser.add_argument('--payment', type=float)
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
args = parser.parse_args()

if args.interest is None or len(sys.argv) < 5:
    print('Incorrect parameters.')
elif args.type == 'diff':
    if args.principal < 0 or args.interest < 0 or args.periods < 0 or args.payment is not None:
        print('Incorrect parameters.')
    else:
        diff_payment(args.principal, args.periods, args.interest)
elif args.type == 'annuity':
    ann_payment(args.principal, args.payment, args.periods, args.interest)
else:
    print('Incorrect parameters.')