import pytest
import final_project as fp
from fp import Item, scrape_items, averages, score, sort_by_price, best_matches

items = [
        Item(name="Carhartt Men's Green and Khaki Jacket", price = 50.00, 
             condition ="Brand New", 
             link = "https://www.depop.com/products/rachelpattir-vintage-carhartt-detroit-jacket-sz/"),
        Item(name="Carhartt Men's Jacket", 
             price = 20.00, condition = "Like New", 
             link ="https://www.depop.com/products/mmmmadelineeee-hooded-carhart-jacket-dupe/"),
        Item(name="Carhartt multi Jacket", price = 35.50, 
            condition = "Brand New", 
            link = "https://www.depop.com/products/vintedgedesigns-kids-carhart-camo-jacket-brand/"),
        Item(name="Carhartt Men's Multi Jacket", price = 49.99, 
             condition = "Used - Good", 
             link = "https://www.depop.com/products/founderskeep-super-nice-carhartt-style-camo/"),
        Item(name="Carhartt Men's Black and Grey Jacket", 
             price = 30.00, condition = "Used - Excellent", 
             link = "https://www.depop.com/products/lickhere-carhartt-insulated-zip-up-hooded/")
    ]

def test_scrape_items():
    """A test case to check that the scrape_items function returns a list
    """
    search = "carhartt jacket"
    result = fp.scrape_items(search)
    assert isinstance(result, list)
     
def test_averages():
    """A test case to check that the averages function returns the correct values
    """
    result = fp.averages(items)
    assert isinstance(result, tuple)
    assert result[0] == 35.16
    assert result[1] == 39.99
    assert result[2] == 37.09
    
def test_score():
    """A test case to check that scores are accurately being assigned based
    on our defined criteria
    """
    result = fp.score(items)
    assert items[0].score == 3.0
    assert items[1].score == 5.0
    assert items[2].score == 3.5
    assert items[3].score == 2.0
    assert items[4].score == 3.0
    
def test_best_match():
    """A test case to check that the best_match function sorts the items based
    on our criteria of a good deal
    """
    expected_order = [
        items[1],
        items[2],
        items[0],
        items[4],
        items[3]
    ]
    result = fp.best_matches(items)
    assert isinstance(result, list)
    assert result == expected_order
    
def test_sort_by_price_asc():
    """A test case to check that the sort_by_price function correctly sorts the 
    items based on their price in ascending order
    """
    ascending = True
    result = fp.sort_by_price(items, ascending)
    assert isinstance(result, list)
    assert len(result) == 5
    assert result[0].price == 20.0
    assert result[4].price == 50.0

def test_sort_by_price_asc():
    """A test case to check that the sort_by_price function correctly sorts the 
    items based on their price in descending order
    """
    ascending = False
    result = fp.sort_by_price(items, ascending)
    assert isinstance(result, list)
    assert len(result) == 6
    assert result[0].price == 50.0
    assert result[4].price == 20.0


  
