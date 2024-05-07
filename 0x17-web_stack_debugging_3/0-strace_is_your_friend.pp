file_line { 'fix-php-in-wp-settings':
  ensure  => present,
  path    => '/var/www/html/wp-settings.php',
  line    => 'require_once( ABSPATH . WPINC . "/phpp/default-constants.php" );',
  match   => '^require_once\( ABSPATH \. WPINC \. "/phpp/default-constants\.php" \);',
}
