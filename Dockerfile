FROM python:3.12.2-slim-bookworm

LABEL key="myapy"

WORKDIR /var/wwww

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app .

RUN apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 5432

CMD ["python3", "main.py"]