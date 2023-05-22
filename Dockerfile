# Base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files to the container
COPY . .

# Expose the port
EXPOSE 8501

# Set the entrypoint command
CMD ["streamlit", "run", "app.py"]
