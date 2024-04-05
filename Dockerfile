FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy requeriments.txt to the working directory
COPY requirements.txt .

# Install the requeriments
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
