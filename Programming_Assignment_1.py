import random
import time
import os
import matplotlib.pyplot as plt
digitList = [4,8,16,32,64,128,256,512]

imagePath = os.getcwd()

def saveFig(figId, tight_layout=True, fig_extension="jpg", resolution=600):
    path = os.path.join(imagePath, figId + "." + fig_extension)
    print("Saving figure", figId)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)
    plt.show()

def myPlot(digit):
    x=range(0,1000)
    plt.scatter(x,timeLog,marker='+')
    plt.ylim((-0.0005,0.0019))
    plt.ylabel('Time Taken in ms')
    plt.xlabel('inputs in hundreds')
    plt.title('Performance checkup of {}-digit signed integer number'.format(digit))

'''
Group 26
Assignment 1
'''


def division(numerator,denominator):
    
    neg = False
    if numerator<0:
        neg=True
        numerator*=(-1)
    if denominator<0:
        neg=True
        denominator*=(-1)
        

    if numerator<denominator:
        numerator,denominator = denominator,numerator
    remainder = 0
    quotient = 0
    while numerator>0 and numerator>=denominator:
        numerator=numerator - denominator
        quotient+=1
    if neg:
        return -1*quotient
    else:
        return quotient

    '''denominator = divisor
    current = 1
    answer=0
    if denominator > dividend:
        return 0
    if denominator == dividend:
        return 1
    while denominator <= dividend:
        denominator <<= 1
        current <<= 1
    denominator >>= 1
    current >>= 1
    while (current>0):
        if dividend >= denominator:
            dividend -= denominator
            answer |= current
        current >>= 1
        denominator >>= 1
    return answer'''

def numRanges(digit):
    posLow = 10 ** (digit - 1)
    posHigh = 10 ** digit - 1
    negLow = -10 ** digit + 1
    negHigh = -10 ** (digit - 1)
    ranges = [(posLow, posHigh), (negLow, negHigh)]
    return ranges


def divRanNum(ranges):
    ranRange = random.choice(ranges) ## chooses between two ranges
    num1 = random.randint(*ranRange)  ## unwinding
    ranRange = random.choice(ranges)
    num2 = random.randint(*ranRange)
    return division(num1,num2)

for digit in digitList:
    ranges = numRanges(digit)
    i = 0
    result = []
    timeLog = []
    temp = 1
    for i in range(1000):
        start = time.time()
        r = divRanNum(ranges)
        timeLog.append(time.time()-start)
        result.append(r)
    print("Output of {}-digit unsigned number".format(digit))
    print(result)
    print('Average time is {0:0.6f} ms for {1}-digit signed number'.format(sum(timeLog)/len(timeLog),digit))
    print('It took {0:0.5f} seconds for {1}-digit signed integer number of 1000 random inputs'.format(sum(timeLog),digit))
    myPlot(digit)
    saveFig('{}-digit'.format(digit))
