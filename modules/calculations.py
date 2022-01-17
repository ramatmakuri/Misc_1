import fire
# Price Calulator
def order_pricing (pz_payment, s_num_pizzas, m_num_pizzas, l_num_pizzas, xl_num_pizzas, toppings_num):
    while pz_payment == 'active':
        global price_calc 
        global sales_tax_rate
        global tax
        price_calc = float(0)
        price_calc_wtax = float(0)
        tax = float(0)
        price_list_size = {
        "XL": int(45),
        "L" : int(40),
        "M" : int(35),
        "S" : int(30),
        }   
        price_per_topping = int(2)
        sales_tax_rate =  float(.08) 
        price_calc += ((price_list_size["S"] * s_num_pizzas + price_list_size["M"] * m_num_pizzas + price_list_size["L"] * l_num_pizzas + price_list_size["XL"] * xl_num_pizzas)+ (price_per_topping * toppings_num))
        tax = price_calc * sales_tax_rate
        price_calc_wtax = price_calc + tax 
        print (f"The price for yor Pizza is $ {price_calc}")
        print (f"The tax on your Pizza is $ {tax}")
        print (f"The total price for yor Pizza is $ {price_calc_wtax}")
        return('active')

