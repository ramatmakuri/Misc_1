import questionary
def pizza_topps (pz_toppings):        
    while pz_toppings == 'active':
        toppings_reqd = questionary.confirm("Do you need extra toppings on your Pizza?").ask()
        if toppings_reqd == True:
            return ('active')
        else:
            return('inactive')
            
""" confirmation = questionary.confirm ("Are you sure that you do not want toppings on your Pizza? : "). ask()
            if confirmation == True:
                toppings_reqd = False """