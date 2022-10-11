import requests
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

        def get_movieID():
            pass

        def get_image():
            self.IMG_PATTERN.format(KEY=self.KEY,imdbid=)
            pass

mv=mvdb()


