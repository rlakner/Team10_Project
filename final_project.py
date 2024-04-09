from bs4 import BeautifulSoup
import requests

def scrape(search):
    """Uses BeautifulSoup to scrape the the data from the entered Depop URL
    to find items being sold at a discounted price.
    
    Args:
    search(string): The item a user is searching for which will be used to add
        to the Depop base URL 
    
    Returns: 
        items(list): a list of dictionaries of the items found with the key as 
        the name of the item and three values being its price, condition, and
        unique direct link 
    """

def group_by_condition(items):
    """"Groups items into either New or Used 
    
    Args:
        items(list): a list of dictionaries that represent items from a search
    
    Returns:
        new_items(list): a list of dictionaries that represent items that 
            are either listed as 'New' or 'Like New'
        used_items(list): a list of dictionaries that represent items that 
            are either listed as any variation of 'Used'
    """

def averages(new_items, used_items):
    """Calculates the average price of an item on Depop in different conditions
    
    Args:
        new_items(list): a list of dictionaries that represent items that 
            are either listed as 'New' or 'Like New'
        used_items(list): a list of dictionaries that represent items that 
            are either listed as any variation of 'Used'

    Returns:
        item_averages(tuple): a tuple containing the calculated average price 
            for the item in brand new condition, non-new
            condition, and for all listed items from a search, regardless
            of condition
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
        items(list): a list of dictionaries that represent items from a search
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
            are either listed as 'New' or 'Like New'
        used_items(list): a list of dictionaries that represent items that 
            are either listed as any variation of 'Used'
        new_price(float): the average price of the item in new or like new
            condition
        used_price(float): the average price of the item in used condition
        avg_price(float): the average price of all listed items from a search, 
            regardlessof condition
    Retruns:
        deals(list): a list of dictionaries that is ordered from best to worst
            deal for the item a user is searching for
    """
    pass