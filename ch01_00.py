#coding:utf-8
"""
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""

str = "stressed"
reverse = ""
print "not change : %s"%(str)

for t in str[::-1]:
	reverse += t

print "change : %s"%(reverse)