# AIM: Write a Python program to calculate the gross salary of an employee.
# Coder: mehreen ansari
# Date: 08\02\26

print("****GROSS SALARY CALCULATOR****")
basic_salary = float(input())
da = basic_salary*0.70
ta = basic_salary*0.30
hra = basic_salary*0.10
gross_salary = basic_salary + da + ta + hra

print("\nSalary Details :")
print(f"{'Basic Salary' :15}\t{basic_salary}")
print(f"{'DA' :15}\t{da}")
print(f"{'TA' :15}\t{ta}")
print(f"{'HRA' :15}\t{hra}")
print(f"{'Gross Salary' :15}\t{gross_salary}")
