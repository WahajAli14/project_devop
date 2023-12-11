FROM python:3.11.7-alpine3.18

LABEL name="Python Application" \   
     maintainer="Ali Wahaj" \
     summary="Backend of doctor"

# Create app directory
WORKDIR /app

EXPOSE 7070

env MONGO_URI="mongodb://localhost:27017"
env MONGO_USERNAME='abc'
env MONGO_PASSWORD="123"
RUN  pip install flask \
    pip install flask_cors \
    pip install pymongo

COPY app.py ./
EntryPoint ["python"]
CMD ["./app.py" ]
