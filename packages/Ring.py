import itertools
import sympy as sp
from tkinter import *
import Group
def is_ring(tset,opr1,opr2,mod1=1,mod2=1):
    if(Group.is_group(tset,opr1,mod1)&Group.commutative(tset, opr1, mod1)):
        if(Group.is_nested_list(tset)):
            m=[]
            for i in range(0,len(tset)):
                m.append(sp.Matrix(tset[i]))
            for i in range(0,len(m)):
                for j in range(0,len(m)):
                    for k in range(0,len(m)):
                        if(mod1<=1&mod2<=1):
                            v1=m[i]*(m[j]*m[k])
                            v2=(m[i]*m[j])*m[k]
                            v3=m[i]*(m[j]+m[k])
                            v4=m[i]*m[j]+m[i]*m[k]
                            v5=(m[j]+m[k])*m[i]
                            v6=m[j]*m[i]+m[k]*m[i]
                            if(v1!=v2 | v3!=v4 | v5!=v6):
                                return 0
                        elif(mod1<=1&mod2>1):
                            v1=sp.Mod(m[j]*m[k],mod2)
                            v1=sp.Mod(m[i]*v1,mod2)
                            v2=sp.Mod(m[i]*m[j],mod2)
                            v2=sp.Mod(v2*m[k],mod2)
                            v3=sp.Mod(m[i]*(m[j]+m[k]),mod2)
                            v4=sp.Mod(m[i]*m[j],mod2)+sp.Mod(m[i]*m[k],mod2)
                            v5=sp.Mod((m[j]+m[k])*m[i],mod2)
                            v6=sp.Mod(m[j]*m[i],mod2)+sp.Mod(m[k]*m[i],mod2)
                            if(v1!=v2 | v3!=v4 | v5!=v6):
                                return 0
                        elif(mod2<=1&mod1>1):
                            v1=m[i]*(m[j]*m[k])
                            v2=(m[i]*m[j])*m[k]
                            v3=sp.Mod((m[j]+m[k]),mod1)
                            v3=m[i]*v3
                            v4=sp.Mod(m[i]*m[j]+m[i]*m[k],mod1)
                            v5=sp.Mod((m[j]+m[k]),mod1)
                            v5=v5*m[i]
                            v6=sp.Mod(m[j]*m[i]+m[k]*m[i],mod1)
                            if(v1!=v2 | v3!=v4 | v5!=v6):
                                return 0
                        elif(mod1>1&mod2>1):
                            v1=sp.Mod(m[j]*m[k],mod2)
                            v1=sp.Mod(m[i]*v1,mod2)
                            v2=sp.Mod(m[i]*m[j],mod2)
                            v2=sp.Mod(v2*m[k],mod2)
                            v3=sp.Mod((m[j]+m[k]),mod1)
                            v3=sp.Mod(m[i]*v3,mod2)
                            v4=sp.Mod((sp.Mod(m[i]*m[j],mod2)+sp.Mod(m[i]*m[k],mod2)),mod1)
                            v5=sp.Mod((m[j]+m[k]),mod1)
                            v5=sp.Mod(v5*m[i],mod2)
                            v6=sp.Mod((sp.Mod(m[j]*m[i],mod2)+sp.Mod(m[k]*m[i],mod2)),mod1)
                            if(v1!=v2 | v3!=v4 | v5!=v6):
                                return 0
            return 1
        else:
            for i in range(0,len(tset)):
                for j in range(0,len(tset)):
                    for k in range(0,len(tset)):
                        if(mod1<=1&mod2<=1):
                            v1=tset[i]*(tset[j]*tset[k])
                            v2=(tset[i]*tset[j])*tset[k]
                            v3=tset[i]*(tset[j]+tset[k])
                            v4=tset[i]*tset[j]+tset[i]*tset[k]
                            v5=(tset[j]+tset[k])*tset[i]
                            v6=tset[j]*tset[i]+tset[k]*tset[i]
                            if(v1!=v2 | v3!=v4 | v5!=v6):
                                return 0
                        elif(mod1<=1&mod2>1):
                            v1=(tset[j]*tset[k])%mod2
                            v1=(tset[i]*v1)%mod2
                            v2=(tset[i]*tset[j])%mod2
                            v2=(v2*tset[k])%mod2
                            v3=(tset[i]*(tset[j]+tset[k]))%mod2
                            v4=((tset[i]*tset[j])%mod2)+((tset[i]*tset[k])%mod2)
                            v5=((tset[j]+tset[k])*tset[i])%mod2
                            v6=((tset[j]*tset[i])%mod2)+((tset[k]*tset[i])%mod2)
                            if(v1!=v2 | v3!=v4 | v5!=v6):
                                return 0
                        elif(mod2<=1&mod1>1):
                            v1=tset[i]*(tset[j]*tset[k])
                            v2=(tset[i]*tset[j])*tset[k]
                            v3=(tset[j]+tset[k])%mod1
                            v3=tset[i]*v3
                            v4=(tset[i]*tset[j]+tset[i]*tset[k])%mod1
                            v5=(tset[j]+tset[k])%mod1
                            v5=v5*tset[i]
                            v6=(tset[j]*tset[i]+tset[k]*tset[i])%mod1
                            if(v1!=v2 | v3!=v4 | v5!=v6):
                                return 0
                        elif(mod1>1&mod2>1):
                            v1=(tset[j]*tset[k])%mod2
                            v1=(tset[i]*v1)%mod2
                            v2=(tset[i]*tset[j])%mod2
                            v2=(v2*tset[k])%mod2
                            v3=(tset[j]+tset[k])%mod1
                            v3=(tset[i]*v3)%mod2
                            v4=(((tset[i]*tset[j])%mod2)+((tset[i]*tset[k])%mod2))%mod1
                            v5=(tset[j]+tset[k])%mod1
                            v5=(v5*tset[i])%mod2
                            v6(((tset[j]*tset[i])%mod2)+((tset[k]*tset[i])%mod2))%mod1
                            if(v1!=v2 | v3!=v4 | v5!=v6):
                                return 0
            return 1
    else:
        return 0
def comm_ring(tset,opr1,opr2,mod1=1,mod2=1):
    if(is_ring(tset, opr1, opr2,mod1,mod2)):
        if(Group.is_nested_list(tset)):
            m=[]
            for i in range(0,len(tset)):
                m.append(sp.Matrix(tset[i]))
            for i in range(0,len(m)):
                for j in range(0,len(m)):
                    if(mod2<=1):
                        v1=m[i]*m[j]
                        v2=m[j]*m[i]
                        if(v1!=v2):
                            return 0
                    else:
                        v1=sp.Mod((m[i]*m[j]),mod2)
                        v2=sp.Mod((m[j]*m[i]),mod2)
                        if(v1!=v2):
                            return 0
            return 1
        else:
            for i in range(0,len(tset)):
                for j in range(0,len(tset)):
                    if(mod2<=1):
                        v1=tset[i]*tset[j]
                        v2=tset[j]*tset[i]
                        if(v1!=v2):
                            return 0
                    else:
                        v1=(tset[i]*tset[j])%mod2
                        v2=(tset[j]*tset[i])%mod2
                        if(v1!=v2):
                            return 0
            return 1
    else:
        return 0
def unity(tset,opr1,opr2,mod1=1,mod2=1):
    if(is_ring(tset, opr1, opr2,mod1,mod2)):
        if(Group.is_nested_list(tset)):
            m=[]
            for i in range(0,len(tset)):
                m.append(sp.Matrix(tset[i]))
            count=0
            for i in range(0,len(m)):
                for j in range(0,len(m)):
                    if(mod2<=1):
                        v1=m[i]*m[j]
                        if(v1==m[j]):
                            count+=1
                            if(count==len(m)):
                                return m[i]
                    else:
                        v1=m[i]*m[j]
                        v1=sp.Mod(v1,mod2)
                        if(v1==m[j]):
                            count+=1
                            if(count==len(m)):
                                return m[i]
            return
        else:
            count=0
            for i in range(0,len(tset)):
                for j in range(0,len(tset)):
                    if(mod2<=1):
                        v1=tset[i]*tset[j]
                        if(v1==tset[j]):
                            count+=1
                            if(count==len(tset)):
                                return tset[i]
                    else:
                        v1=tset[i]*tset[j]
                        v1=v1%mod2
                        if(v1==tset[j]):
                            count+=1
                            if(count==len(tset)):
                                return tset[i]
            return
    else:
        return
def units(tset,opr1,opr2,uni,mod1=1,mod2=1):
    if(is_ring(tset, opr1, opr2,mod1,mod2)):
        if(Group.is_nested_list(tset)):
            unit=[]
            m=[]
            for i in range(0,len(tset)):
                m.append(sp.Matrix(tset[i]))
            for i in range(0,len(m)):
                for j in range(0,len(m)):
                    if(mod2<=1):
                        v1=m[i]*m[j]
                        if(v1==sp.Matrix(uni)):
                            temp=m[i].tolist()
                            unit.append(temp)
                    else:
                        v1=m[i]*m[j]
                        v1=sp.Mod(v1,mod2)
                        if(v1==sp.Matrix(uni)):
                            temp=m[i].tolist()
                            unit.append(temp)
            return unit
        else:
            unit=[]
            for i in range(0,len(tset)):
                for j in range(0,len(tset)):
                    if(mod2<=1):
                        v1=tset[i]*tset[j]
                        if(v1==uni):
                            unit.append(tset[i])
                    else:
                        v1=tset[i]*tset[j]
                        v1=v1%mod2
                        if(v1==uni):
                            unit.append(tset[i])
            return unit
    else:
        return []
def zero_divisor(tset,opr1,opr2,mod1=1,mod2=1):
    if(is_ring(tset, opr1, opr2,mod1,mod2)):
        if(Group.is_nested_list(tset)):
            zd=[]
            m=[]
            for i in range(0,len(tset)):
                m.append(sp.Matrix(tset[i]))
            for i in range(0,len(m)):
                for j in range(0,len(m)):
                    if(mod2<=1):
                        v1=m[i]*m[j]
                        v2=m[j]*m[i]
                        if(v1==0|v2==0):
                            temp=m[i].tolist()
                            zd.append(temp)
                    else:
                       v1=m[i]*m[j]
                       v1=sp.Mod(v1,mod2)
                       v2=m[j]*m[i]
                       v2=sp.Mod(v2,mod2)
                       if(v1==0|v2==0):
                           temp=m[i].tolist()
                           zd.append(temp)
            return zd
        else:
            zd=[]
            for i in range(0,len(tset)):
                for j in range(0,len(tset)):
                    if(mod2<=1):
                        v1=tset[i]*tset[j]
                        v2=tset[j]*tset[i]
                        if(v1==0|v2==0):
                            zd.append(tset[i])
                    else:
                        v1=tset[i]*tset[j]
                        v1=v1%mod2
                        v2=tset[j]*tset[i]
                        v2=v2%mod2
                        if(v1==0|v2==0):
                            zd.append(tset[i])
            return zd
    else:
        return []
def subring(tset,opr1,opr2,mod1=1,mod2=1):
    subr=[]
    if(is_ring(tset, opr1, opr2,mod1,mod2)):
        tsr=[]
        for i in range(1,len(tset)+1):
            tsr+=list(itertools.combinations(tset,i))
        for i in range(0,len(tsr)):
            if(is_ring(tsr[i], opr1, opr2,mod1,mod2)):
                subr.append(tsr[i])
        print(subr)
        return subr
def ideal(tset,opr1,opr2,sr,mod1=1,mod2=1):
    idl=[]
    if(is_ring(tset, opr1, opr2,mod1,mod2)):
        if(Group.is_nested_list(tset)):
            m=[]
            for i in range(0,len(tset)):
                m.append(sp.Matrix(tset[i]))
            for i in range(0,len(sr)):
                for j in range(0,len(sr[i])):
                    tsr=[]
                    tsr.append(sp.Matrix(sr[i]))
                    for s in range(0,len(m)):
                        count=0
                        for t in range(0,len(tsr)):
                            if(mod2<=1):
                                v1=m[s]*tsr[t]
                                v2=tsr[t]*m[s]
                                if(v1==v2 & v1 in m & v2 in m):
                                    count+=1
                                    if(count==len(m)):
                                        idl.append(tsr.tolist())
                            else:
                                v1=m[s]*tsr[t]
                                v1=sp.Mod(v1,mod2)
                                v2=tsr[t]*m[s]
                                v2=sp.Mod(v2,mod2)
                                if(v1==v2 & v1 in m & v2 in m):
                                    count+=1
                                    if(count==len(m)):
                                        idl.append(tsr.tolist())
            return idl
        else:
            for f in range(0,len(tset)):
                for i in range(0,len(sr)):
                    count=0
                    for j in range(0,len(sr[i])):
                        if(mod2<=1):
                           v1=tset[f]*sr[i][j]
                           v2=sr[i][j]*tset[f]
                           if(v1==v2 & v1 in tset & v2 in m):
                               count+=1
                               if(count==len(m)):
                                   idl.append(sr)
                        else:
                            v1=tset[f]*sr[i][j]
                            v1=v1%mod2
                            v2=sr[i][j]*tset[f]
                            v2=v2%mod2
                            if(v1==v2 & v1 in tset & v2 in m):
                                count+=1
                                if(count==len(m)):
                                    idl.append(sr)
            return idl
def ringabout(tset,op1,op2,mod1,mod2):
    rg=is_ring(tset, op1, op2,mod1,mod2)
    comm=comm_ring(tset, op1, op2,mod1,mod2)
    uty=unity(tset, op1, op2,mod1,mod2)    
    uni=units(tset, op1, op2, uty)
    zd=zero_divisor(tset, op1, op2,mod1,mod2)
    sbr=subring(tset, op1, op2,mod1,mod2)
    abt=Tk()
    abt.geometry("900x900")
    if(rg==1):
        Label(abt,text="It is a Ring").place(x=10,y=30)
    else:
        Label(abt,text="It is a Not Ring").place(x=10,y=30)
    if(comm==1):
        Label(abt,text="Commutative:Yes").place(x=10,y=60)
    else:
        Label(abt,text="Commutative:No").place(x=10,y=60)
    if(uty!=None):
        s="Unity:"+str(uty)
        Label(abt,text=s).place(x=10,y=90)
    else:
        Label(abt,text="No Unity").place(x=10,y=90)
    if(len(uni)!=0):
        s="Units:"+str(uni)
        Label(abt,text=s).place(x=10,y=120)
    else:
        Label(abt,text="No Units").place(x=10,y=120)
    if(len(zd)!=0):
        s="Zero Divisors:"+str(zd)
        Label(abt,text=s).place(x=10,y=150)
    else:
        Label(abt,text="No Zero Divisors").place(x=10,y=150)
    if(len(sbr)!=0):
        s="Subrings:"+str(sbr)
        Label(abt,text=s).place(x=10,y=180)
    else:
        Label(abt,text="No Subrings").place(x=10,y=180)
    abt.mainloop()