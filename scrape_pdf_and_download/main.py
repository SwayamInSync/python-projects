import requests
from bs4 import BeautifulSoup

url = "https://ncert.nic.in/"

res = requests.get(url)
data = res.text


soup = BeautifulSoup(data, "html.parser")
links = soup.select(".scroll-content-announcement ul li a")
links = [l.get('href') for l in links if ".pdf" in l.get('href')]
links = links[:3]

for i in range(len(links)):
    download_pdf_link = f"https://ncert.nic.in{links[i]}"
    response = requests.get(download_pdf_link)
    with open(f"pdf{i}.pdf", "wb") as file:
        file.write(response.content)
