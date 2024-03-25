# Puppet manifest to install and configure Nginx web server with redirection

# Install Nginx package
exec { 'update system':
	command => '/usr/bin/apt-get update',
}

package { 'nginx':
	ensure  => 'installed',
		require => Exec['update system'],
}

file { '/var/www/html/index.html':
	content => 'Hello World!',
}

exec { 'redirect_me':
	command => 'sed -i "24i\        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
		provider => 'shell',
}

file_line { 'install':
	ensure => 'present',
	       path   => '/etc/nginx/sites-enabled/default',
	       after  => 'listen 80 default_server;',
	       line   => 'rewrite ^/redirect_me https://www.github.com/yusrA312 or permanent;',
}

service { 'nginx':
	ensure  => running,
		require => Package['nginx'],
}
