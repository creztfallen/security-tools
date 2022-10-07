from bs4 import BeautifulSoup
import requests

# getting the request content
site = requests.get("https://www.climatempo.com.br/").content

# downloading the site html
soup = BeautifulSoup(site, 'html.parser')

# transform the html into string and print it
print(soup.prettify())

x = soup.find("h6", class_="copyright")

print(x.string)

# print(soup.p.string)
# print(soup.a)
print(soup.find('admin'))
