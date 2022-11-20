import pandas as pd
import numpy as np

class Node():
    def __init__(self,name,time):
        self.name = name
        self.time = time
        self.next = None
        
class Linklist():
    def __init__(self, node=None):
        self.head = node
        self.technologies = 0
        self.faucilities = 0

class Array_all():
    def __init__(self,Tech=None,Time=None,Perc=None):
        self.Tech=np.array([],str)
        self.Time=np.array([],int)
        self.Perc=np.array([],float) 

def is_empty(self):
    return self.head == None

def print_linklist(self):
    cur = self.head
    while cur != None:
        print('name ==',cur.name)
        print('time ==',cur.time)
        print('percent ==',cur.time/link.faucilities,'%')
        print('---------------------------------------------')
        cur = cur.next

def search(self, item):
    cur = self.head
    while cur != None:
        if cur.name == item:
            cur.time = cur.time + 1
            return True
        else:
            cur = cur.next

    return False

def append(self,name,time):
    node = Node(name,time)
    if (is_empty(self)):
        self.head = node
    else:
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = node

def choose(link,df,Minimum_Q):
    Max_Row=df.shape[0]
    for i in range(0,Max_Row):
        Tech = df.iloc[i]['投运时间']
        if(float(df.iloc[i]['设计处理能力']) < Minimum_Q):
            continue
        link.faucilities = link.faucilities + 1
        if(search(link,Tech) == False):
            link.technologies = link.technologies + 1
            append(link,Tech,1)

def linklist_to_array(self,Ar):
    cur = self.head
    while(cur != None):
        Ar.Tech = np.append(Ar.Tech,cur.name)
        Ar.Time = np.append(Ar.Time,cur.time)
        Ar.Perc = np.append(Ar.Perc,100*(cur.time/self.faucilities))
        cur = cur.next

def write_data_into_excel(data: dict):
	writer = pd.ExcelWriter(r"D:\1\Py_output\Analysis_of_Time_し尿処理施設_令和２年.xlsx")
	sheetNames = data.keys() 
	data = pd.DataFrame(data)
	for sheetName in sheetNames:
		data.to_excel(writer, sheet_name=sheetName)
	writer.save()

def print_information(self):
    print('List of Technologies:')
    print_linklist(link)
    print('')
    print('Summary of Technologies:')
    print('number of faucilities ==',link.faucilities)
    print('number of technologies ==',link.technologies)
    print('')
    print('令和２年,SUCCESS!!')
    

'''main function'''
if __name__ == '__main__':
    df = pd.read_excel(r'D:\1\Py_read\提取数据_し尿処理施設_令和２年.xlsx',index_col=0)
    df.head(0)

    link = Linklist()
    Minimum_Q = 0   #设计处理能力（万立方米/日)
    choose(link,df,Minimum_Q) #count the faucilities whose Q is over Minimum_Q, and save in linklist
       
    Ar = Array_all()
    linklist_to_array(link,Ar)
    data = {"投运时间":Ar.Tech,"次数":Ar.Time,"%":Ar.Perc}
    write_data_into_excel(data)

    print_information(link)
    
