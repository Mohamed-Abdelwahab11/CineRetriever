# Use a lightweight Python image
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data required for Lab 2 & 8[cite: 1]
RUN python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"

# Copy the rest of the project
COPY . .

# Expose Flask port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]