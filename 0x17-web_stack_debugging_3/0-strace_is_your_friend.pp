# Puppet manifest to fix Appache 500 error by strace
service { 'apache2':
  ensure => running,
}
