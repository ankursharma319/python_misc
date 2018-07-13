import numpy as np
import pylab as pl #for the plotting
from aclab1 import rational_bezier # Bezier function
from aclabtools import *
import os
sep = os.path.sep

a=340.3 #speed of sound
v=12.5 #velocity
M=v/a #Mach number
nu=0.00001461 #kinematic viscosity
L=0.698 #chord length of aircraft wing
Re=v*L/nu

def parametric_aerofoil(w, file_path):
    """
    Creates a aerofoil.dat with coordinates in the given file_path and
    cor
    """
    # control points
    p = np.array([[1.0, 0.0], [0.5, 0.08], [0.0, -0.05]])
    q = np.array([[0.0, 0.1], [0.4, 0.2], [1.0, 0.0]])
    # weights
    zp = np.array([1, 1, 1, 1])
    zq = np.array([1, 1, w, 1])
    # calculate degree
    n = np.float(p.shape[0])
    m = np.float(p.shape[0])
    # calculate connection point
    q_start = p_end = (n / (m + n)) * p[-1, :] + (m / (m + n)) * q[0, :]
    # and add to control points
    pp = np.vstack([p, p_end])
    qq = np.vstack([q_start, q])
    
    lower = rational_bezier(pp, zp)
    upper = rational_bezier(qq, zq)
    
    # open .dat file for writing to
    data_file = open( file_path + "aerofoil.dat", "w")
    # write lower surface to file
    for i in range(0, 100):
        data_file.write("%.15f %.15f\n" %(lower[i, 0], lower[i, 1]))
    # for windows use " " instead of "\t"
    # write upper surface to file
    for i in range(0, 101):
        data_file.write("%.15f %.15f\n" %(upper[i, 0], upper[i, 1]))
    # for windows use " " instead of "\t"
    # close .dat file
    data_file.close()

def run_xfoil_wcl(w, cl, file_path, xfoil_path):
    parametric_aerofoil(w, file_path)
    commands_file = open(file_path + "commands.in", "w")
    commands_file.write(
    """load """ + file_path + """aerofoil.dat
MyAerofoil
panel
oper
visc
""" + str(Re) + """
M
""" + str(M) + """
type
1
pacc
""" + file_path + """polar.dat

iter
5000
cl """ + str(cl) + """


quit""")
    commands_file.close()
    run_xfoil_command = '\"' + xfoil_path + 'xfoilP4.exe\" < ' + file_path + 'commands.in'
    #run_xfoil_command = xfoil_path + "xfoilP4 < " + file_path + "commands.in"
    os.system(run_xfoil_command)

    #--------------------------------------------------------------------
    aero_data_file = open(file_path + "polar.dat")
    
    lines = aero_data_file.readlines()
    
    # close file
    aero_data_file.close()
    
    # delete Xfoil output file ready for next Xfoil run *** use del for Windows
    #os.system("rm -f " + file_path + "polar.dat")
    os.remove(file_path + "polar.dat")
    os.remove(file_path + "aerofoil.dat")
    os.remove(file_path + "commands.in")
    
    cl = np.float(lines[-1][11: 17])
    cd = np.float(lines[-1][20: 27])
    return cd


def parameter_sweep(w_array, cl, file_path, xfoil_path):
    cd_array = np.zeros([len(w_array), 1])
    for i in range(0, len(w_array)):
        cd_array[i] = run_xfoil_wcl(w_array[i], cl, file_path, xfoil_path)
    return cd_array

file_path = "C:\\xf\\2\\"
xfoil_path = "C:\\xf\\"
#parametric_aerofoil(1, file_path)
#print run_xfoil_wcl(1.1, 0.8433, file_path, xfoil_path)
#w_array = np.linspace (0.6 , 1.2 , 11)
#cd = parameter_sweep(w_array, 0.843, file_path , xfoil_path)
###
#print mls_curve_fit(w_array, cd, 1)