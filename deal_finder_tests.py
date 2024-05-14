import deal_finder as df
from deal_finder import Item, Search
from data_analysis import Analysis
from math import isclose

items = [
        Item(name="Carhartt Men's Green and Khaki Jacket", price = 50.00, 
             condition ="New", 
             link = "https://www.depop.com/products/rachelpattir-vintage-"
             "carhartt-detroit-jacket-sz/"),
        Item(name="Carhartt Men's Jacket", 
             price = 20.00, condition = "New", 
             link ="https://www.depop.com/products/mmmmadelineeee-hooded-"
             "carhart-jacket-dupe/"),
        Item(name="Carhartt multi Jacket", price = 35.50, 
            condition = "New", 
            link = "https://www.depop.com/products/vintedgedesigns-kids-"
            "carhart-camo-jacket-brand/"),
        Item(name="Carhartt Men's Multi Jacket", price = 49.99, 
             condition = "Used", 
             link = "https://www.depop.com/products/founderskeep-super-nice"
             "-carhartt-style-camo/"),
        Item(name="Carhartt Men's Black and Grey Jacket", 
             price = 30.00, condition = "Used", 
             link = "https://www.depop.com/products/lickhere-carhartt-insulated"
             "-zip-up-hooded/")
    ]

def test_scrape_items():
    """A test case to check that the scrape_items function returns a list
    *** MUST BE TESTED ONE AT A TIME BECAUSE DEPOP WILL RETURN 403 DUE TO BOT
    PROTECTION
    """
    search = "carhartt jacket"
    tester = Search(search)
    result = tester.scrape_items()
    assert isinstance(result, list)
    
def test_scrape_items_fail():
    """A test case to check that the scrape_items function returns a list
    *** MUST BE TESTED ONE AT A TIME BECAUSE DEPOP WILL RETURN 403 DUE TO BOT
    PROTECTION
    """
    #search = "eorgnwionwei"
    #tester = Search(search)
    #result = tester.scrape_items()
    #assert not result

def test_averages():
    """A test case to check that the averages function returns the correct values
    """
    tester = Analysis()
    result = tester.averages(items)
    round0 = round(result[0], 2)
    round1 = round(result[1], 2)
    round2 = round(result[2], 2)
    assert isinstance(result, tuple)
    assert isclose(round0, 35.17)
    assert isclose(round1, 40.00)
    assert isclose(round2, 37.1)

def test_score_price():
    tester = Analysis()
    new_avg, used_avg, entire_avg = tester.averages(items)
    assert tester.score_price(items[0].price, new_avg) == 0
    assert tester.score_price(items[1].price, new_avg) == 1
    assert tester.score_price(items[2].price, new_avg) == 0
    assert tester.score_price(items[3].price, used_avg) == 0
    assert tester.score_price(items[4].price, used_avg) == 1
    
def test_score():
    """A test case to check that scores are accurately being assigned based
    on our defined criteria
    """
    tester = Analysis()
    tester.score(items)
    assert items[0].score == 1.0
    assert items[1].score == 3.0
    assert items[2].score == 2.0
    assert items[3].score == 0.5
    assert items[4].score == 2.5
    
def test_best_match():
    """A test case to check that the best_match function sorts the items based
    on our criteria of a good deal
    """
    expected_order = [
        items[1],
        items[4],
        items[2],
        items[0],
        items[3]
    ]
    tester = Analysis()
    result = tester.best_matches(items)
    assert isinstance(result, list)
    assert result == expected_order
    