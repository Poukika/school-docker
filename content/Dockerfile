FROM ubuntu:18.04
RUN apt-get update 
RUN apt-get install python3-pip -y 
RUN pip3 install requests

ADD content_test.py /exam/content_test.py
WORKDIR /exam/

CMD python3 content_test.py