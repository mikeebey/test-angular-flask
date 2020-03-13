##Fetch Latest Docker Image Image 
FROM ubuntu:16.04 

RUN apt-get update  \
    && apt-get install -yq --no-install-recommends \
    python3 \
    python3-pip

RUN pip3 install --upgrade pip\
    && pip3 install setuptools

# EXPOSE 5002

# ADD . /app
# WORKDIR /app

# RUN pip3 install -r requirements.txt

# ENTRYPOINT [ "python3" ]

# CMD ["server.py"]






# FROM alpine:latest

# RUN apk add --no-cache python3-dev \
#     && pip3 install --upgrade pip 

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5002

ENTRYPOINT [ "python3" , "server.py" ]

#CMD [ "server.py" ]