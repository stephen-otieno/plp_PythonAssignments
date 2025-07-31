
def calculate_discount():
    original_price = float(input("Enter the price of the item(in Ksh): "))
    discount_percent = float(input("Enter the product discount(in %): "))

    if discount_percent > 20:
        final_price = original_price - (original_price * discount_percent)/100
        print("**********")
        print(f"Payable amount: Ksh.{final_price:.2f}")
        print("**********")

    elif discount_percent < 20:
        print(f"Payable amount: Ksh.{original_price:.2f}")


if __name__ == "__main__":
    calculate_discount()
