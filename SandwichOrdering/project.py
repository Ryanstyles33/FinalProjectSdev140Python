from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkm
from sandwiches_data import *

class Welcome(Tk):
    'Displays the Welcome Window with options'
    
    def __init__(self):
        super(Welcome, self).__init__()

        self.title('Welcome')               # Setting the Window's Title
        self.geometry('800x640+270+20')     # Setting the Window's Size
        self.resizable(0,0)                 # Making Window Unresizable
        self.focus()                        # Making window Focused

        self.main_menu()                    # Calling the main_menu method


    def main_menu(self):
        """ Displays Main Menu Screen """

        ## Frame for Main Menu Widgets ##
        self.mainmenu_frame = Frame(self)
        self.mainmenu_frame.pack()

        ## Importing the sandwich image from directory ##
        self.sandwich_image1 = PhotoImage(file = 'Sandwich.png').subsample(2,2)

        ## Welcome Label ##
        welcome_label = Label(self.mainmenu_frame, text = 'Welcome to', fg = 'green', font = ('Lucida Calligraphy', '25', 'bold', 'italic'), padx = 10)
        welcome_label.pack(pady = (20,0))

        ## Project Name Label ##
        name_label = Label(self.mainmenu_frame, text = 'Online Sandwich Request', fg = 'purple', font = ('Pristina', '35', 'bold'), padx = 10, pady = 10)
        name_label.pack()

        ## Adding the Image to the Menu Screen
        name_label.configure(image = self.sandwich_image1, compound = BOTTOM)

        ### MENU BUTTONS ###
        ## Frame for holding menu buttons ##
        button_Frame = Frame(self.mainmenu_frame)
        button_Frame.pack(pady = 5)

        ## Order Now Button ##
        ordernow_button = Button(button_Frame, text = 'Order Now', bg = 'yellow', fg = 'red', font = ('Lucida Handwriting', '15', 'bold'), command = self.ordernow_menu)
        ordernow_button.pack(padx = 5)

        ## Make You Own Sandwich Button ##
        createown_button = Button(button_Frame, text = 'Make Your Own Sandwich', bg = 'light blue', fg = 'dark blue', font = ('Lucida Handwriting', '12', 'bold'), command = self.make_your_own)
        createown_button.pack(padx = 5, pady = 10)

        ## Exit Button ##
        exit_Button = Button(button_Frame, text = 'EXIT', padx = 5, command = self.destroy, bg = 'pink', fg = 'brown', font = ('Lucida Handwriting', '10', 'bold'))
        exit_Button.pack(padx = 5)


    def ordernow_menu(self):
        """ Displays the list of premade sandwiches with their respective prices """

        ### Hiding the previous screen i.e. Main Menu ###
        self.mainmenu_frame.pack_forget()

        self.title('Premaid Sandwiches')    # Title of New Window
        
        ## Importing the second sandwich image ##
        self.sandwich_image2 = PhotoImage(file = 'Sandwich2.png')
        
        ## Frame for holding menu widgets ##
        self.menu_frame = Frame(self)
        self.menu_frame.pack()

        ## Canvas to show the sandwich image in the background ##
        imagecanvas = Canvas(self.menu_frame, width = 800, height = 640)
        imagecanvas.pack()

        ## Adding the image to the background ##
        imagecanvas.create_image(0,0, anchor = NW, image = self.sandwich_image2)

        ## Inner frame for holding the premaid sandwiches information ## 
        sandwiches_frame = Frame(imagecanvas)
        sandwiches_frame.pack()

        ## Adding the inner frame on the backgound image ##
        imagecanvas.create_window(170,10, window = sandwiches_frame, anchor = NW)

        ## Select Your Sandwich Label ##
        selction_label = Label(sandwiches_frame, text = 'Select Your Sandwich', padx = 25, bg = 'pink', fg = 'brown', font = ('Lucida Calligraphy', '25', 'bold', 'italic'))
        selction_label.pack()

        ## Another inner frame inside the menu_frame ##
        types_frame = Frame(sandwiches_frame)
        types_frame.pack(pady = 10)

        ## Columns names to be displayed ##
        headers = ['Select', 'Sandwich Type', 'Price', 'Quantity']

        ## Adding the labels for the columns headers in a loop ##
        for i in headers:
            Label(types_frame, text = i, font = (" ", 12, 'bold'), fg = 'green').grid(row = 0, column = headers.index(i))

        ## Calling the function display_sandwiches from the module 'sandwiches_data.py' and storing ...
        ## ... the sandwiches information/data in the variable "all_sandwiches" 
        all_sandwiches = display_sandwiches()

        self.cbvars = []    # Defining an empty list to store all variables belonging to checkbuttons for sandwich selection
        self.qnvars = []    # Defining an empty list to store all variables belonging to spinboxes for sandwich qunatity

        i = 1                               # A random variable to keep the record of iterations
        for s in all_sandwiches:            # for loop to the sandwiches list
            var = IntVar(self, value = 0)   # Variable for each checkbutton
            self.cbvars.append(var)         # Storing the variable to the previously defined list
            
            ## Displaying the checkbuttons for sandwich selections in 1st column ##
            check = Checkbutton(types_frame, variable = var, onvalue = all_sandwiches[s], command = self.get_values)
            check.grid(row = i, column = 0)

            ## Displaying the sandwiches names in the 2nd column ##
            sandwich_name = Label(types_frame, text = f"{s}", font = (" ", 10, 'bold'))
            sandwich_name.grid(row = i, column = 1, sticky = W)
            
            ## Displaying the sandwiches prices in the 3rd column ##
            price = Label(types_frame, text = f"${all_sandwiches[s]}.00", font = (" ", 10, 'bold'))
            price.grid(row = i, column = 2, sticky = E, padx = 20)

            ## Displaying the checkbuttons for sandwich quantity in 4th column ##
            quantity = Spinbox(types_frame, width = 4, font = (" ", 10, 'bold'), from_ = 1, to = 20, command = self.get_values)
            quantity.grid(row = i, column = 3)
            
            ## Storing the spinbox to the previously defined list
            self.qnvars.append(quantity)

            i+=1    # Increasing the interation tracker's value by 1

        ## Frame for storing the widgets related to bill displaying ##
        totalbill_frame = Frame(sandwiches_frame)
        totalbill_frame.pack()

        ## Total Bill Label ##
        total_label = Label(totalbill_frame, text = 'Total Bill:', fg = 'dark blue', font = (" ", 12, 'bold'))
        total_label.pack(side = LEFT)

        ## Label to show the bill value ##
        self.total_bill = Label(totalbill_frame, text = f"$0.00", fg = 'dark green', font = (" ", 15, 'bold', 'italic'))
        self.total_bill.pack(side = LEFT)

        ## Place Order Button ##
        order = Button(sandwiches_frame, text = 'Place Order!', fg = 'red', bg = 'yellow', font = ('Lucida Handwriting', '12', 'bold'), command = self.place_order)
        order.pack(pady = (10))

        ## Back to Main Menu Button ##
        back_button = Button(sandwiches_frame, text = 'Back to Main Menu', fg = 'dark blue', bg = 'light blue', font = ('Lucida Handwriting', '10', 'bold'), command = self.back_to_main1)
        back_button.pack(pady = (5,20))


    def get_values(self):
        """ Gets all the values from sandwiches menu and display the total bill """
        
        ## Getting the values of all selected sandwiches ##
        price = [var.get() for var in self.cbvars]

        ## Getting the quantity of all selected sandwiches ##
        quantity = [int(var.get()) for var in self.qnvars]
    
        ## Calculating the total bill
        bill = list(map(lambda x,y: x*y, price, quantity))

        ## Displaying the price in the label ##
        self.total_bill.configure(text = f"${sum(bill)}.00")


    def back_to_main1(self):
        """ Going back to main mneu from premaid sandwiches menu """
        
        ## Hiding the previous screen i.e. Order Now Menu ##
        self.menu_frame.pack_forget()

        ## Displaying the main menu ##
        self.mainmenu_frame.pack()


    def back_to_main2(self):
        """ Going back to main mneu from make your own sandwiche menu """

        ## Hiding the previous screen i.e. Order Now Menu ##        
        self.options_frame.pack_forget()

        ## Displaying the main menu ##
        self.mainmenu_frame.pack()


    def make_your_own(self):
        """ Displays the Window for Make Your Own Sandwich option """

        ### Hiding the previous screen i.e. Main Menu ###
        self.mainmenu_frame.pack_forget()

        self.title('Make Your Own Sandwich')    # Title of New Window

        ## Calling the function all_ingredients from the module 'sandwiches_data.py' and storing ...
        ## ... the ingredients information/data in the variable "ingredients" 
        ingredients = all_ingredients()
        
        ## Frame for holding options/ingredients widgets ##
        self.options_frame = Frame(self)
        self.options_frame.pack()

        ## Importing the third sandwich image ##
        self.sandwich_image3 = PhotoImage(file = 'Sandwich3.png')

        ## Canvas to show the sandwich image in the background ##
        imagecanvas = Canvas(self.options_frame, width = 800, height = 640)
        imagecanvas.pack()

        ## Adding the image to the background ##
        imagecanvas.create_image(0,0, anchor = NW, image = self.sandwich_image3)

        ## Inner frame for holding the ingredients information ##
        ingredients_frame = Frame(imagecanvas)
        ingredients_frame.pack()

        ## Adding the inner frame on the backgound image ##
        imagecanvas.create_window(130,70, window = ingredients_frame, anchor = NW)

        ## Make Your Own Sandwich Label ##
        makeyourown_label = Label(ingredients_frame, text = 'Make Your Own Sandwich', padx = 25, bg = 'pink', fg = 'brown', font = ('Lucida Calligraphy', '25', 'bold', 'italic'))
        makeyourown_label.pack()

        ## Another inner frame inside the ingredients_frame #
        selection_frame = Frame(ingredients_frame)
        selection_frame.pack(pady = 10)

        ## Getting the values to be shown for labels and storing it in the variable options ##
        options = list(ingredients.keys())

        ## Adding the labels for the options in a loop ##
        for i in range(len(options)):
            Label(selection_frame, text = options[i], font = (" ", 12, 'bold')).grid(sticky = W, row = i, column = 0)

        ## Changing the style for the comboboxes ##
        style = ttk.Style()
        style.configure('TCombobox', arrowsize = 15)

        ## Combobox for category ##
        self.category = ttk.Combobox(selection_frame, font = 'TkDefaultFont 11', width = 23, value = [f"{ing} (${'{:.2f}'.format(price)})" for ing,price in ingredients["Category"].items()], style = 'TCombobox')
        self.category.grid(sticky = W, row = 0, column = 1, padx = 15)

        ## Combobox for bread type ##
        self.breadtype = ttk.Combobox(selection_frame, font = 'TkDefaultFont 11', width = 23, value = [f"{ing} (${'{:.2f}'.format(price)})" for ing,price in ingredients['Type of Bread'].items()], style = 'TCombobox')
        self.breadtype.grid(sticky = W, row = 1, column = 1, pady = 8, padx = 15)

        ## Combobox for cheese type ##
        self.cheesetype = ttk.Combobox(selection_frame, font = 'TkDefaultFont 11', width = 23, value = [f"{ing} (${'{:.2f}'.format(price)})" for ing,price in ingredients["Type of Cheese"].items()], style = 'TCombobox')
        self.cheesetype.grid(sticky = W, row = 2, column = 1, padx = 15)

        ## Another inner frame for checkbuttons for topping type ##
        topping_frame = Frame(selection_frame)
        topping_frame.grid(sticky = W, row = 3, column = 1, pady = (12,6), padx = 10)

        ## Changing the style of checkbuttons ##
        style.configure('TCheckbutton', font = 12)

        # Defining an empty list to store all variables belonging to checkbuttons for toppings selection
        self.toppings = []
        
        ## Labels for toppings options ##
        toppings_options = ingredients["Topping(s)"]
        
        r = 0   # A random varibale to keep the row number for widget placement
        c = 0   # A random variable to keep the column number for widget placement

        ## Creating the chechbuttons for topping options in a loop ##
        for t in toppings_options:
            var = IntVar(self, value = 0)   # Variable for each checkbutton
            self.toppings.append(var)       # Storing the variable in the previously defined list
            check = ttk.Checkbutton(topping_frame, text = t, variable = var, onvalue = t, style = 'TCheckbutton')
            check.grid(row = r, column = c, padx = 4)
            c+=1        # Increasing the column number by 1
            if c%3==0:  # If 3 checkbuttons are placed in row ...
                r+=1    # Increment the row number by 1 i.e. move to the next row
                c=0     # Set the varible for column number to 0

        ## Another inner frame for checkbuttons for sauces type ##
        sauces_frame = Frame(selection_frame)
        sauces_frame.grid(sticky = W, row = 4, column = 1, padx = 10, pady = (4,12))

        # Defining an empty list to store all variables belonging to checkbuttons for toppings selection
        self.sauces = []

        ## Labels for sauces options ##
        sauces_options = ingredients["Sauce(s)"]

        r = 0   # A random varibale to keep the row number for widget placement
        c = 0   # A random variable to keep the column number for widget placement

        ## Creating the chechbuttons for sauces options in a loop ##
        for s in sauces_options:
            var = IntVar(self, value = 0)   # Variable for each checkbutton
            self.sauces.append(var)         # Storing the variable in the previously defined list
            check = ttk.Checkbutton(sauces_frame, text = s, variable = var, onvalue = s, style = 'TCheckbutton')
            check.grid(row = r, column = c, padx = 4)
            c+=1        # Increasing the column number by 1
            if c%3==0:  # If 3 checkbuttons are placed in row ...
                r+=1    # Increment the row number by 1 i.e. move to the next row
                c=0     # Set the varible for column number to 0

        ## Another inner frame for radiobuttons for sandwich size ##
        size_frame = Frame(selection_frame)
        size_frame.grid(sticky = W, row = 5, column = 1, padx = 10)

        ## Labels for size options ##
        size_options = [ing for ing in ingredients['Sandwich Size'].keys()]

        ## Variable for each radiobutton ##
        self.sandwich_size = StringVar(None, value = 'None')

        ## Changing the style of the radiobuttons ##
        s = ttk.Style()
        s.configure('my.TRadiobutton', font = (" ", 12), background = self.cget('bg'))

        ## Radiobutton for "Half" sandwich option ##
        half_option = ttk.Radiobutton(size_frame, text = size_options[0], style = 'my.TRadiobutton', variable = self.sandwich_size, value = size_options[0], command = self.calculate_price)
        half_option.grid(row = 0, column = 0, padx = 4)

        ## Radiobuuton for "Whole" sandwich option ##
        whole_option = ttk.Radiobutton(size_frame, text = size_options[1], style = 'my.TRadiobutton', variable = self.sandwich_size, value = size_options[1], command = self.calculate_price)
        whole_option.grid(row = 0, column = 1, padx = 10)

        ## Frame for storing the widgets related to bill displaying ##
        totalbill_frame2 = Frame(ingredients_frame)
        totalbill_frame2.pack(pady = (10,0))

        ## Total Bill Label ##
        total_label = Label(totalbill_frame2, text = 'Total Bill:', fg = 'dark blue', font = (" ", 12, 'bold'))
        total_label.pack(side = LEFT)

        ## Label to show the bill value ##
        self.total_bill2 = Label(totalbill_frame2, text = f"$0.00", fg = 'dark green', font = (" ", 15, 'bold', 'italic'))
        self.total_bill2.pack(side = LEFT)

        ## Place Order Button ##
        order2 = Button(ingredients_frame, text = 'Place Order!', fg = 'red', bg = 'yellow', font = ('Lucida Handwriting', '12', 'bold'), command = self.place_order)
        order2.pack(pady = (10))

        ## Back to Main Menu Button ##
        back_button2 = Button(ingredients_frame, text = 'Back to Main Menu', fg = 'dark blue', bg = 'light blue', font = ('Lucida Handwriting', '10', 'bold'), command = self.back_to_main2)
        back_button2.pack(pady = (5,20))

    
    def place_order(self):
        """ Shows the popup window for order information """

        self.info_window = Toplevel(self, bg = 'light green')   # Creating the popup window
        self.info_window.title('Order Information')             # Title of popup window
        self.info_window.geometry('380x250+480+220')            # Size of popup window
        self.info_window.focus()                                # Make the popup window focused

        ## frame to hold the widgets for order information ##
        info_frame = Frame(self.info_window, bg = 'light green')
        info_frame.pack(pady = (20,10))

        ## Label for 'Name' ##
        name_label = Label(info_frame, text = "Name", font = (" ", 11, 'bold'), bg = 'light green')
        name_label.grid(row = 0, column = 0, sticky = W)

        ## Entrybox to get the name entry from user ##
        self.name_entry = Entry(info_frame, width = 25, font = (" ", 11))
        self.name_entry.grid(row = 0, column = 1, padx = 10)
        self.name_entry.focus()

        ## Label for 'Phone' ##
        phone_label = Label(info_frame, text = "Phone", font = (" ", 11, 'bold'), bg = 'light green')
        phone_label.grid(row = 1, column = 0, sticky = W)

        ## Entrybox to get the name entry from user ##
        self.phone_entry = Entry(info_frame, width = 25, font = (" ", 11))
        self.phone_entry.grid(row = 1, column = 1, pady = 8)

        ## Label for 'Order type'
        ordertype_label = Label(info_frame, text = "Order type", font = (" ", 11, 'bold'), bg = 'light green')
        ordertype_label.grid(row = 2, column = 0, sticky = W)

        ## Inner frame for the two radiobuttons for order type ##
        radio_frame = Frame(info_frame, bg = 'light green')
        radio_frame.grid(row = 2, column = 1, padx = 4, sticky = W)

        ## Changing the style of radiobuttons ##
        s1 = ttk.Style()
        s1.configure('my.TRadiobutton', font = (" ", 11), background = 'light green')

        ## Radiobuttons to get the order type from user. Deafult is "Pickup" ##
        ## Pickup radiobutton ##
        self.ordertype = StringVar(None, value = "Pickup")
        pickup_option = ttk.Radiobutton(radio_frame, text = "Pickup", style = 'my.TRadiobutton', variable = self.ordertype, value = "Pickup", command = self.addressbox_state)
        pickup_option.grid(row = 0, column = 0, padx = 6)

        ## Delivery radiobutton ## 
        delivery_option = ttk.Radiobutton(radio_frame, text = "Delivery", style = 'my.TRadiobutton', variable = self.ordertype, value = "Delivery", command = self.addressbox_state)
        delivery_option.grid(row = 0, column = 1, padx = 8)

        ## Label for 'Address'
        address_label = Label(info_frame, text = 'Address', font = (" ", 11, 'bold'), bg = 'light green')
        address_label.grid(row = 3, column = 0, sticky = W)

        ## Textbox to get the address from the user ##
        self.address_text = Text(info_frame, width = 25, height = 3, font = (" ", 11), state = DISABLED)
        self.address_text.grid(row = 3, column = 1, sticky = W, padx = 10)

        ## Button frame to hold the menu buttons ##
        button_frame = Frame(self.info_window, bg = 'light green')
        button_frame.pack(pady = 15)

        ## Clear Button ##
        clear_button = Button(button_frame, text = 'Clear', width = 8, fg = 'dark blue', bg = 'light blue', font = ('Lucida Handwriting', '10', 'bold'), command = self.clearall)
        clear_button.pack(side = LEFT, padx = 4)

        ## Confirm Button ##
        confirm_button = Button(button_frame, text = "Confirm", width = 8, fg = 'red', bg = 'yellow', font = ('Lucida Handwriting', '10', 'bold'), command = self.order_status)
        confirm_button.pack(side = LEFT, padx = 4)

        ## Cancel Button ##
        cancel_button = Button(button_frame, text = "Cancel", width = 8, bg = 'pink', fg = 'brown', font = ('Lucida Handwriting', '10', 'bold'), command = self.info_window.destroy)
        cancel_button.pack(padx = 4)


    def calculate_price(self):
        """ Calculates the price for self made sandwich """

        category = self.category.get()      # Get the category value selected by user
        breadtype = self.breadtype.get()    # Get the breadtype value selected by user
        cheesetype = self.cheesetype.get()  # Get the cheesetype value selected by user
        size = self.sandwich_size.get()     # Get the size value selected by user

        ## Using the function for calculating the price from module "sandwiches_data.py" and ...
        ## ... assigning it to the variable "price"
        price = get_price(category[:-8], breadtype[:-8], cheesetype[:-8], size)

        ## Displaying the price in the label ##
        self.total_bill2.configure(text = f"${'{:.2f}'.format(price)}")


    def addressbox_state(self):
        """ Changes the state of address text box according to the order type """

        ordertype = self.ordertype.get()    # Get the ordertype entered by the user

        if ordertype == "Delivery":     # If the ordertype is "delivery" ...
            ## Change the state of address text box to "normal"
            self.address_text.configure(state = NORMAL)

        elif ordertype == "Pickup":     # If the ordertype is "pickup: ...
            ## Change the state of address text box to "disabled"
            self.address_text.configure(state = DISABLED)


    def clearall(self):
        """ Clears all the enteries from the order information window """

        self.name_entry.delete(0, END)                  # Clears the name entry box
        self.phone_entry.delete(0, END)                 # Clears the phone entry box
        self.ordertype.set("Pickup")                    # Sets the ordertype to default value i.e. Pickup
        self.address_text.configure(state = NORMAL)     # Sets the state of address text box to normal
        self.address_text.delete('1.0', END)            # Clears the address text box
        self.address_text.configure(state = DISABLED)   # Sets the state of address text box to disabled again
        self.name_entry.focus()                         # Make the name entry box focused


    def order_status(self):
        """ Displays the order placement information in a messagebox """

        name = self.name_entry.get()        # Get the name entered by the user
        phone = self.phone_entry.get()      # Get the phone entered by the user
        order = self.ordertype.get()        # Get the ordertype entered by the user
        address = self.address_text.get("1.0", "end-1c")    # Get the address entered by the user

        if name == "":  # If name entry box is empty ...
            ## Show the error message of missing name ##
            tkm.showerror("Missing Name", "Name entry cannot be empty.", parent = self.info_window)
            self.name_entry.focus()
            return
        
        elif phone == "":   # If the phone entry box is empty ...
            ## Show the error message of missing phone ##
            tkm.showerror("Missing Phone Number", "Phone number is required", parent = self.info_window)
            self.phone_entry.focus()
            return
        
        elif order == "Delivery" and address == "":     # If the ordertype is delivery but the address entry box is empty ...
            ## Show the error message of missing address ## 
            tkm.showerror("Missing Address", "Address is required for delivery.", parent = self.info_window)
            return
        
        else:   # Else if all the entreries are correctly filled ...
            ## Show the info message of order placed ##
            msg = tkm.showinfo("Order Placed", "\n".join(["Woo-Hoo! Your order has been placed.", "Sit back & Relax while we prepare it!"]), parent = self.info_window)
            if msg:
                self.info_window.destroy()


## Running the GUI ##
base = Welcome()
base.mainloop()