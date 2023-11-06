cart_total = float(input("Enter your cart total: "))

if cart_total >= 100:
    discount = 10
    final_total = cart_total - (cart_total * discount / 100)
    print(f"You are eligible for a {discount}% discount. Your final total is ${final_total:.2f}.")
else:
    final_total = cart_total
    print(f"Your final total is ${final_total:.2f}.")
