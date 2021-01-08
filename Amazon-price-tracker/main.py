import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

url = "<url of amazon page that contain product>" # you can also use input to take it fromo user

headers = {
    "Accept-Language": "<your browser's query>",
    "User-Agent": "<your browser query>",
}

res = requests.get(url=url, headers=headers)
website_data = res.text
soup = BeautifulSoup(website_data, "lxml")

price_tag  = soup.find(name="span", class_="a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P")
product_name = soup.find(name="span", id="productTitle").getText()

price = float(price_tag.getText().replace('₹\xa0', ''))
print(price)

min_price = <"set your affordable price">

if price <= min_price:
    with smtplib.SMTP("<your email provider's SMTP service>") as connection:
        connection.starttls()
        connection.login(user="<your email>", password="<your password for email>")
        connection.sendmail(to_addrs="<email to whom you want to sent>", from_addr="<your email>",
                            msg=f"Subject:Product is Affordable\n\n{product_name} is now {price}, Buy now\n{url}")
