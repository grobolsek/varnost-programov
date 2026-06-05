FROM php:8-alpine
WORKDIR /var/www/html
ENV FLAG="flag{fake_flag}"

COPY src/ /var/www/html/
CMD ["php", "-S", "0.0.0.0:8000", "-t", "/var/www/html"]
