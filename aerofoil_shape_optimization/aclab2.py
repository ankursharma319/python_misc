import numpy as np
import pylab as pl #for the plotting
from aclab1 import rational_bezier # Bezier function
import os
sep = os.path.sep

def bezier_spline_aerofoil(file_path):
    """
    creates a Bezier spline aerofoil with
    certain lower curve control points
    """
    # control points
    p = np.array([[1.0, 0.0], [0.5, 0.08],[0.0, -0.05]])
    q = np.array([[0.0, 0.1], [0.4, 0.2], [1.0, 0.0]])
    # weights
    zp = np.array([1, 1, 1, 1])
    zq = np.array([1, 1, 1, 1])
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
        data_file.write("%.11f %.11f\n" %(lower[i, 0], lower[i, 1]))
    # for windows use " " instead of "\t"
    # write upper surface to file
    for i in range(0, 101):
        data_file.write("%.11f %.11f\n" %(upper[i, 0], upper[i, 1]))
    # for windows use " " instead of "\t"
    # close .dat file
    data_file.close()


def run_xfoil(file_path, xfoil_path):
    bezier_spline_aerofoil(file_path)
    commands_file = open(file_path + "commands.in", "w")
    commands_file.write(
    """load """ + file_path + """aerofoil.dat
MyAerofoil
panel
oper
visc
1397535
M
0.1
type
1
pacc
""" + file_path + """polar.dat

iter
5000
cl 1.2


quit""")
    commands_file.close()
    run_xfoil_command = '\"' + xfoil_path + 'xfoilP4.exe\" < ' + file_path\
    + 'commands.in'
    #run_xfoil_command = xfoil_path + "xfoilP4 < " + file_path + "commands.in"
    os.system(run_xfoil_command)

    #--------------------------------------------------------------------
    aero_data_file = open(file_path + "polar.dat")
    
    lines = aero_data_file.readlines()
    print(lines)
    # close file
    aero_data_file.close()
    
    # delete Xfoil output file ready for next Xfoil run *** use del for Windows
    #os.system("rm -f " + file_path + "polar.dat")
    #os.remove(file_path + "polar.dat")
    
    cl = np.float(lines[-1][11: 17])
    cd = np.float(lines[-1][20: 27])
    return (cd, cl)

currentDir = os.path.dirname(os.path.abspath(__file__))
file_path = currentDir + "\\xf\\1\\"
xfoil_path = currentDir + "\\xf\\"
#bezier_spline_aerofoil(file_path)
print(run_xfoil(file_path, xfoil_path))