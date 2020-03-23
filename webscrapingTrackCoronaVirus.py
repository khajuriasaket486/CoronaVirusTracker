# bs4 is a package for webscraping and BeautifulSoup is a class in bs4.
from bs4 import BeautifulSoup

# Requests is an HTTP library, written in Python, for human beings.
# we can use basic http methods with the help of requests
import requests
import re


class CoronaVirus:
    def __init__(self):
        self.data_list = []
        self.epidermic_details = []
        # sending request and storing it in variable response...
        self.response = requests.get('https://www.worldometers.info/coronavirus/')

        # fetching web page's markup and parsing it.
        self.bs = BeautifulSoup(markup=self.response.text, features='html.parser')
        # print(self.bs)

        # find_all extracts a list of Tag objects thaose match the given criteria...
        self.table = self.bs.find_all('table',{'id':'main_table_countries_today'})
        # print(self.table[0])
        self.tr = self.table[0].find_all('tr')
        # print(self.tr[0].text)
    def format_data(self,md):
        for td in self.tr:

            # strip([chars]) will strip characters from start and end of string...
            self.data_list.append(td.text.strip())
        # print(self.data_list)
        for x in self.data_list:
            # re.match matches substring with the string if it exists at the begining of the original string...
            regex = re.match(md, x, re.IGNORECASE)
            # print(self.data_list)
            # print(regex)
            if regex:
                self.epidermic_details=[]
                self.k = x.split(' '*15) # ' '*15 to make count of columns equal to given count
                self.k = self.k[0]+self.k[len(self.k)-1]
                self.k=(self.k.split('\n'))
        # print(self.k)
        # print(self.k[7])
        for i in self.k:
            if i is '':
                self.epidermic_details.append('NA')
            else:
                self.epidermic_details.append(i.strip())


md = input('Please enter a country: ')
cv = CoronaVirus()
cv.format_data(md)
# print(cv.epidermic_details)














