import math as m

def pattern(x_, y_, z_, size, print_speed):
    g_list = []
    x_list = []
    y_list = []
    z_list = []
    e_list = []
    f_list = []

    x_val_right = x_  # right edge
    x_val_left = x_ + size  # left edge
    y_val_up = y_  # top edge
    y_val_down = y_ + size  # bottom edge

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
        z_list.append(z_)
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