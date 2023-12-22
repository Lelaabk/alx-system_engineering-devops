# 2-execute_a_command.pp
# Define exec resource to kill the process
exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin:/bin',
  refreshonly => true,
}
