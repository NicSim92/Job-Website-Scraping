from bs4 import BeautifulSoup
import requests
import time
import re
import os
import csv

inputpage = int(input("Input Page no.: "))

pagenumbersconvert = range(1,(inputpage+1),1)
pagenumberlistconvert =[*pagenumbersconvert]
pages = pagenumberlistconvert

inputkeyword = input("Input Keyword search: ")
inputkeywordconvert = inputkeyword.replace(' ', '-')


with open ('C:/Users/Username/data_analyst.csv', 'a', encoding='utf-8', newline='') as f_output:
    csv_print = csv.writer(f_output)

    file_is_empty = os.stat ('C:/Users/Username/data_analyst.csv').st_size == 0
    if file_is_empty:
        csv_print.writerow(['Job Title', 'Company', 'Location', 'Salary', 'Date', 'Link'])


        for jobs in soup.find_all('div' ,class_='someclass):
                try:
                    job_title = jobs.find('div', class_='someclass1').text.strip()
                except Exception as e:
                    job_title = None
                print('Job Title:', job_title)

                try:
                    company = jobs.find('span', class_='someclass2').text.strip()
                except Exception as e:
                    company = "Company Confidential"
                print('Company:', company)

                try:
                    location = jobs.find('span',class_='someclass3').text.strip()
                except Exception as e:
                    location = None
                print('Location:', location)

                salary = [a.text.strip() for a in jobs.select("someclass4 > div:nth-child(1) > span:nth-child(4)")]
                salary1 = str(salary).replace("[","").replace("]","").replace("'","").replace(r"\xa0"," ")
                print('Salary:', salary1)

                try:
                    date = jobs.find('time').text.strip()
                except Exception as e:
                    date = None
                print('Date Posted:', date)

                link = jobs.find('a', href=True)
                links = str(link['href'])
                linkfinal = str('https://www.JobWebsiteExample.com.sg') + links
                print('URL:', linkfinal)

                csv_print.writerow([job_title, company, location, salary1, date, linkfinal])

                print('-----------------------------')

                
    time.sleep(0.5)



