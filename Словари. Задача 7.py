dic1={1:10, 2:20}
dic2={3:30, 4:40}  
dic3={5:50, 6:60} 
dic4={**dic1, **dic2, **dic3}
proizv=1
print(dic4)
for i in dic4:
    proizv=proizv*dic4[i]
print(proizv)