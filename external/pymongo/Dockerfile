FROM mongo:latest
WORKDIR /usr/share/pymongo/
COPY ./howToPymongo.py ./howToPymongo.py
RUN apt update && apt upgrade -y && apt install python3 -y && apt install python3-pymongo -y
