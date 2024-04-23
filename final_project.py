from bs4 import BeautifulSoup
import requests

class Item:
    """A class for data representing an item listed on Depop
    
    Attributes:
        name(str): the name of the item (what it is listed as)
        price(float): the price of the item
        condition(str): the condition of the item 
        link(str): the unique direct link to the item on Depop
        score(float): a score representing how good of a deal the item is on a 
            scale of from 1 to 5
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
        pass
    
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
        pass
    
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
        pass
    
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
        pass
    