# Using Puppet

exec { 'update':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => 'apt-get -y update'
}
exec { 'nginx':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => 'apt-get -y install nginx'
}
exec { 'index':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "echo "Holberton School" > /var/www/html/index.html"
}
exec { 'config_redirect':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "sed -i '/listen 80 default_server;/a rewrite ^/redirect_me https://www.linkedin.com/ permanent;' /etc/nginx/sites-available/default"
}
exec { 'start_nginx':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => 'service nginx start'
}
