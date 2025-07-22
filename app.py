
from flask import Flask, render_template, request, send_file, url_for
from PIL import Image, ImageDraw, ImageFont
import io
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    pdf_url = None
    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]
        date = request.form["date"]

        cert = Image.open("static/certificate_template.png")
        draw = ImageDraw.Draw(cert)

        try:
            font_name = ImageFont.truetype("arial.ttf", 60)
            font_course = ImageFont.truetype("arial.ttf", 40)
        except:
            font_name = ImageFont.load_default()
            font_course = ImageFont.load_default()

        # Coordinates: tuned to fit the uploaded image (2000 x 1414)
        draw.text((500, 650), name, font=font_name, fill="black")
        draw.text((724, 853.04), course, font=font_course, fill="black")
        draw.text((775, 910.13), date, font=font_course, fill="black")

        output_path = f"static/certificate_preview.pdf"
        cert.save(output_path, "PDF")
        pdf_url = url_for('static', filename="certificate_preview.pdf")

    return render_template("index.html", pdf_url=pdf_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

