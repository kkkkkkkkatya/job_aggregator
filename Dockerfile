FROM python:3.13

RUN pip install --upgrade pip --no-cache-dir

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
