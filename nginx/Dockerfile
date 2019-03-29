FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf*
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
COPY django_project/media /var/www/blog/media
EXPOSE 80