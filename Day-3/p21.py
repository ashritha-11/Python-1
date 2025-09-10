#main program
import p20 as main
cart = {
    "Laptop": 55000,
    "Phone": 30000,
    "Headphones": 2000
}
main.generate_invoice(cart, discount_percent=10)
