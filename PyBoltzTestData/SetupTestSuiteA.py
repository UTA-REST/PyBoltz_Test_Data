import numpy as np
from tables import *
from Definitions import *
import os 
# import magboltz outputs for ArCH4 ( 90% - 10%)
MBAr = np.load("ArCH4.npy")

P10B    = np.genfromtxt("P10-B.csv", delimiter=',')


# import Data for ArCH4 ( 90% - 10%)
ArDl = np.genfromtxt("ArCH4-Dl.csv", delimiter=',')
ArDt = np.genfromtxt("ArCH4-Dt.csv", delimiter=',')
ArV = np.genfromtxt("ArCH4-vel.csv", delimiter=',')

# Ionisation rate data for 100% nitrogen Gas.
Lima = np.loadtxt("Lima.csv", delimiter=',',skiprows=2)

# Magboltz transverse diffusion values from magboltz
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
TestsFile['T1/Input/EField'] = MBAr[80:81,4][::4][0] # taken from data
TestsFile['T1/Input/BField_Mag'] = 0.0 
TestsFile['T1/Input/BField_Angle'] = 0.0 
TestsFile['T1/Input/Steady_State_Threshold'] = 40.00
TestsFile['T1/Input/Console_Output_Flag'] = 0 
TestsFile['T1/Input/Which_Angular_Model'] = 2
TestsFile['T1/Comparisons'] = 3  # 1 - Compare with Magboltz Data
                                 # 2 - Compare with actual data
                                 # 3 - Does both

# Magboltz data
TestsFile['T1/Output/MBdt'] = MBAr[80:81,13][::4][0]
TestsFile['T1/Output/MBdtE'] = MBAr[80:81,13][::4][0]*MBAr[80:81,14][::4][0]
TestsFile['T1/Output/MBdl'] = MBAr[80:81,11][::4][0]
TestsFile['T1/Output/MBdlE'] = MBAr[80:81,11][::4][0]*MBAr[80:81,12][::4][0]
TestsFile['T1/Output/MBvel'] = MBAr[80:81,5][::4][0]
TestsFile['T1/Output/MBvelE'] = MBAr[80:81,5][::4][0] * MBAr[80:81,6][::4][0]
# Argon data
TestsFile['T1/Output/dt'] = ArDt[5,1]
TestsFile['T1/Output/dtE'] = ArDt[5,1] * 0.3
TestsFile['T1/Output/dl'] = ArDl[5,1]
TestsFile['T1/Output/dlE'] = ArDl[5,1] * 0.3
TestsFile['T1/Output/vel'] = ArV[5,1]*10
TestsFile['T1/Output/velE'] = ArV[5,1] * 0.3 *10


# Second Test
TestsFile['T2/type'] = 2 # 1 for Dl,Dt and Vel tests
                         # 2 Bfield test
                         # 3 Attachment and Ionisation rate tests
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
TestsFile['T2/Input/BField_Mag'] = 1.41421356
TestsFile['T2/Input/BField_Angle'] = 0.0
TestsFile['T2/Input/Console_Output_Flag'] = 0
TestsFile['T2/Input/Steady_State_Threshold'] = 1000000
TestsFile['T2/Input/Which_Angular_Model'] = 2
TestsFile['T2/Comparisons'] = 3  # 1 - Compare with Magboltz Data
                                 # 2 - Compare with actual data
                                 # 3 - Does both
# Magboltz data
TestsFile['T2/Output/MBdtr'] = 0.9944e4/0.3616e4
TestsFile['T2/Output/MBdtrE'] = (0.9944e4/0.3616e4) * np.sqrt((magBer[0]/100)**2+(magBer[7]/100)**2)
# Argon data
TestsFile['T2/Output/dtr'] = P10B[3,1]
TestsFile['T2/Output/dtrE'] = 0.5 * P10B[3,1]

# Third Test
TestsFile['T3/type'] = 3 # 1 for Dl,Dt and Vel tests
                         # 2 Bfield test
                         # 3 Attachment and Ionisation rate tests
TestsFile['T3/Input/NumberOfGases'] = 1
TestsFile['T3/Input/MaxNumberOfCollisions'] = 40000000.0
TestsFile['T3/Input/Enable_Penning'] = 0
TestsFile['T3/Input/Enable_Thermal_Motion'] = 1
TestsFile['T3/Input/Max_Electron_Energy'] = 0.0
TestsFile['T3/Input/GasIDs'] = [16,0,0,0,0,0]
TestsFile['T3/Input/GasFractions'] = [100,0,0,0,0,0]
TestsFile['T3/Input/TemperatureCentigrade'] = 23
TestsFile['T3/Input/Pressure_Torr'] = 750
TestsFile['T3/Input/EField'] = 40000
TestsFile['T3/Input/BField_Mag'] = 0.0
TestsFile['T3/Input/BField_Angle'] = 0.0
TestsFile['T3/Input/Console_Output_Flag'] = 0 
TestsFile['T3/Input/Steady_State_Threshold'] = 40.00
TestsFile['T3/Input/Which_Angular_Model'] = 2
TestsFile['T3/Comparisons'] = 3  # 1 - Compare with Magboltz Data
                                 # 2 - Compare with actual data
                                 # 3 - Does both
# Nitrogen Alpha data
TestsFile['T3/Output/AlphaSST'] = Lima[6,1]
TestsFile['T3/Output/AlphaSSTE'] = Lima[6,1]*0.5


np.save(os.path.join(os.path.dirname(os.path.realpath(__file__)),"Tests"), TestsFile)
