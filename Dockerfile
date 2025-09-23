FROM python:3.11.7-alpine3.19

COPY . /app
# Create a unprivileged user
RUN addgroup mrd \
    && adduser -G mrd -D -h /app mrd \
    && mkdir /app/config \
    && chown -R mrd:mrd /app

WORKDIR /app
USER mrd
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "src/main.py" ]
