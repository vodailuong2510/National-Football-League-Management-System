FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p media
RUN mkdir -p static

EXPOSE 8000

RUN echo '#!/bin/bash\n\
python manage.py collectstatic --noinput\n\
python manage.py migrate\n\
python manage.py runserver 0.0.0.0:8000' > /app/start.sh

RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]