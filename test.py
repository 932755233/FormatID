import keyword
import time
import re

print(keyword.kwlist)

print(r'http:\\www.baidu.com')
print(ord('乘'))

ts = '188'
# dt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))
# print(dt)

m, s = divmod(int(ts), 60)
bu0 = ''
if s < 10:
    bu0 = '0'
print("%s'%s%s" % (m, bu0, s))

url = "https://www.vipcard.igetget.com/checkout/jointVip/home/000-005-3516815164571756#/jointVip/claimRights?from=third&sku=PSPKG97654701"
pattern = re.compile('[a-zA-z]+://www.([^\s]*)/')
print(pattern.search(url).group(1))