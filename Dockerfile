FROM python:3.8-slim

USER root
ENV FLASK_APP=app.py

WORKDIR /app
COPY ./app /app
COPY ./docker-entrypoint.sh /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# SHELL ["/bin/bash", "-c"]
# ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["sleep", "3600"]