#*****************************************
#  Project 1 Compare Hashing
#                            Yuehua Duan
#               1. Linear Probing
#               2. Quadratic Probing
#               3. Double Hashing
#*****************************************

# Random integers between 1 and 10,000 as keys.
import random
itemList = random.sample(range(1, 10000), 1100)


# Rehash function to solve the collision.
def reHashLinear(occupiedHash, m, p,keyCountL):
    keyCountL[occupiedHash]=keyCountL[occupiedHash]+1
    return ((occupiedHash+p)% m)

def reHashQuadratic(occupiedHash, m, q,keyCountQ):
    keyCountQ[occupiedHash]=keyCountQ[occupiedHash]+1
    return ((occupiedHash+q*q)% m)

def reHashDouble(occupiedHash, m, n, itemR,keyCountD):
    keyCountD[occupiedHash]=keyCountD[occupiedHash]+1
    return ((occupiedHash+n*(1+(itemR %(m-1))))%m)

# There is the three hashing probing in HashCompare
def HashCompare(itemset, m):
	hashTableLinear = [None]*m
	hashTableQuadratic = [None]*m
	hashTableDouble = [None]*m	
	keyCountLinear = [None]*m
	keyCountQuadratic = [None]*m
	keyCountDouble = [None]*m
			
    # Linear Probing
	for item in itemset:
                slot= item % m
                p=1
                if hashTableLinear[slot] == None:
                                hashTableLinear[slot] = item
                                keyCountLinear[slot]=1
                elif hashTableLinear[slot]!= None:
                        nextSlot = reHashLinear(slot,m,p,keyCountLinear)
                        while hashTableLinear[nextSlot] != None:
                                p=p+1
                                nextSlot=reHashLinear(nextSlot,m,p,keyCountLinear)
                        if hashTableLinear[nextSlot] == None:
                                hashTableLinear[nextSlot] = item
                                keyCountLinear[nextSlot]=1
	countSum('Linear hashing', keyCountLinear, m)

	# Quadratic Probing
	for item in itemset:
                slot= item % m
                q=0
                if hashTableQuadratic[slot] == None:
                                hashTableQuadratic[slot] = item
                                keyCountQuadratic[slot]=1
                elif hashTableQuadratic[slot]!= None:
                        nextSlot = reHashQuadratic(slot,m,q,keyCountQuadratic)
                        while hashTableQuadratic[nextSlot] != None:
                                q=q+1
                                nextSlot=reHashQuadratic(nextSlot,m,q,keyCountQuadratic)
                        if hashTableQuadratic[nextSlot] == None:
                                hashTableQuadratic[nextSlot] = item
                                keyCountQuadratic[nextSlot]=1
	countSum('Quadratic hashing', keyCountQuadratic, m)

	# Double Probing
	for item in itemset:
                slot= item % m
                r=0
                if hashTableDouble[slot] == None:
                                hashTableDouble[slot] = item
                                keyCountDouble[slot]=1

                elif hashTableDouble[slot]!= None:
                        nextSlot = reHashDouble(slot,m,r,item,keyCountDouble)
                        while hashTableDouble[nextSlot] != None:
                                r=r+1
                                nextSlot=reHashDouble(slot,m,r,item,keyCountDouble)
                        if hashTableDouble[nextSlot] == None:
                                hashTableDouble[nextSlot] = item
                                keyCountDouble[nextSlot]=1
	countSum('Double hashing', keyCountDouble, m)
	print('\n\n')

	
#Calcute the total number of probes taken by different hashing probings
def countSum(s,keyCount,a):		
        sumOfCount=0
        j=0
        for j in keyCount:
                if j != None:
                 sumOfCount=sumOfCount+j
	print(" When m is set to %d, the total number of probes taken by %s is %d" % (a, s, sumOfCount))
	
# Test when m is 1223, 1831,2447
HashCompare(itemList,1223)
HashCompare(itemList,1831)
HashCompare(itemList,2447)