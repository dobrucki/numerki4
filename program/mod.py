from functions import *
from math import fabs, e

class Fun:
	# Stablicowane miejsca zerowe wielomianów Laguerre'a
	zeroes = [[0.585786437627, 3.414213562373], [0.415774556783, 2.294280360279, 6.289945082937],[0.322547689619, 1.745761101158, 4.536620296921, 9.395070912301],[0.263560319718, 1.413403059107, 3.596425771041, 7.085810005859, 12.640800844276]]
	weights = [[0.853553390593, 0.146446609407], [0.711093009929, 0.278517733569, 0.0103892565016], [0.603154104342, 0.357418692438, 0.0388879085150, 0.000539294705561],[0.521755610583, 0.398666811083, 0.0759424496817 , 0.00361175867992, 0.0000233699723858]]
	def __init__(self, n):
		if n == 2:
			self.f = f2
		else:
			self.f = f1

	def simpson(self, a, b):
		h = (b - a) / 2
		wynik = self.f(a) + 4 * self.f(a + h) + self.f(b)
		wynik *= h / 3
		return wynik

	def simpsonP(self, a, b, prec):
		step = (b - a) / 2
		last = self.simpson(a, b)
		acct = self.simpson(a, step) + self.simpson(step, b)
		wynik = acct
		n = 3
		while fabs(acct - last) > prec:
			last = acct
			wynik = 0
			i = 0
			step = (b - a) / n
			x0 = a
			x1 = x0 + step
			while i < n:
				wynik += self.simpson(x0, x1)
				x0 = x1
				x1 += step
				i += 1
			acct = wynik
			n += 1
		return acct

	def gauss(self, n):
		wynik = 0
		i = 0
		while i < n:
			wynik += self.weights[n-2][i] * self.f(self.zeroes[n-2][i])
			i += 1
		# wynik = 0.853553390593 * self.f(0.585786437627)
		# wynik += 0.146446609407 * self.f(3.414213562373)
		return wynik

	def rect(self, a, b, n):
		i = 0
		step = fabs(b - a) / n
		wynik = 0
		x = a
		while i < n:
			wynik += step * self.f(x)
			x += step
			i += 1
		return wynik

	def trapez(self, a, b, n):
		i = 0
		step = fabs(b - a) / n
		wynik = 0
		x = a
		while i < n:
			wynik += (self.f(x) + self.f(step + x)) * step / 2
			x += step
			i += 1
		return wynik
