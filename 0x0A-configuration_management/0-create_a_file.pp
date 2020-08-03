# create an file in /tmp with owner, permisions and content
file { 'tmp/holberton'
ensure  => present,
path    => '/tmp/holberton',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet'
}
