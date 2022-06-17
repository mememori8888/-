# -*- coding:utf-8 -*-
# re.sub(pattern, repl, string, count=0, flags=0)

# pattern : 正規表現パターン
# repl : 置換する文字列
# string : 置換される文字列
# count : 置換回数
# count と flags　はオプション

import re
import regex

text = '第4 回学会だよ'
str = 'ひらがなカタカナ漢字'
p = regex.findall('^(?:\p{Script=Hiragana}|\p{Script=Katakana}|\p{Script=Han})+$',text)
# result = p.findall('第4 回学会だよ')
print(p)
# print(type(result))
# m = re.search(r'1|t',text)
# if m:
#   print('ok')
# else:
#   print('ng')

test = text.replace(' ','')
print(test)