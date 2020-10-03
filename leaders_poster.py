# Copyright Joel John Kandathil 2020

from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
import requests
import re
import textwrap
import datetime

x = datetime.datetime.now()
date = x.strftime("%d %b %Y")

url="https://www.iplt20.com/"
html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "html.parser")
Header = list(filter(None, soup.find('ul', class_='leader-stats').get_text().split('\n'))) 
data = [x.strip() for x in Header if (len(x.strip()) > 0)]

players_id = []
mee = soup.find('ul', class_='leader-stats')
for i in mee:
    try:
        players_id.append(i.find_next('img')['data-player-id'])
    except:
        pass

Stats = {}
Stats[data[0]] = data[1:3]
Stats[data[5]] = data[6:8]
Stats[data[10]] = data[11:13]
Stats[data[15]] = data[16:18]
Stats[data[19]] = data[20:22]
Stats[data[24]] = data[25:26]

image = Image.open('Leaders.png')
draw = ImageDraw.Draw(image)
font_name = ImageFont.truetype('IntegralCF-Regular.otf', size=40)
font_stat = ImageFont.truetype('IntegralCF-Regular.otf', size=100)

im = Image.open(requests.get("https://static.iplt20.com/players/210/{}.png".format(players_id[1]), stream=True).raw)
image.paste(im.resize((300,300), resample=4), (-15, 735), im.resize((300,300), resample=4))
orange_cap = textwrap.wrap(Stats['Orange Cap'][0], width=10)
y1 = 740
if(len(orange_cap) == 1):
    orange_cap = orange_cap[0].split()
for line in orange_cap:
    w11, h11 = font_name.getsize(line)
    draw.text(((740 - w11)/2, y1), line, font=ImageFont.truetype('IntegralCF-Regular.otf', size=40),align='center',fill='rgb(0, 0, 0)')
    y1+= h11
w12, h12 = font_stat.getsize(Stats['Orange Cap'][1])
draw.text(((740 - w12)/2, y1), Stats['Orange Cap'][1], font=ImageFont.truetype('IntegralCF-Regular.otf', size=100),align='center',fill='rgb(0, 0, 0)')

im = Image.open(requests.get("https://static.iplt20.com/players/210/{}.png".format(players_id[3]), stream=True).raw)
image.paste(im.resize((300,300), resample=4), (790, 735), im.resize((300,300), resample=4))
purple_cap = textwrap.wrap(Stats['Purple Cap'][0], width=10)
if(len(purple_cap) == 1):
    purple_cap = purple_cap[0].split()
y2 = 740
for line in purple_cap:
    w11, h11 = font_name.getsize(line)
    draw.text(((1440 - w11)/2, y2), line, font=ImageFont.truetype('IntegralCF-Regular.otf', size=40),align='center',fill='rgb(0, 0, 0)')
    y2+= h11
w12, h12 = font_stat.getsize(Stats['Purple Cap'][1])
draw.text(((1440 - w12)/2, y2), Stats['Purple Cap'][1], font=ImageFont.truetype('IntegralCF-Regular.otf', size=100),align='center',fill='rgb(0, 0, 0)')

im = Image.open(requests.get("https://static.iplt20.com/players/210/{}.png".format(players_id[5]), stream=True).raw)
image.paste(im.resize((300,300), resample=4), (-15, 1155), im.resize((300,300), resample=4))
highest_score = textwrap.wrap(Stats['Highest Score'][0], width=10)
if(len(highest_score) == 1):
    highest_score = highest_score[0].split()
y1 = 1170
for line in highest_score:
    w11, h11 = font_name.getsize(line)
    draw.text(((740 - w11)/2, y1), line, font=ImageFont.truetype('IntegralCF-Regular.otf', size=40),align='center',fill='rgb(0, 0, 0)')
    y1+= h11
w12, h12 = font_stat.getsize(Stats['Highest Score'][1])
draw.text(((740 - w12)/2, y1), Stats['Highest Score'][1], font=ImageFont.truetype('IntegralCF-Regular.otf', size=100),align='center',fill='rgb(0, 0, 0)')

im = Image.open(requests.get("https://static.iplt20.com/players/210/{}.png".format(players_id[7]), stream=True).raw)
image.paste(im.resize((300,300), resample=4), (790, 1155), im.resize((300,300), resample=4))
bowling_figures = textwrap.wrap(Stats['Best Bowling Figures'][0], width=10)
if(len(bowling_figures) == 1):
    bowling_figures = bowling_figures[0].split()
y2 = 1170
for line in bowling_figures:
    w11, h11 = font_name.getsize(line)
    draw.text(((1440 - w11)/2, y2), line, font=ImageFont.truetype('IntegralCF-Regular.otf', size=40),align='center',fill='rgb(0, 0, 0)')
    y2+= h11
w12, h12 = font_stat.getsize(Stats['Best Bowling Figures'][1])
draw.text(((1440 - w12)/2, y2), Stats['Best Bowling Figures'][1], font=ImageFont.truetype('IntegralCF-Regular.otf', size=100),align='center',fill='rgb(0, 0, 0)')

# im = Image.open(requests.get("https://static.iplt20.com/players/210/1125.png", stream=True).raw)
# image.paste(im.resize((300,300), resample=4), (-15, 1580), im.resize((300,300), resample=4))
# most_sixes = textwrap.wrap(Stats['Most Sixes'][0], width=10)
# if(len(most_sixes) == 1):
#     most_sixes = most_sixes[0].split()
# y1 = 1590
# for line in most_sixes:
#     w11, h11 = font_name.getsize(line)
#     draw.text(((740 - w11)/2, y1), line, font=ImageFont.truetype('IntegralCF-Regular.otf', size=40),align='center',fill='rgb(0, 0, 0)')
#     y1+= h11
# w12, h12 = font_stat.getsize(Stats['Most Sixes'][1])
# draw.text(((740 - w12)/2, y1), Stats['Most Sixes'][1], font=ImageFont.truetype('IntegralCF-Regular.otf', size=100),align='center',fill='rgb(0, 0, 0)')

im = Image.open(requests.get("https://static.iplt20.com/players/210/{}.png".format(players_id[11]), stream=True).raw)
image.paste(im.resize((300,300), resample=4), (-15, 1580), im.resize((300,300), resample=4))
fairplay = textwrap.wrap(Stats['Paytm Fairplay'][0], width=10)
if(len(fairplay) == 1):
    fairplay = fairplay[0].split()
y1 = 1640
for line in fairplay:
    w11, h11 = font_name.getsize(line)
    draw.text(((740 - w11)/2, y1), line, font=ImageFont.truetype('IntegralCF-Regular.otf', size=40),align='center',fill='rgb(0, 0, 0)')
    y1+= h11

im = Image.open(requests.get("https://static.iplt20.com/players/210/{}.png".format(players_id[9]), stream=True).raw)
image.paste(im.resize((300,300), resample=4), (790, 1580), im.resize((300,300), resample=4))
valuable_player = textwrap.wrap(Stats['Most Valuable Player'][0], width=10)
if(len(valuable_player) == 1):
    valuable_player = valuable_player[0].split()
y2 = 1590
for line in valuable_player:
    w11, h11 = font_name.getsize(line)
    draw.text(((1440 - w11)/2, y2), line, font=ImageFont.truetype('IntegralCF-Regular.otf', size=40),align='center',fill='rgb(0, 0, 0)')
    y2+= h11
w12, h12 = font_stat.getsize(Stats['Most Valuable Player'][1])
draw.text(((1440 - w12)/2, y2), Stats['Most Valuable Player'][1], font=ImageFont.truetype('IntegralCF-Regular.otf', size=100),align='center',fill='rgb(0, 0, 0)')


image.save('Output/leaders_{}.png'.format(date))
