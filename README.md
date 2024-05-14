# Team10_Project
INST326 Final Project - Depop Deal Finder - Documenation

Thank you for using our Depop Deal Finder program! We created this program
to help Depop users with the time consuming and exhausting process of analyzing
items on Depop, especially considering the increasing number of resellers and 
their drastically high prices. This program analyzes the items for you and 
provides you with a list of what we consider to be the best deals from your 
search. 

In order to get the most out of this program, please take the following steps:

STEP 1 - INSTALL CHROMEDRIVER
- Head over to https://googlechromelabs.github.io/chrome-for-testing/ for 
the latest available version of ChromeDriver 
- Scroll down to the Stable section
- Select the 'chromedriver' link that is suited for your operating system
- This is going to download a folder to your computer

STEP 2 - GET THE CHROMEDRIVER FILE PATH 

For Windows:
- Open the Windows File Explorer (Press ⊞ Win+E).
- Find the folder that contains the ChromeDriver file
- Right-click the file which will then display a menu
- Press the Windows key + S to open the search bar
- Click Properties at the bottom of the menu
- Find the path next to “Location”(close to the center of the window)
- Highlight the file path and copy it 

For Mac: 
- Open Finder
- Click View in the toolbar at the top of your screen
- Click Show Path Bar if it is not already on
- Find the ChromeDriver file
- Control-Click the file
- Hold the Option key
- Click on Copy [filename] as Pathname

For Linux:
- Open the terminal
- Use the readlink command: readlink -f [filename]

STEP 3 -  UPDATE PATH IN CODE
-  Navigate to the line of code that initailizes an instance of Service. This 
line of code will say: service = Service() and #Change your path
- Change the value of the executable_path by pasting the path from step 2

OPTIONAL STEP - CHANGE SCROLL LENGTH
- For efficiency and demo purposes, we set the scrolling threshold to 50, 
this is a representation of the time the web driver will scroll for. We 
approximate every increment of 50 to be a single scroll (i.e. 50 = 1 scroll,
100 = 2 scrolls, etc). The longer you scroll for the more listings that will be
analyzed and put into the interface.
- If you would like to change this threshold, please change the integer value on 
line 91 marked by a comment that says "Change this to make it scroll for longer"

STEP 4 - USE THE PROGRAM
- To run the program from the command line, ensure that you have the 
data_analysis.py file as well. Then, type in python3 deal_finder.py (Mac) or 
python deal_finder.py (Windows).\
- When you execute the deal_finder script, there will be a pop up window
that prompts you to enter a search
- Once you click on the Start Finding Deals button, the ChromeDriver application
will open in the background and start scraping through Depop
- You will see this process in real time as the driver scrolls and then gets 
information for each item listed in the results page within the scroll limit
(it will look like as if someone is controlling your computer)
- Once the driver is finished, it will wait a few seconds before it closes and 
displays the results (if it found any)
- You will be redirected to the pop up window once again which will have a
table with the results of the search sorted by their score, price, and its
condition. You will also find the name of the item and a direct link to it
- If you find an item you are interested in based on the information provided,
you can simply copy the direct link into your browser to view it on Depop and 
purchase it if you desire
- If no results are found, you will be asked to adjust your search
- If you are certain that there is nothing wrong with your search, then run it
again by clicking the Start Finding Deals button - sometimes the driver will
stop running if the Depop page does not load fast enough and it will not return
any Items from the search. It is rare, but it happens, so simply try again.
- To run another search, just type it into the input box and click the 
Start Finding Deals button to repeat this process

We hope you enjoyed!