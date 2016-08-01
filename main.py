import sh
from sh import sudo

### TCP Increase TCP Segment size


### TCP Slow Start Optimization
sysctl = sh.Command('sysctl')
tcp_slow_start = sysctl('net.ipv4.tcp_slow_start_after_idle').strip()
if tcp_slow_start == 'net.ipv4.tcp_slow_start_after_idle = 1':
  print 'Optimizing TCP Slow Start'
  sudo('sysctl', '-w', 'net.ipv4.tcp_slow_start_after_idle=0')
elif tcp_slow_start == 'net.ipv4.tcp_slow_start_after_idle = 0':
  print 'TCP Slow Start already optimized'
else:
  print 'Error Occurred with Slow Start Optimization'