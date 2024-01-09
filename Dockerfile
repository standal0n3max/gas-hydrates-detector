FROM python:3.12-slim

WORKDIR /app

# Copy only the necessary project files
COPY requirements.txt /app/requirements.txt
COPY main.py /app/main.py
COPY CV_webcam.py /app/CV_webcam.py
COPY bot.py /app/bot.py
COPY hydrate_model.h5 /app/hydrate_model.h5

# Install dependencies
RUN pip install -r requirements.txt

# Create necessary directories and set permissions
RUN mkdir -p /app/Processing/temp /app/Processing/saved && \
    chmod -R 777 /app/Processing

# Set the command to run when the container starts
CMD python main.py
