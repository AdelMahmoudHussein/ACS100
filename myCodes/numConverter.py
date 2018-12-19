# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 23:46:37 2018

@author: Adel13
"""

hexaDec = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,
        '9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

decHexa = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',
        9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

def hex2dec(fromNum, fromBase, toBase):
    toNum = 0
    rev_fromNum = fromNum[::-1]
    for i in range(len(rev_fromNum)):
        toNum += hexaDec[rev_fromNum[i].upper()]*fromBase**i
    return toNum


def dec2hex(fromNum, fromBase, toBase):
    toNum = ''
    power = 0
    while fromNum > 0:
        toNum = decHexa[fromNum % toBase] + toNum
        fromNum //= toBase
        power += 1
    return toNum    


def convert(fromNum, fromBase, toBase):
    if (fromBase,toBase) == (10,16):
        return dec2hex(fromNum, fromBase, toBase)
    
    if (fromBase,toBase) == (16,10):
        return hex2dec(fromNum, fromBase, toBase)
        
    if fromBase ==10 or toBase == 10:
        toNum = 0
        power = 0
        while fromNum > 0:
            toNum += fromBase**power*(fromNum % toBase)
            fromNum //= toBase
            power += 1
        return toNum
    
    else:
        return convert(convert(fromNum,fromBase,10),10,toBase)

print(convert(101,2,8))
print(convert(101,2,10))
print("""============      
============""")
print(convert(101,8,2))
print(convert(101,8,10))
print("""============
============""")
print(convert(101,10,2)) 
print(convert(101,10,8)) 
print("""============
============""")
print(convert('AF5',16,10))
print(convert('A1',16,10))
print(convert('1F5',16,10))
print("""============
============""")
print(convert(161,10,16))
print(convert(501,10,16))
print(convert(2805,10,16))
print("""============
============""")
print(convert('AF5',16,2))
print(convert('A1',16,8))
print(convert('1F5',16,10))
print("""============
============""")
print(convert(161,10,16))
print(convert(501,10,16))
print(convert(2805,10,16))
print("""============
============""")
