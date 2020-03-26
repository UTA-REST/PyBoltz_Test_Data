import numpy as np
from tables import *
from Definitions import *

# import magboltz outputs for ArCH4 ( 90% - 10%)
MBAr = np.load("ArCH4.npy")

# import Data for ArCH4 ( 90% - 10%)
ArDl = np.genfromtxt("ArCH4-Dl.csv", delimiter=',')
ArDt = np.genfromtxt("ArCH4-Dt.csv", delimiter=',')
ArV = np.genfromtxt("ArCH4-vel.csv", delimiter=',')

magB    = np.array([0.9944e4, 0.8642e4 ,0.7509e3, 0.6307e4, 0.1629e4, 0.1218e4, 0.9223e3, 0.3616e4, 0.2429e4])
magBer  = np.array([3.87    , 2.31     ,2.62    , 3.39    , 2.92    , 2.60    , 3.43    , 2.79    , 3.13   ])

# Setup Tests.npy
TestsFile = {'data': 'file'}

# Number of tests in the .npy file
TestsFile['NTests'] = 3

# setting up the data for the first gas (CF4)
TestsFile['T1/type'] = 1 # 1 for Dl,Dt and Vel tests
                         # 2 Bfield test
                         # 3 Attachment and Ionisation rate tests
# First Test
TestsFile['T1/Input/NumberOfGases'] = 2
TestsFile['T1/Input/MaxNumberOfCollisions'] = 10*40000000.0
TestsFile['T1/Input/Enable_Penning'] = 0
TestsFile['T1/Input/Enable_Thermal_Motion'] = 1
TestsFile['T1/Input/Max_Electron_Energy'] = 0.0
TestsFile['T1/Input/GasIDs'] = [2,8,0,0,0,0]
TestsFile['T1/Input/GasFractions'] = [90,10,0,0,0,0]
TestsFile['T1/Input/TemperatureCentigrade'] = 23
TestsFile['T1/Input/Pressure_Torr'] = 750
TestsFile['T1/Input/EField'] = MBAr[80:81,4][::skip][0] # taken from data
TestsFile['T1/Input/BField_Mag'] = 0.0 
TestsFile['T1/Input/BField_Angle'] = 0.0 
TestsFile['T1/Input/Console_Output_Flag'] = 0 
TestsFile['T1/Input/Which_Angular_Model'] = 2
# Magboltz data
TestsFile['T1/Output/MBdt'] = MBAr[80:81,13][::skip][0]
TestsFile['T1/Output/MBdtE'] = MBAr[80:81,13][::skip][0]*MBAr[80:81,14][::skip][0]
TestsFile['T1/Output/MBdl'] = MBAr[80:81,11][::skip][0]
TestsFile['T1/Output/MBdlE'] = MBAr[80:81,11][::skip][0]*MBAr[80:81,12][::skip][0]
TestsFile['T1/Output/MBvel'] = MBAr[80:81,5][::skip][0]
TestsFile['T1/Output/MBvelE'] = MBAr[80:81,5][::skip][0] * MBAr[80:81,6][::skip][0]
# Argon data
TestsFile['T1/Output/dt'] = ArDt[1,1]
TestsFile['T1/Output/dtE'] = ArDt[1,1] * 0.3
TestsFile['T1/Output/dl'] = ArDl[1,1]
TestsFile['T1/Output/dlE'] = ArDl[1,1] * 0.3
TestsFile['T1/Output/vel'] = ArV[1,1]
TestsFile['T1/Output/velE'] = ArV[1,1] * 0.3


# Second Test
TestsFile['T2/Input/NumberOfGases'] = 2
TestsFile['T2/Input/MaxNumberOfCollisions'] = 10*40000000.0
TestsFile['T2/Input/Enable_Penning'] = 0
TestsFile['T2/Input/Enable_Thermal_Motion'] = 1
TestsFile['T2/Input/Max_Electron_Energy'] = 0.0
TestsFile['T2/Input/GasIDs'] = [2,8,0,0,0,0]
TestsFile['T2/Input/GasFractions'] = [91,9,0,0,0,0]
TestsFile['T2/Input/TemperatureCentigrade'] = 23
TestsFile['T2/Input/Pressure_Torr'] = 750
TestsFile['T2/Input/EField'] = 115
TestsFile['T2/Input/BField_Mag'] = 1.49703468
TestsFile['T2/Input/BField_Angle'] = 0.0
TestsFile['T2/Input/Console_Output_Flag'] = 0 
TestsFile['T2/Input/Which_Angular_Model'] = 2
# Magboltz data
TestsFile['T2/Output/MBdtr'] = 0.9944e4/0.7509e3
TestsFile['T2/Output/MBdtrE'] = (0.9944e4/0.7509e3) * np.sqrt((magBer[0]/100)**2+(magBer[2]/100)**2)
# Argon data
TestsFile['T2/Output/dtr'] = P10B[3,1]
TestsFile['T2/Output/dtrE'] = 0.5 * P10B[3,1]

np.save(os.path.join(os.path.dirname(os.path.realpath(__file__)),"Tests"), gd)
