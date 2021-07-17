from bs4 import BeautifulSoup
import requests
import pandas as pd

table_body = []
columns = ['Rank', 'Major', 'Degree Type', 'Early Career Pay', 'Mid Career Pay', 'High Meaning (%)']

for r in range(34):
    url = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{r + 1}"
    response = requests.get(url, 'html.parser')
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    rows = soup.select('table tbody tr')
    for row in rows:
        table_body.append([cell.string for cell in row.select("span.data-table__value")])

pd.DataFrame(table_body).to_csv('college-salary-report.csv', index=False)
