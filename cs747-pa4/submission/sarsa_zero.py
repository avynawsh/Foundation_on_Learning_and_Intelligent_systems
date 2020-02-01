import numpy as np
import matplotlib.pyplot as plt
import sys  
from envir import environment

def epsilon_greedy(q,s,actions):
    toss= np.random.choice([0,1],p=[0.1,0.9])
    if toss == 0:
        return np.random.choice(actions)
    elif toss ==1:
        return np.argmax(q[s[0]][s[1]])
'''
typ=['normal_moves','king_moves','king_moves_with_stable', 'king_moves_with_stochastic']
typ='king_moves_with_stochastic'
initial_pos=[0,3]
final_pos=[7,3]
max_x=9
max_y=6
    #0=up,1=down,2=left,3=right
wind=[0,0,0,1,1,1,2,2,1,0]
    #0=up,1=down,2=left,3=right,4=top_left,5=top_right,6=down_left,7=down_right
if typ == 'king_moves':
    actions=[0,1,2,3,4,5,6,7]
    stochastic='no'
elif typ=='normal_moves':
    actions=[0,1,2,3]
    stochastic='no'
elif typ == 'king_moves_with_stable':
    actions=[0,1,2,3,4,5,6,7,8]
    stochastic='no'
elif typ == 'king_moves_with_stochastic':
    actions=[0,1,2,3,4,5,6,7,8]
    stochastic='yes'
q=np.zeros([max_x+1,max_y+1,len(actions)])
q[final_pos[0]][final_pos[1]]=0.0
np.random.seed(0)
time=np.zeros(170)
for episode in range(170):
    s=initial_pos
    a=epsilon_greedy(q,s,actions)
    i=0
    while(True):
        i+=1
        s_p=environment(s,a,stochastic,wind)
        a_p=epsilon_greedy(q,s_p,actions)
        g=0.5*(-1+q[s_p[0]][s_p[1]][a_p]-q[s[0]][s[1]][a])
        q[s[0]][s[1]][a]+=g
        s=s_p
        a=a_p
        if s == final_pos:
            break
    time[episode]=i
episode=np.cumsum(time)
plt.plot(episode,range(170),label = typ)
plt.legend()
plt.savefig(typ+'.png')
plt.show()
'''

if __name__ == "__main__":
    typ=['normal_moves','king_moves','king_moves_with_stable', 'king_moves_with_stochastic']
    typ=sys.argv[2]
    initial_pos=[0,3]
    final_pos=[7,3]
    max_x=9
    max_y=6
    #0=up,1=down,2=left,3=right
    wind=[0,0,0,1,1,1,2,2,1,0]
    #0=up,1=down,2=left,3=right,4=top_left,5=top_right,6=down_left,7=down_right
    if typ == 'king_moves':
        actions=[0,1,2,3,4,5,6,7]
        stochastic='no'
    elif typ=='normal_moves':
        actions=[0,1,2,3]
        stochastic='no'
    elif typ == 'king_moves_with_stable':
        actions=[0,1,2,3,4,5,6,7,8]
        stochastic='no'
    elif typ == 'king_moves_with_stochastic':
        actions=[0,1,2,3,4,5,6,7,8]
        stochastic='yes'
    q=np.zeros([max_x+1,max_y+1,len(actions)])
    q[final_pos[0]][final_pos[1]]=0.0
    np.random.seed(0)
    time=np.zeros(170)
    for episode in range(170):
        s=initial_pos
        a=epsilon_greedy(q,s,actions)
        i=0
        while(True):
            i+=1
            s_p=environment(s,a,stochastic,wind)
            a_p=epsilon_greedy(q,s_p,actions)
            g=0.5*(-1+q[s_p[0]][s_p[1]][a_p]-q[s[0]][s[1]][a])
            q[s[0]][s[1]][a]+=g
            s=s_p
            a=a_p
            if s == final_pos:
                break
        time[episode]=i
    episode=np.cumsum(time)
    plt.plot(episode,range(170),label = typ)
    plt.legend()
    plt.savefig(typ+'.png')
    plt.show()