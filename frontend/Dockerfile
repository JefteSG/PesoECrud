FROM node:18-alpine AS build
WORKDIR /app

COPY . .

FROM nginx:1.21.5-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.daemon

COPY --from=build . /usr/share/nginx/html

RUN chmod -R 755 /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]j