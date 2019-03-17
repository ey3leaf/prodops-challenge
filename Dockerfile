FROM python:3.6
MAINTAINER Igor
CMD ["mkdir", "/app"]

WORKDIR /app

COPY app/app.py requirements.txt /app/
RUN pip install -r requirements.txt 

ENTRYPOINT ["python"]
CMD ["app.py"]

EXPOSE 5000


