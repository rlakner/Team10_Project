import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class DepopDealFinder:
    """
    A user interface for an application to help Depop users find reasonable 
    prices on clothes by analyzing data scraped from the Depop website 
    """
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel()
        self.window.geometry("400x300")
        self.window.title("Depop Deal Finder")
        self.window.protocol("WM_DELETE_WINDOW", self.parent.quit)
        self.button = tk.Button(self.window, text="Start Finding Deals"
                                , command=self.popupmsg)
        self.button.place(x=120, y=150)
    
    def popupmsg(self):
        """
        Display a popup message with a given message
        
        Args:
        - msg (str): the message to be displayed to user in popup
        """
        result = simpledialog.askstring("What are you searching for?", "Enter:")
        if result:
            messagebox.showinfo("Greeting", f"Searching for {result}....")
            print("Searching for", result)
        
    def search_deals(self):
        """
        Pop up that asks users to choose/enter a search query which will help 
        them find reasonable deals on the application
        
        Returns:
        str: The results of the search query entered by the user
        """
        query = simpledialog.askstring("Search Deals", "Enter your search query:")
        if query:
            deals = self.fetch_deals(query)
            self.display_deals(deals)
        
    def fetch_deals(self, query):
        """
    Displays a list of deals based on the users requests
    
    Args:
    query (str): The users search query
    
    Returns:
    list: A lisrt of deals based on search query
        """
        return ["Deal 1", "Deal 2", "Deal 3"]
    
    def display_deals(self, deals):
        """
        Displays a list of deals found based on the users requests
        
        Args:
        - deals (list): A list of reasonable deals
        """
        messagebox.showinfo("Deals", "\n".join(deals))
        
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = DepopDealFinder(root)
    root.mainloop()