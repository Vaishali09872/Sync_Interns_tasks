from random import *
from tkinter import *
import  smtplib



def OTP():
    l=['1','2','3','4','5','6','7','8','9','0']
    otp=''
    for i in range(6):
        otp=otp+choice(l)
    msg='{} is your OTP'.format(otp)
    new_otp=otp

    def verification():
        if otp_value.get() == new_otp:
            l4=Label(root,text='verification successful')
            l4.pack()
            l4.pack()
            l4.config(font=('Helvetica bold', 16))
        else:
            l4 = Label(root, text='verification failed')
            l4.config(font=('Helvetica bold', 16))
    id=email_value.get()
    email = smtplib.SMTP('smtp.gmail.com', 587)
    email.starttls()
    email.login("teena081204@gmail.com", "jpmg fama onjs hmka")
    email.sendmail('&&&&&&&&&&&', id, msg)

    otp = Label(root, text="Enter your OTP")
    otp.pack()
    otp_value = StringVar()
    otp_entry = Entry(root, textvariable=otp_value)
    otp_entry.pack()
    Button(root, text='Submit', command=verification).pack()


root=Tk()
root.geometry('666x553')
root.title('OTP Verification')
title=Label(root,text='OTP Verification Program',bg='black',fg='white')
title.pack()
title.config(font=('Helvetica bold', 26))

email=Label(root,text='Enter your email ')
email.pack()

email_value=StringVar()

email_entry=Entry(root,textvariable=email_value)
email_entry.pack()

Button(root,text="Generate OTP ",command=OTP).pack()


root.mainloop()