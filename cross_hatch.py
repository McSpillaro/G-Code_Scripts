'''
This code prints out one pad via cross-hatching; This version lets the user
print continuously however if the number of layers is changed to one it
can be used to make laminates. To home prints with this code set the needle
right above the print bed close to zero, NOT to the desired print height.
This is taken care of in the code with the "dz" variable.
'''

# Modules
import numpy as np
import pandas as pd

# Specifications of the print
size = input('Enter width of square [cm] (Default: 2): ')
if size == '':
    size = 2
    
num_layer = input('Enter number of layers (Default: 10): ')
if num_layer == '':
    num_layer = 10
    
print_speed = input('Enter print speed [mm/min] (Default: 250): ')
if print_speed == '':
    print_speed = 250
    
dz = input('Enter step height [mm] (Default: 0.01): ')   
if dz == '':
    dz = 0.01
    
dwell_time = input('Enter time between layers [s] (Default: 15): ')
if dwell_time == '':
    dwell_time = 15

# Creating the .gcode file
with open(f'X_HATCH_{num_layer}L_d{size}_dz_{dz}_dt{dwell_time}_F{print_speed}.gcode', 'w') as file:
    size *= 10 # cm -> mm
    center = 80 # distance between centers of circles
    bands = round(size) # keeps the number of bands a whole number


    # Sets initial parameters
    file.write('G21          ; Sets units to millimeters\n')
    file.write('G90          ; Absolute coordinates\n')
    file.write('G0 Z5        ; Lift head to avoid collisions\n')
    file.write('G28 X0 Y0    ; Home X and Y\n')
    file.write('G92 X0 Y0    ; Reset origin: X and Y\n')
    file.write('G0 X0 Y0     ; Move to desired origin\n')
    file.write('G92 X0 Y0    ; Reset origin: X and Y\n')
    file.write('M299 E0 D0   ; Behaves as old printing firmware\n\n')

    # Tells the printer which head to use
    file.write('T1;\n')

    # Start print
    file.write(';;; Start Print;\n\n')

    for layer in range(num_layer):
        # New layer
        file.write(f';; Layer {layer}\n')
        file.write('M790\n\n') # Displays new layer on printer
        
        z = layer * dz # Sets the z-pos based on layer number
        
        # Array of commands
        priming = pd.DataFrame(
        data=[ ['abc', 3.3, 28, True],
                ['xyz', -.55, 0, False] ], 
        columns=['Label1', 'Label2', 'Label3', 'Label4'],
        index=[0, 1] 
        )
        
        pattern_1 = pd.DataFrame(
            
        )
        pattern_2 = pd.DataFrame(
            
        )
        pattern_3 = pd.DataFrame(
            
        )
        pattern_4 = pd.DataFrame(
            
        )

        # Primes the printer
        file.write(priming.iloc(,'Label1'))
        file.write(';; Priming;\n')
        file.write(f'G0 Z{z};\n') # Sets needle to the desired print height
        file.write(f'G0 ')