import requests
try:
    line_txt = []
    url_string = {
        "facebook":"https://m.facebook.com/login/?ref=dbl&fl"
    }
    """ help """
    def help():    
        print("""
        <<< help >>>
        userid userpw 만 입력할경우는 
        attempt(id , pw)

        file txt 로 하는경우는
        txt = 
        id:(you id)
        pw:(you pw)
        ↑
        () 는 제거 공백없이
        attelogin.file_name("filename" , "data") <- data 는 무슨 데이터가 들어가는지 알고싶을때만
        예 :
        {'lsd': 'lsd', 'charset_test': 'csettest', 'version': 'version', 'ajax': 'ajax', 'width': 'width', 'pxr': 'pxr', 'gps': 'gps', 'm_ts': 'mts', 'li': 'li',
         'email': 'you id@email', 'pass': 'you pw', 'form': 'login'}
        """)
    a = ""
    """ attempt() Select"""
    attempt_code = "[*] Login comparison failed"
    def attempt(url , userid, password):
        data = {
            'lsd': 'lsd',
            'charset_test': 'csettest',
            'version': 'version',
            'ajax': 'ajax',
            'width': 'width',
            'pxr': 'pxr',
            'gps': 'gps',
            'm_ts': 'mts',
            'li': 'li',
                }
        data['email'] = userid.strip("\n")
        data['pass'] = password
        data['form'] = 'login'
        #print(data)
        try:
            s = requests.Session()
            r = s.post(url_string[url], data=data)
            if r.text.find("로그아웃") > 0:
                attempt_code = "[+] user existence"
            else:
                attempt_code = "[-] user none"
        except ImportError:
            print("import error")

        return attempt_code



    """ file_name() Select"""
    def file_name(url,filename,code_data):
        f= open(filename,"r")
        attempt_code = "[*] Login comparison failed" #reset
        try:
            while True:
                lien = f.readline()
                if not lien: 
                    break
                line_txt.append(lien)
            id_password = []
            for i in line_txt:
                id_password.append(i[3:])
            i_d = id_password[0]
            password = id_password[1]
            f.close()
            #facebook login form data
            data = {
                    'lsd': 'lsd',
                    'charset_test': 'csettest',
                    'version': 'version',
                    'ajax': 'ajax',
                    'width': 'width',
                    'pxr': 'pxr',
                    'gps': 'gps',
                    'm_ts': 'mts',
                    'li': 'li',
                    }
            # facebook.com login
            data['email'] = i_d.strip("\n")
            data['pass'] = password
            data['form'] = 'login'
            if code_data == "data":
                print(data)
            else:
                try:
                    s = requests.Session()
                    r = s.post(url_string[url], data=data)
                    if r.text.find("로그아웃") > 0:
                        attempt_code = "[+] user existence"
                    else:
                        attempt_code = "[-] user none"
                except ImportError:
                    print("import error")
        except:
            print("error",exec)
        return attempt_code
except ImportError:
    print("error: install requests....")
except NameError:
    print("A strange name...")