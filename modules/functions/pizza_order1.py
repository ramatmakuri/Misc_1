import fire
import questionary

def order_confirm (pz_order): 
    while pz_order == 'active':
        pz_order_confirm = questionary.confirm("Please confirm the order").ask()
        #f"Please confirm the order comprising of {size} Pizza with extra {instock}? ")
        if pz_order_confirm == True:
            return ('active')
        else:
            return ('inactive') 
        
def pz_order_paid (pz_pay_confirm): 
    order_paid = questionary.confirm("Did the customer pay for the order?: ").ask()
    if order_paid == True:
        print (f"Your order is confirmed. Finished making your  Pizza with extra toppings")
    else: 
        order_placed = "n"
        s_num_pizzas = int(0)
        m_num_pizzas = int(0)
        l_num_pizzas = int(0)
        xl_num_pizzas = int(0)
        toppings_num = int(0)
        
def toppings_not_required ():
            print ("Your Pizza without extra toppings is ready for your enjoyment!")
