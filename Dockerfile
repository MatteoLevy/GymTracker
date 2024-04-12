# Start your image with a Python base image
FROM alpine:latest

# Install Python and pip
RUN apk update && \
    apk add --no-cache python3 py3-pip

# The /app directory should act as the main application directory
WORKDIR /app

# Copy local directories to the current local directory of our docker image (/app)
COPY ./app.py ./
COPY ./utils ./utils

# Install Python dependencies (if needed)
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 3000

# Command to run the application
CMD ["python3", "app.py"]
