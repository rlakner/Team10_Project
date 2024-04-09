import pytest
from final_project import scrape_items, averages, get_min_price, get_max_price, sort_by_price, group_by_condition, best_match

def test_scrape_items():
    """A test case to check that the scrape_items function returns a list
    """
    search = "carhartt jacket"
    result = scrape_items(search)
    assert isinstance(result, list)
     
def test_group_by_condition():
    """A test case to check that the group_by_condition function correctly 
    separates the items into two lists
    """
    items = [
        {"Carhartt Men's Green and Khaki Jacket": (50.00, "Brand New", "https://www.depop.com/products/rachelpattir-vintage-carhartt-detroit-jacket-sz/")},
        {"Carhartt Men's Jacket": (20.00, "Like New", "https://www.depop.com/products/mmmmadelineeee-hooded-carhart-jacket-dupe/")},
        {"Carhartt multi Jacket": (35.50, "Brand New", "https://www.depop.com/products/vintedgedesigns-kids-carhart-camo-jacket-brand/")},
        {"Carhartt Men's Multi Jacket": (49.99, "Used - Good", "https://www.depop.com/products/founderskeep-super-nice-carhartt-style-camo/")},
        {"Carhartt Men's Black and Grey Jacket": (30.00, "Used - Excellent", "https://www.depop.com/products/lickhere-carhartt-insulated-zip-up-hooded/")},
        {"Carhartt Men's Jacket": (35.50, "Used - Fair", "https://www.depop.com/products/bv1-vintage-faded-carhartt-tan-hooded/")}
    ]
    result = group_by_condition(items)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result[0] == [
        {"Carhartt Men's Green and Khaki Jacket": (50.00, "Brand New", "https://www.depop.com/products/rachelpattir-vintage-carhartt-detroit-jacket-sz/")},
        {"Carhartt Men's Jacket": (20.00, "Like New", "https://www.depop.com/products/mmmmadelineeee-hooded-carhart-jacket-dupe/")},
        {"Carhartt multi Jacket": (35.50, "Brand New", "https://www.depop.com/products/vintedgedesigns-kids-carhart-camo-jacket-brand/")}
    ]
    assert result[1] == [
        {"Carhartt Men's Multi Jacket": (49.99, "Used - Good", "https://www.depop.com/products/founderskeep-super-nice-carhartt-style-camo/")},
        {"Carhartt Men's Black and Grey Jacket": (30.00, "Used - Excellent", "https://www.depop.com/products/lickhere-carhartt-insulated-zip-up-hooded/")},
        {"Carhartt Men's Jacket": (35.50, "Used - Fair", "https://www.depop.com/products/bv1-vintage-faded-carhartt-tan-hooded/")}
    ]
    
def test_averages():
    """A test case to check that the averages function returns the correct values
    """
    new_items_prices = [50.00, 20.00, 35.50]
    used_items_prices = [49.99, 30.00, 35.50]
    result = averages(new_items_prices, used_items_prices)
    assert isinstance(result, tuple)
    assert result[0] == 35.16
    assert result[1] == 38.49
    assert result[2] == 36.83
    
def test_get_min_price():
    """A test case to check that the get_min_price function returns the price
    """
    prices = [10.00, 50.00, 20.00, 35.50, 15.00, 20.00]
    result = get_min_price(prices)
    assert isinstance(result, float)
    assert result == 10.00
    
def test_get_max_price():
    """A test case to check that the get_max_price function returns the price
    """
    prices = [10.00, 50.00, 20.00, 35.50, 15.00, 20.00]
    result = get_max_price(prices)
    assert isinstance(result, float)
    assert result == 50.00

def test_sort_by_price_asc():
    """A test case to check that the sort_by_price function correctly sorts the 
    items based on their price in ascending order
    """
    items = [
        {"Carhartt Men's Green and Khaki Jacket": (50.00, "Brand New", "https://www.depop.com/products/rachelpattir-vintage-carhartt-detroit-jacket-sz/")},
        {"Carhartt Men's Jacket": (20.00, "Like New", "https://www.depop.com/products/mmmmadelineeee-hooded-carhart-jacket-dupe/")},
        {"Carhartt multi Jacket": (35.50, "Brand New", "https://www.depop.com/products/vintedgedesigns-kids-carhart-camo-jacket-brand/")},
        {"Carhartt Men's Multi Jacket": (49.99, "Used - Good", "https://www.depop.com/products/founderskeep-super-nice-carhartt-style-camo/")},
        {"Carhartt Men's Black and Grey Jacket": (30.00, "Used - Excellent", "https://www.depop.com/products/lickhere-carhartt-insulated-zip-up-hooded/")},
        {"Carhartt Men's Jacket": (35.50, "Used - Fair", "https://www.depop.com/products/bv1-vintage-faded-carhartt-tan-hooded/")}
    ]
    ascending = True
    result = sort_by_price(items, True)
    assert isinstance(result, list)
    assert len(result) == 6
    assert result[0] == 20.0
    assert result[5] == 50.0

def test_sort_by_price_asc():
    """A test case to check that the sort_by_price function correctly sorts the 
    items based on their price in descending order
    """
    items = [
        {"Carhartt Men's Green and Khaki Jacket": (50.00, "Brand New", "https://www.depop.com/products/rachelpattir-vintage-carhartt-detroit-jacket-sz/")},
        {"Carhartt Men's Jacket": (20.00, "Like New", "https://www.depop.com/products/mmmmadelineeee-hooded-carhart-jacket-dupe/")},
        {"Carhartt multi Jacket": (35.50, "Brand New", "https://www.depop.com/products/vintedgedesigns-kids-carhart-camo-jacket-brand/")},
        {"Carhartt Men's Multi Jacket": (49.99, "Used - Good", "https://www.depop.com/products/founderskeep-super-nice-carhartt-style-camo/")},
        {"Carhartt Men's Black and Grey Jacket": (30.00, "Used - Excellent", "https://www.depop.com/products/lickhere-carhartt-insulated-zip-up-hooded/")},
        {"Carhartt Men's Jacket": (35.50, "Used - Fair", "https://www.depop.com/products/bv1-vintage-faded-carhartt-tan-hooded/")}
    ]
    ascending = False
    result = sort_by_price(items, True)
    assert isinstance(result, list)
    assert len(result) == 6
    assert result[0] == 50.0
    assert result[5] == 20.0

def test_best_match():
    """A test case to check that the best_match function sorts the items based
    on our criteria of a good deal
    """
    new_items = [
        {"Carhartt Men's Green and Khaki Jacket": (50.00, "Brand New", "https://www.depop.com/products/rachelpattir-vintage-carhartt-detroit-jacket-sz/")},
        {"Carhartt Men's Jacket": (20.00, "Like New", "https://www.depop.com/products/mmmmadelineeee-hooded-carhart-jacket-dupe/")},
        {"Carhartt multi Jacket": (35.50, "Brand New", "https://www.depop.com/products/vintedgedesigns-kids-carhart-camo-jacket-brand/")},
    ]
    used_items = [
        {"Carhartt Men's Multi Jacket": (49.99, "Used - Good", "https://www.depop.com/products/founderskeep-super-nice-carhartt-style-camo/")},
        {"Carhartt Men's Black and Grey Jacket": (30.00, "Used - Excellent", "https://www.depop.com/products/lickhere-carhartt-insulated-zip-up-hooded/")},
        {"Carhartt Men's Jacket": (35.50, "Used - Fair", "https://www.depop.com/products/bv1-vintage-faded-carhartt-tan-hooded/")}
    ]
    result = best_match(new_items, used_items, 35.16, 38.49, 36.83)
    assert isinstance(result, list)
    assert result == [
        {"Carhartt Men's Jacket": (20.00, "Like New", "https://www.depop.com/products/mmmmadelineeee-hooded-carhart-jacket-dupe/")},
        {"Carhartt multi Jacket": (35.50, "Brand New", "https://www.depop.com/products/vintedgedesigns-kids-carhart-camo-jacket-brand/")},
        {"Carhartt Men's Black and Grey Jacket": (30.00, "Used - Excellent", "https://www.depop.com/products/lickhere-carhartt-insulated-zip-up-hooded/")},
        {"Carhartt Men's Jacket": (35.50, "Used - Fair", "https://www.depop.com/products/bv1-vintage-faded-carhartt-tan-hooded/")},
        {"Carhartt Men's Multi Jacket": (49.99, "Used - Good", "https://www.depop.com/products/founderskeep-super-nice-carhartt-style-camo/")},
        {"Carhartt Men's Green and Khaki Jacket": (50.00, "Brand New", "https://www.depop.com/products/rachelpattir-vintage-carhartt-detroit-jacket-sz/")}
    ]
    
  
