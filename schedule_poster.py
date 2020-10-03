from PIL import Image, ImageDraw, ImageFont
import textwrap
from bs4 import BeautifulSoup
import requests
import re
from datetime import date

#match_no = int(input("Match No: "))
for match_no in range(3,57):
    match_id = str(22235 + match_no) 

    url1 = "https://www.iplt20.com/matches/schedule/men" #CHANGE LINK
    html_content1 = requests.get(url1).text
    soup1 = BeautifulSoup(html_content1, "html.parser")
    par = soup1.find("div", {"class": "js-match", "data-match-id": match_id})
    exp = par.get_text().split('\n')
    date = par.attrs["data-timestamp"]
    date = date.split('-')
    date[2] = date[2][:2]
    data1 = list(filter(None, exp)) #MATCH ID
    data1 = [x.strip() for x in data1 if(len(x.strip()) > 1)]


    if(date[1] == '09'):
        date = date[2] + " Sept " + date[0]
    elif(date[1] == '10'):
        date = date[2] + " Oct " + date[0]
    elif(date[1] == '11'):
        date = date[2] + " Nov " + date[0]

    details = {}
    details["Team_1_Name"] = data1[0]
    details["Team_2_Name"] = data1[2]
    details["Match_No"] = data1[5].split()[1]
    details["Venue"] = data1[5].split(',')[-1].strip()
    details["Date"] = date
    details["Time"] = data1[4][0:9]
    print(details)

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

    image = Image.open('Match.png')
    draw = ImageDraw.Draw(image)

    draw.text((850, 112), details["Match_No"], fill='rgb(255, 255, 255)', font=ImageFont.truetype('IntegralCF-Regular.otf', size=81))
    draw.text((495, 260), details["Venue"], fill='rgb(255, 255, 255)', font=ImageFont.truetype('IntegralCF-Regular.otf', size=81), align='center')

    image.paste(details["Team_1_Captain"], (10, 620), details["Team_1_Captain"])
    image.paste(details["Team_2_Captain"], (595, 620), details["Team_2_Captain"])
    image.paste(details["Team_1_Logo"], (60, 920), details["Team_1_Logo"])
    image.paste(details["Team_2_Logo"], (635, 920), details["Team_2_Logo"])

    w1, h1 = draw.textsize(details["Team_1_Name"], font=ImageFont.truetype('IntegralCF-Regular.otf', size=70))
    w2, h2 = draw.textsize(details["Team_2_Name"], font=ImageFont.truetype('IntegralCF-Regular.otf', size=70))


    lines1 = textwrap.wrap(details["Team_1_Name"], width=12)
    y_text = 1280 + h2
    font = ImageFont.truetype('IntegralCF-Regular.otf', size=60)
    for line in lines1:
        width, height = font.getsize(line)
        draw.text((60, y_text), line, font=ImageFont.truetype('IntegralCF-Regular.otf', size=60),align='center',fill='rgb(255, 255,255)')
        y_text += height


    lines2 = textwrap.wrap(details["Team_2_Name"], width=12)
    y_text = 1280 + h2
    font = ImageFont.truetype('IntegralCF-Regular.otf', size=60)
    for line in lines2:
        width, height = font.getsize(line)
        draw.text(((1020 - width), y_text), line, font=ImageFont.truetype('IntegralCF-Regular.otf', size=60),align='center',fill='rgb(255, 255,255)')
        y_text += height

    w3, h3 = draw.textsize(details["Date"], font=ImageFont.truetype('IntegralCF-Regular.otf', size=70))
    w4, h4 = draw.textsize(details["Time"], font=ImageFont.truetype('IntegralCF-Regular.otf', size=70))

    draw.text(((1080 - w3)/2, 1645), details["Date"], font=ImageFont.truetype('IntegralCF-Regular.otf', size=70),align='center',fill='rgb(255, 255,255)')
    draw.text(((1080 - w4)/2, 1745), details["Time"], font=ImageFont.truetype('IntegralCF-Regular.otf', size=70),align='center',fill='rgb(255, 255,255)')


    image.save('Output/schedule_{}.png'.format(match_no))
