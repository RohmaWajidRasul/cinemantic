# Implemented by Bimnet
FROM python:3.13-slim

WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["/bin/bash"]