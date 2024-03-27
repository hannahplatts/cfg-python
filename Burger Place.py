price = input('How much is a burger?')
within_budget = float(price) <= 10

veg = input('Is there a vegetarian option (Yes/No?)')
has_veg = veg == 'yes'

suitable = within_budget and has_veg

if suitable:
    print('This restaurant is a great choice!')

if not suitable:
    print('Probably not a good idea.')
