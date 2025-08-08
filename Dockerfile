# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files to container
COPY . .

# Install any dependencies if you have requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run your app (adjust accordingly)
CMD ["python", "main.py"]
