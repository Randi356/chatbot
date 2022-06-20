FROM rendyprojects/python:latest

COPY . /rendy.py/
WORKDIR /rendy.py/
RUN python3 -m pip install --upgrade pip
RUN pip3 install --upgrade pip setuptools
RUN pip install --ignore-installed PyYAML 
RUN pip3 install -r https://raw.githubusercontent.com/Randi356/chatbot/Master/requirements.txt

CMD bash start
