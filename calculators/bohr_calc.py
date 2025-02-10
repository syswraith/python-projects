import time
radius = 0.53
velocity = 2.18

def find_radius(Z, N):
	answer = 0.53 * ( N * N ) / Z
	Z = str(Z)
	N = str(N)
	print("Radius of " + N + "th orbit of " + Z + " atomic number is " + str(round(answer, 2)) + " A")

def find_velocity(Z, N):
	answer = 2.18 * Z / N
	Z = str(Z)
	N = str(N)
	print("Velocity of electron in "  + N + "th orbit of " + Z + " atomic number is " + str(round(answer, 2)) + " 10^6 M/S")

def find_ke(Z, N):
	answer = 13.6 * ((Z * Z) / (N * N))
	Z = str(Z)
	N = str(N)
	print("Kinetic energy of " + N + "th orbit of " + Z + " atomic number is " + str(round(answer, 2)) + " ev")

def find_pe(Z, N):
	answer = -2 * 13.6 * ((Z * Z) / (N * N))
	Z = str(Z)
	N = str(N)
	print("Potential energy of "  + N + "th orbit of " + Z + " atomic number is " + str(round(answer, 2)) + " ev")

def find_te(Z, N):
	answer =  -13.6 * ((Z * Z) / (N * N))
	Z = str(Z)
	N = str(N)
	print("Total energy of " + N + "th orbit of " + Z + " atomic number is " + str(round(answer, 2)) + " ev")

print("Calculations for Bohr's Atomic Model, valid only for Hydrogen-like atoms")
Z = input("Enter Atomic Number: ")
N = input("Enter Shell Number: ")
Z = int(Z)
N = int(N)

find_radius(Z, N)
find_velocity(Z, N)
find_ke(Z, N)
find_pe(Z, N)
find_te(Z, N)


time.sleep(10)