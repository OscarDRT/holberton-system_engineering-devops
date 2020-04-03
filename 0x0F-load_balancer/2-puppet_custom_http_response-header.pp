# Using Puppet

exec { 'install nginx':
  command  => "sudo apt-get -y update && sudo apt-get -y install nginx %% echo "Holberton School" | sudo tee /var/www/html/index.html && sed -i '/sendfile on;/a add_header X-Served-By $hostname;' /etc/nginx/nginx.conf && service nginx start",
  provider => "shell",
}
