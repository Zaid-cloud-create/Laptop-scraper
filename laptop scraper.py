import requests
from bs4 import BeautifulSoup
import csv

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')



products = soup.find_all('div', class_='col-md-4 col-xl-4 col-lg-4')  
#item=  products[0]

#name  = item.find('a', class_='title').text.strip()
#price = item.find('h4', class_='pull-right price').text.strip()
#description = item.find('p', class_='description').text.strip()
#image = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops" + item.find("img")["src"]
#rating = len(item.find_all('span', class_='glyphicon glyphicon-star'))


with open('laptops.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price', 'Description', 'Image URL', 'Rating'])
    
    for item in products:
        name = item.find('a', class_='title').text.strip()

        price = item.find('h4', class_='price float-end card-title pull-right').text.strip()

        description = item.find('p', class_='description').text.strip()

        image = "https://webscraper.io" + item.find("img")["src"]

        rating = len(item.find('div', class_='ratings').find_all('span', class_='ws-icon ws-icon-star'))
 
				
        writer.writerow([name, price, description, image, rating])

print("code executed")
























































