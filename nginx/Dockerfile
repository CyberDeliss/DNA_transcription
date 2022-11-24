FROM nginx:1.19-alpine

COPY index.html /usr/share/nginx/html/
COPY style.css /usr/share/nginx/html/
COPY ajax.js /usr/share/nginx/html/

COPY images/ /usr/share/nginx/html/images/

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
