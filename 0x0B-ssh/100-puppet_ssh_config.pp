# client configuration file with puppet
file_line {'configuration_file':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    user   => 'ubuntu',
    type   => 'ssh-rsa',
    line   => 'IdentityFile ~/.ssh/school',
}

file_line {'no_password':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    }
