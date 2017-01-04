# -*- coding: utf-8 -*-
from __future__ import absolute_import,print_function
from __future__ import unicode_literals
from __future__ import division
from future import standard_library
standard_library.install_aliases()
from nine import str,iteritems
dictdata={'Z':'(','z':'ผ','X':')','x':'ป','C':'ฉ','c':'แ','V':'ฮ','v':'อ','B':'ฺ','b':'ิ','N':'์','n':'ื','M':'?','m':'ท','<':'ฒ',',':'ม','>':'ฬ','.':'ใ','?':'ฦ','/':'ฝ',
'A':'ฤ','a':'ฟ','S':'ฆ','s':'ห','D':'ฏ','d':'ก','F':'โ','f':'ด','G':'ฌ','g':'เ','H':'็','h':'้','J':'๋','j':'j','K':'ษ','k':'า','L':'ศ','l':'ส',':':'ซ','"':'.',"'":"ง",':':'ซ',';':'ว',
'Q':'๐','q':'ๆ','W':'"','w':'ไ','E':'ฎ','e':'ำ','R':'ฑ','r':'พ','T':'ธ','t':'ะ','Y':'ํ','y':'ั','U':'๊','u':'ี','I':'ณ','i':'ร','O':'ฯ','o':'น','P':'ญ','p':'ย','{':'ฐ','[':'บ','}':',',']':'ล','|':'ฅ',']':'ฃ',
'~':'%','`':'_','@':'๑','2':'/','#':'๒','3':'-','$':'๓','4':'ภ','%':'๔','5':'ถ','^':'ู','6':'ุ','&':'฿','7':'ึ','*':'๕','8':'ค','(':'๖','9':'ต',')':'๗','0':'จ','_':'๘','-':'ข','+':'๙','=':'ช'}
# แก้ไขพิมพ์ภาษาไทยผิดภาษา
def texttothai(data):
	"""เป็นคำสั่งแก้ไขข้อความที่พิมพ์ผิดภาษา ต้องการภาษาไทย แต่พิมพ์เป็นภาษาอังกฤษ 
	รับค่าเป็น ''str'' คืนค่าเป็น ''str''"""
	data = list(data)
	data2 = ""
	for a in data:
		try:
			a = dictdata[a]
		except:
			a = a
		data2+=a
	return data2
# แก้ไขพิมพ์ภาษาอังกฤษผิดภาษา
def texttoeng(data):
	"""เป็นคำสั่งแก้ไขข้อความที่พิมพ์ผิดภาษา ต้องการภาษาอังกฤษ แต่พิมพ์เป็นภาษาไทย
	รับค่าเป็น ''str'' คืนค่าเป็น ''str''"""
	data = list(data)
	data2 = ""
	dictdataeng= {v: k for k, v in iteritems(dictdata)}
	for a in data:
		try:
			a = dictdataeng[a]
		except:
			a = a
		data2+=a
	return data2
if __name__ == "__main__":
	a="l;ylfu8iy["
	a=texttothai(a)
	a=texttothai(a)
	b="นามรสนอำันี"
	b=texttoeng(b)
	print(a)
	print(b)