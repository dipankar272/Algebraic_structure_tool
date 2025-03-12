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
                    #print("cyclic")
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
    if(is_group(tset, opr,mod)):
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

