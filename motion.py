from pylab import *

t = arange(0.0,4.0,.001)
s = t**3 - 6*t**2 + 9*t - 2

scatter(t,s, color='blue')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}
matplotlib.rc('font', **font)

xlim(xmin=-0.15,xmax=4)
ylim(ymin=-2.5,ymax=2.5)
grid(True)
xlabel('time (s)')
ylabel('position (m) ', rotation=90,)

xticks([0,1,2,3,4])
yticks([0])


setp(gca(), frame_on=False)


axhline(linewidth=2, color='black')
axvline(linewidth=2, color='black')

savefig('motion.png')

show()
