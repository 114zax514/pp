#coding:utf-8
import urllib2
import sys
 
print('調べたい単語(exitで終了)')
while True: 
    word = raw_input('>> ')
    if(word == 'exit'):
        sys.exit()
    fp = urllib2.urlopen('http://ejje.weblio.jp/content/'+word)
    html = fp.read()
    fp.close()

    index = html.find('主な意味')+51
    index2 = html.find('</td></tr></tbody></table></div>')
    meaning = html[index:index2]
    if('</div>' in meaning) : 
        print ('該当結果なし')
    else :
        print(html[index:index2])
