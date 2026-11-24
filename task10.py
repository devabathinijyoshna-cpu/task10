venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificates = float(input("Enter certificate cost: "))

sponsorship = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per student: "))

total_cost = venue + equipment + catering + transport + certificates

remaining = total_cost - sponsorship

if remaining > 0:
    students = int(remaining / fee)

    if remaining % fee != 0:
        students = students + 1
else:
    students = 0

print("Total Event Cost:", total_cost)
print("Sponsorship:", sponsorship)
print("Remaining Amount:", max(0, remaining))
print("Minimum Registrations Required:", students)

if sponsorship >= total_cost:
    print("Event is Fully Sponsored")
else:
    print("Registration Fees are Required")