FROM python:3-alpine
RUN mkdir /app
COPY /app /app
RUN pip install -r /app/requirements.txt
RUN mkdir /log

EXPOSE 8080
CMD ["python", "/app/webserver.py"]