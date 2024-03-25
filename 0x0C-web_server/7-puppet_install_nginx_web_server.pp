# Puppet manifest to install and configure Nginx web server with redirection

# Install Nginx package
package { 'nginx':
	ensure => installed,
}

# Create index.html with "Hello World!" message
file { '/var/www/html/index.html':
	ensure  => file,
		content => 'Hello World!',
		require => Package['nginx'],
}

# Configure redirection in Nginx configuration file
file_line { 'add-rewrite-rule':
	ensure  => present,
		path    => '/etc/nginx/sites-available/default',
		line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
		require => Package['nginx'],
		notify  => Service['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
	ensure => running,
}
