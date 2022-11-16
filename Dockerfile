FROM alpine
WORKDIR /api_project
COPY ./api_project requirements.txt ./
EXPOSE 80
RUN apk add --no-cache python3 py3-pip
RUN pip install -r requirements.txt
ENTRYPOINT ["/usr/bin/python3","./flask_web.py"]