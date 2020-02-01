import sys
import numpy as np
import math
import random
#from temp import largest_q
def get_arguments(temp):
    return temp[1],temp[2],int(temp[3]),float(temp[4]),int(temp[5])

def k_armed_bandit(mean,arm):
    arm_mean=mean[arm]
    return np.random.choice([0,1],p=[1-arm_mean,arm_mean])

def arm_mean(instance):

    with open(instance,'r') as inst:
        inst.seek(0)
        contents=inst.read()
        contents=contents.split('\n')
        contents.remove('')
    return np.array(contents,dtype=float)

def list_of_arms(instance):
    if instance=='../instances/i-1.txt':
        possible_arms=list(range(2))
    elif instance=='../instances/i-2.txt':
        possible_arms=list(range(5))
    elif instance=='../instances/i-3.txt':
        possible_arms=list(range(25))
    return possible_arms 

def round_robin(possible_arms,randomSeed,horizon,mean):
    reward=0
    np.random.seed(randomSeed)
    for epochs in range(int(horizon/len(possible_arms))):
        for arm in possible_arms:
            reward+=k_armed_bandit(mean,arm)
    return reward,horizon


def epsilon_greedy(possible_arms,epsilon,horizon,randomSeed,mean):
    q_mean=np.zeros(len(possible_arms))
    np.random.seed(randomSeed)
    for  arm in possible_arms:
        q_mean[arm]=k_armed_bandit(mean,arm)
    no_of_pulls=np.ones(len(possible_arms))
    for epochs in range(horizon-len(possible_arms)):
        toss=np.random.choice([0,1],p=[epsilon,1-epsilon])
        if toss==0:
            arm=np.random.choice(possible_arms)
        elif toss == 1:
            arm=np.argmax(q_mean)
        r=k_armed_bandit(mean,arm)
        q_mean[arm]=q_mean[arm]+(r-q_mean[arm])/no_of_pulls[arm]
        no_of_pulls[arm]+=1
    return int(np.dot(q_mean,no_of_pulls)),no_of_pulls.sum()

def ucb(possible_arms,horizon,randomSeed,mean):
    q_mean=np.zeros(len(possible_arms))
    np.random.seed(randomSeed)
    for  arm in possible_arms:
        q_mean[arm]=k_armed_bandit(mean,arm)
    no_of_pulls=np.ones(len(possible_arms))
    ucb_array=np.zeros(len(possible_arms))
    for epochs in range(horizon-len(possible_arms)):
        arm=np.argmax(ucb_array)
        r=k_armed_bandit(mean,arm)
        q_mean[arm]=q_mean[arm]+(r-q_mean[arm])/no_of_pulls[arm]
        no_of_pulls[arm]+=1
        for arm in possible_arms:
            ucb_array[arm]=q_mean[arm]+math.sqrt(2*math.log(no_of_pulls.sum())/no_of_pulls[arm])
        #print(ucb_array,q_mean,no_of_pulls.sum())
    return int(np.dot(q_mean,no_of_pulls)),no_of_pulls.sum()

def thompson_sampling(possible_arms,horizon,randomSeed,mean):
    np.random.seed(randomSeed)
    s_rewards=np.zeros(len(possible_arms))
    f_rewards=np.zeros(len(possible_arms))
    for arm in possible_arms:
        reward=k_armed_bandit(mean,arm)
        if reward==1:
            s_rewards[arm]+=1
        elif reward==0:
            f_rewards[arm]+=1
    for epochs in range(horizon-len(possible_arms)):
        x=np.random.beta(s_rewards+1,f_rewards+1,size=len(possible_arms))
        #max_array= np.argwhere(np.max(x)==x).squeeze()
        arm=np.argmax(x)
        reward=k_armed_bandit(mean,arm)
        if reward==1:
            s_rewards[arm]+=1
        elif reward==0:
            f_rewards[arm]+=1
        #print(s_rewards,f_rewards,s_rewards.sum()+f_rewards.sum())
    return s_rewards.sum(),s_rewards.sum()+f_rewards.sum()

def kl_ucb(possible_arms,horizon,randomSeed,mean):
    q_mean=np.zeros(len(possible_arms))                  
    np.random.seed(randomSeed)
    for  arm in possible_arms:
        q_mean[int(arm)-1]+=k_armed_bandit(mean,arm)
    no_of_pulls=np.ones(len(possible_arms))
    ucb_array=np.zeros(len(possible_arms),dtype=float)
    for epochs in range(horizon-len(possible_arms)):
        arm=np.argmax(ucb_array)
        r=k_armed_bandit(mean,arm)
        q_mean[arm]=q_mean[arm]+(r-q_mean[arm])/no_of_pulls[arm]
        no_of_pulls[arm]+=1
        #print(q_mean,no_of_pulls,no_of_pulls.sum())
        for arm in possible_arms:
            ucb_array[arm]=largest_q(q_mean[arm],no_of_pulls.sum(),no_of_pulls[arm])
        #print(ucb_array,q_mean,no_of_pulls,no_of_pulls.sum())
    return int(np.dot(q_mean,no_of_pulls)),no_of_pulls.sum()

def f(x,y,k):
    a=(x/y)**x
    b=((1-x)/(1-y))**(1-x)
    z=math.log(a*b)
    #print(a,b,z)
    return k-z
def f_prime(x,y):
    return -(y-x)/((1.0-y)*y)
    

def largest_q(p,t,u):
    
    if p==1.0:
        return 1.0
    else:
        e=10**-12
        d=10**-8
        p=max(p,d)
        q=p+d
        k=(math.log(t)+3*math.log(math.log(t)))/u
        #print(k,f(p,q,k),df(p,q))
        #print(k)
        while(f(p,q,k)**2>=e):
        #print(q-f(p,q,k)/df(p,q))
            q=min(1-d,max(q-f(p,q,k)/f_prime(p,q),p+d))
            #print(q)    
    return q



if __name__ == "__main__":
    instance,algorithm,randomSeed,epsilon,horizon=get_arguments(sys.argv)
    mean=arm_mean(instance)
    possible_arms=list_of_arms(instance)
      
    if algorithm=='round-robin':
        round_robin_reward,total_pulls=round_robin(possible_arms,randomSeed,horizon,mean)
        regret=round_robin_reward-horizon*np.max(mean)
        regret=round(regret,2)
    elif algorithm == 'epsilon-greedy':
        epsilon_greedy_reward,total_pulls=epsilon_greedy(possible_arms,epsilon,horizon,randomSeed,mean)
        regret=epsilon_greedy_reward-total_pulls*np.max(mean)
        regret=round(regret,2)
    elif algorithm == 'ucb':
        ucb_reward,total_pulls=ucb(possible_arms,horizon,randomSeed,mean)
        regret=ucb_reward-total_pulls*np.max(mean)
        regret=round(regret,2)
    elif algorithm == 'kl-ucb':
        kl_ucb_reward,total_pulls=kl_ucb(possible_arms,horizon,randomSeed,mean)
        regret=kl_ucb_reward-total_pulls*np.max(mean)
        regret=round(regret,2)
    elif algorithm == 'thompson-sampling':
        thompson_sampling_reward,total_pulls=thompson_sampling(possible_arms,horizon,randomSeed,mean)
        regret=thompson_sampling_reward-total_pulls*np.max(mean)
        regret=round(regret,2)
    
    with open('outputData2.txt','a+') as output:
        output.write('{}, {}, {}, {}, {}, {}\n'.format(instance,algorithm,randomSeed,epsilon,horizon,-regret))