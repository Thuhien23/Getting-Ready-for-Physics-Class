train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# convert Fahrenheit to celsius
def f_to_c(f_temp):
  return (f_temp - 32) * 5/9
#Define a variable f100_in_celsius and set it equal to the value of f_to_c with 100
f100_in_celsius = f_to_c (100)
print(f100_in_celsius)
# convert celsius to Fahrenheit
def c_to_f(c_temp):
  return c_temp * (9/5) + 32
#test function with a value of 0 Celsius
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Return mass multiplied by acceleration
def get_force(mass, acceleration):
  return mass * acceleration
train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Define a function called get_energy that takes in mass and c.
def get_energy(mass, c = 3*10**8):
  return mass * c ** 2
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy)+  " Joules.")

# Define a final function called get_work
def get_work (mass, accelebration, distance):
  return mass * accelebration * distance
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
