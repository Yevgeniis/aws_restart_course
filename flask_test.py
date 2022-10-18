from flask import Flask, render_template, request, jsonify
from flask import jsonify
from api_conf import *
from base64 import b64encode
from werkzeug.exceptions import InternalServerError
from logging import FileHandler, WARNING
import rollbar
import pytest


app = Flask(__name__,template_folder="Templates")

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

#rollbar.init('POAT_SERVER_ITEM_ACCESS_TOKEN', 'dev')

# @app.errorhandler(InternalServerError)
# def payload_validation_failure(err):
#      return jsonify({"message": "ERROR NAME, PLEASE,TRY AGAIN !!!"}),500
#      return jsonify({"message": "Server attempted to return invalid data"}), 500

@app.errorhandler(InternalServerError)
def validation_failure(err):
  return jsonify({"ERROR NAME !!!":" ---> PLEASE,TRY AGAIN !!!"}),500

#
# @app.route("/profile/<name>")
# def profile(name):
#   return render_template("index.html", name=name)

@app.route('/')
def index():
    return render_template('search.html')  #("index.html")

@app.route('/about')
def about():
    return "About page"

@app.route('/search',methods=['GET', 'POST'])
def load_insert_html():

  #try:
    if request.method == 'POST':

        movie_name = request.form['name']
        imdb = mdb.get_movieid(movie_name)

    # if type(movie_name) != str:
    #      movie_name = "ERROR NAME"
    #      print(movie_name)



    if mdb.find_data():   #!= False:

            binary_file = mdb.read_data()

            image = b64encode(binary_file).decode("utf-8")
            src = "data:image/gif;base64," + image
            return f'<center><img src={src} alt="{movie_name}" width="300" height="400"></center>'

# except: #TypeError:
# rollbar.report_message('There is a data type mismatch', 'fatal')
 #    except:
 # rollbar.report_exc_info()


    # except:
    #  #return render_template('Error.html')
    #   if not isinstance(image):  #(type(mdb.find_data()) != str) :
    #         return render_template('Error.html')
    #  #elif :
    ##return render_template('Error.html')

 # assert isinstance(mdb.name,str), "a should be nonzero!"
# if not isinstance(mdb.name,str):
#     raise ValueError("name should be string")

    mdb.get_image_url(imdb)
    mdb.getPosterFile()
    mdb.insert_data()
    image = b64encode(mdb.f_bin).decode("utf-8")
    src = "data:image/gif;base64," + image


    # except ValueError as e:
    #   print(e)

    return f'<center><img src={src} alt="{movie_name}" width="300" height="400"></center>'
    return render_template('search.html')





if __name__=="__main__":
    app.run(port=80,host="0.0.0.0")









