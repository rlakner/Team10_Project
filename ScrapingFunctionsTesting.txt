TWO OPTIONS TO TEST THE SCRAPE METHODS:
1.
In deal_finder_tests.py, there are unit tests that must be tested one at a time
that will simply test the outputs of scrape_items(). If you want to test the 
interface simultaneously, see the next option.

2.
Since the init_scrape and scrape_items functions cannot be automatically 
tested, here is a testing procedure to determine if it is successful.

- Open the Depop website https://www.depop.com/ 
- Search for any item using their search feature
- Look at the search results (if there are any)
- Open the deal_finder script that has the Search class 
= Run the code by calling deal_finder.py in the terminal and enter the same 
exact search you used on the website 
- Verify that the function returns a table of Item objects 
- Compare the name, price, condition, and link attributes of the Item 
objects in the returned list with the corresponding results displayed
by the Depop website 
- Test a search where no results are found and ensure that this is communicated;
this will print "No items found. Please adjust your search." in the terminal and
"We did not find any results. Please try another search." in the pop up window.
