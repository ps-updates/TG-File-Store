# Use Python 3.11 as the base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements and application files to the container
COPY requirements.txt /app/
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Fix for msg_id error: Synchronize system time
RUN apt-get update && apt-get install -y ntpdate && ntpdate pool.ntp.org && apt-get clean

# Expose port 8080 for Gunicorn
EXPOSE 8080

# Command to run Gunicorn and your bot script
CMD ["sh", "-c", "gunicorn app:app --bind 0.0.0.0:8080 & python3 bot.py"]
