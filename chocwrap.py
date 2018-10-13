money=int(input("ente your money"))
c=w=0
if money>0:                                 #chocolate count by exchange with money
    c+=money//2
w+=c                                        #wrapper count based on chocolate got
print('Chocolates:',c,'Wrapper :',w)
while(w>=3):                                #check at least 3 wrapper remaining
    d=w//3                                  #chocolate got by xchng with wrapper
    c+=d                                    #update chocolate count by ading (d)
    w=w%3+d                                 #update the wrapper count
    print('Chocolates:',c,'Wrapper :',w)
    if(w<3):                                #break if wrapper less than 3
        break
