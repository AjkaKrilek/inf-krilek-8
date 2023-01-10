fr=open('data/meteo_stanice.txt','r',encoding='utf-8')
pocet_merani = sum(1 for line in open("data/meteo_stanice.txt"))
print('pocet merani',pocet_merani)
with open('data/meteo_stanice.txt', 'r') as f:
    for line in f:
        y = line.split()
        print(y[3])

#sorrko ale zvysok mi nejak nefungoval