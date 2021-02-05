import datetime
num_people = int(input('Enter number of competitor : '))
list_name,list_score,list_time,list_hit=[],[],[],[]
for i in range (num_people):
    info = input('Please Enter (name,score,time)=')
    splitinfo = info.split(',')
    list_name.append(splitinfo[0])
    list_score.append(splitinfo[1])
    list_time.append(splitinfo[2])
    list_hit.append(float(list_score[i])/float(list_time[i]))
    
date = datetime.datetime.now()
datenew = date.strftime('%G-%m-%d %H:%M:%S')
print('\nShotgun',date.strftime('%A'),'Training',date.strftime('%Y'))
print(datenew)
print(''+'-'*120+'\n{0:-<8}{1:-<13}{2:-<12}{3:-<20}{4:-<15}{5:-<20}{6}'.format('No.','Points','Time','CompetitorName','Hit factor','State point','State percent'))
for u in range(num_people):
    o=u
    for o in range(num_people):
        if list_hit[u]>list_hit[o]:
            a,s,d,f = list_hit[u],list_name[u],list_score[u],list_time[u]
            list_hit[u],list_name[u],list_score[u],list_time[u]=list_hit[o],list_name[o],list_score[o],list_time[o]
            list_hit[o],list_name[o],list_score[o],list_time[o]= a,s,d,f

for i in range (num_people):
    stage_gg = (((list_hit[i])/(max(list_hit)))*50)
    stage_gk = (stage_gg/((max(list_hit)/(max(list_hit)))*50))*100
    print('{0:-<8}{1:-<13}{2:-<12}{3:-<20}{4:-<15}{5:-<20}{6}'.format(i+1,list_score[i],list_time[i],list_name[i],'%.4f'%list_hit[i],'%.4f'%stage_gg,'%.2f'%stage_gk))