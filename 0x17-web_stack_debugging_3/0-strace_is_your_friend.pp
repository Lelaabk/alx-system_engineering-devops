# Puppet manifest to fix Appache 500 error by strace
# Fix bad extension to "php" in this file 'wp-settings.php'

exec{'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => 'usr/local/bin/:/bin/'
}
