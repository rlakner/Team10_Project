InterfaceTesting
Since the Interface methods cannot be automatically tested, here is a testing 
procedure to determine if they are successful.

__init__: 
- This method is intended to create the the main pop up window once the 
script is called in the command line.
- To test it, call the deal_finder.py script as outlined in our documentation
(README.md).
- Verify that there is a pop-up window titled "Depop Deal Finder" 
(1190x1000 pixels)
- Verify that the pop up has a section to enter a search query under the text
"What are you searching for?" and that there is a button that says
"Start Finding Deals"
- Closing the pop up window should terminate the program

popupmsg:
- This method is intended to get the query entered by the user and display the 
appropriate message based on the results from the scrape_items method
Bad Case:
- Enter an invalid search into the box under "What are you searching for?"; can 
be anything as simple as random letters (e.g. cbr4kcb4ib4)
- Click the "Start Finding Deals" button
- The web driver will open and search on Depop
- Verify that you are redirected to the pop up with an empty table and this
message: "We did not find any results. Please try another search."
Happy Case:
- Enter a valid search into the box under "What are you searching for?"
- Click the "Start Finding Deals" button
- The web driver will open and search on Depop
- Verify that you are redirected to the pop up with a non-empty table 
and a message above it that says "Happy Shopping!"

display_deals:
- This method is intended to create a display a dataframe within the pop up
window with all information pertaining to items found from a search. 
- Enter a valid search query in the box under "What are you searching for?"
- Click the "Start Finding Deals" button
- If products are found, the web driver will start to go through each listed 
item and get its information
- Once the driver closes, verify that you are redirected to the pop up window
you saw when starting the program
- Verify that a table is displayed with the following columns:
"Product Name", "Condition", "Price", "Link", and "Our Score (0-3)"
- Verify that the appropriate values appear under these columns
