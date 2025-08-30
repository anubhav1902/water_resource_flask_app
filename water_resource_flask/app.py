
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash, jsonify
import pandas as pd
import os
from werkzeug.utils import secure_filename
import json

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXT = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'replace-me-with-a-secure-key'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXT

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    liters = max(0, float(data.get('liters',0)))
    leaks = max(0, float(data.get('leaks',0)))
    households = max(0, float(data.get('households',0)))
    liters_saved = liters * 365
    leaks_saved = leaks * 1000
    households_saved = households * 5000
    total = liters_saved + leaks_saved + households_saved
    return jsonify({
        'liters_saved': round(liters_saved,2),
        'leaks_saved': round(leaks_saved,2),
        'households_saved': round(households_saved,2),
        'total': round(total,2)
    })

@app.route('/contact', methods=['POST'])
def contact():
    data = request.form.to_dict()
    fname = os.path.join(app.config['UPLOAD_FOLDER'], 'contacts.jsonl')
    with open(fname, 'a', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")
    flash('Thanks! Your message was captured locally for this demo.')
    return redirect(url_for('index') + '#contact')

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            try:
                df = pd.read_csv(path)
                summary = df.describe(include='all').to_json()
                summary_path = os.path.join(app.config['UPLOAD_FOLDER'], filename + '.summary.json')
                with open(summary_path, 'w', encoding='utf-8') as f:
                    f.write(summary)
                return render_template('upload.html', filename=filename, tables=[df.head(10).to_html(classes='data', header="true", index=False)], summary=json.loads(summary))
            except Exception as e:
                flash('Error processing CSV: ' + str(e))
                return redirect(request.url)
    return render_template('upload.html')

@app.route('/uploads/<path:filename>')
def downloads(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
