import base64
import io
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from flask import render_template
font = ImageFont.truetype("Afacad-Regular.ttf", size=30)


def generate_card(logo_photo, punchline_color, punchline_text, button_text):

    logo = Image.open(io.BytesIO(logo_photo)).resize((213,94), Image.LANCZOS)
    pic = Image.open("photo/coffee-mug.png").resize((360,351), Image.LANCZOS)
    
    return render_template('index.html',punchline=punchline_text, button_text = button_text, image_base64=pic_to_html(logo),image_base642 = pic_to_html(pic), color = punchline_color )


def pic_to_html(pic):
    image_bytes = io.BytesIO()
    pic.save(image_bytes, format='PNG')
    image_bytes = image_bytes.getvalue()

    # Convert bytes to base64 for embedding in HTML
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    return image_base64
#picture: 180-125 sol üst  540-476 sağ alt
#logo : 253-11   466-105


#ard = generate_card()
#card.save("card.jpg")