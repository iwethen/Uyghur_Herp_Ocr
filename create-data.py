#Bu hvjjet mashina oginishide lazim bolidighan sanlik melumatlarni hasil kilidu
#Yeni 32 herpni ishlitip uyghurchida daim ishlitidighan font bilen resim hvjjiti hasil kilidu
from PIL import Image, ImageDraw, ImageFont
import os
herpler=["چ","ۋ","ې","ر","ت","ي","ۇ","ڭ","و","پ","ھ","س","د","ا","ە","ى","ق","ك","ل","ز","ش","غ","ۈ","ۈ","ب","ن","م","ژ","ف","گ","خ","ج","ۆ"]
# peogrammining toghra ishlishi uchun tvwendiki fontlar kompiyotirdda kachilanghan bulishi kirek
fonts=['c:\\windows\\fonts\\alkatip basma tom.ttf','c:\\windows\\fonts\\alkatip basma.ttf','c:\\windows\\fonts\\alkatip kitab tom.ttf','c:\\windows\\fonts\\alkatip kitab.ttf','c:\\windows\\fonts\\alkatip tor.ttf','c:\\windows\\fonts\\alkatip.ttf','c:\\windows\\fonts\\ukij_macekranbold.ttf','c:\\windows\\fonts\\ukijbasma.ttf','c:\\windows\\fonts\\ukijbom.ttf','c:\\windows\\fonts\\ukijchik.ttf','c:\\windows\\fonts\\ukijcjk.ttf','c:\\windows\\fonts\\ukijekran.ttf','c:\\windows\\fonts\\ukijes.ttf','c:\\windows\\fonts\\ukijesbold.ttf','c:\\windows\\fonts\\ukijesc.ttf','c:\\windows\\fonts\\ukijesn.ttf','c:\\windows\\fonts\\ukijesq.ttf','c:\\windows\\fonts\\ukijest.ttf','c:\\windows\\fonts\\ukijinichke.ttf','c:\\windows\\fonts\\ukijinichkeb.ttf','c:\\windows\\fonts\\ukijjunu.ttf','c:\\windows\\fonts\\ukijka.ttf','c:\\windows\\fonts\\ukijkesme.ttf','c:\\windows\\fonts\\ukijkesme-b.ttf','c:\\windows\\fonts\\ukijkesmetuz.ttf','c:\\windows\\fonts\\ukijkesmetuz-b.ttf','c:\\windows\\fonts\\ukijnsq.ttf','c:\\windows\\fonts\\ukijnsqb.ttf','c:\\windows\\fonts\\ukijnsqz.ttf','c:\\windows\\fonts\\ukijnsqzb.ttf','c:\\windows\\fonts\\ukijqara.ttf','c:\\windows\\fonts\\ukijqara-b.ttf','c:\\windows\\fonts\\ukijqol_tuz.ttf','c:\\windows\\fonts\\ukijqol_yantu.ttf','c:\\windows\\fonts\\ukijqolyazma.ttf','c:\\windows\\fonts\\ukijru.ttf','c:\\windows\\fonts\\ukijsaet.ttf','c:\\windows\\fonts\\ukijsls.ttf','c:\\windows\\fonts\\ukijslsbold.ttf','c:\\windows\\fonts\\ukijslstom.ttf','c:\\windows\\fonts\\ukijteng.ttf','c:\\windows\\fonts\\ukijteng-b.ttf','c:\\windows\\fonts\\ukijtor.ttf','c:\\windows\\fonts\\ukijtut.ttf','c:\\windows\\fonts\\ukijtuz.ttf','c:\\windows\\fonts\\ukijtuzb.ttf','c:\\windows\\fonts\\ukijtuzbb.ttf','c:\\windows\\fonts\\ukijtuzbold.ttf','c:\\windows\\fonts\\ukijtuzg.ttf','c:\\windows\\fonts\\ukijtuzgb.ttf','c:\\windows\\fonts\\ukijtuzk.ttf','c:\\windows\\fonts\\ukijtuzk.ttf','c:\\windows\\fonts\\ukijtuzkb.ttf','c:\\windows\\fonts\\ukijtuzq.ttf','c:\\windows\\fonts\\ukijtzneqish.ttf','c:\\windows\\fonts\\ukijtztr.ttf','c:\\windows\\fonts\\ukijtztrbold.ttf','c:\\windows\\fonts\\ukijzilwa.ttf']

#Herpledin ressim hasil kilidu ve data munderijisige saklaydu
for herp in herpler:
    if not os.path.exists(os.path.join("data",herp)):
        os.makedirs(os.path.join("data",herp))
    for font in fonts:
        for i in range(20,22,1):
            img = Image.new('RGB', (50, 50), color=(255, 255, 255))
            fnt = ImageFont.truetype(font, i)
            d = ImageDraw.Draw(img)
            d.text((0, 0), herp, font=fnt, fill=(0, 0, 0))
            img.save(os.path.join("data",herp)+"\\"+os.path.basename(font)+str(i)+".png")


#tekshurush uchun lazim bolidighhan sanlik melumat hasil kilidu
for herp in herpler:
    img = Image.new('RGB', (50, 50), color=(255, 255, 255))
    fnt = ImageFont.truetype('c:\\windows\\fonts\\ukijtuzqb.ttf', 20)
    d = ImageDraw.Draw(img)
    d.text((0, 0), herp, font=fnt, fill=(0, 0, 0))
    if not os.path.exists("ocrtest"):
        os.makedirs("ocrtest")
    img.save(os.path.join("ocrtest", herp)+ ".png")