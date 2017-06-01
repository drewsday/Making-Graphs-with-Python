from pylab import *

t = arange(0.0,10.0,.01)
s3 = 0.12*sin(2.0*pi*t/6.666) -0.20
s2 = 0.24*sin(4.0*pi/3.0*t/6.666) + 0.30
s = 0.48*sin(2.0*pi/3.0*t/6.666) + 0.75

scatter(t,s, color='blue')
scatter(t,s2, color='blue')
scatter(t,s3, color='blue')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}
matplotlib.rc('font', **font)

xlim(xmin=-0.15,xmax=10)
ylim(ymin=-0.5,ymax=1.5)
grid(False)
## xlabel('t')
## ylabel('s', rotation=0,)

xticks([])
yticks([])


setp(gca(), frame_on=False)


#axhline(linewidth=2, color='black')
#axvline(linewidth=2, color='black')

savefig('wave3.png')

show()
