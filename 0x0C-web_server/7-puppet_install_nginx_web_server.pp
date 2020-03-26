# Using Puppet

exec { 'install nginx':
  command  => "apt-get -y update && apt-get -y install nginx && echo 'Holberton School' > /var/www/html/index.html && sed -i '/listen 80 default_server;/a rewrite ^/redirect_me https://www.linkedin.com/ permanent;' /etc/nginx/sites-available/default && service nginx start",
  provider => 'shell',
}
