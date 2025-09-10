#Module

def apply_discount(price, discount_percent):
    discounted_price = price - (price * discount_percent / 100)
    return discounted_price
def add_gst(price, gst_percent=18):
    price_with_gst = price + (price * gst_percent / 100)
    return price_with_gst
def generate_invoice(cart, discount_percent=0, gst_percent=18):
    print("\n------ INVOICE ------")
    subtotal = 0
    for product, price in cart.items():
        print(f"{product:<15}: ₹{price}")
        subtotal += price
    print("---------------------")
    print(f"Subtotal: ₹{subtotal}")
    if discount_percent > 0:
        discounted_total = apply_discount(subtotal, discount_percent)
        print(f"After {discount_percent}% discount: ₹{discounted_total}")
    else:
        discounted_total = subtotal
    final_total = add_gst(discounted_total, gst_percent)
    print(f"After {gst_percent}% GST: ₹{final_total:.2f}")
    print("---------------------")
    print("Thank you for shopping with us!\n")
