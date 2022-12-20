from textwrap import dedent

def hello_world():
    welcome_intro = dedent("""
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
        """)
    print(welcome_intro)


def print_menu():
    menu = dedent("""
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls
    
    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden
    
    Desserts
    --------
    Ice Cream
    Cake
    Pie
    
    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    
    ***********************************
    ** What would you like to order? **
    ***********************************
    """)
    print(menu)

def add_to_order():

    current_order = {
        "Wings": 0,
        "Cookies": 0,
        "Spring Rolls": 0,
        "Salmon": 0,
        "Steak": 0,
        "Meat Tornado": 0,
        "A Literal Garden": 0,
        "Ice Cream": 0,
        "Cake": 0,
        "Pie": 0,
        "Coffee": 0,
        "Tea": 0,
        "Unicorn Tears": 0
    }

    ask_again = True
    while ask_again:
        menu_item = input("> ")
        if menu_item in current_order:
            current_order[menu_item] += 1
            print(f"** {current_order[menu_item]} order of {menu_item} have been added to your meal **")
        elif menu_item=="quit":
            break
        else:
            print_menu()



if __name__ == "__main__":
    hello_world()
    print_menu()
    add_to_order()
