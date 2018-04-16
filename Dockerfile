FROM python:3

WORKDIR /app

ADD .  .

RUN pip install gpiozero

CMD ["python","./HeatFair.py"]
