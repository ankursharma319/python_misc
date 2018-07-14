import numpy as np
import matplotlib.pyplot as plt

def zeros(length):
    """
    Returns an array of size length populated with 0s
    """
    return np.array(np.zeros([length]))


def sphereCd(Re):
    """
    Returns the drag coefficient based on Re number
    """
    cd = (24/Re) + (2.6*(Re/5))/(1+(Re/5)**1.52)
    + (0.411*(Re/263000)**-7.94)/(1+(Re/263000)**-8)
    + (Re**0.8)/461000
    return cd

# ------------------------------------CASE #1------------------------------
# ------------------------------------CASE #1------------------------------


# -------------------------------Constants-----------------------------------

tube_length = 0.15
k = 50 # spring constant
rho = 1.2 # density of air
nu = 1.48e-5 # kinematic viscosity of air
g = 9.81 # acceleration due to gravity
d = 0.04 # diameter of sphere
S = np.pi * (d / 2)**2 # frontal area of sphere
m = 0.015 # mass of sphere
min_alpha = (45.0)*(np.pi/180.0)
max_alpha = (80.0)*(np.pi/180.0)

# -------------------------------Bungee code---------------------------------
# -------------------------------Bungee code---------------------------------


deltaT = 0.00001 # We'll need a much smaller time step for bungee simulation
l = round(0.1 / deltaT)
x = zeros(l) # spring length
x[0] = 0.9*tube_length # initial deflection


v = zeros(l) # velocity
Re = zeros(l) # Reynolds number
cd = zeros(l) # drag coefficient
f = zeros(l) # spring force
v[0] = 0.001 # need to use a very small initial velocity to avoid divide by zeros
Re[0] = v[0] * d / nu # initial Reynolds number
cd[0] = sphereCd(Re[0]) # initial drag coefficient


i = 0;
while (x[i] > 0):
    fs = x[i] * k
    fd = -0.5 * rho * v[i]**2 * S * cd[i]
    f[i] = fs + fd
    a = (fs + fd) / m
    v[i+1] = v[i] + a * deltaT
    x[i+1] = x[i] - v[i] * deltaT
    Re[i] = v[i+1] * S / nu
    cd[i+1] = sphereCd(Re[i])
    i = i + 1
    # print(v[i])
# plot(x[0:i], v[0:i])
# pl.plot(x[0:i], v[0:i], label="Case 1")


# -------------------------------Trajectory code----------------------------
# -------------------------------Trajectory code----------------------------

    
# constants
deltaT = 0.001 # time step for trajectory simulation
l = round(5/deltaT)


# initialize arrays
# we expect the sphere to be in the air no more than three seconds
# so set our array to be of length 3/deltaT (this is quite crude, but works!)
# now initialize arrays for quntities of interest
h = zeros(l) # height of sphere
x = zeros(l) # horizontal ordinate of sphere
vX = zeros(l) # horizontal velocity
vY = zeros(l) # vertical velocity
Re = zeros(l) # Reynolds number
cd = zeros(l) # drag coefficient


# starting conditions
alpha = min_alpha # initial angle of trajectory
h[0] = np.sin(alpha)*tube_length # height of sphere at start
x[0] = 0 # horizontal ordinate of sphere at start
v0 = v[i] # initial velocity of sphere taken from v array from bungee code
vX[0] = v0 * np.cos(alpha) # initial horizontal velocity
vY[0] = v0 * np.sin(alpha) # initial vertical velocity
Re[0] = np.sqrt(vX[0]**2 + vY[0]**2) * d / nu # initial Reynolds number
cd[0] = sphereCd(Re[0]) # initial drag coefficient


i = 0
while h[i] > 0:
    vY[i+1] = vY[i] - (0.5 * rho * vY[i]**2 * S * cd[i] / m) * deltaT
    vX[i+1] = vX[i] - (0.5 * rho * vX[i]**2 * S * cd[i] / m) * deltaT
    vY[i+1] = vY[i+1] - g * deltaT
    x[i+1] = x[i] + vX[i+1] * deltaT
    h[i+1] = h[i] + vY[i+1] * deltaT
    Re[i+1] = np.sqrt(vX[i+1]**2 + vY[i+1]**2) * d / nu
    cd[i+1] = sphereCd(Re[i+1])
    i = i + 1

plt.plot(x[0:i], h[0:i], 'b-', label="Case #1: {} deg".format(alpha*180/np.pi))


# ------------------------------------CASE #2------------------------------
# ------------------------------------CASE #2------------------------------

# Uncomment any one of these constants you want to change for case 2
# Uncomment any one of these constants you want to change for case 2

#tube_length = 0.30
#k = 15.2 # spring constant
#rho = 1.2 # density of air
#nu = 1.48e-5 # kinematic viscosity of air
#g = 9.81 # acceleration due to gravity
#d = 0.04 # diameter of sphere
#S = np.pi * (d / 2)**2 # frontal area of sphere
#m = 0.015 # mass of sphere
alpha = max_alpha # initial angle of trajectory


# -------------------------------Bungee code---------------------------------
# -------------------------------Bungee code---------------------------------


deltaT = 0.00001 # We'll need a much smaller time step for bungee simulation
l = round(0.2 / deltaT)
x = zeros(l) # spring length
x[0] = 0.9*tube_length # initial deflection


v = zeros(l) # velocity
Re = zeros(l) # Reynolds number
cd = zeros(l) # drag coefficient
f = zeros(l) # spring force
v[0] = 0.001 # need to use a very small initial velocity to avoid divide by zeros
Re[0] = v[0] * d / nu # initial Reynolds number
cd[0] = sphereCd(Re[0]) # initial drag coefficient


i = 0;
while (x[i] > 0):
    fs = x[i] * k
    fd = -0.5 * rho * v[i]**2 * S * cd[i]
    f[i] = fs + fd
    a = (fs + fd) / m
    v[i+1] = v[i] + a * deltaT
    x[i+1] = x[i] - v[i] * deltaT
    Re[i] = v[i+1] * S / nu
    cd[i+1] = sphereCd(Re[i])
    i = i + 1

# -------------------------------Trajectory code----------------------------
# -------------------------------Trajectory code----------------------------

# initialize arrays
# we expect the sphere to be in the air no more than three seconds
# so set our array to be of length 3/deltaT (this is quite crude, but works!)
deltaT = 0.001 # time step for trajectory simulation
l = round(5/deltaT)

# now initialize arrays for quntities of interest
h = zeros(l) # height of sphere
x = zeros(l) # horizontal ordinate of sphere
vX = zeros(l) # horizontal velocity
vY = zeros(l) # vertical velocity
Re = zeros(l) # Reynolds number
cd = zeros(l) # drag coefficient

# starting conditions
h[0] = np.sin(alpha)*tube_length # height of sphere at start
x[0] = 0 # horizontal ordinate of sphere at start
v0 = v[i]
vX[0] = v0 * np.cos(alpha) # initial horizontal velocity
vY[0] = v0 * np.sin(alpha) # initial vertical velocity
Re[0] = np.sqrt(vX[0]**2 + vY[0]**2) * d / nu # initial Reynolds number
cd[0] = sphereCd(Re[0]) # initial drag coefficient

j = 0
while h[j] > 0:
    vY[j+1] = vY[j] - (0.5 * rho * vY[j]**2 * S * cd[j] / m) * deltaT
    vX[j+1] = vX[j] - (0.5 * rho * vX[j]**2 * S * cd[j] / m) * deltaT
    vY[j+1] = vY[j+1] - g * deltaT
    x[j+1] = x[j] + vX[j+1] * deltaT
    h[j+1] = h[j] + vY[j+1] * deltaT
    Re[j+1] = np.sqrt(vX[j+1]**2 + vY[j+1]**2) * d / nu
    cd[j+1] = sphereCd(Re[j+1])
    j = j + 1

plt.plot(x[0:j], h[0:j], 'r-', label="Case #2: {} deg".format(alpha*180/np.pi))
plt.xlabel('X position (m)')
plt.ylabel('Height (m)')
plt.title('Flight trajectory with different initial angle of launch')
plt.legend()
plt.show()

# ----------------------------NOTES----------------------------------------
#with following consts - 
#
#tube_length = 0.15
#k = 50 # spring constant
#rho = 1.2 # density of air
#nu = 1.48e-5 # kinematic viscosity of air
#g = 9.81 # acceleration due to gravity
#d = 0.04 # diameter of sphere
#S = np.pi * (d / 2)**2 # frontal area of sphere
#m = 0.015 # mass of sphere
#min_alpha = (45.0)*(np.pi/180.0)
#max_alpha = (80.0)*(np.pi/180.0)
#

#we get the following dimensions for different target distances (meters)
# target(m)  angle    x_length      height
#   2        80 deg     0.026       0.148
#   2.5      78 deg     0.031       0.147
#   3        75 deg     0.039       0.145
#   3.5      72 deg     0.046       0.143
#   4        70 deg     0.051       0.141
#   4.5      66 deg     0.061       0.137
#   5        62 deg     0.070       0.132
#   5.5      58 deg     0.079       0.127
#   6        45 deg     0.106       0.106