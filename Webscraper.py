import requests
from bs4 import BeautifulSoup
import pandas as pd

data = requests.get(input("Enter url : "))

soup = BeautifulSoup(data.text,'html.parser')

data = []

for main_block in soup.find_all('div',{'class':'_3liAhj _1R0K0g'}):
    for a in main_block.find_all('a',{'class':'_2cLu-l'}):
        name = a.text
    for p in main_block.find_all('div',{'class':'_1vC4OE'}):
        price = p.text
    data.append([name,price])
print(data)

df=pd.DataFrame(data,columns=['Name','Price'])
df.to_csv('flip_data.csv',index=False,header=False)
