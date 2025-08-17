
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        print("Final Price after discount:", final_price)
    else:
        print("No discount applied. Final Price:", price)

price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

calculate_discount(price, discount_percent)

