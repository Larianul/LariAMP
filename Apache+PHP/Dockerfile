FROM ubuntu:latest

# Actualizare pachete Ubuntu
RUN apt-get update && apt-get upgrade -y

# Instalare Apache și PHP
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_DOCUMENT_ROOT /var/www/html
ENV APACHE_LOG_DIR /var/log/apache2
RUN mkdir -p /var/run/apache2
COPY ./site/ ${APACHE_DOCUMENT_ROOT}/
COPY ./configmap.yaml /var/lib/docker/configmap.yaml
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q apache2 libapache2-mod-php php
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Setare document radacina si mod rewrite
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf && \
    sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf && \
    a2enmod rewrite

# Setare servername
#RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Copiere site
RUN chown -R www-data:www-data ${APACHE_DOCUMENT_ROOT}

# Expunere port
EXPOSE 80

# Comanda de rulare
CMD ["apachectl", "-D", "FOREGROUND"]
