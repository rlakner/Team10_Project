import unittest
from unittest.mock import Mock, patch
from tkinter import Tk, Entry, Button, Toplevel
from deal_finder import Interface, Search, Item
from selenium.common.exceptions import NoSuchWindowException
import pandas as pd
from io import StringIO

class TestDepopDealFinder(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.interface = Interface(self.root)
        
    def test_interface_initialization(self):
        self.assertIsInstance(self.interface.window, Toplevel)
        self.assertIsInstance(self.interface.entry, Entry)
        self.assertIsInstance(self.interface.button, Button)
    
    def test_search_init(self):
        search = Search("clothing")
        self.assertEqual(search.query, "clothing")
        self.assertEqual(search.items_list, [])
    
    def test_item_init(self):
        item = Item("Shirt", 20.0, "New", "https://example.com/shirt")
        self.assertEqual(item.name, "Shirt")
        self.assertEqual(item.price, 20.0)
        self.assertEqual(item.condition, "New")
        self.assertEqual(item.link, "https://example.com/shirt")
    
    def test_search_init_scrape(self):
        search = Search("pants")
        search.driver = Mock()
        search.driver.page_source = "<html><body><ul><li>Item 1</li><li>Item 2</li></ul></body></html>"
        
        try:
            search.init_scrape()
        except NoSuchWindowException as e:
            print(f"Caught NoSuchWindowException: {e}")
            
    
    def setUp(self):
        self.root = Tk()
        self.interface = Interface(self.root)

    @patch('deal_finder.Search')
    @patch('deal_finder.Analysis')
    @patch('deal_finder.scrolledtext.ScrolledText')
    def test_popupmsg(self, mock_scrolledtext, mock_analysis, mock_search):
        user_input = "shirts"

      
        interface = Interface(self.root)

        # Mock user input and button click
        interface.entry.get = Mock(return_value=user_input)
        interface.popupmsg()

        # Assert that the Search class was called with the correct query
        mock_search.assert_called_once_with(user_input)

        # Assert that the scrape_items method of Search was called
        mock_search_instance = mock_search.return_value
        mock_search_instance.scrape_items.assert_called_once()

        # Assert that the Analysis class was created
        mock_analysis.assert_called_once()

        # Assert that the score method of Analysis was called with items from Search
        mock_analysis_instance = mock_analysis.return_value
        mock_analysis_instance.score.assert_called_once_with(mock_search_instance.scrape_items())

        # Assert that the best_matches method of Analysis was called
        mock_analysis_instance.best_matches.assert_called_once()

        # Assert that the display_deals method was called with sorted items
        mock_scrolledtext.return_value.insert.assert_called_once()
        
    def setUp(self):
        self.root = Tk()
        self.interface = Interface(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_display_deals(self):
    
        mock_scrolledtext = Mock()
        self.interface.window.scrolledtext = mock_scrolledtext

       
        mock_sorted_items = [
            Mock(name='Item1', condition='New', price=50.0, link='https://example.com/shoes1', score=2.0),
            Mock(name='Item2', condition='Used', price=20.0, link='https://example.com/shirt1', score=3.5),
        ]

        
        self.interface.display_deals(mock_sorted_items)

    
        mock_scrolledtext.insert.assert_called_once_with(Tk.END, 'Expected text to be inserted')  # Adjust the expected text as needed

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()