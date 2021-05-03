# Creater :: Mayank Shrivastava
from flask import Flask, render_template, request
import pyshorteners as ps 

app = Flask(__name__)

def urlShortener(url):
    # We will use nullpointer API from pyshorteners module
    # domain :: 'https://ttm.sh'
    # alternate domain :: 'https://0x0.st'
    url_shorten = ps.Shortener(domain = 'https://ttm.sh')
    # return the shortened url using the API
    return url_shorten.nullpointer.short(url)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def shortURL():
    text = request.form['url']
    if text == '':
        # When no link is enter 
        # Then error message will be printed
        error = "Enter a valid URL"
        return render_template('index.html', processed_text=error)
    # if there is no error then 
    # short url of the given url 
    # will be printed
    newURL = urlShortener(text)
    return render_template('index.html', processed_text=newURL)


if __name__ == '__main__':
    app.run(debug=True)