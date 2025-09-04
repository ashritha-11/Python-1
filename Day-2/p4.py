def cost(x):
    if 1 <= x <= 50:
        cbill = x * 3.80
    elif 51 <= x <= 100:
        cbill = (50 * 3.80) + ((x - 50) * 4.20)
    elif 101 <= x <= 200:
        cbill = (50 * 3.80) + (50 * 4.20) + ((x - 100) * 5.10)
    elif 201 <= x <= 300:
        cbill = (50 * 3.80) + (50 * 4.20) + (100 * 5.10) + ((x - 200) * 6.30)
    elif x > 300:
        cbill = (50 * 3.80) + (50 * 4.20) + (100 * 5.10) + (100 * 6.30) + ((x - 300) * 7.50)
    else:
        print("Invalid input")
        return
    
    print("Total Bill =", cbill)

cost(154)
