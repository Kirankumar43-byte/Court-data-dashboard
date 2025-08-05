FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
# Install browser deps
RUN playwright install firefox
CMD ["python", "app.py"]
