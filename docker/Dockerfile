#docker build -t my_image .
#docker exec -it 2bd322c361e8 bash
#docker run -p 5000:5000 naughtytao/pyflow

FROM ubuntu:18.04

RUN apt update
RUN apt install -y nodejs npm libstdc++6 libgconf-2-4
RUN apt install -y python-pip git yarn
RUN apt install -y build-essential python-dev libxml2 libxml2-dev zlib1g-dev libatlas3-base liblzma-dev
RUN rm -rf /var/cache/apt/*

RUN cd /home \
	&& git clone https://github.com/swcmdb/pyflow.git
	
RUN cd /home/pyflow/src \
	&& pip install --target . flask

RUN cd /home/pyflow/src/static \
	&& npm install
	
WORKDIR /
EXPOSE 5000

CMD python /home/pyflow/src/server.py
 
	



