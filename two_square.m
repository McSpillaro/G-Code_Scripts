%% Printing two pads 
%  Old code, but it prints two squares of equal size. This version is
%  designed to let the user print continuously; however, if the number of
%  layers is changed to one it can be used to make laminates. To home
%  prints with this code set the needle right above the print bed cose to
%  zero. DO NOT SET IT TO THE DESIRED PRINT HEIGHT. That is taken care of
%  in the code with the dz variable. 

l=input('Enter width of square [cm](Default: 2): ');
if isempty(l)==1
    l=2;
end

n=input('Enter number of layers (Default: 10): ');
if isempty(n)==1
    n=10;
end

print_speed=input('Enter print speed [mm/min](Default: 250): ');
if isempty(print_speed)==1
    print_speed=250;
end

dz=input('Enter step height [mm](Default: 0.01): ');
if isempty(dz)==1
    dz=0.01;
end

dewll_time=input('Enter time bewteen layers [s](Default: 15): ');
if isempty(dewll_time)==1
    dewll_time=15;
end

file = fopen(sprintf('TWO_PAD_%sL_d%s_dz%s_dt%s_F%s.gcode',num2str(n), num2str(l), num2str(dz),num2str(dwell_time),num2str(print_speed)),'wt');

l=l*10; % cm->mm
% centers=80; % distance between centers of cirlces 
bands=round(l); % keeps the number of bands a whole number 



center_1=[70 80];
center_2=[150 80];

pos_1=center_1-[l/2 l/2];
pos_2=center_2-[l/2 l/2];


% Sets initial praramets 
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

    z = layer*dz;

    % Primes 
    fprintf(file, ';; Priming;\n');
    fprintf(file, 'G0 Z%s;\n', num2str(z));
    fprintf(file, 'G0 X%s Y%s;\n\n',num2str(pos_1(1)),num2str(pos_1(2)-50));
    
    
    fprintf(file, '; Pad 1\n');
    
    
    for k=1:bands
       x=(k-1)+pos_1(1);
       if k~=bands % checks for k not= bands 
          if rem(k,2)==0 % prints away
               fprintf(file, 'G1 X%s Y%s E1 F%s;\n',num2str(x),num2str(pos_1(2)),num2str(print_speed));
               fprintf(file, 'G1 X%s Y%s E1 F%s;\n',num2str(x+1),num2str(pos_1(2)),num2str(print_speed));
          else % prints towards 
               fprintf(file, 'G1 X%s Y%s E1 F%s;\n',num2str(x),num2str(pos_1(2)+l),num2str(print_speed));
               fprintf(file, 'G1 X%s Y%s E1 F%s;\n',num2str(x+1),num2str(pos_1(2)+l),num2str(print_speed));
          end
       else
          if rem(k,2)==0 % prints away
               fprintf(file, 'G1 X%s Y%s E1 F%s;\n',num2str(x),num2str(pos_1(2)),num2str(print_speed));
          else % prints towards 
               fprintf(file, 'G1 X%s Y%s E1 F%s;\n',num2str(x),num2str(pos_1(2)+l),num2str(print_speed));
          end
       end
    end
    
    fprintf(file, '\n');
    fprintf(file, '; Pad 2\n');
    fprintf(file, 'G0 Z3;\n');
    fprintf(file, 'G0 X%s Y%s;\n',num2str(pos_2(1)),num2str(pos_2(2)));
    fprintf(file, 'G0 Z%s;\n\n',num2str(z));
    
    for k=1:bands
       x=(k-1)+pos_2(1);
       if k~=bands % checks for k not= bands 
          if rem(k,2)==0 % prints away
               fprintf(file, 'G1 X%s Y%s E1 F%s;\n',num2str(x),num2str(pos_2(2)),num2str(print_speed));
               fprintf(file, 'G1 X%s Y%s E1 F%s;\n',num2str(x+1),num2str(pos_2(2)),num2str(print_speed));
          else % prints towards 
               fprintf(file, 'G1 X%s Y%s E1 F%s;\n',num2str(x),num2str(pos_2(2)+l),num2str(print_speed));
               fprintf(file, 'G1 X%s Y%s E1 F%s;\n',num2str(x+1),num2str(pos_2(2)+l),num2str(print_speed));
          end
       else
          if rem(k,2)==0 % prints away
               fprintf(file, 'G1 X%s Y%s E1 F%s;\n',num2str(x),num2str(pos_2(2)),num2str(print_speed));
          else % prints towards 
               fprintf(file, 'G1 X%s Y%s E1 F%s;\n',num2str(x),num2str(pos_2(2)+l),num2str(print_speed));
          end
       end
    end

    % Dwell time
    fprintf(file, 'G4 S%s;\n',num2str(dwell_time));

end

fprintf(file, '\n');
fprintf(file, ';; Rehome and wait');
fprintf(file, 'G0 Z3;\n');
fprintf(file, 'G0 X0 Y0;\n');
fprintf(file, 'G0 Z0;\n\n');

% Wait time so the printer's hot bed doesn't turn off 
% fprintf(file, 'G4 S1800;\n');


fclose(file);