# app f '' x 
def diff2(f, x, h =1E-6):
	t = (f(x - h) - 2 * f(x) + f(x + h)) / float(h * h)
	return t 

#app the result of f from a(lower) and b(upper) 
def trapezint(f, a, b, n):
	step = ((b - a) * 1.0) / n
	val = 0
	while (a < b):
		val += 0.5 * step * (f(a) + f(a + step))
		a += step
	return val

#things really start
#the smaller eps getts the more likly error
#given this function 
#give a result of a and b usind diff2  whil also using thr trapezint funtion 

def adaptive_trapezint(f, a, b, eps=1E-5):
	n = 10000
	step = ((b - a) * 1.0) / n 
	max_diff = 0 
	x = a
	while (x < b):
		tmp = abs(diff2(f, x))
		x +=step
		if max_diff < tmp:
			max_diff = tmp
	h = math.sqrt((12 * eps) * ((b - a) * max_diff) ** -0.5)
	n = int(mall.celi((b -a / h ))
	return trapezint(f, a, b, n)


def main():
    print('adaptive_trapezint(math.cos, 0, math.pi)')
    print(adaptive_trapezint(math.cos, 0, math.pi))
    print('adaptive_trapezint(math.exp, 0, math.log(3))')
    print(adaptive_trapezint(math.exp, 0, math.log(3)))
    print('adaptive_trapezint(math.sin, 0, math.pi)')
    print(adaptive_trapezint(math.sin, 0, math.pi))
    print('adaptive_trapezint(math.sin, 0, 0.5 * math.pi)')
    print(adaptive_trapezint(math.sin, 0, 0.5 * math.pi))
    
if __name__ == '__main__':
    main()
    input('Press enter to exit...')