import urllib.request
import json 
import time
from PIL import Image
from PIL import ImageFont 
from PIL import ImageDraw

def get_views():
    views = 1000000
    return views 

def views_to_string(views): 
    ret = []
    curr = 0 
    v = str(views)[::-1]
    for idx, i in enumerate(v):
        if idx % 3 == 0 and idx > 0: 
            ret.append(",") 
        ret.append(i)
    
    return "".join(ret[::-1])

def create_thumbnail(views): 
    view_string = views_to_string(views)

    img = Image.open("sample-in.JPG")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Corp-Bold.otf", 90)
    draw.text((510,100), view_string + " VIEWS", (50, 205, 50), font=font)
    draw.text((520,200), "Likes", (50, 205, 50), font=font)
    draw.text((530,300), "Dislikes", (50, 205, 50), font=font)
    draw.text((540,400), "Comments", (50, 205, 50), font=font)
    img.save("thumbnail.jpg")

def main():
    # STEP 1: Get Video Views
    current_views = get_views()
    create_thumbnail(current_views)
    print("Finish The thumbnails")       
if __name__ == "__main__":
    main()





