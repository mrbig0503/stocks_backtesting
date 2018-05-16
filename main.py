from __future__ import print_function

from stock_data_reader import read_one_stock
from stock_data_ploter import plot_one_stock

if __name__ == "__main__":
	[_date, _volumes, _values, _open, _highest, _lowest, _close, _delta] = read_one_stock()
	plot_one_stock(_date, _close)
	
