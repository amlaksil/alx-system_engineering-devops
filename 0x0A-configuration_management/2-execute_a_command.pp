# kill a process named killmenow

exec {'killmeknow':
    command  => 'pkill killmenow',
    provider => 'shell',
}
