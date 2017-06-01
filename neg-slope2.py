from pylab import *

t = arange(0.0,10.0,.01)
s = -0.23*t + 1.4

scatter(t,s, color='blue')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}
matplotlib.rc('font', **font)

xlim(xmin=-0.15,xmax=10)
ylim(ymin=-0.25,ymax=1.5)
grid(True)
xlabel('time (s)')
ylabel('velocity (m/s)', rotation=90,)

xticks(arange(0,10,2))
yticks(arange(-2,3,1))


setp(gca(), frame_on=False)

gcf().subplots_adjust(bottom=0.20)
axhline(linewidth=2, color='black')
axvline(linewidth=2, color='black')

savefig('velocity-graph.png')

show()
