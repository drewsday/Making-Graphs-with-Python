from pylab import *

##t = arange(0.0,10.0,.01)
##s = 0.0063*t**2 + 0.0

##scatter(t,s, color='blue')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}
matplotlib.rc('font', **font)

xlim(xmin=-0.15,xmax=10)
ylim(ymin=-1.5,ymax=1.5)
grid(True)
xlabel('time (s)')
ylabel('acceleration (m/s/s)', rotation=90,)

xticks([0])
yticks([0])


setp(gca(), frame_on=False)


axhline(linewidth=2, color='black')
axvline(linewidth=2, color='black')

savefig('axis-blank.png')

show()
