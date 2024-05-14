from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
from tkinter import scrolledtext
import pandas as pd
from data_analysis import Analysis

service = Service(executable_path=
                          "../chromedriver.exe") #Change to your path
driver = webdriver.Chrome(service=service)

class Item:
    """A class for data representing an item listed on Depop
    
    Attributes:
        name(str): the name of the item (what it is listed as)
        price(float): the price of the item
        condition(str): the condition of the item 
        link(str): the unique direct link to the item on Depop
        score(float): a score representing how good of a deal the item is on a 
            scale of from 0 to 3
    """
    
    def __init__(self, name, price, condition, link, score = 0):
        """Initializes an Item object
        
        Args:
            name(str): the name of the item (what it is listed as)
            price(float): the price of the item
            condition(str): the condition of the item 
            link(str): the unique direct link to the item on Depop
        """
        self.name = name
        self.price = price
        self.condition = condition
        self.link = link
class Search:
    """A class for scraping and analyzing data for items listed on Depop"""
    def __init__(self, query):
        """Initializes a Search with a query to find items
        
        Args:
            query(str): The string value of the user input from the interface
            which will be used in the url for Selenium
        """
        self.query = query
        self.items_list = []
    
    def init_scrape(self):
        url = f'https://www.depop.com/search/?q={self.query}'
        driver.get(url)

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "li"))
        )
        
        time.sleep(5)
        
        x = 0
        while True:
            x += 1
            driver.execute_script('scrollBy(0,50)')
            if x > 50: #Change this to make it scroll for longer
                break
    
        source = driver.page_source
        soup = bs(source, "html.parser")
        listings = soup.find('ul', class_='styles__ProductListGrid'
                             '-sc-4aad5806-1 hGGFgp')
        error = soup.findAll(string="Sorry, we couldn't find anything")

        if not listings and error:
            self.ignore = True
            print("No items found. Please adjust your search.")
            return []
        
        self.temp_list = []
        self.check = 0
        self.ignore = False
        
        if listings is not None:
            for listing in listings:
                #Gets the direct link to the item
                link = f"http://depop.com{listing.find('a', 
                        class_='styles__ProductCard-sc-4aad5806-4 ffvUlI')
                        ['href']}"
                
                # Gets the discounted price, if there is one
                disc_price = listing.find('div', class_='Price-styles__Price'
                                          'WithDiscountWrapper-sc-f7c1dfcc-2')
                if disc_price:
                    price_element = disc_price.find('p', class_='sc-eDnWTT '
                                        'Price-styles__DiscountPrice-sc-f7c1'
                                                    'dfcc-1 fRxqiS KMEBr')
                    price_text = price_element.text.strip('$')
                    price = float(price_text)
                # Gets the full price if the item is not on sale
                else:
                    price_element = listing.find('p', class_='sc-eDnWTT Price-'
                                                'styles__FullPrice-sc-f7c1dfcc-'
                                                '0 fRxqiS hmFDou')
                    price_string = price_element.text
                    price = float(price_string[1:])
                self.temp_list.append([price, link])
                self.check = 1
            
            if listings is None:
                source = driver.page_source
                soup = bs(source, "html.parser")
                listings = soup.find('ul', class_='styles__ProductListGrid-sc-4'
                                     'aad5806-1 hGGFgp')
                for listing in listings:
                    link = f"http://depop.com{listing.find('a', class_='styles_'
                    '_ProductCard-sc-4aad5806-4 ffvUlI')['href']}"
                    # gets the price
                    disc_price = listing.find('div', class_='Price-styles__Pric'
                                              'eWithDiscountWrapper-sc-'
                                              'f7c1dfcc-2')
                    if disc_price:
                        price = float(disc_price.find('p', class_='sc-eDnWTT '
                                                      'Price-styles__Discount'
                                                      'Price-sc-f7c1dfcc-1 '
                                                'fRxqiS KMEBr').text.strip('$'))
                    else:
                        price_element = listing.find('p', class_='sc-eDnWTT '
                                                     'Price-styles__FullPrice'
                                                     '-sc-f7c1dfcc-0 fRxqiS '
                                                     'hmFDou')
                        price_string = price_element.text
                        price = float(price_string[1:])
                    self.temp_list.append([price, link])
                    self.check = 1
        
    def scrape_items(self):
        """Uses Selenium and BeautifulSoup to navigate through Depop listings
        and scrape information regarding the name, price, condition, and link 
        of the items

        Returns: 
            items_list(list): A list of Item objects that contain the name, 
            price, condition, and link of the scraped item
        
        Side Effects:
            - Creates new Item objects and sets their name, price, condition, 
            and link attributes 
            - Modifies the items_list attribute
        """
        
        self.init_scrape()
        
        if self.ignore == True:
            return
        
        while self.check == 1:   
            
        #Gets the name, price, and condition 
            for item in self.temp_list:
                driver.get(item[1])
                item_source = driver.page_source
                item_soup = bs(item_source, "html.parser")  
                name_div = item_soup.find('div', class_='styles__ContentWrapper'
                                          '-sc-569ef83f-3 cyzIGA')
                find_name = name_div.find('h1', class_='sc-grYavY styles__Mobil'
                                    'eProductTitle-sc-569ef83f-9 HXICV cTNEru')
                brand_div = item_soup.find('div', class_ = 'ProductAttributes-'
                                    'styles__Attributes-sc-303d66c3-1 dIfGXO'
                                    ' styles__StyledProductAttributes-sc-569'
                                    'ef83f-16 hcLsNE')
                find_brand = brand_div.find('a', class_='sc-eDnWTT Product'
                                            'Attributes-styles__Attribute-sc-'
                                            '303d66c3-0 kcKICQ iIJjeL')
                find_condition = item_soup.find_all('p', class_='sc-eDnWTT Pro'
                                            'ductAttributes-styles__Attribute-'
                                            'sc-303d66c3-0 kcKICQ iIJjeL')[1]
                #For items without a name, set the name to an item of the brand
                if find_name:
                    name = find_name.text
                else:
                    brand = find_brand.text
                    name = f"{brand} Item"
                
                #Gets the condition    
                if find_condition:
                    condition_text = find_condition.text.lower()
                    if "new" in condition_text:
                        condition = "New"
                    else:
                        condition = "Used"
                self.items_list.append(Item(name, item[0], condition, item[1]))
            
            time.sleep(5)
            driver.quit()
            return self.items_list
    
class Interface:
    """
    A class for a user interface for an application to help users find 
    reasonably priced clothes by analyzing data scraped from the Depop website
    
    Attributes:
        parent: a parent object that manages the interface
        window: a window from Tkinter Toplevel for the interface
        entry_label: a Tkinter label to prompt users for a search
        entry: gets the user input query using Tkinter Entry  
        button: a Tkinter button that will start the deal finding process
    """
    def __init__(self, parent):
        """Initializes an instance of an Interface to get a query input
        
        Side Effects:
            Creates a pop up window that users can interact with
        """
        self.parent = parent
        self.window = tk.Toplevel()
        self.window.geometry("1190x1000")
        self.window.title("Depop Deal Finder")
        self.window.protocol("WM_DELETE_WINDOW", self.parent.quit)
        self.entry_label = tk.Label(self.window, 
                                    text="What are you searching for?")
        self.entry_label.place(x=495, y=50)
        self.entry = tk.Entry(self.window)
        self.entry.place(x=495, y=70)
        
        self.button = tk.Button(self.window, text="Start Finding Deals", 
                                command=self.popupmsg)
        self.button.place(x=515, y=100)
    
    def popupmsg(self):
        """Takes a users query and uses it to scrape through Depop
        
        Side Effects:
            Modifies the query attribute 
            Creates instances of Search and Analysis 
        """
        self.query = self.entry.get()
        if self.query:
            if " " in self.query:
                self.query.replace(" ","+")
            scraper = Search(self.query)
            items = scraper.scrape_items()
        
        if not items:
            message = "We did not find any results. Please try another search."
            label = tk.Label(self.window, text=message)
            label.place(x=438, y=430)       
        else: 
            message = (f"Happy Shopping!")
            label = tk.Label(self.window, text=message)
            label.place(x=530, y=130)
            analyzer = Analysis()
            scored_items = analyzer.score(items)
            sorted_items = analyzer.best_matches(scored_items)
            self.display_deals(sorted_items)
        
    def display_deals(self, sorted_items):
        """Creates a dataframe for deals found on Depop
        
        Args:
            sorted_items(list): a list of Items found and sorted by best match
        
        Side Effects:
            Creates and displays the dataframe of deals within the pop up 
        """
        items_info = []
        for item in sorted_items:
            item_info = {
                "Product Name": item.name,
                "Condition": item.condition,
                "Price": f'${item.price}',
                "Link": item.link,
                "Our Score (0-3)": item.score
            }
            items_info.append(item_info)
        products = pd.DataFrame(items_info)
        pd.set_option('display.colheader_justify', 'center')
        products_text = scrolledtext.ScrolledText(self.window, width=165,
                                                  height=40)
        products_text.place(x=5, y=150)
        products_text.insert(tk.END, products.to_string(index=False))
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()
