FROM python:3.8-buster

RUN adduser --disabled-password dropbot

WORKDIR /home/dropbot

RUN mkdir maps
RUN apt update
RUN apt install libgl1-mesa-glx --yes

COPY bot.py ./
COPY circle_drawer.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN chown -R dropbot:dropbot ./
USER dropbot

CMD ["python", "bot.py"]
