import re
# from html import unescape

with open('dp.html') as f:
	html = f.read()

p_teams = re.findall(r'<a href="/npb/teams/[0-9]+/"\sdata-ylk="slk:team.*?</a></td>', html, re.DOTALL)

for p_team in p_teams:
	team = re.search(r'>(.*)</a>', p_team).group(0)
	team = team.lstrip('>')
	team = team.replace('</a>', '')
	print(team)