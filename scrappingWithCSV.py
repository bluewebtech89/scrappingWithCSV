#First, we need to import all the libraries that we are going to use.

# import libraries
import urllib2  
from bs4 import BeautifulSoup  
import csv  
from datetime import datetime  

#Next, declare a variable for the url of the page.
# specify the url

quote_page = 'http://www.bloomberg.com/quote/SPX:IND'  

#Then, make use of the Python urllib2 to get the HTML page of the url declared.

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)  

#Finally, parse the page into BeautifulSoup format so we can use BeautifulSoup to work on it
# parse the html using beautiful soap and store in variable `soup`

soup = BeautifulSoup(page, 'html.parser')  

#Now we have a variable soup containing the HTML of the page. Here's where we can start coding the part that extracts the data.

# Take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'class': 'name'})  
name = name_box.text.strip() # strip() is used to remove starting and trailing  
print "Name = ", name  

# get the index price
price_box = soup.find('div', attrs={'class':'price'})  
price = price_box.text  
print "Price = ", price  

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:  
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])
