import pytest
from final_project import scrape, averages, get_min_price, get_max_price, sort_by_price, group_by_condition, best_match

def test_scrape():
    url = "https://www.depop.com/item123"
    discount_percent = 10.0
    result = scrape(url, discount_percent)
    assert isinstance(result, dict)
     
def test_averages():
    prices = [1.0,2.0,3.0,4.5]
    result = averages(prices)
    assert isinstance(result, tuple)
    
def test_get_min_price():
    prices = [10.0, 15.0, 20.0]
    result = get_min_price(prices)
    assert isinstance(result, float)
    assert result == 10.0
    
def test_get_max_price():
    prices =  [10.0, 15.0, 20.0]
    result = get_max_price(prices)
    assert isinstance(result, float)
    assert result == 20.0

def test_sort_by_price():
    items = [{"item": "palet", "price": 50.0}, {"item": "wood", "price": 20.0} ]
    ascending = True
    result = sort_by_price(items, ascending)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["price"] == 20.0  

def test_group_by_condition():
    items = [{"name": "item1", "condition": "New"}, {"name": "item2", "condition": "Used"}]
    result = group_by_condition(items)
    assert isinstance(result, tuple)
    assert len(result) == 2
    
  
