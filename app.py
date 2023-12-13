from flask import Flask, request, render_template_string,send_file
from weasyprint import HTML
import img_generate_inference
import create_card
from pdf2image import convert_from_bytes


app = Flask(__name__)

pipe = img_generate_inference.load_pipe()
print("Pipe loaded...")



@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/generateCard', methods=['POST'])
def generate_card_controller():
    sample_photo = request.files['samplePhoto'].read()
    logo_photo = request.files['logoPhoto'].read()
    prompt = request.form.get('prompt')
    color = request.form.get('color')
    punchline_color = request.form.get("punchlineColor")
    punchline_text = request.form.get("punchlineText")
    button_text = request.form.get("buttonText")

    img_generate_inference.generate_img(pipe, sample_photo, prompt, color)
    photo = create_card.generate_card(logo_photo,punchline_color,punchline_text,button_text)

    template = render_template_string(photo)
    pdf_options = {
        'width': int(request.form.get('pdf_width', 7.3)),  # Default width in inches
        'height': int(request.form.get('pdf_height', 7.5)),  # Default height in inches
    }
    pdf_bytes = HTML(string=template).write_pdf(**pdf_options)
    images = convert_from_bytes(pdf_bytes, fmt='png',size=(702, 795))
    image_path = 'output.png'
    images[0].save(image_path, 'PNG')

    # Return the image file as a response
    return send_file(image_path, mimetype='image/png', as_attachment=True)

    


if __name__ == '__main__':
    app.run(debug=True, port=80)
