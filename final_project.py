from bs4 import BeautifulSoup
import requests

def scrape_items(search):
    """Uses BeautifulSoup to scrape the data from the entered Depop URL
    to find items being sold at a discounted price.
    
    Args:
    search(string): The item a user is searching for which will be used to add
        to the Depop base URL 
    
    Returns: 
        items(list): a list of dictionaries of the items found with the key as 
        the name of the item and the value being a tuple containaint its price, 
        condition, and unique direct link 
    """
    
def scrape_images(items):
    """Uses BeautifulSoup to scrape the images of the items associated with the 
    gathered unique direct links from scrape_items.
    
    Args:
    items(list): The list of dictionaries returned by scrape_items which will
        then be parsed to extract the unique direct links
    
    Returns: 
        images(list): A list of dictionaries of the item images to be displayed
            in the user interface, having the links as keys and the image
            source links
    """

def group_by_condition(items):
    """"Groups items into either New or Used 
    
    Args:
        items(list): a list of dictionaries of the items found with the key as 
        the name of the item and the value being a tuple containaint its price, 
        condition, and unique direct link  
    
    Returns:
        new_items(list): a list of dictionaries that represent items that 
            are either listed as 'New' or 'Like New' with the key as 
            the name of the item and the value being a tuple containaint its 
            price, condition, and unique direct link
        used_items(list): a list of dictionaries that represent items that 
            are either listed as any variation of 'Used' with the key as 
            the name of the item and the value being a tuple containaint its 
            price, condition, and unique direct link
    """

def averages(new_items_prices, used_items_prices):
    """Calculates the average price of an item on Depop in different conditions
    
    Args:
         new_items_prices(list): a list of floats the represent the price of 
            items that result from a search that are either listed as 'New' or 
            'Like New' 
        used_items(list): a list of floats the represent the price of 
            items that result from a search that are listed as any variation of 
            'Used'
    Returns:
        item_averages(tuple): a tuple containing the calculated average price 
            for the item in new condition, used condition, and for all listed 
            items from a search, regardless of condition
    """
    pass

def get_min_price(prices):
    """Calculates the minimum price of items from a search on Depop
    
    Args:
        prices(list): a list of floats the represent the price of listed items
            that result from a search
    
    Returns:
        min_price(float): the lowest price found in a search
    """
    pass

def get_max_price(prices):
    """Calculates the maximum price of items from a search on Depop
    
    Args:
        prices(list): a list of floats the represent the price of listed items
            that result from a search
    
    Returns:
        min_price(float): the highest price found in a search
    """
    pass

def sort_by_price(items, ascending):
    """"Sorts items from a search either in ascending or descending order
    
    Args:
        items(list): a list of dictionaries of the items found with the key as 
        the name of the item and the value being a tuple containaint its price, 
        condition, and unique direct link  
        ascending(boolean): the desired search condition where True sorts items 
            in ascending order and False sorts items in descending order
    
    Returns:
        sorted_items(list): a list of dictionaries sorted in the desired order
    """
    pass


def best_match(new_items, used_items, new_price, used_price, avg_price):
    """Sorts items from a search by how good of a deal they are

    Args:
        new_items(list): a list of dictionaries that represent items that 
            are either listed as 'New' or 'Like New' with the key as 
            the name of the item and the value being a tuple containaint its 
            price, condition, and unique direct link
        used_items(list): a list of dictionaries that represent items that 
            are either listed as any variation of 'Used' with the key as 
            the name of the item and the value being a tuple containaint its 
            price, condition, and unique direct link
        new_price(float): the average price of the items in new or like new
            condition
        used_price(float): the average price of the items in used condition
        avg_price(float): the average price of all listed items from a search, 
            regardless of condition
    
    Returns:
        deals(list): a list of dictionaries that is ordered from best to worst
            deal for the item a user is searching for
    """
    pass