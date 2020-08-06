#!/usr/bin/ruby
range = 1..254

for ip in range 
    ip_address = "192.168.99.#{ip}"
    puts `ping -c1 #{ip_address} |grep "bytes from" |cut -d " " -f4 | cut -d":" -f1 &`
end

