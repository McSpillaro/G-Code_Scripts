size = input('Enter width of square [cm] (Default: 2): ')
if isempty(size) == 1
    size = 2;
end

num_layers = input('Enter number of layers (Default: 10): ')
if isempty(num_layers) == 1
    num_layers = 10;
end

print_speed = input('Enter print speed [mm/min](Default: 250): ');
if isempty(print_speed) == 1
    print_speed = 250;
end

dz = input('Enter step height [mm](Default: 0.01): ');
if isempty(dz) == 1
    dz = 0.01;
end

dwell_time = input('Enter time bewteen layers [s](Default: 15): ');
if isempty(dwell_time) == 1
    dwell_time = 15;
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

for layer=1:num_layers
    % New Layer 
    fprintf(file, ';; Layer %s\n',num2str(layer));
    fprintf(file, 'M790\n\n'); % Displays new layer on printer 

    z = layer * dz

    % Primes 
    fprintf(file, ';; Priming;\n');
    fprintf(file, 'G0 Z%s;\n', num2str(z));
    fprintf(file, 'G0 X%s Y%s;\n\n',num2str(pos_1(1)),num2str(pos_1(2)-50));
    
    
    fprintf(file, '; Pad 1\n');

    for k=1:bands
        x = (k-1)+pos_1(1):
        if k~=bands % checks for k not = bands
            if rem(k,2) == 0 % prints
                fprintf(file, 'G1 X%s Y%s E1 F%s;\n', )


    
