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
import string
import math as m

# GLOBAL VARS
GLOBAL_COLUMNS = ['G', 'X', 'Y', 'Z', 'E', 'F']
X_CENTER = 70
Y_CENTER = 80

# Specifications of the print
user_input = input('Enter width of square [cm] (Default: 2): ')
if user_input == '':
    size = 2 # 1 mm -> 1 axis value (e.g. X60 to X80 = 2 cm)
else:
    size = int(user_input)
size *= 10 # cm -> mm

user_input = input('Enter number of layers (Default: 10): ')
if user_input == '':
    num_layer = 10
else:
    num_layer = int(user_input)

user_input = input('Enter print speed [mm/min] (Default: 250): ')
if user_input == '':
    print_speed = 250
else:
    print_speed = int(user_input)

user_input = input('Enter step height [mm] (Default: 0.01): ')
if user_input == '':
    dz = 0.01
else:
    dz = float(user_input)

user_input = input('Enter time between layers [s] (Default: 15): ')
if user_input == '':
    dwell_time = 15
else:
    dwell_time = int(user_input)

# Creates a dataframe based on given column and pattern data -> column => list; data => dictionary
def create_gcode_dataframe(columns, data):
    df = pd.DataFrame(data, columns=columns) 
    for i in range(len(df)): # loops through the rows in the df
        row = df.iloc[i] # accesses the info in the current row
        for column in columns:
            if row[column] not in string.digits: # formats empty values
                if column == 'E':
                    row[column] = 1
                elif column == 'F':
                    row[column] = print_speed
            row_values = ' '.join(str(f'{column}{row[column]}') for column in columns) # creates a string of all instructions for file writing
            print(row_values)
    
    return row_values

# Sets default XY positions based on size of print
X_POS = X_CENTER - (size / 2)
Y_POS = Y_CENTER - (size / 2)
    
# Dictionaries containing pattern information
# X_CENTER = 70 --- Y_CENTER = 80
def pattern_1():
    g_list = []
    x_list = []
    y_list = []
    z_list = []
    e_list = []
    f_list = []
    
    count = 0
    
    for i in range(size):
        g_list.append('1')
    
    x_val = X_POS
    while x_val < (X_POS+size-1):
        x_list.append(x_val)
        if (x_val) not in x_list:
            count += 1
        elif (x_val) in x_list and count == 1:
            count = 2
            x_list.append(x_val)
            
        n+=1
        
    n=0
    y_val = 90 # the end of the print bed size
    while n < range(size*10):
        if y_val == 90:
            y_list.append(y_val)
        
    data = {
        
    }
    
    return data


# Creating the .gcode file
with open(f'X_HATCH_{num_layer}L_d{size/10}_dz_{dz}_dt{dwell_time}_F{print_speed}.gcode', 'w') as file:
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

        file.write(';; Priming;\n')
        file.write(f'G0 Z{z};\n')  # Sets needle to the desired print height
        file.write(f'G0 X{m.floor(X_POS)} Y{m.floor(Y_POS-50)};\n\n')  # Sets needle to default XY location
        
        file.write(';; Pattern 1;\n')
        

'''
When printing, have the first layer at a flow rate of 2.000 and the succeeding layers be
a flow rate of 0.250 to allow for optimal printing quality with wt% 60 and below.
'''
