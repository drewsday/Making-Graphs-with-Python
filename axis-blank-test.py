from pylab import *

t = arange(0.0,10.0,.01)
s = 0.0063*t**2 + 0.0

##scatter(t,s, color='blue')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}
matplotlib.rc('font', **font)

xlim(xmin=-0.15,xmax=12.1)
ylim(ymin=-.15,ymax=2.1)
grid(True)
xlabel('time (s)')
ylabel('position (m)', rotation=90,)

title('Final Result', y=1.04)

xticks([4,8,12])
yticks([1,2])


setp(gca(), frame_on=False)
gcf().subplots_adjust(bottom=0.20)

axhline(linewidth=2, color='black')
axvline(linewidth=2, color='black')

savefig('axis-blank-test2.png')

show()
