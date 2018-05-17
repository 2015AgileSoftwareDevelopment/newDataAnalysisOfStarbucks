import queue
import threading
class node(object):
    def __init__(self,priority,description):
        self.priority = priority
        self.description = description
    #下面两个方法重写一个就可以了
    def __lt__(self,other):#operator < 
        return self.priority < other.priority
    def __cmp__(self,other):
        #call global(builtin) function cmp for int
        return cmp(self.priority,other.priority)
    def __str__(self):
        return '(' + str(self.priority)+',\'' + self.description + '\')'

lx=[2.1,3.1,4.1,1.0]
ly=[3.1,4.1,5.1,1.2]
k=3
x=1.3
y=1.4
def top_k(lx,ly,k,x,y):
    que = queue.PriorityQueue()
    a=[]
    for i in range(len(lx)):
        #print(''+str(lx[i])+'='+str(ly[i]))
        dis=(lx[i]-x)*(lx[i]-x)+(ly[i]-y)*(ly[i]-y)
        que.put(node(dis,i))
    for i in range(k):
        
        if(que.empty()==False):
            node1=que.get()
            #print(''+str(node1.priority)+' ='+str(node1.description))
            a.append(int(node1.description))
    return a    
b=top_k(lx,ly,k,x,y)
for i in range(len(b)):
    print('i='+str(i)+' '+str(lx[b[i]])+' '+str(ly[b[i]]))
