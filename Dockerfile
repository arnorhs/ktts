# Use an official Python runtime as a parent image
FROM python:3.9

# Update the package list and install build-essential, which includes GCC
RUN apt-get update && \
    apt-get install -y build-essential && \
    rm -rf /var/lib/apt/lists/*

# (Optional) Verify the GCC installation
RUN gcc --version

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Define environment variables (optional)
ENV NAME="World"

# Run the Python application
CMD ["python", "main.py"]
