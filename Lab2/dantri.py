# 1.1 Open connection to page
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "https://dantri.com.vn"
connection = urlopen(url)

# 1.2 Read data

raw_data = connection.read()

# 1.3 Decode data
html_page = raw_data.decode("utf-8")

# 1.4 Save data to file
# Open connection to file
# Write data
# Close connection
# f_conn = open('dantri.html', 'wb')
# f_conn.write(raw_data)
# f_conn.close()

soup = BeautifulSoup(html_page, "html.parser")
ul = soup.find("ul", "ul1 ulnew")  # id = "tbl_grade"....

li_list = ul.find_all('li')

news_list = []

for li in li_list:
    a = li.h4.a
    title = a.string
    link = url + a['href']
    news = {
        "Title": title,
        "Link": link,
    }
    news_list.append(news)

pyexcel.save_as(records=news_list, dest_file_name="dantri.xlsx")
