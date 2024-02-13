FROM ubuntu:18.04
RUN apt-get update 
RUN apt-get install python3-pip -y 
RUN pip3 install requests

ADD authentication_test.py /exam/authentication_test.py
WORKDIR /exam/

CMD python3 authentication_test.py