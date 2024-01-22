# Maximum open files limit for nginx increased inorder to 
# increase the number of requests handled by nginx

exec { 'set_ulimit_to 5000':
  command  => '/bin/sed -i "s/ULIMIT.*/ULIMIT=\"-n 5000\"/" /etc/default/nginx'

} -> exec { 'restart nginx':
  command  => '/usr/sbin/service nginx restart',
}
