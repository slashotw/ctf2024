FROM tiangolo/uwsgi-nginx-flask:python3.10

COPY src /app
ADD flag /
RUN chmod 444 /flag
RUN pip3 install -r requirements.txt

CMD python3 main.py