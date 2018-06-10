import numpy as np
import sys

#STOCK=sys.argv[1]
#MA_X=sys.argv[2]
line_counts=0

def rkd(price_highest, price_lowest, price_close):
    k = np.zeros(8)
    d = np.zeros(8)
    r = np.zeros(8)
    if(len(price_close) < 8):
        return r, k, d
    tmp = 0
    r[7] = 0
    k[7] = 50
    d[7] = 50
    for idx in np.arange(8, len(price_close), 1):
        if (max(price_highest[idx-8:idx+1])-min(price_lowest[idx-8:idx+1]) > 0):
            tmp = (price_close[idx]-min(price_lowest[idx-8:idx+1]))*100/(max(price_highest[idx-8:idx+1])-min(price_lowest[idx-8:idx+1]))
			#r = np.append(r, (price_close[idx]-min(price_lowest[idx-8:idx+1]))*100/(max(price_highest[idx-8:idx+1])-min(price_lowest[idx-8:idx+1])))
        r = np.append(r, tmp)
        k = np.append(k, (r[idx]+k[idx-1]*2)/3)
        d = np.append(d, (k[idx]+d[idx-1]*2)/3)
    return r, k, d

def moving_average(values, days=3):
    ret = np.cumsum(values, dtype=float)
    ret[days:] = ret[days:] - ret[:-days]
    return ret[days - 1:] / days

def weight_moving_average(values, volumes, days):
	vol = np.cumsum(volumes, dtype=float)
	mul = np.multiply(values, volumes)
	val = np.cumsum(mul, dtype=float)
	return (val[days:] - val[:-days]) / (vol[days:] - vol[:-days])
	

def technical_analysis(date, volumes, values, open_values, highest_values, lowest_values, close_values, delta):
	line_counts = len(close_values)

	MA5=moving_average(close_values, 5)
	MA10=moving_average(close_values, 10)
	MA20=moving_average(close_values, 20)
	if line_counts < 60:
		MA60=0
	else:
		MA60=moving_average(close_values, 60)

	if line_counts < 120:
		MA120=0
	else:
		MA120=moving_average(close_values, 120)

	if line_counts < 240:
		MA240=0
	else:
		MA240=moving_average(close_values, 240)

	r,k,d=rkd(highest_values, lowest_values, close_values)

	return [MA5, MA10, MA20, MA60, MA120, MA240, r, k, d]
	#print "%.1f %.1f %.1f %.1f %.1f %.1f %.1f %.1f %.1f" % (MA5[-1], MA10[-1], MA20[-1], MA60[-1], MA120[-1], MA240[-1], r[-1], k[-1], d[-1])


def weight_ma(date, volumes, values, open_values, highest_values, lowest_values, close_values, delta):
    line_counts = len(close_values)

    WMA5  = np.zeros(line_counts-5)
    WMA5  = np.append(WMA5, weight_moving_average(close_values, volumes, 5))
    print(WMA5)
    WMA10 = np.zeros(line_counts-10)
    WMA10 = np.append(WMA10, weight_moving_average(close_values, volumes, 10))
    print(WMA10)
    WMA20 = np.zeros(line_counts-20)
    WMA20 = np.append(WMA20, weight_moving_average(close_values, volumes, 20))
    print(WMA20)
    if line_counts < 60:
        WMA60=0
    else:
        WMA60=weight_moving_average(close_values, volumes, 60)

    if line_counts < 120:
        WMA120=0
    else:
        WMA120=weight_moving_average(close_values, volumes, 120)

    if line_counts < 240:
        WMA240=0
    else:
        WMA240=weight_moving_average(close_values, volumes, 240)	

    return [WMA5, WMA10, WMA20, WMA60, WMA120, WMA240]

