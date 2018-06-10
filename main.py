from __future__ import print_function

import stock_data_reader as reader
import stock_data_ploter as ploter
import stock_data_analyze as analysis

if __name__ == "__main__":
	days = 100
	[_date, _volumes, _values, _open, _highest, _lowest, _close, _delta] = reader.read_one_stock()
	[MA5, MA10, MA20, MA60, MA120, MA240, r, k, d] = analysis.technical_analysis(_date, _volumes, _values, _open, _highest, _lowest, _close, _delta)

	ploter.plot_stock_close(_date, _close, days)
	ploter.plot_stock_MA(MA5, MA10, MA20, days)
#	ploter.plot()

	[WMA5, WMA10, WMA20, WMA60, WMA120, WMA240] = analysis.weight_ma(_date, _volumes, _values, _open, _highest, _lowest, _close, _delta)
	ploter.plot_stock_close(_date, _close, days)
	ploter.plot_stock_WMA(WMA5, WMA10, WMA20, days)
	ploter.plot()
