"""Pizza Order Processing Application.
This is a command line application to collect and process pizza orders""" 

import fire
import questionary
from pathlib import Path
from modules.functions.pizza_sizes1 import pizza_sizes
from modules.functions.pizza_toppings2 import pizza_topps
from modules.functions.pizza_toppings1 import pizza_required
from modules.functions.pizza_order1 import (
    order_confirm, 
    pz_order_paid, 
    toppings_not_required
    )
from modules.calculations import order_pricing

def pizza_order (): 
    pizza_order = questionary.confirm("Hello, this is R&H Pizza! Would you like a Pizza this fine afternoon?").ask()
    if pizza_order == True:
        print ("Excellent! We have a Small (S), Medium (M), Large (L), and Extra-Large (XL) Pizzas.")
        return('active')
    else:
        print("No issues, you can come back later on when you want a Pizza!")
        return ()

"""The main function for running the script."""
def run ():
    order_s = pizza_order()
    if order_s == 'active':
        pz_toppings,s_num_pizzas, m_num_pizzas, l_num_pizzas, xl_num_pizzas  = pizza_sizes(order_s)
    else: 
        return()
    if pz_toppings == 'active':
        pz_top = pizza_topps(pz_toppings)
    else: 
        toppings_not_required ()
    if pz_top == 'active':
        pz_order, toppings_num = pizza_required(pz_top)
    else: 
        return()
    pz_payment = order_confirm(pz_order)
    if pz_order == 'active':
        pz_pay_confirm = order_pricing(pz_payment, s_num_pizzas, m_num_pizzas, l_num_pizzas, xl_num_pizzas, toppings_num)
    else:
        return ()
    complete = pz_order_paid (pz_pay_confirm)

run()
if __name__ == '--main--':
    fire.Fire()
#next_step = input ("Do you want to order pizza again?:")
#if next_step == 'y':
#    pizza_order ()
#else:
#print ("Thank you, Looking forard to serve you again!")