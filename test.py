import nmap
'''
# 创建一个 Nmap 扫描器对象
scanner = nmap.PortScanner()

# 执行端口扫描
scanner.scan('127.0.0.1', '1-1024', '-v')

# 输出扫描结果
for host in scanner.all_hosts():
    print('Host : %s (%s)' % (host, scanner[host].hostname()))
    print('State : %s' % scanner[host].state())
    for proto in scanner[host].all_protocols():
        print('Protocol : %s' % proto)
        lport = scanner[host][proto].keys()
        for port in lport:
            print('port : %s\tstate : %s' % (port, scanner[host][proto][port]['state']))

# 检测漏洞
nm_script_output = scanner.run_script('vuln', '-p 22')
for host, script_result in nm_script_output.items():
    print('Host : %s' % host)
    for result in script_result:
        print('Vulnerability : %s' % result['id'])

import nmap

# 创建nmap扫描器对象
scanner = nmap.PortScanner()

# 扫描目标主机的指定端口范围
scanner.scan('127.0.0.1', '1-1024')

# 输出扫描结果
for host in scanner.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, scanner[host].hostname()))
    print('State : %s' % scanner[host].state())

    for proto in scanner[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        lport = scanner[host][proto].keys()
        for port in sorted(lport):
            print(type(port))
            print('port : %s\tstate : %s' % (port, scanner[host][proto][port]['state']))
            print('Service : %s' % scanner[host][proto][port]['name'])
'''
from scapy.all import *

# 开启网卡的混杂模式
conf.promisc=True

# 开始抓包
sniff(filter="tcp", prn=lambda x:x.summary())