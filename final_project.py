from bs4 import BeautifulSoup
import requests

def scrape(url, discount_percent):
    """Uses BeautifulSoup to scrape the the data from the entered Depop URL
    to find items being sold at a discounted price.
    
    Args:
    url(string): Link of the Depop page passed through by the user
    
    discount_percent(float): The minimum deal percentage that the user is
    searching for
    
    Returns: Returns a dictionary of the items with the key as the name of the
    item and two values being the link of the item and the discount percentage
    """