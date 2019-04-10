import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
def remove_n(string):
    if type(string) == str:
        return string.split('\n')[0]
    else:
        return string
def parse():
    
    fileobj = open("ASFG_Ts.txt",'r')
    temp_list = fileobj.readlines()
    days = np.zeros(np.size(temp_list)-4)
    lat = np.zeros(np.size(temp_list)-4)
    long = np.zeros(np.size(temp_list)-4)
    temps = np.zeros(np.size(temp_list)-4)
    
    for line in range (3,np.size(temp_list)-1):
        data_list = temp_list[line].split ('\t')
        if (np.size(data_list)<4):
            data_list[0] = float(remove_n(data_list[0]))
            data_list.append(0)
            data_list.append(0)
            data_list.append(0)    
        days [line-3] = data_list[0]
        if (data_list[1] != ''):
            lat[line-3] = float(remove_n(data_list[1]))
        # if (data_list[2] != ''):
        #     long[line-3] = float(remove_n(data_list[2]))
        print (data_list[2])
        # if (data_list[3] != ''):
        #     temps[line-3] = float(remove_n(data_list[3]))
    # print(days)
    # print(lat)
    # print(long)
    # print(temps)
    fileobj.close()