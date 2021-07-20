
FROM python:3.8
COPY . /project2
WORKDIR /project2
RUN pip install -r requirements.txt
RUN apt-get -y install python3
ENV PORT 5000
EXPOSE 5000
CMD ["python3","app.py"]