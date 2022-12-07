FROM byjg/nginx-extras:1.21
WORKDIR /nginx
COPY ./static /django/static/
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d