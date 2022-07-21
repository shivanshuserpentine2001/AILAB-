def gp(x):
    if x =='S':
        return 10
        return
    elif x=='A':
        return 9
        return
    elif x == 'B':
        return 8
        return
    elif x == 'C':
        return 7
        return
    elif x == 'D':
        return 6
        return
    elif x == 'E':
        return 4
        return
    else:
        return 0

mlmarks=input("ENTER MACHINE LEARNING GP GRADE:")
mlgp=gp(mlmarks)
print(mlgp)
bdamarks=input("ENTER BIG DATA ANALYSTICS GP GRADE:")
bdagp=gp(bdamarks)
print(bdagp)
memarks=input("ENTER MANAGEMENT AND ENTREPRE. GRADE:")
memgp=gp(memarks)
print(memgp)
cnsmarks=input("ENTER CRYPTOGRAPHY AND NETWORK SECURITY GRADE:")
cnsgp=gp(cnsmarks)
print(cnsgp)
opemarks=input("ENTER OPEN ELECTIVE GRADE:")
opegp=gp(opemarks)
print(opegp)
pwmarks=input("ENTER PROJECT WORK-4 GRADE:")
pwgp=gp(pwmarks)
print(pwgp)
oomdmarks=input("ENTER OOMD GRADE:")
oomdgp=gp(oomdmarks)
print(oomdgp)
moocmarks=input("ENTER MOOC/INTERNS GRADE:")
moocgp=gp(moocmarks)
print(moocgp)
sgpa=(mlgp*4+oomdgp*4+cnsgp*4+bdagp*4+memgp*3+opegp*3+moocgp*1+pwgp*2)/25
print("CONGRATULATIONS ON GETTING:"+str(sgpa))
cgpatillnow=float(input("CGPA TILL NOW"))
cgpapost6thsem=(cgpatillnow*116+(sgpa*25))/141
print("CONGRATULATIONS UR NEW CGPA IS ",round(cgpapost6thsem,2))