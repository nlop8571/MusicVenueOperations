# procurement_main_gui.py
# France Cheong
# 22/11/2018

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox
from organizer_gui import OrganizerGUI
from event_gui import EventGUI
# #################################################
# Import any of your classes defined in other files
# #################################################

# Import all the GUI classes implementing each menu option
# e.g. EmployeeGUI, ProductGUI, SupplierGUI, PurchaseOrderGUI
# Each GUI class will import the corresponding data access class 
# to communicate with the database
# The GUI classes also import a single Validation class containing 
# all necessary validation methods

# From file xxx.py import class Xxxx

#from product_gui import ProductGUI
#from supplier_gui import SupplierGUI # ==> Not implemented
#from purchase_order_gui import PurchaseOrderGUI

# Reports GUI
#from product_report_gui import ProductReportGUI
#from category_report_gui import CategoryReportGUI


# ################
# Global Constants 
# ################


# ####################
# ProcurementGui Class
# ####################

class ProcurementGUI():

    def __init__(self):   

        print("Creating Procurement GUI ...")

        self.current_gui = None # Reference to current GUI 
        # Step 1. Create main window of the application
        # 900x500 pixels in the middle of the screen
        # Can minimise to 0x0 pixels
        self.root = tk.Tk()
        self.root.title("Procurement System")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = 900
        height = 600
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        print("Main window coordinates (width, height, x, y) :", 
              width, height, x, y)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.resizable(0, 0)

        # Step 2. Add a menu

        # Create a toplevel menu
        menubar = tk.Menu(self.root)

        # File menu (pulldown)
        # Create a pulldown menu
        filemenu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        filemenu.add_command(label="Open", command="")
        filemenu.add_command(label="Save", command="")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="File", menu=filemenu)
       
        # Employee menu (pulldown)
        # Create a pulldown menu
    
        # Add menu items
        organizer_menu = tk.Menu(menubar, tearoff=0)
        organizer_menu.add_command(label="Organizer", command=self.create_organizer_gui) 
        # Add Organizer pulldown menu to toplevel menu bar
        menubar.add_cascade(label="Organizer", menu=organizer_menu)

        # Create Event pulldown menu
        event_menu = tk.Menu(menubar, tearoff=0)
        event_menu.add_command(label="Event", command=self.create_event_gui) 
        # Add Event pulldown menu to toplevel menu bar
        menubar.add_cascade(label="Event", menu=event_menu)

        # Display the menu
        self.root.config(menu=menubar)

        pass
            
    # Functions to create child frames 
    # when menu options are selected

    def create_organizer_gui(self):
        if self.current_gui:
            self.current_gui.destroy()

        organizer_gui = OrganizerGUI()
        self.current_gui = organizer_gui.create_gui(self.root)
        pass

    def create_event_gui(self):
        if self.current_gui:
            self.current_gui.destroy()

        event_gui = EventGUI()
        self.current_gui = event_gui.create_gui(self.root)
        pass

    def exit(self):
        exit()


# ###########
# Main method
# ###########

if __name__ == '__main__':
    """
    The main method is only executed when the file is 'run' 
    (not imported in another file)
    """

    # Instantiate the main application gui 
    # it will create all the necessary GUIs
    gui = ProcurementGUI()

    # Run the mainloop 
    # the endless window loop to process user inputs
    gui.root.mainloop()
    pass        