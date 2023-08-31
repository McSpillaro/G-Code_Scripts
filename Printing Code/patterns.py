def pattern_1(g_, x_, y_, z_, e_, f_, size, print_speed):
    g_list = []
    x_list = []
    y_list = []
    z_list = []
    e_list = []
    f_list = []

    x_val = g_  # border of print in X
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
    y_val_up = Y_POS - 1 # top edge
    y_val_down = Y_POS + size  # bottom edge
    
    # For X-axis
    for i in range(m.floor(x_val_left - x_val_right - 2)):
        if (i in x_list) and (i != x_val_right):
            continue
        
        x_list.append(m.floor(x_val_right))
        x_list.append(m.floor(x_val_right))
        x_list.append(m.floor(x_val_right+i))
        x_list.append(m.floor(x_val_right+i+1))
    
    # For Y-axis
    for i in range(m.floor(y_val_down - y_val_up - 1)):
        if (i in y_list) and (i != y_val_up + 1):
            continue
        
        y_list.append(m.floor(y_val_up+i))
        y_list.append(m.floor(y_val_up+i+1))
        y_list.append(m.floor(y_val_up+1))
        y_list.append(m.floor(y_val_up+1))
    
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

def pattern_2(z):
    g_list = []
    x_list = []
    y_list = []
    z_list = []
    e_list = []
    f_list = []

    x_val_right = X_POS  # right edge
    x_val_left = X_POS + size  # left edge
    y_val_up = Y_POS # top edge
    y_val_down = Y_POS + size  # bottom edge

    step = 0
    
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


#def pattern_4(z):
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
