from time import time #line:3
from hashlib import md5 #line:4
from copy import deepcopy #line:5
from urllib .parse import urlparse #line:6
from urllib .parse import parse_qs #line:7
from urllib .parse import urlencode #line:8
import requests #line:9
import json #line:10
from flask import Flask #line:11
from flask import request #line:12
import base64 #line:13
app =Flask (__name__ )#line:15
class XGorgon :#line:18
    def encryption (OOO00OO00000OO0OO ):#line:19
        OO0OO00OO0O0O0O0O =''#line:20
        OO0OO000O00O00OO0 =[]#line:21
        for OO00O000OOO0OOOOO in range (0 ,256 ):#line:22
            OO0OO000O00O00OO0 .append (OO00O000OOO0OOOOO )#line:23
        for OO00O000OOO0OOOOO in range (0 ,256 ):#line:24
            if OO00O000OOO0OOOOO ==0 :#line:25
                OOOO00O00OOOOOO00 =0 #line:26
            elif OO0OO00OO0O0O0O0O :#line:27
                OOOO00O00OOOOOO00 =OO0OO00OO0O0O0O0O #line:28
            else :#line:29
                OOOO00O00OOOOOO00 =OO0OO000O00O00OO0 [OO00O000OOO0OOOOO -1 ]#line:30
            O0000O0O0O0O0OO00 =OOO00OO00000OO0OO .hex_str [OO00O000OOO0OOOOO %8 ]#line:31
            if OOOO00O00OOOOOO00 ==85 :#line:32
                if OO00O000OOO0OOOOO !=1 :#line:33
                    if OO0OO00OO0O0O0O0O !=85 :#line:34
                        OOOO00O00OOOOOO00 =0 #line:35
            OOO00OO0OOO0O0O0O =OOOO00O00OOOOOO00 +OO00O000OOO0OOOOO +O0000O0O0O0O0OO00 #line:36
            while OOO00OO0OOO0O0O0O >=256 :#line:37
                OOO00OO0OOO0O0O0O =OOO00OO0OOO0O0O0O -256 #line:38
            if OOO00OO0OOO0O0O0O <OO00O000OOO0OOOOO :#line:39
                OO0OO00OO0O0O0O0O =OOO00OO0OOO0O0O0O #line:40
            else :#line:41
                OO0OO00OO0O0O0O0O =''#line:42
            OOO0O00O0O000O00O =OO0OO000O00O00OO0 [OOO00OO0OOO0O0O0O ]#line:43
            OO0OO000O00O00OO0 [OO00O000OOO0OOOOO ]=OOO0O00O0O000O00O #line:44
        return OO0OO000O00O00OO0 #line:45
    def initialize (OO00000OOOOOO0O0O ,O00OOOOOO00OOOO00 ,O0O00O000O000OOO0 ):#line:47
        O0O0O0O0OO0000O0O =[]#line:48
        O0O00000OOOO00OOO =deepcopy (O0O00O000O000OOO0 )#line:49
        for O00O00O0OOOOO000O in range (OO00000OOOOOO0O0O .length ):#line:50
            O0OO00OO0OO0OO0OO =O00OOOOOO00OOOO00 [O00O00O0OOOOO000O ]#line:51
            if not O0O0O0O0OO0000O0O :#line:52
                OOO0O00OO0O0O000O =0 #line:53
            else :#line:54
                OOO0O00OO0O0O000O =O0O0O0O0OO0000O0O [-1 ]#line:55
            OO00000000OO00O00 =O0O00O000O000OOO0 [O00O00O0OOOOO000O +1 ]+OOO0O00OO0O0O000O #line:56
            while OO00000000OO00O00 >=256 :#line:57
                OO00000000OO00O00 =OO00000000OO00O00 -256 #line:58
            O0O0O0O0OO0000O0O .append (OO00000000OO00O00 )#line:59
            O00OO0OOO000O000O =O0O00000OOOO00OOO [OO00000000OO00O00 ]#line:60
            O0O00000OOOO00OOO [O00O00O0OOOOO000O +1 ]=O00OO0OOO000O000O #line:61
            O0OO00O00O0OO000O =O00OO0OOO000O000O +O00OO0OOO000O000O #line:62
            while O0OO00O00O0OO000O >=256 :#line:63
                O0OO00O00O0OO000O =O0OO00O00O0OO000O -256 #line:64
            O00OOOO000OO00OO0 =O0O00000OOOO00OOO [O0OO00O00O0OO000O ]#line:65
            O000OOO0O0O0OOOOO =O0OO00OO0OO0OO0OO ^O00OOOO000OO00OO0 #line:66
            O00OOOOOO00OOOO00 [O00O00O0OOOOO000O ]=O000OOO0O0O0OOOOO #line:67
        return O00OOOOOO00OOOO00 #line:68
    def handle (O000OOOO00OO00000 ,O00OOOOO00O00O000 ):#line:70
        for O0OO00OOO000OOO00 in range (O000OOOO00OO00000 .length ):#line:71
            OO00O0OOO0OO000O0 =O00OOOOO00O00O000 [O0OO00OOO000OOO00 ]#line:72
            O00OOOOOOO00000O0 =choice (OO00O0OOO0OO000O0 )#line:73
            OO0OO0O00OOO000O0 =O00OOOOO00O00O000 [(O0OO00OOO000OOO00 +1 )%O000OOOO00OO00000 .length ]#line:74
            OO0O000O000000OOO =O00OOOOOOO00000O0 ^OO0OO0O00OOO000O0 #line:75
            O0OOOOO0OO000O0OO =rbpt (OO0O000O000000OOO )#line:76
            OOO0O000O0O0O0O00 =O0OOOOO0OO000O0OO ^O000OOOO00OO00000 .length #line:77
            O0OO0000OOOO0OOOO =~OOO0O000O0O0O0O00 #line:78
            while O0OO0000OOOO0OOOO <0 :#line:79
                O0OO0000OOOO0OOOO +=4294967296 #line:80
            O0000000OO00OOO0O =int (hex (O0OO0000OOOO0OOOO )[-2 :],16 )#line:81
            O00OOOOO00O00O000 [O0OO00OOO000OOO00 ]=O0000000OO00OOO0O #line:82
        return O00OOOOO00O00O000 #line:83
    def main (O0O00OO0OOOOOO00O ):#line:85
        O0000OOOO0O000O0O =''#line:86
        for O0OO0O00O0000O0O0 in O0O00OO0OOOOOO00O .handle (O0O00OO0OOOOOO00O .initialize (O0O00OO0OOOOOO00O .debug ,O0O00OO0OOOOOO00O .encryption ())):#line:87
            O0000OOOO0O000O0O =O0000OOOO0O000O0O +hex2string (O0OO0O00O0000O0O0 )#line:88
        O00OO00OO0O0O00OO =hex2string (O0O00OO0OOOOOO00O .hex_str [7 ])#line:90
        OOO000O0O00OO000O =hex2string (O0O00OO0OOOOOO00O .hex_str [3 ])#line:91
        return '0404{}{}0001{}'.format (O00OO00OO0O0O00OO ,OOO000O0O00OO000O ,O0000OOOO0O000O0O )#line:92
    def __init__ (OOO00OOOOO00OO000 ,OO000OO00O0000O0O ):#line:94
        OOO00OOOOO00OO000 .length =20 #line:95
        OOO00OOOOO00OO000 .debug =OO000OO00O0000O0O #line:96
        OOO00OOOOO00OO000 .hex_str =[30 ,0 ,224 ,228 ,147 ,69 ,1 ,208 ]#line:97
def choice (OO0OO0O00000O00OO ):#line:100
    OOO000OOOOOOO0OO0 =hex (OO0OO0O00000O00OO )[2 :]#line:101
    if len (OOO000OOOOOOO0OO0 )<2 :#line:102
        OOO000OOOOOOO0OO0 ='0'+OOO000OOOOOOO0OO0 #line:103
    return int (OOO000OOOOOOO0OO0 [1 :]+OOO000OOOOOOO0OO0 [:1 ],16 )#line:104
def rbpt (O00O0O0OOO0OO000O ):#line:107
    OOO0OO00OO0000O0O =''#line:108
    O00O0O000OO0OOOOO =bin (O00O0O0OOO0OO000O )[2 :]#line:109
    while len (O00O0O000OO0OOOOO )<8 :#line:110
        O00O0O000OO0OOOOO ='0'+O00O0O000OO0OOOOO #line:111
    for OOO0OOO0OO00O000O in range (0 ,8 ):#line:112
        OOO0OO00OO0000O0O =OOO0OO00OO0000O0O +O00O0O000OO0OOOOO [7 -OOO0OOO0OO00O000O ]#line:113
    return int (OOO0OO00OO0000O0O ,2 )#line:114
def hex2string (OOOOOO00O0O00000O ):#line:117
    OO00OO00OOO0O0O0O =hex (OOOOOO00O0O00000O )[2 :]#line:118
    if len (OO00OO00OOO0O0O0O )<2 :#line:119
        OO00OO00OOO0O0O0O ='0'+OO00OO00OOO0O0O0O #line:120
    return OO00OO00OOO0O0O0O #line:121
@app .route ('/sign',methods =['get'])#line:123
def X_Gorgon0404 ():#line:124
    OO00O0000OOO0OO0O =str (base64 .b64decode (request .args .get ('url')),"utf-8")#line:125
    print (OO00O0000OOO0OO0O )#line:126
    OO00O0000OOO0OO0O =splitParams (OO00O0000OOO0OO0O )#line:127
    OO00OO00O0OOOOO00 =request .args .get ('data')#line:128
    print (OO00OO00O0OOOOO00 )#line:129
    O0O0OOO0OOO0OO0O0 ='' #str (base64 .b64decode (request .args .get ('cookie')),"utf-8")#line:130
    print (O0O0OOO0OOO0OO0O0 )#line:131
    O0O0OO000OOOOO0O0 ='utf-8'#line:132
    OO00O0OO0O0O0O0OO =[]#line:134
    OO00000OO0OO00OO0 =hex (int (time ()))[2 :]#line:135
    OOOOO0O0OO000O000 =md5 (bytearray (OO00O0000OOO0OO0O ,'utf-8')).hexdigest ()#line:136
    for O0OOOOOOO00O000O0 in range (0 ,4 ):#line:137
        OO00O0OO0O0O0O0OO .append (int (OOOOO0O0OO000O000 [2 *O0OOOOOOO00O000O0 :2 *O0OOOOOOO00O000O0 +2 ],16 ))#line:138
    if OO00OO00O0OOOOO00 :#line:139
        if O0O0OO000OOOOO0O0 =='utf-8':#line:140
            OOO0OO00O0OO0000O =md5 (bytearray (OO00OO00O0OOOOO00 ,'utf-8')).hexdigest ()#line:141
            for O0OOOOOOO00O000O0 in range (0 ,4 ):#line:142
                OO00O0OO0O0O0O0OO .append (int (OOO0OO00O0OO0000O [2 *O0OOOOOOO00O000O0 :2 *O0OOOOOOO00O000O0 +2 ],16 ))#line:143
        elif O0O0OO000OOOOO0O0 =='octet':#line:144
            OOO0OO00O0OO0000O =md5 (OO00OO00O0OOOOO00 ).hexdigest ()#line:145
            for O0OOOOOOO00O000O0 in range (0 ,4 ):#line:146
                OO00O0OO0O0O0O0OO .append (int (OOO0OO00O0OO0000O [2 *O0OOOOOOO00O000O0 :2 *O0OOOOOOO00O000O0 +2 ],16 ))#line:147
    else :#line:148
        for O0OOOOOOO00O000O0 in range (0 ,4 ):#line:149
            OO00O0OO0O0O0O0OO .append (0 )#line:150
    if O0O0OOO0OOO0OO0O0 :#line:151
        OOOOO000OO0O0O0OO =md5 (bytearray (O0O0OOO0OOO0OO0O0 ,'utf-8')).hexdigest ()#line:152
        for O0OOOOOOO00O000O0 in range (0 ,4 ):#line:153
            OO00O0OO0O0O0O0OO .append (int (OOOOO000OO0O0O0OO [2 *O0OOOOOOO00O000O0 :2 *O0OOOOOOO00O000O0 +2 ],16 ))#line:154
    else :#line:155
        for O0OOOOOOO00O000O0 in range (0 ,4 ):#line:156
            OO00O0OO0O0O0O0OO .append (0 )#line:157
    for O0OOOOOOO00O000O0 in range (0 ,4 ):#line:158
        OO00O0OO0O0O0O0OO .append (0 )#line:159
    for O0OOOOOOO00O000O0 in range (0 ,4 ):#line:160
        OO00O0OO0O0O0O0OO .append (int (OO00000OO0OO00OO0 [2 *O0OOOOOOO00O000O0 :2 *O0OOOOOOO00O000O0 +2 ],16 ))#line:161
    return {'xgorgon':XGorgon0404 (OO00O0OO0O0O0O0OO ).main (),'ts':str (int (OO00000OO0OO00OO0 ,16 ))}#line:162

