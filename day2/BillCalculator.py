bill = int(input("Enter the bill:"))
tip = int(input("Enter the tip percentage:"))
people = int(input("Enter the numberof people:"))

total_bill = bill * (tip/100) + bill
split = total_bill / people 

print("Total bill:",round(total_bill,2))
print("Each person has to pay:",round(split,2))
