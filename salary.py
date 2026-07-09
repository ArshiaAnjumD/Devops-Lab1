salary = float(input("Enter the basic salary: "))
hra = 0.2*salary
da = 0.1*salary
total = salary + hra + da
tax = 0.05*gross

net_sal= total-tax

print("Net Salary is ",net_sal)