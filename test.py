import keyword
import time

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
