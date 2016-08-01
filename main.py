import sh
from sh import sudo

### TCP Increase TCP Segment size


### TCP Slow Start Optimization
sysctl = sh.Command('sysctl')
tcp_slow_start = sysctl('net.ipv4.tcp_slow_start_after_idle').strip().replace(' ','')
enabled_tcp_slow_start = 'net.ipv4.tcp_slow_start_after_idle=1'
disabled_tcp_slow_start = 'net.ipv4.tcp_slow_start_after_idle=0'
if tcp_slow_start == enabled_tcp_slow_start:
  print 'Optimizing TCP Slow Start'
  sudo('sysctl', '-w', disabled_tcp_slow_start)
elif tcp_slow_start == disabled_tcp_slow_start:
  print 'TCP Slow Start already optimized'
else:
  print 'Error Occurred with Slow Start Optimization'