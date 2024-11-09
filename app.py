from flask import Flask, render_template

# Create the Flask app instance
app = Flask(__name__, template_folder='template')

# Define the homepage route
@app.route('/')
def home():
    return render_template('index.html')  # This will render the HTML page

if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask application
