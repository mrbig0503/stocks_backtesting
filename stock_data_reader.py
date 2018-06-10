from __future__ import print_function

file_name="STOCKS/2330.txt"

def read_one_stock():
	_date=[]
	_volumes=[]
	_values=[]
	_open=[]
	_highest=[]
	_lowest=[]
	_close=[]
	_delta=[]
	_non=[]
	
	file=open(file_name, "r")
	for line in file:
		sep = line.split(" ")
		_date.append(sep[0])
		_volumes.append(int(sep[1]))
		_values.append(sep[2])
		_open.append(float(sep[3]))
		_highest.append(float(sep[4]))
		_lowest.append(float(sep[5]))
		_close.append(float(sep[6]))
		_delta.append(sep[7])
	
	return [_date, _volumes, _values, _open, _highest, _lowest, _close, _delta]
		

if __name__ == "__main__":
	[_date, _volumes, _values, _open, _highest, _lowest, _close, _delta] = read_one_stock()
	
	print(_close)
