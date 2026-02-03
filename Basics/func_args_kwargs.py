def pizza(size, *toppings, **details):
   print (f'You ordered a {size} pizza with the following toppings:\n')
   for topping in toppings:
        print (f'-{topping}\n')
   print('Additional details:')
   for key, value in details.items():
        print (f'{key}:{value}')

pizza('Large', 'Chicken', 'Mushrooms', 'Corn', crust='Thin', extra_cheese=True)
      