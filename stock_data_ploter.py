from __future__ import print_function

import matplotlib.pyplot as plt


def plot_stock_MA(MA5, MA10, MA20, days):
	plt.plot(MA5[-days:],  'r')
	plt.plot(MA10[-days:], 'g')
	plt.plot(MA20[-days:], 'b')

def plot_stock_WMA(WMA5, WMA10, WMA20, days):
	plt.plot(WMA5[-days:], 'r+')
	plt.plot(WMA10[-days:], 'g+')
	plt.plot(WMA20[-days:], 'b+')

def plot_stock_close(dates, close_values, days):
	plt.plot(dates[-days:], close_values[-days:], 'k')

def plot():
	plt.show()	
