FROM python:3.9-slim

WORKDIR /app

COPY websocket_client.py /app/websocket_client.py
COPY requirements.txt /app/requirements.txt
COPY start.sh /app/start.sh

RUN pip install -r requirements.txt
RUN chmod +x /app/start.sh

CMD ["./start.sh"]
