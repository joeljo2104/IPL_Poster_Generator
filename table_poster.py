from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
import requests
import re
import datetime

x = datetime.datetime.now()

url="https://www.iplt20.com/points-table/2020"
html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "html.parser")
Header = list(filter(None, soup.find('tr', class_='standings-table__header').get_text().split('\n'))) 

data = []
for i in soup.find_all('td'):
    data.append(re.sub(r'\n[\s]*', " ", i.get_text().strip()))

Team = {}
for i in range(8):
    req = []
    req.append("")
    team = data[i*12 +1].split()
    req.append(team[-1])#NAME
    req.append(data[i*12 +2])
    req.append(data[i*12 +3])
    req.append(data[i*12 +10])
    req.append(data[i*12 +7])
    Team[i+1] = req
image = Image.open('Points_Table.png')
draw = ImageDraw.Draw(image)

date = x.strftime("%d %b %Y")
draw.text((740, 580), date, fill='rgb(255, 255, 255)', font=ImageFont.truetype('IntegralCF-Regular.otf', size=45))
#{Rank : [Logo, Name, Matches, Won, Points, NRR]}

for i in range(0,8):
    if(Team[i+1][1] == "CSK"):
        Team[i+1][0] = Image.open('Team_Logos/Chennai_Super_Kings.png')
    elif(Team[i+1][1] == "DC"):
        Team[i+1][0] = Image.open('Team_Logos/Delhi_Capitals.png')
    elif(Team[i+1][1] == "KXIP"):
        Team[i+1][0] = Image.open('Team_Logos/Kings_XI_Punjab.png')
    elif(Team[i+1][1] == "KKR"):
        Team[i+1][0] = Image.open('Team_Logos/Kolkata_Knight_Riders.png')
    elif(Team[i+1][1] == "MI"):
        Team[i+1][0] = Image.open('Team_Logos/Mumbai_Indians.png')
    elif(Team[i+1][1] == "RCB"):
        Team[i+1][0] = Image.open('Team_Logos/Royal_Challengers_Bangalore.png')
    elif(Team[i+1][1] == "RR"):
        Team[i+1][0] = Image.open('Team_Logos/Rajasthan_Royals.png')
    elif(Team[i+1][1] == "SRH"):
        Team[i+1][0] = Image.open('Team_Logos/Sunrisers_Hyderabad.png')
    else:
        Team[i+1][0] = Image.open('Team_Logos/Velocity.png')

    image.paste(Team[i+1][0].resize((80,80), resample=4), (140, 815 + (137*i)), Team[i+1][0].resize((80,80), resample=4))
    
    draw.text((75, 820 + (137*i)), str(i+1), fill='rgb(255, 255, 255)', font=ImageFont.truetype('IntegralCF-Regular.otf', size=45))
    draw.text((240, 820 + (137*i)), str(Team[i+1][1]), fill='rgb(255, 255, 255)', font=ImageFont.truetype('IntegralCF-Regular.otf', size=45))
    draw.text((430, 820 + (137*i)), str(Team[i+1][2]), fill='rgb(255, 255, 255)', font=ImageFont.truetype('IntegralCF-Regular.otf', size=45))
    draw.text((600, 820 + (137*i)), str(Team[i+1][3]), fill='rgb(255, 255, 255)', font=ImageFont.truetype('IntegralCF-Regular.otf', size=45))
    draw.text((770, 820 + (137*i)), str(Team[i+1][4]), fill='rgb(255, 255, 255)', font=ImageFont.truetype('IntegralCF-Regular.otf', size=45))
    draw.text((890, 830 + (137*i)), str(Team[i+1][5]), fill='rgb(255, 255, 255)', font=ImageFont.truetype('IntegralCF-Regular.otf', size=35))

image.save('Output/table_{}.png'.format(date))
