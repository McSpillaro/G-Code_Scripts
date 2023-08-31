'''
This code prints out one pad via cross-hatching; This version lets the user
print continuously however if the number of layers is changed to one it
can be used to make laminates. To home prints with this code set the needle
right above the print bed close to zero, NOT to the desired print height.
This is taken care of in the code with the "dz" variable.
'''

# Modules
import pandas as pd
import math as m

# GLOBAL VARS
GLOBAL_COLUMNS = ['G', 'X', 'Y', 'Z', 'E', 'F']
X_CENTER = 70
Y_CENTER = 80

# Specifications of the print
user_input = input('Enter width of square [cm] (Default: 2): ')
if user_input == '':
    size = 2  # 1 mm -> 1 axis value (e.g. X60 to X80 = 2 cm)
else:
    size = int(user_input)
size *= 10  # cm -> mm

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
    list_elems = []
    for i in range(len(df)):  # loops through the rows in the df
        row = df.iloc[i]  # accesses the info in the current row

        # creates a string of all instructions for file writing
        row_values = ' '.join(
            str(f'{column}{row[column]}') for column in columns)
        list_elems.append(row_values)

    return list_elems


# Sets default XY positions based on size of print
X_POS = X_CENTER - (size / 2)
Y_POS = Y_CENTER - (size / 2)

# Dictionaries containing pattern information
# X_CENTER = 70 --- Y_CENTER = 80


def pattern_1(z):
    g_list = []
    x_list = []
    y_list = []
    z_list = []
    e_list = []
    f_list = []

    x_val = X_POS  # border of print in X
    y_val_min = Y_POS  # border of print in Y (min)
    y_val_max = Y_POS + size  # border of print in Y (max)

    x_list.append(m.floor(x_val))
    x_val += 1

    while x_val < (X_POS+size):
        for i in range(2):
            x_list.append(m.floor(x_val))
        x_val += 1

    for i in range(len(x_list)):
        g_list.append('1')
        z_list.append(z)
        e_list.append('1')
        f_list.append(str(print_speed))

    for i in range(m.floor((len(x_list)+1) / 4)):
        for j in range(2):
            y_list.append(m.floor(y_val_max))
        for k in range(2):
            y_list.append(m.floor(y_val_min))
    y_list.pop(len(y_list)-1)

    data = {
        'G': g_list,
        'X': x_list,
        'Y': y_list,
        'Z': z_list,
        'E': e_list,
        'F': f_list
    }

    return data


def pattern_22(z):
    g_list = []
    x_list = []
    y_list = []
    z_list = []
    e_list = []
    f_list = []

    x_val_right = X_POS  # right edge
    x_val_left = X_POS + size  # left edge
    y_val_up = Y_POS  # top edge
    y_val_down = Y_POS + size  # bottom edge

    # For X-axis
    step_1 = x_val_right + 1
    step_2 = x_val_right + 2

    while (step_2 < x_val_left) and (step_2 != x_val_left):
        step_1 += 2
        step_2 += 2
        x_list.append(m.floor(x_val_right))
        x_list.append(m.floor(x_val_right))
        x_list.append(m.floor(step_1))
        x_list.append(m.floor(step_2))
    
    step_1 = x_val_right
    step_2 = x_val_right + 1 
        
    while (step_2 < x_val_left) and (step_2 != x_val_left - 1):
        step_1 += 2
        step_2 += 2
        x_list.append(m.floor(step_1))
        x_list.append(m.floor(step_2))
        x_list.append(m.floor(x_val_left))
        x_list.append(m.floor(x_val_left))

    # For Y-axis
    step_1 = y_val_up + 1
    step_2 = y_val_up + 2

    while (step_2 < y_val_down) and (step_2 != y_val_down):
        step_1 += 2
        step_2 += 2
        y_list.append(m.floor(step_1))
        y_list.append(m.floor(step_2))
        y_list.append(m.floor(y_val_up))
        y_list.append(m.floor(y_val_up))

    step_1 = y_val_up + 1
    step_2 = y_val_up + 2

    while (step_2 < y_val_down) and (step_2 != y_val_down):
        step_1 += 2
        step_2 += 2
        y_list.append(m.floor(y_val_down))
        y_list.append(m.floor(y_val_down))
        y_list.append(m.floor(step_1))
        y_list.append(m.floor(step_2))

    # For non XY values
    for i in range(len(x_list)):
        g_list.append('1')
        z_list.append(z)
        e_list.append('1')
        f_list.append(str(print_speed))

    data = {
        'G': g_list,
        'X': x_list,
        'Y': y_list,
        'Z': z_list,
        'E': e_list,
        'F': f_list
    }

    return data

#def pattern_44(z):
    g_list = []
    x_list = []
    y_list = []
    z_list = []
    e_list = []
    f_list = []

    x_val_right = X_POS  # right edge
    x_val_left = X_POS + size  # left edge
    y_val_up = Y_POS  # top edge
    y_val_down = Y_POS + size  # bottom edge

    # For X-axis
    step_1 = x_val_left - 1
    step_2 = x_val_left - 2

    while (step_2 > x_val_right) and (step_2 != x_val_right):
        step_1 -= 2
        step_2 -= 2
        x_list.append(m.floor(x_val_left))
        x_list.append(m.floor(x_val_left))
        x_list.append(m.floor(step_1))
        x_list.append(m.floor(step_2))
    
    step_1 = x_val_left
    step_2 = x_val_left - 1
        
    while (step_2 > x_val_right) and (step_2 != x_val_right):
        step_1 -= 2
        step_2 -= 2
        x_list.append(m.floor(step_1))
        x_list.append(m.floor(step_2))
        x_list.append(m.floor(x_val_left))
        x_list.append(m.floor(x_val_left))

    # For Y-axis
    step_1 = y_val_down - 1
    step_2 = y_val_down - 2

    while (step_2 > y_val_up) and (step_2 != y_val_up):
        step_1 -= 2
        step_2 -= 2
        y_list.append(m.floor(step_1))
        y_list.append(m.floor(step_2))
        y_list.append(m.floor(y_val_down))
        y_list.append(m.floor(y_val_down))

    step_1 = y_val_down - 1
    step_2 = y_val_down - 2

    while (step_2 > y_val_up) and (step_2 != y_val_up):
        step_1 -= 2
        step_2 -= 2
        y_list.append(m.floor(y_val_down))
        y_list.append(m.floor(y_val_down))
        y_list.append(m.floor(step_1))
        y_list.append(m.floor(step_2))

    # For non XY values
    for i in range(len(x_list)):
        g_list.append('1')
        z_list.append(z)
        e_list.append('1')
        f_list.append(str(print_speed))
    
    data = {
        'G': g_list,
        'X': x_list,
        'Y': y_list,
        'Z': z_list,
        'E': e_list,
        'F': f_list
    }

    return data

#def pattern_2(z):
    g_list = []
    x_list = []
    y_list = []
    z_list = []
    e_list = []
    f_list = []

    x_val_right = X_POS  # right edge
    x_val_left = X_POS + size  # left edge
    y_val_up = Y_POS  # top edge
    y_val_down = Y_POS + size  # bottom edge

    # For X-Axis values
    step = x_val_right
    while (step < x_val_left) and (step != x_val_left - 1):
        step += 1
        x_list.append(m.floor(step+1))
        x_list.append(m.floor(x_val_right))
        x_list.append(m.floor(x_val_right))
        x_list.append(m.floor(step+1))

    step = x_val_right
    while (step < x_val_left) and (step != x_val_left - 1):
        step += 1
        x_list.append(m.floor(x_val_left))
        x_list.append(m.floor(x_val_left))
        x_list.append(m.floor(step))
        x_list.append(m.floor(step+1))

    # For Y-Axis values
    step = y_val_up
    while (step < y_val_down) and (step != y_val_down - 1):
        step += 1
        y_list.append(m.floor(y_val_up))
        y_list.append(m.floor(step))
        y_list.append(m.floor(step+1))
        y_list.append(m.floor(y_val_up))

    step = y_val_up
    while (step < y_val_down) and (step != y_val_down - 1):
        step += 1
        y_list.append(m.floor(step))
        y_list.append(m.floor(step+1))
        y_list.append(m.floor(y_val_down))
        y_list.append(m.floor(y_val_down))

    # For non XY values
    for i in range(len(x_list)):
        g_list.append('1')
        z_list.append(z)
        e_list.append('1')
        f_list.append(str(print_speed))

    data = {
        'G': g_list,
        'X': x_list,
        'Y': y_list,
        'Z': z_list,
        'E': e_list,
        'F': f_list
    }

    return data


def pattern_3(z):
    g_list = []
    x_list = []
    y_list = []
    z_list = []
    e_list = []
    f_list = []

    y_val = Y_POS  # border of print in Y
    x_val_min = X_POS  # border of print in X (min)
    x_val_max = X_POS + size  # border of print in X (max)

    y_list.append(m.floor(y_val))
    y_val += 1

    while y_val < (Y_POS+size):
        for i in range(2):
            y_list.append(m.floor(y_val))
        y_val += 1

    for i in range(len(y_list)):
        g_list.append('1')
        z_list.append(z)
        e_list.append('1')
        f_list.append(str(print_speed))

    for i in range(m.floor((len(y_list)+1) / 4)):
        for j in range(2):
            x_list.append(m.floor(x_val_max))
        for k in range(2):
            x_list.append(m.floor(x_val_min))
    x_list.pop(len(x_list)-1)

    data = {
        'G': g_list,
        'X': x_list,
        'Y': y_list,
        'Z': z_list,
        'E': e_list,
        'F': f_list
    }

    return data


# def pattern_4(z):
    g_list = []
    x_list = []
    y_list = []
    z_list = []
    e_list = []
    f_list = []

    x_val_right = X_POS  # right edge
    x_val_left = X_POS + size  # left edge
    y_val_up = Y_POS  # top edge
    y_val_down = Y_POS + size  # bottom edge

    step = 0

    # For X-Axis values
    step1 = x_val_left - 2
    step2 = step1 - 1

    # initial (before pattern officially starts)
    x_list.append(m.floor(x_val_left))
    x_list.append(m.floor(x_val_left-1))
    x_list.append(m.floor(x_val_left))
    x_list.append(m.floor(x_val_left))

    while (step2 > x_val_right) and (step != x_val_right + 3):
        step1 -= 1
        step2 -= 1
        x_list.append(m.floor(step1))
        x_list.append(m.floor(step2))
        x_list.append(m.floor(x_val_left))
        x_list.append(m.floor(x_val_left))

    step = x_val_right
    while (step > x_val_right) and (step != x_val_right + 1):
        step -= 1
        x_list.append(m.floor(x_val_left))
        x_list.append(m.floor(x_val_left))
        x_list.append(m.floor(step))
        x_list.append(m.floor(step+1))

    # For Y-Axis values
    step1 = y_val_up + 2
    step2 = step1 + 1

    while (step2 < y_val_down) and (step2 != y_val_down - 3):
        step1 += 1
        step2 += 1
        y_list.append(m.floor(y_val_up))
        y_list.append(m.floor(y_val_up))
        y_list.append(m.floor(step1))
        y_list.append(m.floor(step2))

    step = y_val_up
    while (step < y_val_down) and (step != y_val_down - 1):
        step += 1
        y_list.append(m.floor(step))
        y_list.append(m.floor(step+1))
        y_list.append(m.floor(y_val_down))
        y_list.append(m.floor(y_val_down))

    # For non XY values
    for i in range(len(x_list)):
        g_list.append('1')
        z_list.append(z)
        e_list.append('1')
        f_list.append(str(print_speed))

    data = {
        'G': g_list,
        'X': x_list,
        'Y': y_list,
        'Z': z_list,
        'E': e_list,
        'F': f_list
    }

    return data


# Creating the .gcode file
with open(
    # windows
    f'E:\Programming\Public_Repos\G-Code_Scripts\G-Code Files\X_HATCH_{num_layer}L_d{m.floor(size/10)}_dz_{dz}_dt{dwell_time}_F{print_speed}.gcode', 'w'
    # mac
    # f'/Users/espiller/Programming/Public_Repos/G-Code_Scripts/G-Code Files/X_HATCH_{num_layer}L_d{m.floor(size/10)}_dz_{dz}_dt{dwell_time}_F{print_speed}.gcode', 'w'
) as file:

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

        # Priming
        file.write(';; Priming;\n')
        file.write(f'G0 Z{z};\n')  # Sets needle to the desired print height
        # Sets needle to default XY location
        file.write(f'G0 X{m.floor(X_POS)} Y{m.floor(Y_POS-50)};\n\n')

        # Pattern 1
        file.write(';; Pattern 1;\n')
        p1 = create_gcode_dataframe(GLOBAL_COLUMNS, pattern_1(z))
        for i in p1:
            file.write(f'{i}\n')
        file.write('\n')

        # Priming
        file.write(';; Priming;\n')
        file.write(f'G0 Z{z};\n')  # Sets needle to the desired print height
        # Sets needle to default XY location
        file.write(f'G0 X{m.floor(X_POS)} Y{m.floor(Y_POS-50)};\n\n')

        # Pattern 2
        file.write(';; Pattern 2;\n')
        p2 = create_gcode_dataframe(GLOBAL_COLUMNS, pattern_22(z))
        for i in p2:
            file.write(f'{i}\n')
        file.write('\n')

        # Priming
        file.write(';; Priming;\n')
        file.write(f'G0 Z{z};\n')  # Sets needle to the desired print height
        # Sets needle to default XY location
        file.write(f'G0 X{m.floor(X_POS)} Y{m.floor(Y_POS-50)};\n\n')

        # Pattern 3
        file.write(';; Pattern 3;\n')
        p3 = create_gcode_dataframe(GLOBAL_COLUMNS, pattern_3(z))
        for i in p3:
            file.write(f'{i}\n')
        file.write('\n')

        # Priming
        file.write(';; Priming;\n')
        file.write(f'G0 Z{z};\n')  # Sets needle to the desired print height
        # Sets needle to default XY location
        file.write(f'G0 X{m.floor(X_POS)} Y{m.floor(Y_POS-50)};\n\n')

        # Pattern 4
        # file.write(';; Pattern 4;\n')
        # p4 = create_gcode_dataframe(GLOBAL_COLUMNS, pattern_44(z))
        # for i in p4:
        #     file.write(f'{i}\n')
        # file.write('\n')

        # Dwell time
        file.write(f'G4 S{dwell_time};\n')

    file.write('\n')
    file.write(';; Rehome and wait\n')
    file.write('G0 Z3;\n')
    file.write('G0 X0 Y0;\n')
    file.write('G0 Z0;\n\n')

'''
When printing, have the first layer at a flow rate of 2.000 and the succeeding layers be
a flow rate of 0.250 to allow for optimal printing quality with wt% 60 and below.
'''
