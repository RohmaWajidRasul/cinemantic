FROM python:3.13-slim

WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
# This command keeps the server running in the foreground
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]