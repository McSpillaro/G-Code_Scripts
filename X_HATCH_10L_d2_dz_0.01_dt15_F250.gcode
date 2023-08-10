G21          ; Sets units to millimeters
G90          ; Absolute coordinates
G0 Z5        ; Lift head to avoid collisions
G28 X0 Y0    ; Home X and Y
G92 X0 Y0    ; Reset origin: X and Y
G0 X0 Y0     ; Move to desired origin
G92 X0 Y0    ; Reset origin: X and Y
M299 E0 D0   ; Behaves as old printing firmware

T1;
;;; Start Print;

;; Layer 0
M790

   G   X   Y    Z E F
0  0            3    
1  0  60  20         
2  0          0.0    ;; Priming;
G0 Z0.0;
G0 ;; Layer 1
M790

   G   X   Y     Z E F
0  0             3    
1  0  60  20          
2  0          0.01    ;; Priming;
G0 Z0.01;
G0 ;; Layer 2
M790

   G   X   Y     Z E F
0  0             3    
1  0  60  20          
2  0          0.02    ;; Priming;
G0 Z0.02;
G0 ;; Layer 3
M790

   G   X   Y     Z E F
0  0             3    
1  0  60  20          
2  0          0.03    ;; Priming;
G0 Z0.03;
G0 ;; Layer 4
M790

   G   X   Y     Z E F
0  0             3    
1  0  60  20          
2  0          0.04    ;; Priming;
G0 Z0.04;
G0 ;; Layer 5
M790

   G   X   Y     Z E F
0  0             3    
1  0  60  20          
2  0          0.05    ;; Priming;
G0 Z0.05;
G0 ;; Layer 6
M790

   G   X   Y     Z E F
0  0             3    
1  0  60  20          
2  0          0.06    ;; Priming;
G0 Z0.06;
G0 ;; Layer 7
M790

   G   X   Y     Z E F
0  0             3    
1  0  60  20          
2  0          0.07    ;; Priming;
G0 Z0.07;
G0 ;; Layer 8
M790

   G   X   Y     Z E F
0  0             3    
1  0  60  20          
2  0          0.08    ;; Priming;
G0 Z0.08;
G0 ;; Layer 9
M790

   G   X   Y     Z E F
0  0             3    
1  0  60  20          
2  0          0.09    ;; Priming;
G0 Z0.09;
G0 