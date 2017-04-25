from urllib.request import urlopen
from bs4 import BeautifulSoup
# import re

f = urlopen('https://baseball.yahoo.co.jp/npb/')
# f = urlopen('https://baseball.yahoo.co.jp/npb/schedule/?date=20170426')  for test
soup = BeautifulSoup(f, 'lxml')

npbbox_part = soup.find(id='gm_sch')
# npbbox_part = soup.find(class_='NpbScoreBg clearFix')
# gametag = npbbox_part.find_all("a", href=re.compile("npb/teams/*/"))
gametag = npbbox_part.find_all("a", title=True)
game_teams = [gametag[i].get('title') for i in range(len(gametag))]

for i in range(0, len(game_teams), 2):
	print('Game', int(i / 2) + 1, ': ', game_teams[i], ' - ', game_teams[i + 1])
