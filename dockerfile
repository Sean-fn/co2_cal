FROM python:3.11-alpine

WORKDIR /app

RUN mkdir -p /app/logs && chmod 777 /app/logs

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "api.py" ]