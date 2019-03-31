FROM python:3.7-alpine

WORKDIR /app
COPY requirements/ .

RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

RUN pip install -r prod.txt

# Add entrypoint script
COPY scripts/entrypoint.sh /usr/local/bin/entrypoint.sh

COPY ./ ./

EXPOSE 8990

ENTRYPOINT ["entrypoint.sh"]

WORKDIR /app

CMD gunicorn -b 0.0.0.0:8990 -w 4 django_project.wsgi