meal_price = float(input('How much did the meal cost?'))
discount = input('Do you have a discount? (Y/N)')

meal_total = meal_price >= 20
discount_yes = discount == 'yes'
discount_apply = meal_total and discount_yes

if discount_apply:
    meal_price = (meal_price * 0.9)
    print('Discount applied')
else:
    print('No discount applied')

print('Total cost {}'.format(meal_price))
