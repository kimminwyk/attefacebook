import requests
try:
    line_txt = []
    url_string = {
        "facebook":"https://m.facebook.com/login/?ref=dbl&fl"
    }
    a = ""
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
    def attemptdata(url , userid, password,data_code):
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
        if data_code=="data":
            print(data)
        else:
            pass
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



    try:
        def file_name(url,filename):
            try:
                f= open(filename,"r")
                attempt_code = "[*] Login comparison failed"
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
                    data['email'] = i_d.strip("\n")
                    data['pass'] = password
                    data['form'] = 'login'
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
                except:
                    print("Error But I can't find any errors\nError content:" ,exec)
            except:
                print("Error But I can't find any errors\nError content:" ,exec)
    except TypeError:
        print("type error")
    except:
        print("Error But I can't find any errors\nError content:" ,exec)
    try:
        def file_namedata(url,filename,code_data):
            try:
                f= open(filename,"r")
                attempt_code = "[*] Login comparison failed"
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
                    data['email'] = i_d.strip("\n")
                    data['pass'] = password
                    data['form'] = 'login'
                    if code_data == "data":
                        print(data)
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
                    print("Error But I can't find any errors\nError content:" ,exec)
                return attempt_code
            except FileNotFoundError:
                print("There are no files Please check again")
            except UnboundLocalError:
                print("Error returned. Please check the file name and arguments again.")
    except ImportError:
        print("import error")

    except TypeError:
        print("type error")
    except:
        print("Error But I can't find any errors\nError content:" ,exec)
except ImportError:
    print("error: install requests....")
except NameError:
    print("A strange name...")