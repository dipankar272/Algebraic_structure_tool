import operator
import itertools
import sympy as sp
ops = {'+' : operator.add,'-' : operator.sub,'*' : operator.mul,'/' : operator.truediv,'%' : operator.mod,'^' : operator.xor}
def is_nested_list(list1):
    for item in list1:
        if isinstance(item, list):
            return True
    return False
def closure(tset,opr,mod):
    if(is_nested_list(tset)):
        m=[]
        for i in range(0,len(tset)):
            m.append(sp.Matrix(tset[i]))
        for i in range(0,len(tset)):
            for j in range(0,len(tset)):
                val=ops[opr](m[i],m[j])
                #print(val)
                #print(sp.Mod(val,mod))
                if(mod<=1):
                    if(val not in m):
                        return 0
                else:
                    if(sp.Mod(val,mod) not in m):
                        return 0
    else:  
        for i in range(0,len(tset)):
            for j in range(0,len(tset)):
                val=ops[opr](tset[i],tset[j])
                if mod<=1:
                    if(val not in tset):
                        return 0
                else:
                    if((val%mod) not in tset):
                        return 0;
    return 1
def associativity(tset,opr,mod):
    if(is_nested_list(tset)):
        m=[]
        for i in range(0,len(tset)):
            m.append(sp.Matrix(tset[i]))
        for i in range(0,len(tset)):
            for j in range(0,len(tset)):
                for k in range(0,len(tset)):
                   if(mod<=1):
                       v1=ops[opr](m[i],m[j])
                       v2=ops[opr](v1,m[k])
                       v3=ops[opr](m[j],m[k])
                       v4=ops[opr](m[i],v3)
                       if(v2!=v4):
                           return 0
                       else:
                           v1=ops[opr](m[i],m[j])
                           v1=sp.Mod(v1,mod)
                           v2=ops[opr](v1,m[k])
                           v2=sp.Mod(v2,mod)
                           v3=ops[opr](m[j],m[k])
                           v3=sp.Mod(v3,mod)
                           v4=ops[opr](m[i],v3)
                           v4=sp.Mod(v4,mod)
                           if(v2!=v4):
                               return 0
    else:
        for i in range(0,len(tset)):
            for j in range(0,len(tset)):
                for k in range(0,len(tset)):
                    if(mod<=1):
                        v1=ops[opr](tset[i],tset[j])
                        v2=ops[opr](v1,tset[k])
                        v3=ops[opr](tset[j],tset[k])
                        v4=ops[opr](tset[i],v3)
                        if(v2!=v4):
                            return 0
                    else:
                        v1=ops[opr](tset[i],tset[j])
                        v1=v1%mod
                        v2=ops[opr](v1,tset[k])
                        v2=v2%mod
                        v3=ops[opr](tset[j],tset[k])
                        v3=v3%mod
                        v4=ops[opr](tset[i],v3)
                        v4=v4%mod
                        if(v2!=v4):
                            return 0
    return 1
def identity(tset,opr,mod):
    count=0
    if(is_nested_list(tset)):
        m=[]
        for i in range(0,len(tset)):
            m.append(sp.Matrix(tset[i]))
        for i in range(0,len(tset)):
            for j in range(0,len(tset)):
                v1=ops[opr](m[i],m[j])
                if(mod<=1):
                    if(v1==m[j]):
                        count+=1
                        if(count==len(tset)):
                            return m[i].tolist()
                else:
                    v1=ops[opr](m[i],m[j])
                    v1=sp.Mod(v1,mod)
                    if(v1==m[j]):
                        count+=1
                        if(count==len(tset)):
                            return m[i].tolist()
            count=0
        return
    else:
        for i in range(0,len(tset)):
            for j in range(0,len(tset)):
                v1=ops[opr](tset[i],tset[j])
                if(mod<=1):
                    if(v1==tset[j]):
                        count+=1
                        if count==len(tset):
                            return tset[i]
                else:
                    v1=ops[opr](tset[i],tset[j])
                    v1=v1%mod
                    if(v1==tset[j]):
                        count+=1
                        if(count==len(tset)):
                            return tset[i]
            count=0
        return 
def inverse(tset,opr,tid,mod):
    tlist=[]
    if(is_nested_list(tset)):
        m=[]
        for i in range(0,len(tset)):
            m.append(sp.Matrix(tset[i]))
        for i in range(0,len(tset)):
            for j in range(0,len(tset)):
                v1=ops[opr](m[i],m[j])
                if(mod<=1):
                    if(v1==sp.Matrix(tid)):
                        tl=(m[i].tolist(),m[j].tolist())
                        tlist.append(tl)
                else:
                    v1=ops[opr](m[i],m[j])
                    v1=sp.Mod(v1,mod)
                    if(v1==sp.Matrix(tid)):
                        tl=(m[i].tolist(),m[j].tolist())
                        tlist.append(tl)
        if(len(tset)!=len(tlist)):
            return []
        else:
            return tlist
    else:
        for i in range(0,len(tset)):
            for j in range(0,len(tset)):
                v1=ops[opr](tset[i],tset[j])
                if(mod<=1):
                    if(v1==tid):
                        tl=(tset[i],tset[j])
                        tlist.append(tl)
                else:
                    v1=ops[opr](tset[i],tset[j])
                    v1=v1%mod
                    if(v1==tid):
                        tl=(tset[i],tset[j])
                        tlist.append(tl)
        if(len(tset)!=len(tlist)):
            return []
        else:
            return tlist
def commutative(tset,opr,mod):
    if(is_nested_list(tset)):
        m=[]
        for i in range(0,len(tset)):
            m.append(sp.Matrix(tset[i]))
        for i in range(0,len(tset)):
            for j in range(0,len(tset)):
                v1=ops[opr](m[i],m[j])
                v2=ops[opr](m[j],m[i])
                if(mod<=1):
                    if(v1!=v2):
                        return 0
                else:
                    if(sp.Mod(v1,mod)!=sp.Mod(v2,mod)):
                        return 0
        return 1
    else:
        for i in range(0,len(tset)):
            for j in range(0,len(tset)):
                v1=ops[opr](tset[i],tset[j])
                v2=ops[opr](tset[j],tset[i])
                if(mod<=1):
                    if(v1!=v2):
                        return 0
                else:
                    if(v1%mod!=v2%mod):
                        return 0
        return 1
def cyclic(tset,opr,mod):
    tcount=0
    generator=[]
    if(is_nested_list(tset)):
        m=[]
        for i in range(0,len(tset)):
            m.append(sp.Matrix(tset[i]))
        for i in range(0,len(m)):
            if m[i].norm==0:
                continue
            for j in range(0,len(m)):
                if(mod<=1):
                    if(sp.Mod(m[j],m[i])==0):
                        tcount+=1
                else:
                    if(sp.Mod((sp.Mod(m[j],m[i])),mod)==0):
                        print("h")
                        tcount+=1
                    else:
                        for k in range(0,mod+1):
                            if(sp.Mod((k*m[i]),mod)==sp.Mod(m[j],m[i])):
                                tcount+=1
            if(tcount==len(m)):
                generator.append(m[i].tolist())
            tcount=0
        return generator
    else:
        for i in range(0,len(tset)):
            if(tset[i]==0):
                continue
            for j in range(0,len(tset)):
                if(mod<=1):
                    if(tset[j]%tset[i]==0):
                        tcount+=1
                else:
                    if(tset[j]%tset[i]==0):
                        tcount+=1
                    else:
                        for k in range(0,mod+1):
                            if((k*tset[i])%mod==(tset[j]%tset[i])):
                                tcount+=1
            if(tcount==len(tset)):
                generator.append(tset[i])
            tcount=0
        return generator
def is_group(tset,opr,mod=1):
    #inverse=[]
    flag=0
    if(closure(tset, opr,mod)&associativity(tset, opr, mod)):
        e=identity(tset, opr, mod)
        if(e!='no'):
            inverse_elements=inverse(tset,opr,e,mod)
            if(len(inverse_elements)==len(tset)):
                flag=1
                if(commutative(tset, opr,mod)):
                    abelian=1
                return 1
                print("It is a group")
    if(flag==0):
        return 0
        print("It is not a group")
    gen=cyclic(tset,opr,mod)
    if(len(gen)==0|(len(gen)==1&gen[0]==1)):
        cycle=0
    elif(c!=1 for c in gen):
        cycle=1
    if(cycle==0):
        print("It is not cyclic")
    elif(cycle>0):
        print("It is cyclic")
        
def subgroup(tset,opr,mod=1):
    tsubs=[]
    if(is_nested_list(tset)):
   # if(is_group(tset, opr,mod)):
        tempm=[]
        for i in range(1,len(tset)+1):
            tempm+=list(itertools.combinations(tset, i))
        for i in range(0,len(tempm)):
            if(is_group(tempm[i],opr,mod)):
                tsubs.append(tempm[i])
        return tsubs
    '''else:
            tempm=[]
            for i in range(1,len(tset)+1):
                tempm+=list(itertools.combinations(tset, i))
            for i in range(0,len(tempm)):
                if(is_group(tempm[i],opr,mod)):
                    tsubs.append(tempm[i])
            return tsubs'''
def left_coset(tset,opr,mod,subset):
    lcoset=[]
    if(is_nested_list(tset)):
        m=[]
        tsub=[]
        for i in range(0,len(tset)):
            m.append(sp.Matrix(tset[i]))
        for i in range(0,len(subset)):
            tsub.append(sp.Matrix(subset[i]))
            for i in range(0,len(m)):
                for j in range(0,len(tsub)):
                    if(mod<=1):
                        v1=ops[opr](m[i],tsub[j])
                        lcoset.append(v1.tolist())
                    else:
                        v1=ops[opr](m[i],tsub[j])
                        v1=sp.Mod(v1,mod)
                        lcoset.append(v1.tolist())
        return lcoset
    else:
        for i in range(0,len(tset)):
            for j in range(0,len(subset)):
                if(mod<=1):
                    lcoset.append(ops[opr](tset[i],subset[j]))
                else:
                    v1=ops[opr](tset[i],subset[j])
                    v1=v1%mod
                    lcoset.append(v1)
        return lcoset
def right_coset(tset,opr,mod,subset):
    rcoset=[]
    if(is_nested_list(tset)):
        m=[]
        tsub=[]
        for i in range(0,len(tset)):
            m.append(sp.Matrix(tset[i]))
        for i in range(0,len(subset)):
            tsub.append(sp.Matrix(subset[i]))
            for i in range(0,len(m)):
                for j in range(0,len(tsub)):
                    if(mod<=1):
                        rcoset.append((ops[opr](tsub[j],m[i])).tolist())
                    else:
                        v1=ops[opr](tsub[j],m[i])
                        v1=sp.Mod(v1,mod)
                        rcoset.append(v1.tolist())
        return rcoset
    else:
        for i in range(0,len(tset)):
            for j in range(0,len(subset)):
                if(mod<=1):
                    rcoset.append(ops[opr](tset[i],subset[j]))
                else:
                    v1=ops[opr](tset[i],subset[j])
                    v1=v1%mod
                    rcoset.append(v1)
        return rcoset
def normal_group(tset,opr,subset,mod):
    if(left_coset(tset, opr, mod, subset)==right_coset(tset, opr, mod, subset)):
        return 1
    else:
        return 0
#def homomorphism(tset1,tset2,)
def is_ring(tset,opr1,opr2,mod1=1,mod2=1):
    if(is_group(tset,opr1,mod1)&commutative(tset, opr1, mod1)):
        if(is_nested_list(tset)):
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
        if(is_nested_list(tset)):
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
        if(is_nested_list(tset)):
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
        if(is_nested_list(tset)):
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
        return
def zero_divisor(tset,opr1,opr2,mod1=1,mod2=1):
    if(is_ring(tset, opr1, opr2,mod1,mod2)):
        if(is_nested_list(tset)):
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
        return
def subring(tset,opr1,opr2,mod1=1,mod2=1):
    subr=[]
    if(is_ring(tset, opr1, opr2,mod1,mod2)):
        tsr=[]
        for i in range(1,len(tset)+1):
            tsr+=list(itertools.combinations(tset,i))
        for i in range(0,len(tsr)):
            if(is_ring(tsr[i], opr1, opr2,mod1,mod2)):
                subr.append(tsr[i])
        return subr
def ideal(tset,opr1,opr2,sr,mod1=1,mod2=1):
    idl=[]
    if(is_ring(tset, opr1, opr2,mod1,mod2)):
        if(is_nested_list(tset)):
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
#is_group([[[1,0],[0,1]],[[1,1],[1,1]],[[0,0],[0,0]]],'+')
#is_group([1,2,3,4],'*',5)
#is_group([1,-1,complex(0,1),complex(0,-1)],'*')
#a=([[[1,0],[0,1]],[[1,1],[1,1]],[[0,0],[0,0]]],'*',1)
#print(a)
#print(identity([0,1,2,3,4], '*', 5))
#a=cyclic([[[1,0],[0,1]]],'*',1)
#print(a)
#a=subgroup([1,2,3,4],'*',5)
#print(a)
#a=subgroup([1,-1,complex(0,1),complex(0,-1)],'*')
a=is_group([1,2],'*')
print(a)
#print(a)
#a=left_coset([1,2,3,4],'*',5,subgroup([1,2,3,4],'*',5)[1])
#print(a)
#a=right_coset([[[1,0],[0,1]],[[1,1],[1,1]],[[0,0],[0,0]]],'+',1,subgroup([[[1,0],[0,1]],[[1,1],[1,1]],[[0,0],[0,0]]],'+')[0])
#print(a)
#a=is_ring([0,1,2,3,4,5,6],'+','*',7,7)
#print(a)
#a=subring([0,1,2,3,4,5,6,7],'+','*',8,8)
#print(a)
#a=ideal([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35],'+','*', subring([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35],'+','*',36,36),36,36)
#print(a)
#a=is_group([[[0, 0], [0, 0]], [[0, 0], [0, 1]], [[0, 0], [0, 2]], [[0, 0], [0, 3]], [[0, 0], [0, 4]], [[0, 0], [1, 0]], [[0, 0], [1, 1]], [[0, 0], [1, 2]], [[0, 0], [1, 3]], [[0, 0], [1, 4]], [[0, 0], [2, 0]], [[0, 0], [2, 1]], [[0, 0], [2, 2]], [[0, 0], [2, 3]], [[0, 0], [2, 4]], [[0, 0], [3, 0]], [[0, 0], [3, 1]], [[0, 0], [3, 2]], [[0, 0], [3, 3]], [[0, 0], [3, 4]], [[0, 0], [4, 0]], [[0, 0], [4, 1]], [[0, 0], [4, 2]], [[0, 0], [4, 3]], [[0, 0], [4, 4]], [[0, 1], [0, 0]], [[0, 1], [0, 1]], [[0, 1], [0, 2]], [[0, 1], [0, 3]], [[0, 1], [0, 4]], [[0, 1], [1, 0]], [[0, 1], [1, 1]], [[0, 1], [1, 2]], [[0, 1], [1, 3]], [[0, 1], [1, 4]], [[0, 1], [2, 0]], [[0, 1], [2, 1]], [[0, 1], [2, 2]], [[0, 1], [2, 3]], [[0, 1], [2, 4]], [[0, 1], [3, 0]], [[0, 1], [3, 1]], [[0, 1], [3, 2]], [[0, 1], [3, 3]], [[0, 1], [3, 4]], [[0, 1], [4, 0]], [[0, 1], [4, 1]], [[0, 1], [4, 2]], [[0, 1], [4, 3]], [[0, 1], [4, 4]], [[0, 2], [0, 0]], [[0, 2], [0, 1]], [[0, 2], [0, 2]], [[0, 2], [0, 3]], [[0, 2], [0, 4]], [[0, 2], [1, 0]], [[0, 2], [1, 1]], [[0, 2], [1, 2]], [[0, 2], [1, 3]], [[0, 2], [1, 4]], [[0, 2], [2, 0]], [[0, 2], [2, 1]], [[0, 2], [2, 2]], [[0, 2], [2, 3]], [[0, 2], [2, 4]], [[0, 2], [3, 0]], [[0, 2], [3, 1]], [[0, 2], [3, 2]], [[0, 2], [3, 3]], [[0, 2], [3, 4]], [[0, 2], [4, 0]], [[0, 2], [4, 1]], [[0, 2], [4, 2]], [[0, 2], [4, 3]], [[0, 2], [4, 4]], [[0, 3], [0, 0]], [[0, 3], [0, 1]], [[0, 3], [0, 2]], [[0, 3], [0, 3]], [[0, 3], [0, 4]], [[0, 3], [1, 0]], [[0, 3], [1, 1]], [[0, 3], [1, 2]], [[0, 3], [1, 3]], [[0, 3], [1, 4]], [[0, 3], [2, 0]], [[0, 3], [2, 1]], [[0, 3], [2, 2]], [[0, 3], [2, 3]], [[0, 3], [2, 4]], [[0, 3], [3, 0]], [[0, 3], [3, 1]], [[0, 3], [3, 2]], [[0, 3], [3, 3]], [[0, 3], [3, 4]], [[0, 3], [4, 0]], [[0, 3], [4, 1]], [[0, 3], [4, 2]], [[0, 3], [4, 3]], [[0, 3], [4, 4]], [[0, 4], [0, 0]], [[0, 4], [0, 1]], [[0, 4], [0, 2]], [[0, 4], [0, 3]], [[0, 4], [0, 4]], [[0, 4], [1, 0]], [[0, 4], [1, 1]], [[0, 4], [1, 2]], [[0, 4], [1, 3]], [[0, 4], [1, 4]], [[0, 4], [2, 0]], [[0, 4], [2, 1]], [[0, 4], [2, 2]], [[0, 4], [2, 3]], [[0, 4], [2, 4]], [[0, 4], [3, 0]], [[0, 4], [3, 1]], [[0, 4], [3, 2]], [[0, 4], [3, 3]], [[0, 4], [3, 4]], [[0, 4], [4, 0]], [[0, 4], [4, 1]], [[0, 4], [4, 2]], [[0, 4], [4, 3]], [[0, 4], [4, 4]], [[1, 0], [0, 0]], [[1, 0], [0, 1]], [[1, 0], [0, 2]], [[1, 0], [0, 3]], [[1, 0], [0, 4]], [[1, 0], [1, 0]], [[1, 0], [1, 1]], [[1, 0], [1, 2]], [[1, 0], [1, 3]], [[1, 0], [1, 4]], [[1, 0], [2, 0]], [[1, 0], [2, 1]], [[1, 0], [2, 2]], [[1, 0], [2, 3]], [[1, 0], [2, 4]], [[1, 0], [3, 0]], [[1, 0], [3, 1]], [[1, 0], [3, 2]], [[1, 0], [3, 3]], [[1, 0], [3, 4]], [[1, 0], [4, 0]], [[1, 0], [4, 1]], [[1, 0], [4, 2]], [[1, 0], [4, 3]], [[1, 0], [4, 4]], [[1, 1], [0, 0]], [[1, 1], [0, 1]], [[1, 1], [0, 2]], [[1, 1], [0, 3]], [[1, 1], [0, 4]], [[1, 1], [1, 0]], [[1, 1], [1, 1]], [[1, 1], [1, 2]], [[1, 1], [1, 3]], [[1, 1], [1, 4]], [[1, 1], [2, 0]], [[1, 1], [2, 1]], [[1, 1], [2, 2]], [[1, 1], [2, 3]], [[1, 1], [2, 4]], [[1, 1], [3, 0]], [[1, 1], [3, 1]], [[1, 1], [3, 2]], [[1, 1], [3, 3]], [[1, 1], [3, 4]], [[1, 1], [4, 0]], [[1, 1], [4, 1]], [[1, 1], [4, 2]], [[1, 1], [4, 3]], [[1, 1], [4, 4]], [[1, 2], [0, 0]], [[1, 2], [0, 1]], [[1, 2], [0, 2]], [[1, 2], [0, 3]], [[1, 2], [0, 4]], [[1, 2], [1, 0]], [[1, 2], [1, 1]], [[1, 2], [1, 2]], [[1, 2], [1, 3]], [[1, 2], [1, 4]], [[1, 2], [2, 0]], [[1, 2], [2, 1]], [[1, 2], [2, 2]], [[1, 2], [2, 3]], [[1, 2], [2, 4]], [[1, 2], [3, 0]], [[1, 2], [3, 1]], [[1, 2], [3, 2]], [[1, 2], [3, 3]], [[1, 2], [3, 4]], [[1, 2], [4, 0]], [[1, 2], [4, 1]], [[1, 2], [4, 2]], [[1, 2], [4, 3]], [[1, 2], [4, 4]], [[1, 3], [0, 0]], [[1, 3], [0, 1]], [[1, 3], [0, 2]], [[1, 3], [0, 3]], [[1, 3], [0, 4]], [[1, 3], [1, 0]], [[1, 3], [1, 1]], [[1, 3], [1, 2]], [[1, 3], [1, 3]], [[1, 3], [1, 4]], [[1, 3], [2, 0]], [[1, 3], [2, 1]], [[1, 3], [2, 2]], [[1, 3], [2, 3]], [[1, 3], [2, 4]], [[1, 3], [3, 0]], [[1, 3], [3, 1]], [[1, 3], [3, 2]], [[1, 3], [3, 3]], [[1, 3], [3, 4]], [[1, 3], [4, 0]], [[1, 3], [4, 1]], [[1, 3], [4, 2]], [[1, 3], [4, 3]], [[1, 3], [4, 4]], [[1, 4], [0, 0]], [[1, 4], [0, 1]], [[1, 4], [0, 2]], [[1, 4], [0, 3]], [[1, 4], [0, 4]], [[1, 4], [1, 0]], [[1, 4], [1, 1]], [[1, 4], [1, 2]], [[1, 4], [1, 3]], [[1, 4], [1, 4]], [[1, 4], [2, 0]], [[1, 4], [2, 1]], [[1, 4], [2, 2]], [[1, 4], [2, 3]], [[1, 4], [2, 4]], [[1, 4], [3, 0]], [[1, 4], [3, 1]], [[1, 4], [3, 2]], [[1, 4], [3, 3]], [[1, 4], [3, 4]], [[1, 4], [4, 0]], [[1, 4], [4, 1]], [[1, 4], [4, 2]], [[1, 4], [4, 3]], [[1, 4], [4, 4]], [[2, 0], [0, 0]], [[2, 0], [0, 1]], [[2, 0], [0, 2]], [[2, 0], [0, 3]], [[2, 0], [0, 4]], [[2, 0], [1, 0]], [[2, 0], [1, 1]], [[2, 0], [1, 2]], [[2, 0], [1, 3]], [[2, 0], [1, 4]], [[2, 0], [2, 0]], [[2, 0], [2, 1]], [[2, 0], [2, 2]], [[2, 0], [2, 3]], [[2, 0], [2, 4]], [[2, 0], [3, 0]], [[2, 0], [3, 1]], [[2, 0], [3, 2]], [[2, 0], [3, 3]], [[2, 0], [3, 4]], [[2, 0], [4, 0]], [[2, 0], [4, 1]], [[2, 0], [4, 2]], [[2, 0], [4, 3]], [[2, 0], [4, 4]], [[2, 1], [0, 0]], [[2, 1], [0, 1]], [[2, 1], [0, 2]], [[2, 1], [0, 3]], [[2, 1], [0, 4]], [[2, 1], [1, 0]], [[2, 1], [1, 1]], [[2, 1], [1, 2]], [[2, 1], [1, 3]], [[2, 1], [1, 4]], [[2, 1], [2, 0]], [[2, 1], [2, 1]], [[2, 1], [2, 2]], [[2, 1], [2, 3]], [[2, 1], [2, 4]], [[2, 1], [3, 0]], [[2, 1], [3, 1]], [[2, 1], [3, 2]], [[2, 1], [3, 3]], [[2, 1], [3, 4]], [[2, 1], [4, 0]], [[2, 1], [4, 1]], [[2, 1], [4, 2]], [[2, 1], [4, 3]], [[2, 1], [4, 4]], [[2, 2], [0, 0]], [[2, 2], [0, 1]], [[2, 2], [0, 2]], [[2, 2], [0, 3]], [[2, 2], [0, 4]], [[2, 2], [1, 0]], [[2, 2], [1, 1]], [[2, 2], [1, 2]], [[2, 2], [1, 3]], [[2, 2], [1, 4]], [[2, 2], [2, 0]], [[2, 2], [2, 1]], [[2, 2], [2, 2]], [[2, 2], [2, 3]], [[2, 2], [2, 4]], [[2, 2], [3, 0]], [[2, 2], [3, 1]], [[2, 2], [3, 2]], [[2, 2], [3, 3]], [[2, 2], [3, 4]], [[2, 2], [4, 0]], [[2, 2], [4, 1]], [[2, 2], [4, 2]], [[2, 2], [4, 3]], [[2, 2], [4, 4]], [[2, 3], [0, 0]], [[2, 3], [0, 1]], [[2, 3], [0, 2]], [[2, 3], [0, 3]], [[2, 3], [0, 4]], [[2, 3], [1, 0]], [[2, 3], [1, 1]], [[2, 3], [1, 2]], [[2, 3], [1, 3]], [[2, 3], [1, 4]], [[2, 3], [2, 0]], [[2, 3], [2, 1]], [[2, 3], [2, 2]], [[2, 3], [2, 3]], [[2, 3], [2, 4]], [[2, 3], [3, 0]], [[2, 3], [3, 1]], [[2, 3], [3, 2]], [[2, 3], [3, 3]], [[2, 3], [3, 4]], [[2, 3], [4, 0]], [[2, 3], [4, 1]], [[2, 3], [4, 2]], [[2, 3], [4, 3]], [[2, 3], [4, 4]], [[2, 4], [0, 0]], [[2, 4], [0, 1]], [[2, 4], [0, 2]], [[2, 4], [0, 3]], [[2, 4], [0, 4]], [[2, 4], [1, 0]], [[2, 4], [1, 1]], [[2, 4], [1, 2]], [[2, 4], [1, 3]], [[2, 4], [1, 4]], [[2, 4], [2, 0]], [[2, 4], [2, 1]], [[2, 4], [2, 2]], [[2, 4], [2, 3]], [[2, 4], [2, 4]], [[2, 4], [3, 0]], [[2, 4], [3, 1]], [[2, 4], [3, 2]], [[2, 4], [3, 3]], [[2, 4], [3, 4]], [[2, 4], [4, 0]], [[2, 4], [4, 1]], [[2, 4], [4, 2]], [[2, 4], [4, 3]], [[2, 4], [4, 4]], [[3, 0], [0, 0]], [[3, 0], [0, 1]], [[3, 0], [0, 2]], [[3, 0], [0, 3]], [[3, 0], [0, 4]], [[3, 0], [1, 0]], [[3, 0], [1, 1]], [[3, 0], [1, 2]], [[3, 0], [1, 3]], [[3, 0], [1, 4]], [[3, 0], [2, 0]], [[3, 0], [2, 1]], [[3, 0], [2, 2]], [[3, 0], [2, 3]], [[3, 0], [2, 4]], [[3, 0], [3, 0]], [[3, 0], [3, 1]], [[3, 0], [3, 2]], [[3, 0], [3, 3]], [[3, 0], [3, 4]], [[3, 0], [4, 0]], [[3, 0], [4, 1]], [[3, 0], [4, 2]], [[3, 0], [4, 3]], [[3, 0], [4, 4]], [[3, 1], [0, 0]], [[3, 1], [0, 1]], [[3, 1], [0, 2]], [[3, 1], [0, 3]], [[3, 1], [0, 4]], [[3, 1], [1, 0]], [[3, 1], [1, 1]], [[3, 1], [1, 2]], [[3, 1], [1, 3]], [[3, 1], [1, 4]], [[3, 1], [2, 0]], [[3, 1], [2, 1]], [[3, 1], [2, 2]], [[3, 1], [2, 3]], [[3, 1], [2, 4]], [[3, 1], [3, 0]], [[3, 1], [3, 1]], [[3, 1], [3, 2]], [[3, 1], [3, 3]], [[3, 1], [3, 4]], [[3, 1], [4, 0]], [[3, 1], [4, 1]], [[3, 1], [4, 2]], [[3, 1], [4, 3]], [[3, 1], [4, 4]], [[3, 2], [0, 0]], [[3, 2], [0, 1]], [[3, 2], [0, 2]], [[3, 2], [0, 3]], [[3, 2], [0, 4]], [[3, 2], [1, 0]], [[3, 2], [1, 1]], [[3, 2], [1, 2]], [[3, 2], [1, 3]], [[3, 2], [1, 4]], [[3, 2], [2, 0]], [[3, 2], [2, 1]], [[3, 2], [2, 2]], [[3, 2], [2, 3]], [[3, 2], [2, 4]], [[3, 2], [3, 0]], [[3, 2], [3, 1]], [[3, 2], [3, 2]], [[3, 2], [3, 3]], [[3, 2], [3, 4]], [[3, 2], [4, 0]], [[3, 2], [4, 1]], [[3, 2], [4, 2]], [[3, 2], [4, 3]], [[3, 2], [4, 4]], [[3, 3], [0, 0]], [[3, 3], [0, 1]], [[3, 3], [0, 2]], [[3, 3], [0, 3]], [[3, 3], [0, 4]], [[3, 3], [1, 0]], [[3, 3], [1, 1]], [[3, 3], [1, 2]], [[3, 3], [1, 3]], [[3, 3], [1, 4]], [[3, 3], [2, 0]], [[3, 3], [2, 1]], [[3, 3], [2, 2]], [[3, 3], [2, 3]], [[3, 3], [2, 4]], [[3, 3], [3, 0]], [[3, 3], [3, 1]], [[3, 3], [3, 2]], [[3, 3], [3, 3]], [[3, 3], [3, 4]], [[3, 3], [4, 0]], [[3, 3], [4, 1]], [[3, 3], [4, 2]], [[3, 3], [4, 3]], [[3, 3], [4, 4]], [[3, 4], [0, 0]], [[3, 4], [0, 1]], [[3, 4], [0, 2]], [[3, 4], [0, 3]], [[3, 4], [0, 4]], [[3, 4], [1, 0]], [[3, 4], [1, 1]], [[3, 4], [1, 2]], [[3, 4], [1, 3]], [[3, 4], [1, 4]], [[3, 4], [2, 0]], [[3, 4], [2, 1]], [[3, 4], [2, 2]], [[3, 4], [2, 3]], [[3, 4], [2, 4]], [[3, 4], [3, 0]], [[3, 4], [3, 1]], [[3, 4], [3, 2]], [[3, 4], [3, 3]], [[3, 4], [3, 4]], [[3, 4], [4, 0]], [[3, 4], [4, 1]], [[3, 4], [4, 2]], [[3, 4], [4, 3]], [[3, 4], [4, 4]], [[4, 0], [0, 0]], [[4, 0], [0, 1]], [[4, 0], [0, 2]], [[4, 0], [0, 3]], [[4, 0], [0, 4]], [[4, 0], [1, 0]], [[4, 0], [1, 1]], [[4, 0], [1, 2]], [[4, 0], [1, 3]], [[4, 0], [1, 4]], [[4, 0], [2, 0]], [[4, 0], [2, 1]], [[4, 0], [2, 2]], [[4, 0], [2, 3]], [[4, 0], [2, 4]], [[4, 0], [3, 0]], [[4, 0], [3, 1]], [[4, 0], [3, 2]], [[4, 0], [3, 3]], [[4, 0], [3, 4]], [[4, 0], [4, 0]], [[4, 0], [4, 1]], [[4, 0], [4, 2]], [[4, 0], [4, 3]], [[4, 0], [4, 4]], [[4, 1], [0, 0]], [[4, 1], [0, 1]], [[4, 1], [0, 2]], [[4, 1], [0, 3]], [[4, 1], [0, 4]], [[4, 1], [1, 0]], [[4, 1], [1, 1]], [[4, 1], [1, 2]], [[4, 1], [1, 3]], [[4, 1], [1, 4]], [[4, 1], [2, 0]], [[4, 1], [2, 1]], [[4, 1], [2, 2]], [[4, 1], [2, 3]], [[4, 1], [2, 4]], [[4, 1], [3, 0]], [[4, 1], [3, 1]], [[4, 1], [3, 2]], [[4, 1], [3, 3]], [[4, 1], [3, 4]], [[4, 1], [4, 0]], [[4, 1], [4, 1]], [[4, 1], [4, 2]], [[4, 1], [4, 3]], [[4, 1], [4, 4]], [[4, 2], [0, 0]], [[4, 2], [0, 1]], [[4, 2], [0, 2]], [[4, 2], [0, 3]], [[4, 2], [0, 4]], [[4, 2], [1, 0]], [[4, 2], [1, 1]], [[4, 2], [1, 2]], [[4, 2], [1, 3]], [[4, 2], [1, 4]], [[4, 2], [2, 0]], [[4, 2], [2, 1]], [[4, 2], [2, 2]], [[4, 2], [2, 3]], [[4, 2], [2, 4]], [[4, 2], [3, 0]], [[4, 2], [3, 1]], [[4, 2], [3, 2]], [[4, 2], [3, 3]], [[4, 2], [3, 4]], [[4, 2], [4, 0]], [[4, 2], [4, 1]], [[4, 2], [4, 2]], [[4, 2], [4, 3]], [[4, 2], [4, 4]], [[4, 3], [0, 0]], [[4, 3], [0, 1]], [[4, 3], [0, 2]], [[4, 3], [0, 3]], [[4, 3], [0, 4]], [[4, 3], [1, 0]], [[4, 3], [1, 1]], [[4, 3], [1, 2]], [[4, 3], [1, 3]], [[4, 3], [1, 4]], [[4, 3], [2, 0]], [[4, 3], [2, 1]], [[4, 3], [2, 2]], [[4, 3], [2, 3]], [[4, 3], [2, 4]], [[4, 3], [3, 0]], [[4, 3], [3, 1]], [[4, 3], [3, 2]], [[4, 3], [3, 3]], [[4, 3], [3, 4]], [[4, 3], [4, 0]], [[4, 3], [4, 1]], [[4, 3], [4, 2]], [[4, 3], [4, 3]], [[4, 3], [4, 4]], [[4, 4], [0, 0]], [[4, 4], [0, 1]], [[4, 4], [0, 2]], [[4, 4], [0, 3]], [[4, 4], [0, 4]], [[4, 4], [1, 0]], [[4, 4], [1, 1]], [[4, 4], [1, 2]], [[4, 4], [1, 3]], [[4, 4], [1, 4]], [[4, 4], [2, 0]], [[4, 4], [2, 1]], [[4, 4], [2, 2]], [[4, 4], [2, 3]], [[4, 4], [2, 4]], [[4, 4], [3, 0]], [[4, 4], [3, 1]], [[4, 4], [3, 2]], [[4, 4], [3, 3]], [[4, 4], [3, 4]], [[4, 4], [4, 0]], [[4, 4], [4, 1]], [[4, 4], [4, 2]], [[4, 4], [4, 3]], [[4, 4], [4, 4]]],'+',5)
#print(a)         