import fire
import questionary

def pizza_sizes (order_s):
    av_sizes = ['Small','Medium','Large','Extra Large',]
    #order_s = "active"
    global size 
    global s_num_pizzas
    s_num_pizzas = 0
    global m_num_pizzas
    m_num_pizzas = 0
    global l_num_pizzas
    l_num_pizzas = 0
    global xl_num_pizzas 
    xl_num_pizzas = 0
    while  order_s == "active":
        size = questionary.select ("What size Pizza would you like?:", choices = ['Small', 'Medium', 'Large', 'Extra Large']).ask()
        if size in av_sizes:            
            if size == 'Small': 
                s_num_pizzas +=1
            elif size == 'Medium':
                m_num_pizzas +=1
            elif size == 'Large':
                l_num_pizzas +=1
            elif size == 'Extra Large':
                xl_num_pizzas +=1
            print (f"Great! We will check on Toppings next")
            order_s = "inactive"
            pz_toppings = 'active'
            return ('active',s_num_pizzas, m_num_pizzas, l_num_pizzas, xl_num_pizzas)
        else:
            print ("Sorry, R&H serves only specified sizes. Please select an available Pizza size and reorder.")
            recheck = questionary.confirm("Would you want to select an available size pizza?: ").ask()
            if recheck == True:
                order_s = "active"
            else: 
                order_s = "inactive" 
                return ("inactive")
            