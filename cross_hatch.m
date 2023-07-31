size = input('Enter width of square [cm] (Default: 2): ')
if isempty(size) == 1
    size = 2;
end

layer = input('Enter number of layers (Default: 10): ')
if isempty(layer) == 1
    layer = 10;
end

print_speed = input('Enter print speed [mm/min](Default: 250): ');
if isempty(print_speed) == 1
    print_speed = 250;
end

dz = input('Enter step height [mm](Default: 0.01): ');
if isempty(dz) == 1
    dz = 0.01;
end

dewll_time = input('Enter time bewteen layers [s](Default: 15): ');
if isempty(dewll_time) == 1
    dewll_time = 15;
end

file = fopen(sprintf('X_HATCH_%sL_d%s_dz%s_dt%s_F%s.gcode', num2str(num_layers), num2str(layers), num2str(dz), num2str(dwell_time), num2str(print_speed)), 'wt');

size = size * 10 % cm -> mm
% centers = 80; % distance between centers of cirlces
bands = round(size); % keeps the number of bands a whole number



center_1 = [70 80];
center_2 = [150 80];

pos_1 = center_1 - [size / 2 size / 2];
pos_2 = center_2 - [size / 2 size / 2];


% Sets initial parameters
fprintf(file, 'G21       ; Set units to millimeters\n');
fprintf(file, 'G90       ; Absolute coordinates\n');
fprintf(file, 'G0 Z5     ; lift head to avoid collisions\n');
fprintf(file, 'G28 X0 Y0 ; home X and Y\n');
fprintf(file, 'G92 X0 Y0 ; reset origin: X and Y\n');
fprintf(file, 'G0 X0 Y0  ; move to desired origin\n');
fprintf(file, 'G92 X0 Y0 ; reset origin: X and Y\n');
fprintf(file, 'M299 E0 D0; Behaves as old printing firmware\n\n');

% Tells printer which head to use 
fprintf(file, 'T1;\n');

    % Start print
    fprintf(file, ';;; Start Print;\n\n');

for layer=1:n
    % New Layer 
    fprintf(file, ';; Layer %s\n',num2str(layer));
    fprintf(file, 'M790\n\n'); % Displays new layer on printer 

