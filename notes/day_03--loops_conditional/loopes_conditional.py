""" Loops and Conditionals Refresher """
import sys

# Need to be at least 13 years old
# You need to contribute at least $100
# Don't have a criminal record.

# Result:  Your approved or
# Not approved
# - Tell the reason why.

MIN_AGE = 13
MIN_DONATION = 100

def check_age(age):
    """ Returns true/false if the user is old enough """
    if int(age) >= MIN_AGE:  # types (Python does not know how to compare different types)
        return True
    else:
        return False


def check_donation(donation):
    if int(donation) >= MIN_DONATION:
        return True
    return False


def check_record(record):
    if record.upper() == 'TRUE':
        return True
    return False


def check_inputs(is_old_enough, donated_enough, has_a_record):
    is_approved = True
    reasons = []  # Create a array of reason

    if not is_old_enough:
        is_approved = False
        reasons.append('Not old enough')  

    if not donated_enough:
        is_approved = False
        reasons.append('Did not donate enough')  

    if has_a_record:
        is_approved = False
        reasons.append('Has a criminal record')  # reasons['Not old enough', 'Did not donate enough', 'Has a criminal record']
        # reasons['Has a criminal record']
    if is_approved:
        print('Congratulations, you are approved!!!')
    else:
        print('Sorry, you are not approved.')
        print('Reason = ' + ','.join(reasons))

    return is_approved


if __name__ == "__main__":
    AGE = input('How old are you (in years)? ')  # integer
    # if not (1 == 1):
    #     print('inside True Block')
    # else:
    #     print('inside False Block')

    DONATION = input('How much would you like to donate? ')  # integer

    RECORD = input('Do you have a criminal record (True/False)? ')  # boolean 
    if RECORD.upper() != "TRUE" and RECORD.upper() != "FALSE":
        print('[ERROR] Record should be True/False')
        sys.exit(1)

    is_old_enough = check_age(AGE)
    donated_enough = check_donation(DONATION)
    has_a_record = check_record(RECORD)

    check_inputs(is_old_enough, donated_enough, has_a_record)