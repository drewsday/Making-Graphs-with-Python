from pylab import *

t = arange(0.0,2.0,.01)
s = 0.25*t + 0.75
scatter(t,s, color='blue')

hold(True)

t = arange(2.0,6.0,.01)
s = ones(len(t))
s = s * 1.25
scatter(t,s, color='blue')

t = arange(6.0,10.0,.01)
s = 0.078125*(t-10.0)**2 + 0.0
scatter(t,s, color='blue')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}
matplotlib.rc('font', **font)

xlim(xmin=-0.15,xmax=10)
ylim(ymin=-0.05,ymax=1.5)
grid(True)
xlabel('time (s)')
ylabel('position (m)', rotation=90,)

xticks(arange(0,10,2))
yticks(arange(0,2,.5))


setp(gca(), frame_on=False)

gcf().subplots_adjust(bottom=0.20)
axhline(linewidth=2, color='black')
axvline(linewidth=2, color='black')

savefig('piecewise.png')

show()
