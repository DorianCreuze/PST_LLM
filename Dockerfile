# Base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies

RUN pip install --no-cache-dir flask ollama httpx

# Copy application files
COPY summarize.py /app

# Expose port if the Flask app serves HTTP
EXPOSE 5000

# Command to run the app
CMD ["python", "summarize.py"]
