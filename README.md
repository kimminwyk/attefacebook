# attefacebook
2020-06-14
attefacebook 1.0 version

This module is a module for making facebook login request easy.

How to use the module

1. attempt("facebook", your facebook email, your facebook password)

2.file_name("facebook,filename,"data") "data" <- Output of transmitted data

                         ↑
                         
                       file 
                       
              file Contents 
              
             ****************
             
             id:you email
              
             pw:you password
              
             Example explanation ↓
              
             ****************
             
             id:hello@naver.com
             
             pw:world
            
def attempt()

How to use

import attefacebook

a = attefacebook.attempt("facebook", your facebook email, your facebook password)

print(a)

↑

Whether the login was successful or failed


def file_name()

How to use

import attefacebook

a =file_name("facebook",filename,"data")

print(a)

↑

Whether the login was successful or failed


 ####################################################################################

# attefacebook
2020-06-14
attefacebook 1.1 version
Modified things
-Add and modify exception handling
-# """ """ remove
url only supports facebook
                     ↓
attefacebook.attempt(url , useremail, userpassword)
                         ↓
attefacebook.attemptdata(url , useremail, userpassword,"data")
                        ↓
attefacebook.file_name(url,filename)
                           ↓
attefacebook.file_namedata(url,filename,"data")
 
 
 ####################################################################################
 
 
 
 
 
 
 
 
 
 
