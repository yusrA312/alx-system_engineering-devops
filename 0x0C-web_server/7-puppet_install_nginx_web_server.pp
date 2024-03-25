# Puppet manifest to install and configure Nginx web server with redirection

# Install Nginx package
package { 'nginx':
	ensure => installed,
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
	ensure  => file,
		content => "
			server {
				listen 80 default_server;
				listen [::]:80 default_server;

				root /var/www/html;
				index index.html index.htm index.nginx-debian.html;

				server_name _;

				location / {
					try_files $uri $uri/ =404;
				}

				location /redirect_me {
					return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
				}

				error_page 404 /error_404.html;
				location = /error_404.html {
					root /var/www/html;
				}
			}
	",
}

# Create index.html with "Hello World!" message
file { '/var/www/html/index.html':
	ensure  => file,
		content => 'Hello World!',
}

# Create custom error page
file { '/var/www/html/error_404.html':
	ensure  => file,
		content => "Ceci n'est pas une page",
}

# Ensure Nginx service is running and enabled
service { 'nginx':
	ensure  => running,
		enable  => true,
		require => File['/etc/nginx/sites-available/default'],
}

