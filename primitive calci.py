
# coding: utf-8

# In[60]:


import sys
glbl_opert=dict()
limit=100000

def seq_synthesizer(opert,m,iter):
    n=1
    seq=[1]
    while n<m:
        k=n*3
        if k in opert and opert[k]==iter-1:
            n=k
            seq.append(n)
            #print(seq)
            iter=iter-1
        elif (n*2) in opert and opert[n*2]==iter-1:
            n=n*2
            seq.append(n)
            #print(seq)
            iter=iter-1
        else:
            k=n+1
            if k in opert and opert[k]==iter-1:
                n=k
                seq.append(n)
                #print(seq)
                iter=iter-1
    return seq
    
def calci1(n,op,opert):
    #print('div by 3')
    #print(n)
    opert_l=opert
    op_l=op
    global limit
    
    if n%3==0:
        n=n/3
        op_l+=1
        if op_l>limit:
            return
        if n in opert:
            if opert_l[n]>op_l:
                opert_l[n]=op_l
                primitive_calci(n,op_l,opert_l)
                
            else:
                return   
        else:
            opert_l[n]=op_l
            primitive_calci(n,op_l,opert_l)
        
        
        
        
def calci2(n,op,opert):
    #print('div by 2')
    #print(n)
    opert_l=opert
    op_l=op
    global limit
    
    if n%2==0:
        n=n/2
        op_l+=1
        if op_l>limit:
            return
        if n in opert:
            if opert_l[n]>op_l:
                opert_l[n]=op_l
                primitive_calci(n,op_l,opert_l)
                
            else:
                return  
        else:
            opert_l[n]=op_l
            primitive_calci(n,op_l,opert_l)
        
        
    
def calci3(n,op,opert):
    #print('sub 1')
    #print(n)
    opert_l=opert
    op_l=op
    global limit, glbl_opert
    
    if n==1:
        #print('yoyoyo')
        limit=op_l
        glbl_opert=opert
        return
    n=n-1
    #print(n)
    op_l+=1
    if op_l>limit:
        return
    if n in opert:
        if opert_l[n]>op_l:
            opert_l[n]=op_l
            
            primitive_calci(n,op_l,opert_l)
                
        else:
            return   
    else:
        opert_l[n]=op_l
        primitive_calci(n,op_l,opert_l)
    
    

def primitive_calci(n,op,opert):
    
    if n%3==0:
        calci1(n,op,opert)
    if n%2==0:
        calci2(n,op,opert)
    calci3(n,op,opert)
    
def primitive_calci_initializer(n):
    m=n
    op=0
    opert=dict()
    opert[n]=0
    primitive_calci(n,op,opert)
    iter=glbl_opert[1]
    seq=seq_synthesizer(glbl_opert,m,iter)
    #print(iter)
    return seq
        
input = sys.stdin.read()
n = int(input)
sequence = list(primitive_calci_initializer(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')


# In[61]:





# In[45]:



    

