from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import tkinter as tk
from tkinter import scrolledtext
import pandas as pd
from data_analysis import Analysis

service = Service(executable_path="/usr/local/bin/chromedriver") #Change to your path
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
        """Initializes a search query to be used in scrape_items
        
        Args:
        query(str): The string value of the user input from the query interface
        which will be used in the url for Selenium
        
        """
        
        self.query = query
        self.items_list = []
    
    def init_scrape(self):
        """Uses Selenium and BeautifulSoup to navigate through Depop listings
        and scrape information regarding the link and price

        Args: None

        Returns: None
        """
        
        url = f'https://www.depop.com/search/?q={self.query}'
        driver.get(url)

        x = 0
        while True:
            x += 1
            driver.execute_script('scrollBy(0,50)')
            if x > 500: #Change this to make it scroll for longer
                break
    
        source = driver.page_source
        soup = bs(source, "html.parser")
        listings = soup.find('ul', class_='styles__ProductListGrid-sc-4aad5806-1 hGGFgp')

        self.temp_list = []
        self.check = 0
        
        for listing in listings:
            link = f"http://depop.com{listing.find('a', class_='styles__ProductCard-sc-4aad5806-4 ffvUlI')['href']}"
            # gets the price
            disc_price = listing.find('div', class_='Price-styles__PriceWithDiscountWrapper-sc-f7c1dfcc-2')
            if disc_price:
                price = float(disc_price.find('p', class_='sc-eDnWTT Price-styles__DiscountPrice-sc-f7c1dfcc-1 fRxqiS KMEBr').text.strip('$'))
            else:
                price_element = listing.find('p', class_='sc-eDnWTT Price-styles__FullPrice-sc-f7c1dfcc-0 fRxqiS hmFDou')
                price = float(price_element.text.strip('$'))
            self.temp_list.append([price, link])
              
        self.check = 1
        
    def scrape_items(self):
        """Uses Selenium and BeautifulSoup to navigate through Depop listings
        and scrape information on each individual page regarding the name and
        condition

        Args: None

        Returns: 
            items_list(list): A list of Item objects that contain the name, 
            price, condition, and link of the scraped item
        """
        
        self.init_scrape()
        
        while self.check == 1:
        
            for item in self.temp_list:
                driver.get(item[1])
                item_source = driver.page_source
                item_soup = bs(item_source, "html.parser")  
                name_div = item_soup.find('div', class_='styles__ContentWrapper-sc-569ef83f-3 cyzIGA')
                find_name = name_div.find('h1', class_='sc-grYavY styles__MobileProductTitle-sc-569ef83f-9 HXICV cTNEru')
                brand_div = item_soup.find('div', class_ = 'ProductAttributes-styles__Attributes-sc-303d66c3-1 dIfGXO styles__StyledProductAttributes-sc-569ef83f-16 hcLsNE')
                find_brand = brand_div.find('a', class_='sc-eDnWTT ProductAttributes-styles__Attribute-sc-303d66c3-0 kcKICQ iIJjeL')
                find_condition = item_soup.find_all('p', class_='sc-eDnWTT ProductAttributes-styles__Attribute-sc-303d66c3-0 kcKICQ iIJjeL')[1]
                if find_name:
                    name = find_name.text
                else:
                    brand = find_brand.text
                    name = f"{brand} Item"
                    
                if find_condition:
                    condition_text = find_condition.text.lower()
                    if "new" in condition_text:
                        condition = "New"
                    else:
                        condition = "Used"
                self.items_list.append(Item(name, item[0], condition, item[1]))
            
            time.sleep(10)
            driver.quit()
            return self.items_list
    
class Interface:
    """
    A user interface for an application to help Depop users find reasonable 
    prices on clothes by analyzing data scraped from the Depop website 
    """
    def __init__(self, parent):
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
        """
        Display a popup message with a given message
        
        Args:
        - msg (str): the message to be displayed to user in popup
        """
        self.query = self.entry.get()
        if self.query:
            if " " in self.query:
                self.query.replace(" ","+")
            message = (f"Happy Shopping!")
        label = tk.Label(self.window, text=message)
        label.place(x=530, y=130)
        
        scraper = Search(self.query)
        items = scraper.scrape_items()

        analyzer = Analysis()
        scored_items = analyzer.score(items)
        sorted_items = analyzer.best_matches(scored_items)
        self.display_deals(sorted_items)
        
    def display_deals(self, sorted_items):
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
        products_text = scrolledtext.ScrolledText(self.window, width=165, height=40)
        products_text.place(x=5, y=150)
        products_text.insert(tk.END, products.to_string(index=False))
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()
