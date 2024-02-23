# Using Puppet, create a manifest 

exec { 'killmenow':
    command  => '/usr/bin/pkill killmenow',
    provider => 'shell',
}
