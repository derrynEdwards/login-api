# Base Image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy Source Code
COPY . /app/
COPY application /app/

# Install Requirements
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

# Expose Port
EXPOSE 5000

# Run API
CMD ["python", "web.py"]
