from pylab import *

t = arange(0.0,10.0,.01)
s = -0.13*t + 0.70

scatter(t,s, color='blue')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}
matplotlib.rc('font', **font)

xlim(xmin=-0.15,xmax=10)
ylim(ymin=-.75,ymax=.75)
grid(True)
xlabel('t')
ylabel('v', rotation=0,)

xticks([0])
yticks([0])


setp(gca(), frame_on=False)


axhline(linewidth=2, color='black')
axvline(linewidth=2, color='black')

savefig('curve1.png')

show()
