FROM mongo:4
WORKDIR /usr/share/pymongo/
COPY ./howToPymongo.py ./howToPymongo.py
RUN apt update && apt install python3 -y && apt install python3-pymongo -y
