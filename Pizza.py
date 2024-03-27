temp = float(input('What temperature is the oven?'))

if temp > 200:
    print('The oven is too hot')
elif temp < 150:
    print('The oven is too cold')
elif temp == 180:
    print('The oven is at the perfect temperature')
else:
    print('The temperature is close enough')
