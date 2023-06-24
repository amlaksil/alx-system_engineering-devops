# creates puppet file inside /tmp directory and set file permission, owner
# and grop

file { '/tmp/school':
    ensure  => file,
    path    => '/tmp/school',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}
