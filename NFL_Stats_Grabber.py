# Import libraries
import requests
import lxml.html as lh
import pandas as pd

url='https://www.footballdb.com/statistics/nfl/player-stats/receiving/2021/regular-season?sort=recnum&limit=10000'
#Create a handle, page, to handle the contents of the website
page = requests.get(url)
