# 如何调整字符串文本中的格式 2017-05-11改成05/11/2017

import re

log = open('kk.log').read()
# 正则表达式捕获组 捕获组
# log = re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',log)

log = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<month>/\g<day>/\g<year>',log)

print(log)

