# Using Puppet

exec { 'install nginx':
  command  => "apt-get -y update && apt-get -y install nginx && echo 'Holberton School' > /var/www/html/index.html && sed -i '/sendfile on;/a add_header X-Served-By $HOSTNAME;' /etc/nginx/nginx.conf
 && service nginx start",
  provider => 'shell',
}
