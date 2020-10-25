# attefacebook 1.0

### attefacebook module example
 
 
 attefacebook에 사용되는 module

__os__
__requests__
 
* * *

#### attefacebook 사용 예시
```py
from attefacebook import *

print(attempt('user id','user password'))
# attempt(uid : str, upw : str) -> str:
# 반환 -> type str

readattempt('.txt file action')
# readattempt(FileName : str) -> list
# 반환 -> type list
```

### attempt

attempt 함수는 requests 모듈을 사용하여

facebook login 페이지에 요청을 합니다.
 
### readattempt

readattempt 함수는 os 모듈을 이용하여 파일 위치를 인자로 받고

attempt 함수를 호출합니다.

file text 형식은 

예)
```
(user id) (user password)
hello@naver.com asdf1234
adnub@gmail.com qwe123
```

파일을 읽고 띄어쓰기로 아이디 비밀번호 구별합니다.

