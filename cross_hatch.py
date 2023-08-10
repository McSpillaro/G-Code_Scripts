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

# GLOBAL VARS
global_columns = ['G', 'X', 'Y', 'Z', 'E', 'F']

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

# Creates a dataframe based on given column and pattern data -> column => list; data => dictionary
def create_gcode_dataframe(columns, data):
    df = pd.DataFrame(data, columns=columns) 
    for i in range(len(df)): # loops through the rows in the df
        row = df.iloc[i] # accesses the info in the current row
        for column in columns:
            if row[column] == '': # formats empty values
                continue
            row_values = ' '.join(str(f'{column}{row[column]}') for column in columns) # creates a string of all instructions for file writing
            print(row_values)
    
    return row_values
    
# Creating the .gcode file
with open(f'X_HATCH_{num_layer}L_d{size}_dz_{dz}_dt{dwell_time}_F{print_speed}.gcode', 'w') as file:
    size *= 10  # cm -> mm
    center = 80  # distance between centers of circles
    bands = round(size)  # keeps the number of bands a whole number

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
        file.write('M790\n\n')  # Displays new layer on printer

        z = (layer + 1) * dz  # Sets the z-pos based on layer number
        
        # PRIMING INSTRUCTIONS
        priming_dictionary = {
            'G': [1, 2, 3],
            'X': [1, 2, 3],
            'Y': [1, 2, 3],
            'Z': [1, 2, 3]
        }
        
        file.write(create_gcode_dataframe(global_columns, priming_dictionary))

    file.write(';; Priming;\n')
    file.write(f'G0 Z{z};\n')  # Sets needle to the desired print height
    file.write(f'G0 ')

'''
When printing, have the first layer at a flow rate of 2.000 and the succeeding layers be
a flow rate of 0.250 to allow for optimal printing quality with wt% 60 and below.
'''