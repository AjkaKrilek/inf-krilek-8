fr=open('data/hada.txt','r',encoding='utf-8')
pocet_hier = sum(1 for line in open("data/hada.txt"))
print('pocet hier',pocet_hier)
pocet_krokov=0
with open('data/hada.txt','r') as f:
    lines = f.readlines()
    longest_line = max(lines, key=len)
    #print('The longest line is:', longest_line)
    for i in longest_line:
            pocet_krokov+=1
print('pocet krokov',pocet_krokov)