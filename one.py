from os import link
import requests
from bs4 import BeautifulSoup
website = "https://infopark.in/companies/job-search"
keywords=["react"]
output_file = open("one.txt", "w")
res=requests.get(website)
soup=BeautifulSoup(res.text,'lxml')
jobs=soup.find_all('div',{'class':'row company-list joblist'})
for job in jobs:
    title_element=job.find('a')
    title=title_element.text
    link=title_element['href']
    company=job.find('div',{'class':'jobs-comp-name'}).text
    last_date=job.find('div',{'class':'job-date'}).text
    if any(keyword.lower() in title.lower() for keyword in keywords):
        print(title,company,last_date)
        output_file.write(title+"\n"+link+"\n"+company+"\n"+last_date+"\n\n") 