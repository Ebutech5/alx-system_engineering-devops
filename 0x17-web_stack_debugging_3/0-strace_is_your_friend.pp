
# Puppet manifest to fix Apache returning a 500 error

exec { 'fix wordpress':
  command     => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path        => '/usr/local/bin:/bin',
}
