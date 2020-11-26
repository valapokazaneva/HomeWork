start = int(input("¬ведите начало интервала: "))
end = int(input("¬ведите конец интервала: "))
for i in range(start-1,end+1):
            delitel=2
            schet=0            
            if i%delitel==0 and delitel<i:
                        delitel=delitel+1
                        schet=schet+1
            if i>0 and schet==0:
                        print (i)