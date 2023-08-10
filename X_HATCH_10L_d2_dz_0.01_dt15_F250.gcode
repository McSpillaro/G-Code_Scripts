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

G3 X3 Y3 Z3 Enan Fnan;; Layer 1
M790

G3 X3 Y3 Z3 Enan Fnan;; Layer 2
M790

G3 X3 Y3 Z3 Enan Fnan;; Layer 3
M790

G3 X3 Y3 Z3 Enan Fnan;; Layer 4
M790

G3 X3 Y3 Z3 Enan Fnan;; Layer 5
M790

G3 X3 Y3 Z3 Enan Fnan;; Layer 6
M790

G3 X3 Y3 Z3 Enan Fnan;; Layer 7
M790

G3 X3 Y3 Z3 Enan Fnan;; Layer 8
M790

G3 X3 Y3 Z3 Enan Fnan;; Layer 9
M790

G3 X3 Y3 Z3 Enan Fnan;; Priming;
G0 Z0.1;
G0 