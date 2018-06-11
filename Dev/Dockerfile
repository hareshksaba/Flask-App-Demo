# Comments in Dockerfiles
FROM python:3.5

# Update and install dependencies
RUN apt-get update
RUN pip install Flask

# Add code
COPY . /app

# Set the working directory
WORKDIR /app

# Set environment variables
ENV FLASK_ENV=development
ENV FLASK_APP=hello.py

# Expose the application's port
EXPOSE 5001

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]