import random
username_formula={}
# filling the user credentials (i.e username and respective formulas) from txt file to the above dictionary 
try:
    qw=open('usernameformula.txt')
    for df in qw:
        zz,xx=df.split(':')
        username_formula[zz]=xx.strip('\n')
    qw.close()
except:
    pass
kl=list(username_formula.keys())




while True:
    print(f'''{'============================================================'*2} \n \n1) User Registeration\n2) User Sign-in\n3) Exit\n''')

    homeinput =(input("Input the no. accordingly :"))
    homeinput =int(homeinput)
    
    # User registeration code
    if homeinput == 1:
        
        username =input('input the email-id as username :')
        if len(username)>30:
            print('\nError : you have exceeded the limit of character length of username')
            continue
        if username in kl:
            
            print('\nthis email as username is already registered')
            continue
        
                
        try:        
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            import random
            
            m= str(random.randrange(1000,10000))
            print(m)
            mail_content = 'your OTP is '+ m
            #The mail addresses and password
            sender_address = 'xyz@xyz.com'
            sender_pass = 'etyciuwxkihamzcz'
            receiver_address = username
            #Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
            #The body and the attachments for the mail
            message.attach(MIMEText(mail_content, 'plain'))
            #Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(sender_address, sender_pass) #login with mail_id and password
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
        except:
            print('\nError : some error has occured while sending otp to email')
            continue    
        
        k=(input('enter OTP which has been sent to your email : '))
                                    
        if k==m :
            while True:
                formula =input('''\n\n(instructions for formula generation :\n\n1) u can use +,-,*,/ & ** arithmatical operators only\n2) max & min character length of the formula should be 30 & 10 respectively\n3) u can create a formula with only 4 variables (i.e a,b,c & d) & only positive integers are allowed as arithmetic constants in an mathematical expression \n4) put all the raw strings outside the {} & operational/processing stuffs inside the {} \n\n eg : {a*3}tonny{bc+d}mk )\n\n input the formula : ''')
                if len(formula)>30:
                    print('\nError : you have exceeded the limit of character length of formula ')
                    continue
                
                #fitting a user input formula into the formatted string format
                s = '''f\"'''
                e = '''\"'''
                formula = s+formula+e
                def formula_check(a=1,b=2,c=3,d=4):
                    value=eval(formula)
                    return value

                verify_value=formula_check()
                print(f'\nverify the formula value evaluated by the program for otp(1234) matches the value calculated by you\n\nyour formula value : {verify_value}')

                formul=int(input("\ntype '1' if formula value calculated by program matches the value calculated by you & type '0' if not and you want to reset the formula : "))
                
                if formul==1:
                    userformula_write=open('usernameformula.txt','a')
                    userformula_write.write(f"{username}:{formula}\n")
                    userformula_write.close()
                    print('\nyou have successfully registered')
                    break
                elif formul == 0:
                    continue
                else:
                    print('\nError : invalid input')

        

            
        elif k!=m :
            print("\nError : invalid otp")

    # user login code
    elif homeinput == 2:
        
        def formula_pin():
            a=str(random.randrange(1,10))
            b=str(random.randrange(1,10))
            c=str(random.randrange(1,10))
            d=str(random.randrange(1,10))
            e=a+b+c+d
            return e
        while True:
            xc=input('\nenter your registered email-id as username : ')
                
            if xc in kl :
                otp=(formula_pin())
                
                a=int(otp[0])
                b=int(otp[1])
                d=int(otp[3])
                c=int(otp[2])
                
                userformu=username_formula[xc]
                forvalue=eval(userformu)
                print(f'OTP : {otp}')
                form_val_input=input('enter your formula value : ')
                if form_val_input == forvalue :
                    print('\nyou have successfully logged in to your account')
                    break
                elif form_val_input != forvalue :
                    print('\nError : you have entered wrong formula value')
                    continue
            
            if xc not in kl:
                print("\nError : this email-id is not registered as username")
                continue


        
    elif homeinput == 3:    
        exit()

    else:
        print('\nError : entered input is invalid')


