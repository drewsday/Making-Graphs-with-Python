from pylab import *
import mpld3 


t = arange(0.0,10.0,.01)
s = 1/(t+0.5) - 0.15

scatter(t,s, color='blue')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}
matplotlib.rc('font', **font)

xlim(xmin=-0.15,xmax=10)
ylim(ymin=-0.25,ymax=1.5)
grid(True)
xlabel('t')
ylabel('s', rotation=0,)

xticks([0])
yticks([0])


setp(gca(), frame_on=False)


axhline(linewidth=2, color='black')
axvline(linewidth=2, color='black')

savefig('curve4.png')

plt = mpld3.show()
#show()
#plt.savefig('mpld3.png')
mpld3.save_html(plt,'test.html')