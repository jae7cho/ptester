import matplotlib.pyplot as plt

def ptest_scatter(x,y,marker='.',s=10):
    fig,ax = plt.subplots()
    plt.scatter(x,y,marker=marker,s=s)
    plt.show()
