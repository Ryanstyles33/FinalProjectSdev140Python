"""
    Contains the functions to display the premiad sandwiches information with prices,
    all the ingredients for making your own sandwich with prices,
    calculating the total bill of self made sandwich using the user inputs

"""


def display_sandwiches():
    """ Display the premade sandwiches information with prices """
    
    ## A dictionary with sandwiches and their prices ##
    sandwiches = {'Grilled Cheese Sandwich':5,
                        'Grilled Chicken Sandwich':8,
                        'Turkey Sandwich':8,
                        'Roast Beef Sandwich':8, 
                        'Ham Sandwich':8,
                        'BLT Sandwich':8,
                        'Club Sandwich':8,
                        'Bacon Sandwich':8,
                        'Peanut Butter & Jelly':5, 
                        'Pulled Pork Sanwdwich':9,
                        'Tuna Sandwich':5,
                        'Egg Salad Sandwich':5,
                        'Meatball Sandwich':8,
                        'Reuben Sandwich':8,
                        'French Dip Sandwich':9}
    
    ## Sorting the dictionary alphabetically ##
    sorted_sandwiches = dict(sorted(sandwiches.items()))

    ## Return the sorted dictionary
    return sorted_sandwiches


def all_ingredients():
    """ Displays the ingredients and their prices for self made sandwiches """

    ## Dictionary contaning all the ingredients and information with prices ##
    options = {'Category': {'Veggie':3,
                            'Chicken':5,
                            'Beef':4}, 
               
               'Type of Bread': {'White Bread':2,
                                 'Sourdough Bread':3,
                                 'Whole Wheat Bread':2.5,
                                 'Rye Bread':2.7,
                                 'Potato Bread':2,
                                 'Gluten Free Bread':2.3,
                                 'Honey Oat Bread':2},

               'Type of Cheese': {'American':0.8,
                                  'Cheddar':0.5,
                                  'Colby':0.4,
                                  'Gouda':0.5,
                                  'Monterey Jack':0.6,
                                  'Mozzarella':0.7,
                                  'American Muenster':0.8,
                                  'Swiss':0.9},

               'Topping(s)': ['Lettuce', 'Tomato', 'Onion', 'Pickles'],

               'Sauce(s)': ['Mayonnaise', 'Ketchup', 'Mustard'],

               'Sandwich Size': {'Half':2,
                                 'Whole':1}
            }

    ## Return the dictionary ##
    return options


def get_price(category, breadtype, cheesetype, size):
    """ Calculates the total bill of self made sandwich using the user inputs """

    ## calling the all_ingredients function to get the ingredients dictionary ##
    ingredients = all_ingredients()

    category_price = ingredients["Category"][category]          # Getting the price of selected category
    bread_price = ingredients["Type of Bread"][breadtype]       # GEtting the price of selected bread type
    cheese_price = ingredients["Type of Cheese"][cheesetype]    # Getting the price of selected cheese type
    size_price = ingredients["Sandwich Size"][size]             # GEtting the price of selected sandwich size 

    ## Calculating the total bill ##
    total_price = (category_price + bread_price + cheese_price)/(size_price)

    ## Returning the total bill value ##
    return total_price