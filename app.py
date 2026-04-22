import json
import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "super_secret_key_mangaung" # Used for simple flash messages (optional)

# Load database
def load_data():
    data_path = os.path.join(app.root_path, 'data', 'db.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"dances": [], "interviews": [], "gallery": []}

@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', dances=data.get('dances', []))

@app.route('/dance/<int:dance_id>')
def dance(dance_id):
    data = load_data()
    dances = data.get('dances', [])
    dance_info = next((d for d in dances if d['id'] == dance_id), None)
    if not dance_info:
        return "Dance not found", 404
    return render_template('dance.html', dance=dance_info, dances=dances)

@app.route('/interviews')
def interviews():
    data = load_data()
    return render_template('interviews.html', interviews=data.get('interviews', []), dances=data.get('dances', []))

@app.route('/gallery')
def gallery():
    data = load_data()
    return render_template('gallery.html', items=data.get('gallery', []), dances=data.get('dances', []))

@app.route('/about')
def about():
    data = load_data()
    return render_template('about.html', dances=data.get('dances', []))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    data = load_data()
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Here we would normally save or email this. For now, print to console.
        print(f"New Contact Message: {name} ({email}) - {message}")
        flash("Thank you for your message! We will get back to you soon.", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html', dances=data.get('dances', []))

@app.route('/team')
def team():
    data = load_data()
    return render_template('team.html', dances=data.get('dances', []))

@app.route('/documents')
def documents():
    data = load_data()
    documents_list = [
        {"name": "Dance Research", "file": "Dance Research.pdf", "type": "pdf", "icon": "ph-file-pdf"},
        {"name": "Project Charter", "file": "Project Charter.pdf", "type": "pdf", "icon": "ph-file-pdf"},
        {"name": "Risk Register", "file": "Risk Register.pdf", "type": "pdf", "icon": "ph-file-pdf"},
        {"name": "DevCore Project Document", "file": "DevCore Project Document.2.4.docx", "type": "docx", "icon": "ph-file-doc"},
        {"name": "Interview Questions", "file": "Interview Questions.docx", "type": "docx", "icon": "ph-file-doc"},
        {"name": "Gantt Chart DevCore", "file": "Gantt Chart DevCore.xlsx", "type": "xlsx", "icon": "ph-file-xls"},
        {"name": "Network Diagram", "file": "Network Diagram.pdf", "type": "pdf", "icon": "ph-file-pdf"}
    ]
    return render_template('documents.html', documents=documents_list, dances=data.get('dances', []))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
