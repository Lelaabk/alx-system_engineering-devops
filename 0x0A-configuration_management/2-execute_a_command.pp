# 2-execute_a_command.pp
# Define exec resource to kill the process
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/bin/',
}
