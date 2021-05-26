# import libraries
from bs4 import BeautifulSoup
from urllib import request
import csv
import re

urlpage = 'https://en.wikipedia.org/wiki/Bubacarr_Bah'
page = request.urlopen(urlpage)
soup = BeautifulSoup(page, 'html.parser')

table = soup.find('table', attrs={'class': 'infobox biography vcard'})
html_table = table.find_all('tr')



# html_table[1].find('div', attrs={'class': 'birthplace'})
# html_table[1].find('td')
# html_table[2]
# html_table[0].getText()
html_table[2].find_all('a')

buba = []
buba.append(['name', [html_table[0].getText()]])

for data in html_table[1:]:
    rowname = data.find('th', attrs={'scope': 'row'})
    rowdata = data.find('td')
    if (rowdata is not None) and (rowname is not None):
        if len(rowname) + len(rowdata) != 0:
            # looking for multiple a tags
            # since this field may contain more than one data
            rowdata = [a_tag.getText() for a_tag in rowdata.find_all('a')]
            # separating multiple occurrences by newline
            rowdata = ", ".join(rowdata)
            # rowname = re.sub(re.UNICODE, ' ', rowname.getText())
            rowname = rowname.getText()
            buba.append([rowname, [rowdata]])

with open('buba.csv', 'w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerow(buba)
