FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

COPY main.py /

COPY own_commands.json /

COPY mongo_startup.py /

COPY entrypoint.sh /

COPY requirements.txt /app

# Copy the current directory contents into the container at /app
COPY app /app

ENV PYTHONPATH /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

WORKDIR /

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
