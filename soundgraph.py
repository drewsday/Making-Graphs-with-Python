from pylab import *
W = 1000E-6
I0 = 1E-12

Li = raw_input("What is the minimum sound intensity level?")
Li = float(Li)

t = arange(1,1000,1)
#s = sqrt((t*W)/(2*pi()*I0*(10^(Li/10))))
s = sqrt((t*W)/(2*pi*I0*(10.0**(Li/10.0))))

scatter(t,s, color='blue')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}
matplotlib.rc('font', **font)

# xlim(xmin=-0.15,xmax=10)
# ylim(ymin=-0.25,ymax=1.5)
grid(True)
xlabel('t')
ylabel('s', rotation=0,)

#xticks([0])
#yticks([0])


setp(gca(), frame_on=False)


axhline(linewidth=2, color='black')
axvline(linewidth=2, color='black')

savefig('curve1.png')

show()
