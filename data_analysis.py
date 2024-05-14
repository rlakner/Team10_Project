    
class Analysis:
    def averages(self, items):
        """Calculates the average price of items in different conditions

        Args:
            items(list): The list of Items scraped from Depop
        
        Returns:
            item_averages(tuple): a tuple containing the calculated average 
                price for the item in new condition, used condition, and for all 
                listed items from a search (regardless of condition)
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
    
    def score_price(self, price, avg):
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
    
    def score(self, items):
        """Gives an item an overall score based on its price and condition
        
        Args: 
            items(list): The list of Items scraped from Depop

        Side Effects:
            Modifies the score attribute of an item
        """
        new_avg, used_avg, entire_avg = self.averages(items)
        
        for item in items:
            if item.condition == "New":
                item.score = self.score_price(item.price, new_avg)
                item.score += 1
            else:
                item.score = self.score_price(item.price, used_avg)
                item.score += 0.5
            # provides a higher score if the item is also below the average 
            # price from the entire search
            item.score += self.score_price(item.price, entire_avg)
        
        return items
    
    def best_matches(self, scored_items):
        """Sorts items from a search by how good of a deal they are

        Args:
            scored_items(list): The list of Items from the search with their 
            assigned scores 

        Returns:
            deals(list): a list of the same items but ordered from best to 
            worst deal according to our criteria 
        """
        deals_list = sorted(scored_items, key= lambda item: (-item.score, 
                            item.price))
        return deals_list