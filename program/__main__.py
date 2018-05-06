from mod import Fun
import os


print("Witaj w programie obliczającym całki! \n")
while True:
	metoda = 1
	funkcja = 1
	print("Wybierz interesującą Cię opcję:")
	print("1. Metoda Simpsona. ")
	print("2. Kwadratura Gaussa (wariant 3). ")
	print("3. Metoda prostokątów. ")
	print("4. Metoda trapezów. ")
	print("5. Wyjscie. ")
	wybor = int(input("Wybór: "))
	if wybor == 1:
		metoda = 1
	elif wybor == 2:
		metoda = 2
	elif wybor == 3:
		metoda = 3
	elif wybor == 4:
		metoda = 4
	else:
		break
	print("Wybierz funkcję: ")
	if metoda == 2:
		print("Waga została dodana automatycznie (e ^ -x). ")
	print("1. f(x) = 1/(x+1)")
	print("2. f(x) = x*x*x+1")

	funkcja = int(input("Wybór: "))
	fun = Fun(funkcja)
	if metoda != 2:
		print("Podaj początek przedziału: ")
		a = float(input("a: "))
		print("Podaj koniec przedziału: ")
		b = float(input("b: "))
	if metoda == 1:
		print("Podaj precyzję: ")
		prec = float(input("prec: "))
		wynik = fun.simpsonP(a, b, prec)
	elif metoda == 2:
		print("Podaj liczbę węzłów (od 2 do 5): ")
		wezly = int(input("Wezly: "))
		wynik = fun.gauss(wezly)
	elif wybor == 3:
		print("Podaj liczbe prostokątów: ")
		n = int(input("n: "))
		wynik = fun.rect(a, b, n)
	elif wybor == 4:
		print("Podaj liczbe trapezów: ")
		n = int(input("n: "))
		wynik = fun.trapez(a, b, n)
	else:
		print("Nieprawidlowy wybor!")
		continue
	os.system("cls")
	print("Wynik to: ", wynik, "\n")
	wybor1 = input("Czy chcesz kontynuować (T/n) ?: ")
	if wybor1 == "n":
		break
	else:
		os.system("cls")
print("Dziękujemy za skorzystanie z programu!\n")
exit(0)