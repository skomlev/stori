FROM python:3.11-slim-bullseye

RUN mkdir /opt/stori
WORKDIR /opt/stori
ADD . /opt/stori

# Install the specified packages
RUN pip install -r requirements.txt

CMD ["python", "main.py" ]
