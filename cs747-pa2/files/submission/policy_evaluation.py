import sys

import numpy as np
from scipy.optimize import linprog
from scipy.linalg import solve 

def read_mdp(mdp_file):
    with open(mdp_file,'r') as mdp:
        mdp.seek(0)
        states=int(mdp.readline())
        actions=int(mdp.readline())
        r = np.zeros((states,actions,states), dtype = float)
        t = np.zeros((states, actions, states), dtype= float)
        for s in range(states):
            for a in range(actions):
                temp=mdp.readline().split('\t')
                temp.remove('\n')                                
                for s_prime in range(states):
                    r[s][a][s_prime]=float(temp[s_prime])
        for s in range(states):
            for a in range(actions):
                temp=mdp.readline().split('\t')
                temp.remove('\n')                                
                for s_prime in range(states):
                    t[s][a][s_prime]=float(temp[s_prime])
        gamma = float(mdp.readline())
        type_of_mdp = mdp.readline()

    return states,actions,r,t,gamma,type_of_mdp

def policy_eval(states,actions,t,r,gamma,policy):
    T=np.zeros([states,states])
    R=np.zeros([states,states])
    #v=np.zeros(states)
    for s,a in zip(range(states),policy):
        T[s]=t[s][a]
        R[s]=r[s][a]
    b=np.multiply(T,R)
    b_dash= np.zeros([states])
    for i in range(states):
        b_dash[i]= b[i].sum()
    I=np.identity(states)
    A=I-gamma*T
    return solve(A,b_dash)

def policy_improve(states,actions,t,r,gamma,v):
    new_policy=[0]*states
    for s in range(states):
        x=np.zeros(actions,dtype=float)
        for a in range(actions):
            for sp in range(states):
                x[a]=x[a]+ t[s][a][sp]*(r[s][a][sp]+gamma*v[sp])
        new_policy[s]=np.argmax(x)
    return new_policy

def lpi(states,acioons,t,r,gamma):
    T=t.reshape(states*actions,states)
    R=r.reshape(states*actions,states)  
    b_dash=np.multiply(T,R)
    b=np.zeros(states*actions)
    I=np.zeros([1,states])
    for i in range(states*actions):
        b[i]=b_dash[i].sum()
    for s in range(states):
        x=np.zeros([1,states])
        x[0][s]=1.0
        for a in range(actions):
            I=np.append(I,x,axis=0)
    I=np.delete(I, (0), axis=0)
    A=gamma*T-I
    c=np.ones(states)
    bou = [(None, None)]*states
    res=linprog(c,A_ub=A,b_ub=-b,bounds=bou,method='revised simplex')
    v=res.x
    policy=policy_improve(states,actions,t,r,gamma,v)
    return v, policy


def hpi(states,actions,t,r,gamma):
    policy=[0]*states
    policy_stable=False
    while(policy_stable==False):
        old_policy=policy
        v=policy_eval(states,actions,t,r,gamma,policy)
        policy=policy_improve(states,actions,t,r,gamma,v)
        if (old_policy==policy):
            policy_stable=True
    return v, policy

if __name__ == "__main__":
    mdp_file=sys.argv[1]
    algorithm= sys.argv[2]
    states,actions,r,t,gamma,type_of_mdp=read_mdp(mdp_file)
    if (algorithm == 'hpi'):
        v,policy=hpi(states,actions,t,r,gamma)
    elif (algorithm == 'lp'):
        v,policy=lpi(states,actions,t,r,gamma)
    
    for s in range(states):
        print('{}\t{}'.format(v[s],policy[s]))
    

