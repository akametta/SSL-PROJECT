import matplotlib.pyplot as p
fig1 = p.figure()
p.plot([1,2,3,5,8,10],[200,300,353,412,456,734],'g',label='n=1')
p.xlabel('No. of Clients')
p.ylabel('Latency (in ms)')
fig1.suptitle('Performance Analysis')
p.legend(loc='lower right')
fig1.savefig('fig1.jpg')
#####
fig2 = p.figure()
fig2.suptitle('Data Analysis') 
labels = 'A', 'B', 'C', 'D', 'E', 'F'
sizes = [50,100,28,56,230,80]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'blue']
explode = (0, 0, 0, 0, 0, 0)  # explode 1st slice
p.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
p.axis('equal')
p.show()
fig2.savefig('fig2.jpg')
####


