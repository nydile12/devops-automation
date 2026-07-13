# Base Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first
# (better layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of app
COPY . .

# Expose Flask port
EXPOSE 5000

# Environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run the app
CMD ["python", "app.py"]