start = int(input("Ââåäèòå íà÷àëî èíòåðâàëà: "))
end = int(input("Ââåäèòå êîíåö èíòåðâàëà: "))
for i in range(start-1,end+1):
            delitel=2
            schet=0            
            if i%delitel==0 and delitel<i:
                        delitel=delitel+1
                        schet=schet+1
            if i>0 and schet==0:
                        print (i)
