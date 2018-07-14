from scipy.optimize import minimize_scalar, fmin_l_bfgs_b
from aclab3 import *

a=340.3 #speed of sound
v=12.5 #velocity
M=v/a #Mach number
nu=0.00001461 #kinematic viscosity
L=0.698 #chord length of aircraft wing
Re=v*L/nu

def one_dim_opt(x0, cl, file_path, xfoil_path):
    """
    """
    bs = [0.6, x0, 1.1]
    opt_out = minimize_scalar(run_xfoil_wcl, args=\
    (cl, file_path, xfoil_path), method="brent", bracket=bs)
    return opt_out


def four_dim_parametric_aerofoil(w, file_path):
    """
    """
    # control points
    p = np.array([[1.0, 0.0], [0.5, 0.08], [0.0, -0.05]])
    q = np.array([[0.0, 0.1], [0.4, 0.2], [1.0, 0.0]])
    # weights
    zp = np.array([1, w[2], w[3], 1])
    zq = np.array([1, w[0], w[1], 1])
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
        data_file.write("%.18f %.18f\n" %(lower[i, 0], lower[i, 1]))
    # for windows use " " instead of "\t"
    # write upper surface to file
    for i in range(0, 101):
        data_file.write("%.18f %.18f\n" %(upper[i, 0], upper[i, 1]))
    # for windows use " " instead of "\t"
    # close .dat file
    data_file.close()

def four_dim_run_xfoil_wcl(w, cl, file_path, xfoil_path):
    four_dim_parametric_aerofoil(w, file_path)
    #Re = 597193.7029
    #M = 0.0367647
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
    run_xfoil_command = '\"' + xfoil_path + 'xfoilP4.exe\" < ' + file_path\
    + 'commands.in'
    #run_xfoil_command = xfoil_path + "xfoilP4 < " + file_path + "commands.in"
    os.system(run_xfoil_command)

    #--------------------------------------------------------------------
    aero_data_file = open(file_path + "polar.dat")
    
    lines = aero_data_file.readlines()
    
    # close file
    aero_data_file.close()
    
    # delete Xfoil output file ready for next Xfoil run *** use del for Windows
    #os.system("rm -f " + file_path + "polar.dat")
    cd = np.float(lines[-1][20: 27])

    os.remove(file_path + "polar.dat")
    os.remove(file_path + "aerofoil.dat")
    os.remove(file_path + "commands.in")

    return cd


def four_dim_opt(x0, weight_limits, cl, file_path, xfoil_path):
    """
    """
    opt_out = fmin_l_bfgs_b(four_dim_run_xfoil_wcl, x0, args=\
    (cl, file_path, xfoil_path), bounds = weight_limits,\
    epsilon = 0.05, approx_grad = True)
    return opt_out

file_path = "C:\\xf\\2\\"
xfoil_path = "C:\\xf\\"

#print one_dim_opt(1.0, 0.843, file_path, xfoil_path)
x0 = [1, 1, 1, 1]
weight_limits = ((0.5, 1.3),(0.5, 1.3),(0.5, 1.3),(0.5, 1.3))
print(four_dim_opt(x0, weight_limits, 0.843, file_path, xfoil_path))