from team_structure import *

emp1 = Employee("Eugen", "Developer", 20000)
emp2 = Employee("Anna", "Designer", 18000)
emp3 = Employee("John", "Tester", 15000)
emp4 = Employee("Kate", "Support", 14000)
emp5 = Employee("Tom", "Analyst", 17000)
emp6 = Employee("Mike", "Intern", 10000)
emp7 = Employee("Sara", "HR", 16000)
emp8 = Employee("Bob", "DevOps", 19000)
emp9 = Employee("Linda", "Marketing", 17500)
emp10 = Employee("James", "Sales", 16500)
emp11 = Employee("Nancy", "Junior Developer", 12300)
emp12 = Employee("Chris", "Junior Designer", 11500)
emp13 = Employee("Pat", "Junior Tester", 11000)
emp14 = Employee("Alex", "Web Designer", 10500)

creative_team = [emp2, emp12 , emp14]
qa_team = [emp3, emp13]
dev_team = [emp1, emp8, emp11]
support_team = [emp4, emp5, emp6]
business_team = [emp7,  emp9, emp10]


creative_manager = Manager("Olivia", "Creative Manager", 30000, creative_team)
qa_manager = Manager("Liam", "QA Manager", 28000, qa_team)
dev_manager = Manager("Noah", "Development Manager", 35000, dev_team)
support_manager = Manager("Emma", "Support Manager", 27000, support_team)
business_manager = Manager("Ava", "Business Manager", 32000, business_team)

managers = [creative_manager, qa_manager, dev_manager, support_manager, business_manager]
slaves = [emp1, emp2, emp3, emp4, emp5, emp6, emp7, emp8, emp9, emp10, emp11, emp12, emp13, 
            emp14, creative_manager, qa_manager, dev_manager, support_manager, business_manager]