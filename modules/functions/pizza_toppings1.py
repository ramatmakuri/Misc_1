import fire
import questionary

def pizza_required (pz_top): 
    toppings = ['Mushroom', 'Pepperoni', 'Basil', 'Pineapple', 'Extra cheese', 'Black olives', 'Tomatoes']
    global toppings_num
    toppings_num =  0
    global instock
    global requested_topping
    instock = []
    topping = []
    top = []
    instock =  questionary.checkbox (f"select the toppings you require",  choices =  ['Mushroom', 'Pepperoni', 'Basil', 'Pineapple', 'Extra cheese', 'Black olives', 'Tomatoes']).ask()
    a_set = set(toppings)
    b_set = set(instock)
    while pz_top == 'active':
        if len (a_set.intersection(b_set))>0:
            print (f"adding {topping}")
            top.append (topping)
            toppings_num += len(instock) 
            print (f"Number of toppings added is equal to {toppings_num}")
            return ("active", toppings_num) 
        else: 
            return ("No toppings are added")



"""def pizza_required (): 
    toppings = ['mushroom', 'pepperoni', 'basil', 'pineapple', 'extra cheese', 'black olives', 'tomatoes']
    global toppings_num
    toppings_num =  0
    global top
    global requested_topping
    topping = []
    top = []
    for topping in toppings:
        instock =  questionary.confirm (f'do you want  {topping}?: ').ask()
        if instock == True:
            print (f"adding {topping}")
            top.append (topping)
            toppings_num += 1 
        else: print (f"topping {topping}, is not added")
    print (f"Number of toppings added is equal to {toppings_num}")
    order_confirm ()"""    