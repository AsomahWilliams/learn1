total_bill = float(input("Enter the total bill amount: $"))
if total_bill > 100:
    discount = total_bill * 0.10
    final_amount = total_bill - discount
    print(f"Discount applied: ${discount:.2f}")
else:
    final_amount = total_bill
print(f"Final amount to be paid: ${final_amount:.2f}")   