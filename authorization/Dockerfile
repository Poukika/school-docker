FROM ubuntu:18.04
RUN apt-get update 
RUN apt-get install python3-pip -y 
RUN pip3 install requests

ADD authorization_test.py /exam/authorization_test.py
WORKDIR /exam/

CMD python3 authorization_test.py