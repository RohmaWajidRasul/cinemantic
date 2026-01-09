FROM python:3.12-slim

WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application using a production server (Gunicorn)
# Use 'server.wsgi' which corresponds to the DJANGO_SETTINGS_MODULE in manage.py
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "server.wsgi:application"]