FROM alpine
COPY . /app
WORKDIR /app
EXPOSE 80
RUN apk add --no-cache python3 py3-pip
RUN pip install flask
RUN pip install requests
RUN pip install cinemagoer
RUN pip install pymongo
ENTRYPOINT ["/usr/bin/python3","./flask_web.py"]
