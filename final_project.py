from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

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

class DepopScraper:
    """A class for scraping and analyzing data for items listed on Depop"""
    
    def scrape_items(search):
        """Uses BeautifulSoup to scrape the data from the entered Depop URL
            to find items being sold at a discounted price.

        Args:
            search(string): The item a user is searching for which will be used 
            to add to the Depop base URL 

        Returns: 
            items(list): a list of Items found from the search
        
        Side Effects:
            Creates new Items and sets their name, price, condition, and link
            attributes 
        
        Raises:
            NoItemsFound: If no items are found from the search
        """
        url = f'https://www.depop.com/search/?q={search}'

        service = Service(executable_path="chromedriver.exe") #Change to your path
        driver = webdriver.Chrome(service=service)

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

        items_list = []
        complete_list = []

        for listing in listings:
            price_div = listing.find('div', class_='Price-styles__PriceWithDiscountWrapper-sc-f7c1dfcc-2')
            if price_div:
                disc_price = price_div.find('p', class_='sc-eDnWTT Price-styles__DiscountPrice-sc-f7c1dfcc-1 fRxqiS KMEBr').text
                link = f"http://depop.com{listing.find('a', class_='styles__ProductCard-sc-4aad5806-4 ffvUlI')['href']}"
            
        items_list.append([disc_price, link])   

        for item in items_list:
            driver.get(item[1])
            item_source = driver.page_source
            item_soup = bs(item_source, "html.parser")  
            info_div = item_soup.find('div', class_='_app__FocusWrapper-sc-ed3f3631-0 erUfoA')
            name = info_div.find('h1', class_='sc-grYavY styles__MobileProductTitle-sc-569ef83f-9 HXICV cTNEru').text
            p = info_div.find_all('p', class_='sc-eDnWTT ProductAttributes-styles__Attribute-sc-303d66c3-0 kcKICQ iIJjeL')
            condition = p[1].text
    
            complete_list.append({name:(item[0], condition, item[1],)})

        time.sleep(10)
        driver.quit()
        return complete_list
    
    def scrape_images(items):
        """Uses BeautifulSoup to scrape the images of the items associated with 
            the gathered unique direct links from scrape_items.

        Args:
            items(list): The list of Items returned by scrape_items which 
                will then be parsed to extract the unique direct links

        Returns: 
            images(list): A list of dictionaries of the item images to be 
            displayed in the user interface, having the direct links as keys and 
            the image source links as values
        """
        images = []
        service = Service(executable_path="chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        
        for item in items:
            driver.get(item[2])
            item_source = driver.page_source
            item_soup = bs(item_source, "html.parser")
            info_div = item_soup.find('div', class_='styles__Layout-sc-569ef83f-2 MYFCM')
            img = info_div.find('img')['src']
            name = info_div.find('img')['alt']
            
            images.append({img: name})
            
        return images
        
    
    def averages(items):
        """Calculates the average price of an item in different conditions

        Args:
            items(list): The list of Items returned by scrape_items which 
                will then be parsed
        
        Returns:
            item_averages(tuple): a tuple containing the calculated average 
                price for the item in new condition, used condition, and for all 
                listed items from a search, regardless of condition
        """
        new_prices = []
        used_prices = []
        for item in items:
            if item.condition == "New":
                new_prices.append(item.price)
            elif item.condition == "Used":
                used_prices.append(item.price)
        all_prices = new_prices + used_prices
        
        if len(new_prices) > 0:
            new_average = sum(new_prices) / len(new_prices)
        else:
            new_average = None

        if len(used_prices) > 0:
            used_average = sum(used_prices) / len(used_prices)
        else:
            used_average = None
    
        if len(all_prices) > 0:
            all_average = sum(all_prices) / len(all_prices)
        else:
            all_average = None
    
        return (new_average, used_average, all_average)
    
    def score_price(price, avg):
        """Scores the price of an item
        
        Args:
            price(float): the price of an item 
            avg(float): the average price of the items in similar condition
        
        Returns:
            price_score(int): a score for the item's price based on the average
         """
        if price < avg:
            price_score = 1
        elif price == avg:
            price_score = 0.5
        else:
            price_score = 0
        return price_score
    
    def score(items):
        """Gives an item an overall score based on its price and condition
        
        Args: 
            items(list): The list of Items returned by scrape_items which 
                will then be parsed

        Returns: None
        
        Side Effects:
            Modifies the score attribute of an item
        """
        # gets the average price for the item in new condition, used 
        # condition, and for all listed items from a search
        new_avg, used_avg, entire_avg = averages(items)
        
        for item in items:
            if item.condition == "New":
                item.score = score_price(item.price, new_avg)
                item.score += 1
            else:
                item.score = score_price(item.price, used_avg)
                item.score += 0.5
            # provides a higher score if the item is also below the average price
            # from the entire search
            item.score += score_price(item.price, entire_avg)
    
    def best_matches(scored_items):
        """Sorts items from a search by how good of a deal they are

        Args:
            scored_items(list): The list of Items from the search with their 
            assigned 
            scores 

        Returns:
            deals(list): a list of the same items but ordered from best to 
            worst deal according to our criteria 
        """
        # assign a score to each item from a search
        deals_list = sorted(scored_items, key= lambda item: item.score, 
                           reverse=True)
        return deals_list
    
    def sort_by_price(items, ascending):
        """"Sorts items from a search either in ascending or descending order

        Args:
            items(list): The list of Items from the search with their assigned 
            scores  
            ascending(boolean): the desired search condition where True sorts 
            items in ascending order and False sorts items in descending order

        Returns:
            sorted_items(list): a list of Items sorted in the desired order
        """
        sorted_items = sorted(items, key=lambda x: x['price'], reverse=not ascending)
        return sorted_items
    
if __name__ == "__main__":
    search = input("Enter search: ")
    if " " in search:
        search.replace(" ","+")