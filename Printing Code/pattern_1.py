import math as m

def pattern(x_, y_, z_, size, print_speed):
    g_list = []
    x_list = []
    y_list = []
    z_list = []
    e_list = []
    f_list = []

    x_val = x_  # border of print in X
    y_val_min = y_  # border of print in Y (min)
    y_val_max = y_ + size  # border of print in Y (max)

    x_list.append(m.floor(x_val))
    x_val += 1

    while x_val < (x_ + size):
        for i in range(2):
            x_list.append(m.floor(x_val))
        x_val += 1

    for i in range(len(x_list)):
        g_list.append('1')
        z_list.append(z_)
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