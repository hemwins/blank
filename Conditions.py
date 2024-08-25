house_price = 100000
has_good_credit = True
#if has_good_credit :
#    house_price = house_price/10
#    print(f'house price for 10: {house_price}')
#else:
#    house_price = house_price/5
#    print(f'house price for 20: {house_price}')
name = input("Please enter your name ")
if len(name) < 3:
    print("enter at least three characters")
elif len(name) > 50:
    print("too long name")
else:
    print("great name!")