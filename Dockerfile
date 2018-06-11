FROM ubuntu:latest
COPY . /app
WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install -r requirements.txt
ENTRYPOINT ["flask"]
CMD ["run", "--port=5001"]
#ENTRYPOINT ["python"]
#CMD ["app.py", "--port=5001"]
#trying to run on port 5001