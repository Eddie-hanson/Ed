#for calculating basic salary
hourly_wage= float(12.00)
hour_worked= int(8)
basic_salary=(hour_worked*hourly_wage)

#for calculating overtime pay
overtime_wage= float(15.00)
overtime_worked= int(4)
overtime_salary=(overtime_wage*overtime_worked)

#for calculating total salary
total_salary= basic_salary+ overtime_salary 
print(f" Your basic salary is {basic_salary} and your over time pay is {overtime_salary}. \n Your total salary is Ghc. {total_salary}")

