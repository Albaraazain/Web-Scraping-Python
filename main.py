import requests
from bs4 import BeautifulSoup

URL = "https://www.drugs.com/strattera.html"  # replace with the URL you want to scrape
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# print(soup)


# **********************************************************
# p_tag = soup.find('h1')
# print(p_tag.get_text())  # Print the text inside the <p> tag


# **********************************************************
# # Find all <p> tags on the page
# p_tags = soup.find_all('p')
#
# # Print the text inside each <p> tag
# for tag in p_tags:
#     print(tag.get_text())


# **********************************************************
# # Find all <div> tags with class "my-class"
# for link in soup.find_all('a'):
#     print(link.get('href'))


# **********************************************************
# # Another common task is extracting all the text from a page:
# print(soup.get_text())


# **********************************************************
# Find all <a> tags with http links
for link in soup.find_all('a'):
    theLink = link.get('href')
    http = "http"
    if theLink[0:3] == http[0:3]:
        print(theLink)

