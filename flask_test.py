from flask import Flask, render_template,request
from api_conf import *
from base64 import b64encode

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
        if mdb.find_data() != False:
            binary_file = mdb.read_data()
            image = b64encode(binary_file).decode("utf-8")
            src = "data:image/gif;base64," + image
            return f'<img src={src} alt="{movie_name}" width="128" height="128">'

        mdb.get_image_url(imdb)
        mdb.getPosterFile()
        mdb.insert_data()
        image = b64encode(mdb.f_bin).decode("utf-8")
        src = "data:image/gif;base64," + image
        return f'<img src={src} alt="{movie_name}" width="128" height="128">'
    return render_template('search.html')

if __name__=="__main__":
    app.run(port=80,host="0.0.0.0")