# This puppet manifest will create a new user account for holberton, give it sudo privileges
user { 'holberton':
  ensure   => present,
  password => '',
  groups   => ['sudo'],
}
file { '/etc/sudoers.d/holberton':
  ensure  => present,
  # grants the holberton user the ability to run any command as any other user
  # without having to enter a password. 
  content => 'holberton ALL=(ALL) NOPASSWD: ALL',
}
