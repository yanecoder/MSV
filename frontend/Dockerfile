FROM nginx:alpine
COPY static/ /usr/share/nginx/html/static/
COPY templates/ /usr/share/nginx/html/templates/
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
