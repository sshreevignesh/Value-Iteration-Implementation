import random
import numpy as np
import os

path = os.getcwd()
path = path + '/outputs'
os.mkdir(path)

f = open("./outputs/task_1_trace.txt","w")

# States stores the reward of the given state
# state[i][j][k]
# i = enemy health, 0=0,1=25,2=50,3=75,4=100
# j - number of arrows
# k = stamina 0=0,1=50,2=100
states=np.zeros((5,4,3))
oldstates=np.zeros((5,4,3))
action=np.zeros((5,4,3)) #0=shoot,1=dodge,2=recharge


def actionstr(n):
    if n==0:
        return "SHOOT"
    if n==1:
        return "DODGE"
    if n==2:
        return "RECHARGE"
    return "-1"

def recharge(i,j,k):
    if k==2:
        return 0.99*(oldstates[i][j][k])-5
    return 0.99*(0.8*oldstates[i][j][k+1]+0.2*oldstates[i][j][k])-5

def dodge(i,j,k):
    if k==1:#stamina =50
        if j==3:
            return 0.99*oldstates[i][j][0]-5
        return 0.99*(0.8*oldstates[i][j+1][0]+0.2*oldstates[i][j][0])-5
    elif k==2:
        if j==3:
            return 0.99*(0.2*oldstates[i][j][0] + 0.8*oldstates[i][j][1])-5
        return 0.99*(0.2*(0.8*oldstates[i][j+1][0]+0.2*oldstates[i][j][0]) +0.8*(0.8*oldstates[i][j+1][1]+0.2*oldstates[i][j][1]))-5

def shoot(i,j,k):
    if i==1:
        return 0.99*(0.5*oldstates[i][j-1][k-1])+10*0.5 -5
    return 0.99*(0.5*oldstates[i-1][j-1][k-1] + 0.5*oldstates[i][j-1][k-1])-5

for j in range(4):
    for k in range(3):
        states[0][j][k]=0.
        action[0][j][k]=-1
# print(states)
oldstates[:]=states[:]
iter=0
while 1:
    # print(states)
    for i in range(1,5):
        # print(i)
        for j in range(4):
            for k in range(3):
                # print(oldstates)
                if k==0:
                    states[i][j][k]=recharge(i,j,k)
                    action[i][j][k]=2
                elif j==0:
                    states[i][j][k]=max(recharge(i,j,k),dodge(i,j,k))
                    if max(recharge(i,j,k),dodge(i,j,k))==dodge(i,j,k):
                        action[i][j][k]=1
                    else:
                        action[i][j][k]=2
                else:
                    states[i][j][k]=max(recharge(i,j,k),dodge(i,j,k),shoot(i,j,k))
                    if max(recharge(i,j,k),dodge(i,j,k),shoot(i,j,k))==dodge(i,j,k):
                        action[i][j][k]=1
                    elif max(recharge(i,j,k),dodge(i,j,k),shoot(i,j,k)) == recharge(i,j,k):
                        action[i][j][k]=2
                    else:
                        action[i][j][k]=0
    if np.amax(oldstates-states)<0.001:
        break
    oldstates[:]=states[:]
    f.write("iteration="+str(iter)+"\n")
    for i in range(5):
        for j in range(4):
            for k in range(3):
                f.write("("+str(i)+","+str(j)+","+str(k)+"):"+actionstr(action[i][j][k])+"=["+str(round(states[i][j][k],3))+"]"+"\n")
    f.write("\n")
    f.write("\n")
    iter=iter+1
f.close()

f = open("./outputs/task_2_part_1_trace.txt","w")

states=np.zeros((5,4,3))
oldstates=np.zeros((5,4,3))
action=np.zeros((5,4,3)) #0=shoot21,1=dodge21,2=recharge21


def actionstr21(n):
    if n==0:
        return "SHOOT"
    if n==1:
        return "DODGE"
    if n==2:
        return "RECHARGE"
    return "-1"

def recharge21(i,j,k):
    if k==2:
        return 0.99*(oldstates[i][j][k])-2.5
    return 0.99*(0.8*oldstates[i][j][k+1]+0.2*oldstates[i][j][k])-2.5

def dodge21(i,j,k):
    if k==1:#stamina =50
        if j==3:
            return 0.99*oldstates[i][j][0]-2.5
        return 0.99*(0.8*oldstates[i][j+1][0]+0.2*oldstates[i][j][0])-2.5
    elif k==2:
        if j==3:
            return 0.99*(0.2*oldstates[i][j][0] + 0.8*oldstates[i][j][1])-2.5
        return 0.99*(0.2*(0.8*oldstates[i][j+1][0]+0.2*oldstates[i][j][0]) +0.8*(0.8*oldstates[i][j+1][1]+0.2*oldstates[i][j][1]))-2.5

def shoot21(i,j,k):
    if i==1:
        return 0.99*(0.5*oldstates[i][j-1][k-1])+10*0.5 -0.25
    return 0.99*(0.5*oldstates[i-1][j-1][k-1] + 0.5*oldstates[i][j-1][k-1])-0.25

for j in range(4):
    for k in range(3):
        states[0][j][k]=0.
        action[0][j][k]=-1
# print(states)
oldstates[:]=states[:]
iter=0
while 1:
    # print(states)
    for i in range(1,5):
        # print(i)
        for j in range(4):
            for k in range(3):
                # print(oldstates)
                if k==0:
                    states[i][j][k]=recharge21(i,j,k)
                    action[i][j][k]=2
                elif j==0:
                    states[i][j][k]=max(recharge21(i,j,k),dodge21(i,j,k))
                    if max(recharge21(i,j,k),dodge21(i,j,k))==dodge21(i,j,k):
                        action[i][j][k]=1
                    else:
                        action[i][j][k]=2
                else:
                    states[i][j][k]=max(recharge21(i,j,k),dodge21(i,j,k),shoot21(i,j,k))
                    if max(recharge21(i,j,k),dodge21(i,j,k),shoot21(i,j,k))==dodge21(i,j,k):
                        action[i][j][k]=1
                    elif max(recharge21(i,j,k),dodge21(i,j,k),shoot21(i,j,k)) == recharge21(i,j,k):
                        action[i][j][k]=2
                    else:
                        action[i][j][k]=0
    if np.amax(oldstates-states)<0.001:
        break
    oldstates[:]=states[:]
    f.write("iteration="+str(iter)+"\n")
    for i in range(5):
        for j in range(4):
            for k in range(3):
                f.write("("+str(i)+","+str(j)+","+str(k)+"):"+actionstr21(action[i][j][k])+"=["+str(round(states[i][j][k],3))+"]"+"\n")
    f.write("\n")
    f.write("\n")
    iter=iter+1
f.close()

f = open("./outputs/task_2_part_2_trace.txt","w")

# States stores the reward of the given state
# state[i][j][k]
# i = enemy health, 0=0,1=25,2=50,3=75,4=100
# j - number of arrows
# k = stamina 0=0,1=50,2=100
states=np.zeros((5,4,3))
oldstates=np.zeros((5,4,3))
action=np.zeros((5,4,3)) #0=shoot22,1=dodge22,2=recharge22


def actionstr22(n):
    if n==0:
        return "SHOOT"
    if n==1:
        return "DODGE"
    if n==2:
        return "RECHARGE"
    return "-1"

def recharge22(i,j,k):
    if k==2:
        return 0.1*(oldstates[i][j][k])-2.5
    return 0.1*(0.8*oldstates[i][j][k+1]+0.2*oldstates[i][j][k])-2.5

def dodge22(i,j,k):
    if k==1:#stamina =50
        if j==3:
            return 0.1*oldstates[i][j][0]-2.5
        return 0.1*(0.8*oldstates[i][j+1][0]+0.2*oldstates[i][j][0])-2.5
    elif k==2:
        if j==3:
            return 0.1*(0.2*oldstates[i][j][0] + 0.8*oldstates[i][j][1])-2.5
        return 0.1*(0.2*(0.8*oldstates[i][j+1][0]+0.2*oldstates[i][j][0]) +0.8*(0.8*oldstates[i][j+1][1]+0.2*oldstates[i][j][1]))-2.5

def shoot22(i,j,k):
    if i==1:
        return 0.1*(0.5*oldstates[i][j-1][k-1])+10*0.5 -2.5
    return 0.1*(0.5*oldstates[i-1][j-1][k-1] + 0.5*oldstates[i][j-1][k-1])-2.5

for j in range(4):
    for k in range(3):
        states[0][j][k]=0.
        action[0][j][k]=-1
# print(states)
oldstates[:]=states[:]
iter=0
while 1:
    # print(states)
    for i in range(1,5):
        # print(i)
        for j in range(4):
            for k in range(3):
                # print(oldstates)
                if k==0:
                    states[i][j][k]=recharge22(i,j,k)
                    action[i][j][k]=2
                elif j==0:
                    states[i][j][k]=max(recharge22(i,j,k),dodge22(i,j,k))
                    if max(recharge22(i,j,k),dodge22(i,j,k))==dodge22(i,j,k):
                        action[i][j][k]=1
                    else:
                        action[i][j][k]=2
                else:
                    states[i][j][k]=max(recharge22(i,j,k),dodge22(i,j,k),shoot22(i,j,k))
                    if max(recharge22(i,j,k),dodge22(i,j,k),shoot22(i,j,k))==dodge22(i,j,k):
                        action[i][j][k]=1
                    elif max(recharge22(i,j,k),dodge22(i,j,k),shoot22(i,j,k)) == recharge22(i,j,k):
                        action[i][j][k]=2
                    else:
                        action[i][j][k]=0
    if np.amax(oldstates-states)<0.001:
        break
    oldstates[:]=states[:]
    f.write("iteration="+str(iter)+"\n")
    for i in range(5):
        for j in range(4):
            for k in range(3):
                f.write("("+str(i)+","+str(j)+","+str(k)+"):"+actionstr22(action[i][j][k])+"=["+str(round(states[i][j][k],3))+"]"+"\n")
    f.write("\n")
    f.write("\n")
    iter=iter+1
f.close()

f = open("./outputs/task_2_part_3_trace.txt","w")

# States stores the reward of the given state
# state[i][j][k]
# i = enemy health, 0=0,1=25,2=50,3=75,4=100
# j - number of arrows
# k = stamina 0=0,1=50,2=100
states=np.zeros((5,4,3))
oldstates=np.zeros((5,4,3))
action=np.zeros((5,4,3)) #0=shoot23,1=dodge23,2=recharge23


def actionstr23(n):
    if n==0:
        return "SHOOT"
    if n==1:
        return "DODGE"
    if n==2:
        return "RECHARGE"
    return "-1"

def recharge23(i,j,k):
    if k==2:
        return 0.1*(oldstates[i][j][k])-2.5
    return 0.1*(0.8*oldstates[i][j][k+1]+0.2*oldstates[i][j][k])-2.5

def dodge23(i,j,k):
    if k==1:#stamina =50
        if j==3:
            return 0.1*oldstates[i][j][0]-2.5
        return 0.1*(0.8*oldstates[i][j+1][0]+0.2*oldstates[i][j][0])-2.5
    elif k==2:
        if j==3:
            return 0.1*(0.2*oldstates[i][j][0] + 0.8*oldstates[i][j][1])-2.5
        return 0.1*(0.2*(0.8*oldstates[i][j+1][0]+0.2*oldstates[i][j][0]) +0.8*(0.8*oldstates[i][j+1][1]+0.2*oldstates[i][j][1]))-2.5

def shoot23(i,j,k):
    if i==1:
        return 0.1*(0.5*oldstates[i][j-1][k-1])+10*0.5 -2.5
    return 0.1*(0.5*oldstates[i-1][j-1][k-1] + 0.5*oldstates[i][j-1][k-1])-2.5

for j in range(4):
    for k in range(3):
        states[0][j][k]=0.
        action[0][j][k]=-1
# print(states)
oldstates[:]=states[:]
iter=0
while 1:
    # print(states)
    for i in range(1,5):
        # print(i)
        for j in range(4):
            for k in range(3):
                # print(oldstates)
                if k==0:
                    states[i][j][k]=recharge23(i,j,k)
                    action[i][j][k]=2
                elif j==0:
                    states[i][j][k]=max(recharge23(i,j,k),dodge23(i,j,k))
                    if max(recharge23(i,j,k),dodge23(i,j,k))==dodge23(i,j,k):
                        action[i][j][k]=1
                    else:
                        action[i][j][k]=2
                else:
                    states[i][j][k]=max(recharge23(i,j,k),dodge23(i,j,k),shoot23(i,j,k))
                    if max(recharge23(i,j,k),dodge23(i,j,k),shoot23(i,j,k))==dodge23(i,j,k):
                        action[i][j][k]=1
                    elif max(recharge23(i,j,k),dodge23(i,j,k),shoot23(i,j,k)) == recharge23(i,j,k):
                        action[i][j][k]=2
                    else:
                        action[i][j][k]=0
    if np.amax(oldstates-states)<1e-10:
        break
    oldstates[:]=states[:]
    f.write("iteration="+str(iter)+"\n")
    for i in range(5):
        for j in range(4):
            for k in range(3):
                f.write("("+str(i)+","+str(j)+","+str(k)+"):"+actionstr23(action[i][j][k])+"=["+str(round(states[i][j][k],3))+"]"+"\n")
    f.write("\n")
    f.write("\n")
    iter=iter+1
f.close()
