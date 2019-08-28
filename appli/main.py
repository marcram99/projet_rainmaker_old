from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    return render_template('main.html')