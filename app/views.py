from flask import Flask, render_template, request, send_file, redirect, url_for
from rembg import remove
from PIL import Image
import os
from app import app
from app.forms import UploadForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()

    if request.method == 'POST' and form.validate_on_submit():
        uploaded_file = form.image.data
        if uploaded_file.filename != '':
            image_path = os.path.join('app', 'static', uploaded_file.filename)
            uploaded_file.save(image_path)

            input_image = Image.open(image_path)
            input_image = input_image.convert('RGB')
            output_image = remove(input_image)

            output_filename = 'output_' + uploaded_file.filename
            output_path = os.path.join(app.root_path, 'static', output_filename)

            output_image.save(output_path, format='PNG')

            return redirect(url_for('resultado', filename=output_filename))

    return render_template('index.html', form=form)

@app.route('/resultado/<filename>')
def resultado(filename):
    
    output_path = os.path.join(app.root_path, 'static', filename)


    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
