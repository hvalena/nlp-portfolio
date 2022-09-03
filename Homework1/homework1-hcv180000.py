# Homework 1
# Hannah Valena - HCV180000
# CS 4395.001: Human Language Technologies

import sys
import pathlib
import pickle
import re


class Person:
    def __init__(self, last, first, mi, id_, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id_ = id_
        self.phone = phone

    def display(self):
        """
        :return: print Person fields
        """

        print(f'Employee id: {self.id_}')
        print(f'\t\t{self.first} {self.mi} {self.last}')
        print(f'\t\t{self.phone}\n')


def process_input(text_input):
    """
    :param text_input: list of lines in the input file
    :return: dictionary of Persons, where the key is employee id, and Person data is standardized
    """

    persons = {}

    for text in text_input:
        # get fields as text variables
        text = text.split(",")

        # last and first name should be Capital Case
        last = text[0].capitalize()
        first = text[1].capitalize()

        # mi should be single letter UPPER CASE; if mi missing, use "X"
        if not text[2]:
            text[2] = "X"
        mi = text[2][0].upper()

        # id should be 2 letters + 4 digits
        id_ = verify_id(text[3], first, mi, last)

        # phone should be in format 999-999-9999
        phone = verify_phone(text[4], first, mi, last)

        # handle duplicate id
        if id_ in persons:
            print(f'\nError: Duplicate id {id_} found for {first} {mi} {last} and '
                  f'{persons[id_].first} {persons[id_].mi} {persons[id_].last}'
                  f'\nPlease correct this error in the input file')
            quit()

        # employee data is corrected
        p = Person(last, first, mi, id_, phone)
        persons[id_] = p

    return persons


def verify_id(id_, first, mi, last):
    """
    :param id_: employee's id to be verified
    :param first: employee's first name
    :param mi: employee's middle initial
    :param last: employee's last name
    :return: a valid formatted id
    """

    id_pattern = "[a-zA-z]{2}[0-9]{4}"
    while not re.fullmatch(id_pattern, id_):
        print(f"\nID invalid: {id_} for {first} {mi} {last}")
        print("ID is two letters followed by 4 digits")
        id_ = input("Please enter a valid id: ")
    return id_.upper()


def verify_phone(phone, first, mi, last):
    """
    :param phone: employee's phone number to be verified
    :param first: employee's first name
    :param mi: employee's middle initial
    :param last: employee's last name
    :return: a valid formatted phone number
    """

    phone_pattern_correct = r"[0-9]{3}-[0-9]{3}-[0-9]{4}"
    while not re.fullmatch(phone_pattern_correct, phone):
        print(f"\nPhone {phone} is invalid format for {first} {mi} {last}")

        # correct the format of phone numbers (eg 1234567890, 123 456 7890, (123) 456 7890, +1 (123) 456 7890, etc.)
        phone_pattern_any = r"(\+[0-9]+)?[ ]?(\(?[0-9]{3}\)?)[ -.]?([0-9]{3})[ -.]?([0-9]{4})"
        result = re.search(phone_pattern_any, phone)

        if result: # enough digits to reformat phone number
            phone_reformatted = f"{result.group(2)}-{result.group(3)}-{result.group(4)}"
            correct = input(f"Phone number reformatted to {phone_reformatted}\n"
                            f"Is this correct (Y/N)? ")

        if result and "y" in correct.lower():
            phone = phone_reformatted
        else:  # not enough digits in phone number or incorrect reformat
            phone = input("Enter phone number in format 999-999-9999: ")
    return phone


if __name__ == '__main__':
    # check sysarg for relative path
    if len(sys.argv) < 2:
        print('Error: You must specify a sysarg')
        quit()

    # read file
    rel_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r') as file:
        text_in = file.read().splitlines()

    # process input, ignore header line
    employees = process_input(text_in[1:])

    # save employees dict as a pickle file
    pickle.dump(employees, open('employees.pickle', 'wb'))

    # open pickle file for reading
    employees_in = pickle.load(open('employees.pickle', 'rb'))

    # print each Person employee
    print('\nEmployee list:\n')
    for employee_id in employees_in.keys():
        employees_in[employee_id].display()
