# app.py
from flask import Flask, render_template, request, redirect, jsonify, url_for

app = Flask(__name__)

# Dummy users for authentication
users = {"test@example.com": {"password": "password"}}

# Dictionary to store leaf significance
leaf_significance = {
    "tomato": "Tomato leaves are considered sacred in Indian traditions. They are believed to have healing properties and are used in rituals."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    # Here, implement signup logic if needed.
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    # Simple user authentication logic
    if email in users and users[email]['password'] == password:
        return render_template('index.html', show_leaf_form=True)  # Show the leaf form after login
    return redirect('/')

@app.route('/leaf_info', methods=['POST'])
def leaf_info():
    leaf_name = request.form['leaf_name'].lower()
    significance = leaf_significance.get(leaf_name, "Significance not found.")
    return render_template('index.html', significance=significance, show_leaf_form=False)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Handle file upload
        file = request.files['file']
        if file:
            return jsonify({"message": "File uploaded successfully!"})
        return jsonify({"message": "No file uploaded."})
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
