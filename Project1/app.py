from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def gallery():
    images = sorted(os.listdir(app.config['UPLOAD_FOLDER']))
    return render_template('index.html', images=images)

@app.route('/upload', methods=['POST'])
def upload_image():
    image = request.files['image']
    if image:
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)