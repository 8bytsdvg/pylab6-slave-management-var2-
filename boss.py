from team_structure import *
from slaves import *
import random

if __name__ == "__main__":
    salary = 0

    # for manager in managers:
    #     print(manager.hierarchy_info())

    for slave in slaves:
        slave.bonus(random.randint(1, 52))

    salary = sum(slave.salary for slave in slaves)

    # print(f"Total salary expenditure: {salary}")

    Menu = True
    while Menu:
        print("Menu:\n1. Viev employees\n2. Viev managers\n3. Viev total salary expenditure\n0. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            for slave in slaves:
                if not isinstance(slave, Manager):
                    print(slave.info())
        elif choice == '2':
            for manager in managers:
                print(manager.info())
        elif choice == '3':
            print(f"Total salary expenditure: {salary}")
        elif choice == '0':
            print("Exit the program.....")
            Menu = False