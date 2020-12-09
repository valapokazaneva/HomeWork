s="один два три четыре пять шесть семь"
n=3
s_list=s.split()
s2=""
for i in s_list[n:]:
    s2+=i+" "
for i in s_list[:n]:
    s2+=i+" "
print(' '.join(s_list[n:] + s_list[:n]))