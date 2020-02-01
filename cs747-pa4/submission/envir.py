import numpy as np


def environment(current_pos,a,stochastic,wind):
    x=current_pos[0]
    y=current_pos[1]
    a=int(a)
    if a==0:
        y+=1
    elif a==1:
        y-=1
    elif a==2:
        x-=1
    elif a==3:
        x+=1
    elif a==4:
        x-=1
        y+=1
    elif a==5:
        y+=1
        x+=1
    elif a==6:
        y-=1
        x-=1
    elif a==7:
        y-=1
        x+=1
    elif a==8:
        pass
       
    if x<0:
        x=0
    if x>9:
        x=9
    if stochastic == 'yes':
        s=np.random.choice([-1,0,1])
    else:
        s=0
    y+=wind[current_pos[0]]+s
    if y<0:
        y=0
    if y>6:
        y=6
    return [x,y]


if __name__ == "__main__":
    wind=[0,0,0,1,1,1,2,2,1,0]
    x_co=int(input('Enter X_co-ordinate of current_postion\n'))
    y_co=int(input('Enter Y_co-ordinate of current_postion\n'))
    print('0=up,1=down,2=left,3=right,4=top_left,5=top_right,6=down_left,7=down_right,8=no_move')
    a=int(input('Enter action\n'))
    stochastic = input(' Do you want to enter in stochastic environment? (yes) or (no) without brackets\n')
    s=[x_co,y_co]
    if s==[7,3]:
        r=0
    else: 
        r=-1
    print('next_state=',environment(s,a,stochastic,wind),'\n','reward=',r)
