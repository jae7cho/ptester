import matplotlib.pyplot as plt

def ptest_scatter(x,y,figsize,marker,s):
    plt.figure(figsize=(figsize[0],figsize[1]))
    plt.scatter(x,y,marker,s)