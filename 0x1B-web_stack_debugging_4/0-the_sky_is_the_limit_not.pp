#Fix wp-settings.php increase the file open simultaly
exec { 'fix-nginx-open-files':
command => '/bin/sed -i \'s/ULIMIT="-n 15"/ULIMIT="-n 4096"/\' /etc/default/nginx',
}
# resetar nginx
exec { 'restart nginex':                                                                                 command => '/usr/sbin/service nginx restart',
}
