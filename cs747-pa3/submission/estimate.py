import sys 

import numpy as np


def read(data_file):
    with open(data_file,'r') as data:
        data.seek(0)
        states=int(data.readline())
        actions=int(data.readline())
        gamma=float(data.readline())
        episode=[]
        for i,line in enumerate(data):
            temp=line.split('\n')
            temp=temp[0].split('\t')
            if len(temp)==1:
                temp=[temp[0],np.nan,np.nan]
            t=np.array(temp)
            #print(t)
            episode=np.append(episode,t,axis=0)
            #print(episode)
        a=int(len(episode)/3)
        episode=episode.reshape(a,3)
    return states,gamma,episode


def esimate_v(states,gamma,episode):
    v=np.zeros(states)
    for k in range(6):
        g=0.0
        returns=np.zeros(states)
        count=np.zeros(states)
        for i in range(len(episode)-2, -1, -1):
            s=int(episode[i][0])
            g=(gamma*g)+float(episode[i][2])
            returns[s]+=g
            count[s]+=1
        if k==0:
            v=returns/count
        else:
            v-=0.00001*returns/count
    return v



if __name__ == "__main__":
    data_file=sys.argv[1]
    print(sys.argv[1])
    states,gamma,episode=read(data_file)
    v=esimate_v(states,gamma,episode)
    for i in range(states):
        print(v[i])
    

    