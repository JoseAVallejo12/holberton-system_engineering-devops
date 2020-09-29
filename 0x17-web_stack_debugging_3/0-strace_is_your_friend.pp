# Fix wp-settings.php
exec { 'fix-wordpress-php-confg':
  command => '/bin/sed -i \'s/.phpp/.php/\' /var/www/html/wp-settings.php',
}
