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
    :return: dictionary of Persons, where the key is id

    Processes the input file to make the text uniform
    """

    # type checking
    if not type(text_input) == list:
        return "Error: \"names\" is not a list"

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

        # id should be 2 letters + 4 digit
        id_ = text[3]
        id_pattern = "[a-zA-z]{2}[0-9]{4}"
        while not re.fullmatch(id_pattern, id_):
            print(f"\nID invalid: {id_}")
            print("ID is two letters followed by 4 digits")
            id_ = input("Please enter a valid id: ")
        id_ = id_.upper()

        # phone should be in format 999-999-9999
        phone = text[4]
        phone_pattern = "[0-9]{3}-[0-9]{3}-[0-9]{4}"
        while not re.fullmatch(phone_pattern, phone):
            print(f"\nPhone {phone} is invalid")
            print(f"Enter phone number in form 123-456-7890")
            phone = input("Enter phone number: ")

        # employee data is correct
        p = Person(last, first, mi, id_, phone)

        # handle duplicate id
        if id_ in persons:
            print(f'Error: id {id_} is repeated')
            quit()

        persons[id_] = p

    return persons


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
