# -*- coding: utf-8 -*-
import subprocess
import time
# для доменов второго уровня, вида domain.ru
dnsservers = ['ns3-l2.nic.ru','ns4-l2.nic.ru']

domens = open('domens.txt', 'r').read().split('\n')
subdomains = open('subdomains-10000.txt', 'r').read().split('\n')
finalresult = open('result.txt', 'a')


for dnsserver in dnsservers:
    for domen in domens:
        for subdomain in subdomains:
            target = subdomain + '.' + domen
            try:
                time.sleep(0.3)
                #result = subprocess.run('nslookup -q=any ' + 'www.sberauto.com' + ' ' + dnsserver, stdout=subprocess.PIPE)
                result = subprocess.run('nslookup -q=any ' + target + ' ' + dnsserver, stdout=subprocess.PIPE)
            except subprocess.CalledProcessError:
                pass

            outputSingleString = result.stdout.decode('utf-8', 'backslashreplace')
            outputMultiString = outputSingleString.split('\r\n')
            if outputMultiString[3] != '':
                print(
                    result.args + '\n' +
                    outputMultiString[3] + '\r\n')
                finalresult.write(
                    result.args + '\n' +
                    outputMultiString[3] + '\r\n')
                pass

# import dns.resolver
#
# dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
# dns.resolver.default_resolver.nameservers = ['ns1-cloud.nic.ru']
#
# domens = open('domens.txt', 'r').read().split('\n')
# subdomains = open('subdomains-10000.txt', 'r').read().split('\n')
#
# for domen in domens:
#     for subdomain in subdomains:
#         target = subdomain + '.' + domen
#         try:
#             answersIPv4 = dns.resolver.resolve(target, 'A') # IPv4
#             answersIPv6 = dns.resolver.resolve(target, 'AAAA') # IPv6
#         except dns.resolver.NoAnswer:
#             pass
#         except dns.resolver.NXDOMAIN:
#             pass
#
#         if 'answersIPv4' in locals():
#             for rdata in answersIPv4:
#                 print(target + ' - ' + rdata.address)
#
#         if 'answersIPv6' in locals():
#             for rdata in answersIPv6:
#                 print(target + ' - ' + rdata.address)