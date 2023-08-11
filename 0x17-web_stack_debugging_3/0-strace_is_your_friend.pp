# Fix 500 error caused by Apache server
exec {'replace':
    provider => shell,
    command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
