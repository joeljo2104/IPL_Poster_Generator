from PIL import Image, ImageDraw, ImageFont
import textwrap
from bs4 import BeautifulSoup
import requests
import re
import os
import time

match_no = int(input("Match No: "))
match_id = str(22235 + match_no) 

while(True):
    try:
        url1 = "https://www.iplt20.com/matches/results/men/2020" #CHANGE LINK
        html_content1 = requests.get(url1).text
        soup1 = BeautifulSoup(html_content1, "html.parser")
        data1 = list(filter(None, soup1.find("div", {"class": "js-match", "data-match-id": match_id}).get_text().split('\n'))) #MATCH ID
        data1 = [x.strip() for x in data1 if(len(x.strip()) > 1)]
    except:
        print("Loading...")
        time.sleep(3)
        pass
    else:
        break

details = {}
details["Result"] = data1[0]
details["Team_1_Name"] = data1[1]
details["Team_1_Score"] = data1[2]
details["Team_1_Overs"] = data1[3]
details["Team_2_Name"] = data1[4]
details["Team_2_Score"] = data1[5]
details["Team_2_Overs"] = data1[6]
details["Match_No"] = data1[7].split()[1]
details["Venue"] = data1[7].split(',')[-1].strip()

if(details["Team_1_Name"][:4] == "Chen"):
    details["Team_1_Logo"] = Image.open('Team_Logos/Chennai_Super_Kings.png')
    details["Team_1_Captain"] = Image.open('Captains/CSK.png')
elif(details["Team_1_Name"][:4] == "Delh"):
    details["Team_1_Logo"] = Image.open('Team_Logos/Delhi_Capitals.png')
    details["Team_1_Captain"] = Image.open('Captains/DC.png')
elif(details["Team_1_Name"][:4] == "King"):
    details["Team_1_Logo"] = Image.open('Team_Logos/Kings_XI_Punjab.png')
    details["Team_1_Captain"] = Image.open('Captains/KXIP.png')
elif(details["Team_1_Name"][:4] == "Kolk"):
    details["Team_1_Logo"] = Image.open('Team_Logos/Kolkata_Knight_Riders.png')
    details["Team_1_Captain"] = Image.open('Captains/KKR.png')
elif(details["Team_1_Name"][:4] == "Mumb"):
    details["Team_1_Logo"] = Image.open('Team_Logos/Mumbai_Indians.png')
    details["Team_1_Captain"] = Image.open('Captains/MI.png')
elif(details["Team_1_Name"][:4] == "Roya"):
    details["Team_1_Logo"] = Image.open('Team_Logos/Royal_Challengers_Bangalore.png')
    details["Team_1_Captain"] = Image.open('Captains/RCB.png')
elif(details["Team_1_Name"][:4] == "Raja"):
    details["Team_1_Logo"] = Image.open('Team_Logos/Rajasthan_Royals.png')
    details["Team_1_Captain"] = Image.open('Captains/RR.png')
elif(details["Team_1_Name"][:4] == "Sunr"):
    details["Team_1_Logo"] = Image.open('Team_Logos/Sunrisers_Hyderabad.png')
    details["Team_1_Captain"] = Image.open('Captains/SRH.png')
else:
    details["Team_1_Logo"] = Image.open('Team_Logos/Velocity.png')
    details["Team_1_Captain"] = Image.open('Captains/CSK.png')

if(details["Team_2_Name"][:4] == "Chen"):
    details["Team_2_Logo"] = Image.open('Team_Logos/Chennai_Super_Kings.png')
    details["Team_2_Captain"] = Image.open('Captains/CSK.png')
elif(details["Team_2_Name"][:4] == "Delh"):
    details["Team_2_Logo"] = Image.open('Team_Logos/Delhi_Capitals.png')
    details["Team_2_Captain"] = Image.open('Captains/DC.png')
elif(details["Team_2_Name"][:4] == "King"):
    details["Team_2_Logo"] = Image.open('Team_Logos/Kings_XI_Punjab.png')
    details["Team_2_Captain"] = Image.open('Captains/KXIP.png')
elif(details["Team_2_Name"][:4] == "Kolk"):
    details["Team_2_Logo"] = Image.open('Team_Logos/Kolkata_Knight_Riders.png')
    details["Team_2_Captain"] = Image.open('Captains/KKR.png')
elif(details["Team_2_Name"][:4] == "Mumb"):
    details["Team_2_Logo"] = Image.open('Team_Logos/Mumbai_Indians.png')
    details["Team_2_Captain"] = Image.open('Captains/MI.png')
elif(details["Team_2_Name"][:4] == "Roya"):
    details["Team_2_Logo"] = Image.open('Team_Logos/Royal_Challengers_Bangalore.png')
    details["Team_2_Captain"] = Image.open('Captains/RCB.png')
elif(details["Team_2_Name"][:4] == "Raja"):
    details["Team_2_Logo"] = Image.open('Team_Logos/Rajasthan_Royals.png')
    details["Team_2_Captain"] = Image.open('Captains/RR.png')
elif(details["Team_2_Name"][:4] == "Sunr"):
    details["Team_2_Logo"] = Image.open('Team_Logos/Sunrisers_Hyderabad.png')
    details["Team_2_Captain"] = Image.open('Captains/SRH.png')
else:
    details["Team_2_Logo"] = Image.open('Team_Logos/Velocity.png')
    details["Team_2_Captain"] = Image.open('Captains/CSK.png')

if(details["Result"][:4] == "Chen"):
    details["Foreground"] = 'rgb(29, 65, 140)'
    details["Background"] = 'rgb(252, 206, 6)'
elif(details["Result"][:4] == "Delh"):
    details["Foreground"] = 'rgb(255, 255, 255)'
    details["Background"] = 'rgb(40, 41, 104)'
elif(details["Result"][:4] == "King"):
    details["Foreground"] = 'rgb(255, 255, 255)'
    details["Background"] = 'rgb(237, 31, 39)'
elif(details["Result"][:4] == "Kolk"):
    details["Foreground"] = 'rgb(243, 196, 51)'
    details["Background"] = 'rgb(58, 34, 93)'
elif(details["Result"][:4] == "Mumb"):
    details["Foreground"] = 'rgb(255, 255, 255)'
    details["Background"] = 'rgb(0, 79, 145)'
elif(details["Result"][:4] == "Roya"):
    details["Foreground"] = 'rgb(203, 169, 43)'
    details["Background"] = 'rgb(0, 0, 0)'
elif(details["Result"][:4] == "Raja"):
    details["Foreground"] = 'rgb(0, 0, 255)'
    details["Background"] = 'rgb(255, 105, 180)'
elif(details["Result"][:4] == "Sunr"):
    details["Foreground"] = 'rgb(255, 255, 255)'
    details["Background"] = 'rgb(230, 100, 61)'
else:
    details["Foreground"] = 'rgb(255, 255, 255)'
    details["Background"] = 'rgb(0, 0, 0)'


image = Image.open('Match.png')
draw = ImageDraw.Draw(image)

image.paste(details["Team_1_Captain"], (10, 620), details["Team_1_Captain"])
image.paste(details["Team_2_Captain"], (595, 620), details["Team_2_Captain"])
image.paste(details["Team_1_Logo"], (60, 920), details["Team_1_Logo"])
image.paste(details["Team_2_Logo"], (635, 920), details["Team_2_Logo"])


w1, h1 = draw.textsize(details["Team_2_Score"], font=ImageFont.truetype('IntegralCF-Regular.otf', size=100))
w2, h2 = draw.textsize(details["Team_2_Overs"], font=ImageFont.truetype('IntegralCF-Regular.otf', size=45))
w3, h3 = draw.textsize(details["Result"], font=ImageFont.truetype('IntegralCF-Regular.otf', size=70))

draw.text((850, 112), details["Match_No"], fill='rgb(255, 255, 255)', font=ImageFont.truetype('IntegralCF-Regular.otf', size=81))
draw.text((495, 260), details["Venue"], fill='rgb(255, 255, 255)', font=ImageFont.truetype('IntegralCF-Regular.otf', size=81), align='center')
draw.text((60, 1345), details["Team_1_Score"], fill='rgb(255, 255, 255)', font=ImageFont.truetype('IntegralCF-Regular.otf', size=100))
draw.text((60, 1467), details["Team_1_Overs"], fill='rgb(255, 255, 255)', font=ImageFont.truetype('IntegralCF-Regular.otf', size=45))
draw.text((1020-w1, 1345), details["Team_2_Score"], fill='rgb(255, 255, 255)', font=ImageFont.truetype('IntegralCF-Regular.otf', size=100), align ="right")
draw.text((1020-w2, 1467), details["Team_2_Overs"], fill='rgb(255, 255, 255)', font=ImageFont.truetype('IntegralCF-Regular.otf', size=45), align ="right")

draw.rectangle([0,1900, 1080,1600], fill = details['Background'])
lines = textwrap.wrap(details["Result"], width=20)
y_text = 1545 + h3
w_text = 40 + w3
font = ImageFont.truetype('IntegralCF-Regular.otf', size=70)
for line in lines:
    width, height = font.getsize(line)
    draw.text(((1080 - width) / 2, y_text), line, font=ImageFont.truetype('IntegralCF-Regular.otf', size=70),align='center',fill=details['Foreground'])
    y_text += height

image.save('Output/match_{}.png'.format(match_no))
os.system('python table_poster.py')
os.system('python leaders_poster.py')