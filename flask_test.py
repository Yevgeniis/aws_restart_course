from flask import Flask, render_template,request
from api_conf import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return "About page"

@app.route('/search',methods=['GET', 'POST'])
def load_insert_html():
    if request.method == 'POST':
        movie_name = request.form['name']
        imdb = mdb.get_movieid(movie_name)

        mdb.get_image_url(imdb)
        mdb.getPosterFile()
        mdb.insert_data()
        return "matrix"
    return render_template('search.html')

if __name__=="__main__":
    app.run()