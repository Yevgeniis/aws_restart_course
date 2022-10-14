import requests
import imdb
import os
import pymongo
import gridfs

class mvdb():

    def __init__(self):
        self.KEY = os.environ.get('API_Key')
        self.url = f'http://api.themoviedb.org/3/configuration?api_key={self.KEY}'
        self.r = requests.get(self.url)
        self.config = self.r.json()
        self.base_url = self.config['images']['base_url']
        self.sizes = self.config['images']['poster_sizes'][-1]
        self.IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={KEY}'

    def get_movieid(self,movie_name):
        self.name = movie_name
        ia = imdb.Cinemagoer()
        search = ia.search_movie_advanced(self.name)
        self.movieid = "tt" + str(search[0].movieID)
        return self.movieid

    def get_image_url(self,imdbid):
        self.imgurl = self.IMG_PATTERN.format(KEY=self.KEY,imdbid=imdbid)
        r = requests.get(self.imgurl)
        self.api_response = r.json()
        self.imgname = self.api_response['posters'][0]['file_path']
        self.url = "{0}{1}{2}".format(self.base_url, self.sizes, self.imgname)
        return self.url

    def getPosterFile(self):
        r = requests.get(self.url)
        filetype = r.headers['content-type'].split('/')[-1]
        filename = 'poster_{0}.{1}'.format(self.name, filetype)
        self.filename = filename
        with open(self.filename, 'wb') as w:
            w.write(r.content)
        return self.filename

class mongo(mvdb):
    """ DAL for mongo DB"""
    def __init__(self,ip,port,db_name,col_name):
        mvdb.__init__(self)
        self.myclient = pymongo.MongoClient(ip, port)
        self.db=self.myclient[db_name]
        self.col=self.db[col_name]


    def insert_data(self):
        #ans=self.col.insert_one({"name":self.filename})
        #self.ans = ans
        fs = gridfs.GridFS(self.db)
        with open(self.filename, 'rb') as read_file:
           file_bin = read_file.read()
           self.f_bin = file_bin
        file_id = fs.put(file_bin, filename=f"{self.movieid}")
        print(fs.list())
        print(fs.get(file_id).read())
        return

    def find_data(self):
        result = self.col.find_one({"filename": self.movieid})
        if result == None:
            return False
        self.objid = result['_id']
        return self.objid

    def delete_data(self):
        mongo.find_data(self)
        self.col.delete_one({"_id":self.objid})
        return

    def update_data(self):
        #fs.update(fileId, QC_RESULT=qcResult)
        pass

    def read_data(self):
        #file = mongo.find_data(self)
        fs = gridfs.GridFS(self.db)
        result = fs.find_one({"filename": self.movieid})
        #print(result)
        image = result.read()
        #print(image)
        return image

#if __name__ == "__main__":
    """
    test module
    """
db_name="mydatabase"
col_name="fs.files"
ip="localhost"
port=27017
mdb=mongo(ip,port,db_name,col_name)

# imdb = mdb.get_movieid('matri')
# print(imdb)
# mdb.get_image_url(imdb)
# print(mdb.getPosterFile())
# mdb.insert_data()
# print(mdb.read_data())
# #mdb.delete_data()


# imdb = mv.get_movieid("matrix")
# url = mv.get_image_url(imdb)
# mv.getPosterFile()

#mv.get_image(movieid)
#mv.get_
#print(mv)

