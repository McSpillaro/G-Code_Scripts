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

;; Priming;
G0 Z0.01;
G0 X60 Y20;

;; Pattern 1;
;; Layer 1
M790

;; Priming;
G0 Z0.02;
G0 X60 Y20;

;; Pattern 1;
;; Layer 2
M790

;; Priming;
G0 Z0.03;
G0 X60 Y20;

;; Pattern 1;
;; Layer 3
M790

;; Priming;
G0 Z0.04;
G0 X60 Y20;

;; Pattern 1;
;; Layer 4
M790

;; Priming;
G0 Z0.05;
G0 X60 Y20;

;; Pattern 1;
;; Layer 5
M790

;; Priming;
G0 Z0.06;
G0 X60 Y20;

;; Pattern 1;
;; Layer 6
M790

;; Priming;
G0 Z0.07;
G0 X60 Y20;

;; Pattern 1;
;; Layer 7
M790

;; Priming;
G0 Z0.08;
G0 X60 Y20;

;; Pattern 1;
;; Layer 8
M790

;; Priming;
G0 Z0.09;
G0 X60 Y20;

;; Pattern 1;
;; Layer 9
M790

;; Priming;
G0 Z0.1;
G0 X60 Y20;

;; Pattern 1;
