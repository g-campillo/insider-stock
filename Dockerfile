FROM python:3.9.7
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY setup_certs.py .
RUN python setup_certs.py