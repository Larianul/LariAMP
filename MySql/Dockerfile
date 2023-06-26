FROM ubuntu:latest

# Instalare dependințe necesare
RUN apt-get update && \
    apt-get -y install gnupg curl && \
    apt-key adv --fetch-keys 'https://mariadb.org/mariadb_release_signing_key.asc'

RUN apt-get install mysql-server -y

# Instalare și configurare MySQL
RUN apt-get update && \
    echo "mysql-server mysql-server/root_password password root" | debconf-set-selections && \
    echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections && \
    apt-get -y install mariadb-server



# Configurare MySQL pentru a accepta conexiuni de la orice adresă IP
RUN sed -i 's/bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/' /etc/mysql/mariadb.conf.d/50-server.cnf

RUN /etc/init.d/mysql start && \
    mysql -u root -proot -e "CREATE DATABASE testdb;" && \
    mysql -u root -proot -e "GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';"

# Expunerea portului 3306 pentru conexiunea la MySQL
EXPOSE 3306

# Configurare serviciu MySQL pentru a rula la pornirea containerului
CMD ["mysqld", "--user=mysql", "--console"]
