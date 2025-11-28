from team_structure import *
from slaves import *
import random

if __name__ == "__main__":
    salary = 0

    for manager in managers:
        print(manager.hierarchy_info())

    for slave in slaves:
        slave.bonus(random.randint(1, 52))

    salary = sum(slave.salary for slave in slaves)

    print(f"Total salary expenditure: {salary}")