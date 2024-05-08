<<<<<<< HEAD
# 0-strace_is_your_friend.pp

package {
 'libapache2-mod-php':
  ensure => installed,
}

# Define a service resource to ensure Apache is restarted after the fix
service {
 'apache2':
  ensure => running,
  enable => true,
  require => Package['libapache2-mod-php'],
}
=======
# fixing Apache is returning a 500 error

exec { 'fix_apache_error_config':
        command  => 'sed -i s/.phpp/.php/g /var/www/html/wp-settings.php',
        provider => 'shell'
}
>>>>>>> 755381b5e999927009f3053f59c2d6eb6aafd233
