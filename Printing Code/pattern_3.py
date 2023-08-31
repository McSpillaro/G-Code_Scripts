import math as m

def pattern(x_, y_, z_, size, print_speed):
    g_list = []
    x_list = []
    y_list = []
    z_list = []
    e_list = []
    f_list = []

    y_val = x_  # border of print in Y
    x_val_min = x_  # border of print in X (min)
    x_val_max = x_ + size  # border of print in X (max)

    y_list.append(m.floor(y_val))
    y_val += 1

    while y_val < (y_ + size):
        for i in range(2):
            y_list.append(m.floor(y_val))
        y_val += 1

    for i in range(len(y_list)):
        g_list.append('1')
        z_list.append(z_)
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