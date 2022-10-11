import requests
import imdb
import os

class mvdb:

    def __init__(self):
        self.KEY = os.environ.get('API_Key')
        self.url = f'http://api.themoviedb.org/3/configuration?api_key={self.KEY}'
        self.r = requests.get(self.url)
        self.config = self.r.json()
        self.base_url = self.config['images']['base_url']
        self.sizes = self.config['images']['poster_sizes'][-1]
        self.IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={KEY}'

    def get_movieid(self,movie_name):
        name = movie_name
        ia = imdb.Cinemagoer()
        search = ia.search_movie(name)
        self.movieid = "tt" + str(search[0].movieID)
        return self.movieid

    def get_image_url(self,imdbid):
        self.imgurl = self.IMG_PATTERN.format(KEY=self.KEY,imdbid=imdbid)
        r = requests.get(self.imgurl)
        self.api_response = r.json()

        posters = self.api_response['posters']
        poster_urls = []
        for poster in posters:
            imagename = poster['file_path']
            url = "{0}{1}{2}".format(self.base_url, max_size, imagename)
            poster_urls.append(url)
        return self.imgurl
        pass

    def download_image(self,imageurl):
        pass

mv = mvdb()
imdb = mv.get_movieid("matrix")
url = mv.get_image_url(imdb)
mv.download_image(url)


#mv.get_image(movieid)
#mv.get_
#print(mv)


#name = 'The Lord of the Rings: The Fellowship of the Ring'


#print(id)
