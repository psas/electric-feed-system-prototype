
### MANUFACTURING

- [ ] Completed Pump System 
  - [ ] Impellers - James please update 
  - [ ] Completed Bearing Plates
    - [ ] Upper Bearing Plate
        - [x] .SLDPRT
        - [x] Squared
        - [ ] Mastercam
        - [ ] G-Code
        - [ ] Faced
        - [ ] Critical Features Machined
        - [ ] Finising
     - [x] Lower Bearing Plate
        - [x] .SLDPRT
        - [x] Squared
        - [x] Mastercam
        - [x] G-Code
        - [x] Faced
        - [x] Critical Features Machined       
        - [x] Finising
  - [ ] Completed Seal Plates
    - [ ] Upper Seal Plate
       - [x] .SLDPRT
       - [x] Squared
       - [ ] Mastercam
       - [ ] G-Code
       - [ ] Faced
       - [ ] Critical Features Machined
       - [ ] Finising
    - [ ] Lower Seal Plate 
      - [x] .SLDPRT
      - [x] Squared
      - [ ] Mastercam
      - [ ] G-Code
      - [ ] Faced
      - [ ] Critical Features Machined
      - [ ] Finising
  - [ ] Housing 
     - [x] .SLDPRT
     - [ ] Squared
     - [ ] Mastercam
     - [ ] G-Code
     - [ ] Faced
     - [ ] Critical Features Machined
     - [ ] Finising
  - [ ] Shaft 
     - [x] .SLDPRT
     - [ ] Squared
     - [ ] Mastercam
     - [ ] G-Code
     - [ ] Faced
     - [ ] Critical Features Machined
     - [ ] Finising
- [ ] Completed Motor Assembly
   - [ ] Motor Hub
     - [ ] .SLDPRT
     - [ ] Squared
     - [ ] Mastercam
     - [ ] G-Code
     - [ ] Faced
     - [ ] Critical Features Machined
     - [ ] Finising
   - [ ] Motor Mount
     - [ ] .SLDPRT
     - [ ] Squared
     - [ ] Mastercam
     - [ ] G-Code
     - [ ] Faced
     - [ ] Critical Features Machined
     - [ ] Finising
   - [ ] Motor Rest
     - [ ] .SLDPRT
     - [ ] Squared
     - [ ] Mastercam
     - [ ] G-Code
     - [ ] Faced
     - [ ] Critical Features Machined
     - [ ] Finising
   - [ ] Torque Arm
     - [ ] .SLDPRT
     - [ ] Squared
     - [ ] Mastercam
     - [ ] G-Code
     - [ ] Faced
     - [ ] Critical Features Machined
     - [ ] Finising
   - [ ] Assebly Base Plate
     - [ ] .SLDPRT
     - [ ] Squared
     - [ ] Mastercam
     - [ ] G-Code
     - [ ] Faced
     - [ ] Critical Features Machined
     - [ ] Finising
  

###### *Documentation*

- [ ] Manufacturing Methods/procedures
- [ ] EFS Working drawings
   - [ ] Assemblies
        - [ ] Pump
        - [ ] Motor Mount
        - [ ] Full Assembly
    - [ ] Housing 
    - [ ] Upper Seal Plate
    - [ ] Lower Seal Plate 
    - [ ] Upper Bearing Plate
    - [ ] Lower Bearing Plate
    - [ ] Shaft
    - [ ] Motor Hub
    - [ ] Motor Mount
    - [ ] Motor Rest
    - [ ] Torque Arm
    - [ ] Assebly Base Plate     
- [ ] CNC g-code files
- [ ] Photos

-------------------

### ASSEMBLY

##### Pump Chassis:

- [ ] Assemble shaft and bearing housings
- [ ] Assemble pump casing and main housing
- [ ] Assemble diffuser sleeves and flange
- [ ] Tap and assemble pump chassis fittings
- [ ] Verify/check fits and play in completed pump assembly
- [ ] Verify/check seals, bearings, and impeller clearances

##### Test Stand Plumbing:

- [ ] Size and cut aluminum tubing

> Make sure the required number of straight pipe diameters are provided between each measurement device.

- [ ] Drill suction side tee cap fitting for TC1S
- [ ] Establish pump centerline

> All pressure measurements must be adjusted to the pump center line.

- [ ] Install vibration dampening methods
- [ ] Assemble EFS test plumbing fittings, tubing (including supports) and valves

> Check entire test assembly for alignment before tightening fittings and valves for performance testing.

- [ ] Install suction and discharge pressure gauges
- [ ] Install PT1S and PT1D
- [ ] Install suction and discharge pressure gauges
- [ ] Install suction side thermocouple TC1S
- [ ] Install turbine flow meter

-------------------

### CONTROL SYSTEMS

- [ ] Assemble of ESC to BL motor, receiver, battery [[NO BEC](https://github.com/psas/electric-feed-system/blob/master/Documentation/Spec%20Sheets/Electronics/Swordfish%20ESC%20manuals.pdf)]
- [ ] Assemble smooth, tight, water cooling tube to ESC
- [ ] Wire ESC to computer [[Use B-b config.](https://github.com/psas/electric-feed-system/blob/master/Documentation/Spec%20Sheets/Electronics/233180132-Swordfish-Plus-ESC-Manuals.pdf)]
- [ ] Complete bench test of motor/ESC to verify parameter settings
- [ ] Decide on PWM switching rate for most temp efficient operating conditions
- [ ] Integrate motor/ESC into EFS test assembly after bench testing is completed

##### ESC:

- [ ] Program/verify low voltage cut-off (LVC)
- [ ] Program/verify cut-off voltage/cell
- [ ] Program/verify Brake type parameter
- [ ] Program/verify Timing Advance
- [ ] Program/verify cut-off/startup type parameter
- [ ] Program/verify PWM switching rate

+ [Specs](https://github.com/psas/electric-feed-system/blob/master/Documentation/Images/ESC_specs.PNG)
+ [Factory settings](https://github.com/psas/electric-feed-system/blob/master/Documentation/Images/ESC_Factory_set_parameters.PNG)
+ [Programmable parameters](https://github.com/psas/electric-feed-system/blob/master/Documentation/Images/ESC%20programmable%20parameters.PNG)

##### Power System Checks:

- [ ] Confirm motor wattage feedback
- [ ] Confirm motor current feedback
- [ ] Confirm motor RPM feedback
- [ ] Confirm ESC temp feedback

##### EFS Performance Feedback Checks:

- [ ] Test/calibrate/verify Suction side transducer PT1S
- [ ] Test/calibrate/verify Discharge side transducer PT1D
- [ ] Test/calibrate/verify vapor pressure thermocouple TC1S
- [ ] Test/calibrate/verify flow meter FMD1
- [ ] Test/calibrate/verify Supply tank pressure and regulation

###### *Documentation*

- [ ] Controls systems theory/outline
- [ ] Brief EFS controls system operation/data collection manual
- [ ] Wiring/Controls diagrams
- [ ] Photos

-------------------

### PERFORMANCE TESTING

##### Pre-test:

- [ ] Complete test procedure document
* Outline casing inspection and casing hydrostatic test to be performed before performance testing.
* Establish 0, Qmin, Qmean, Qnom, Q120% using standard measurement of 5 points (9 max.)
* Establish operating line (system curves for inspection during testing)
* **Verify** NPSR/NPSA requirements
- [ ] EFS NPSH test

##### Analysis:
- [ ] Q - H Curves
- [ ] P - Q Curves
- [ ] n - Q Curves
- [ ] P - Q Curves
- [ ] NPSH vs NPSHR
- [ ] Define EFS BEP, Shut-off, Max. Q, Max. H, BHP, WHP and assess efficiencies
- [ ] Regression Analysis
- [ ] Use affinity laws to size 8.0 kN pump :smirk: :rocket:

+ [Processing test data for head measurement](https://github.com/psas/electric-feed-system/blob/master/Documentation/Images/Test%20data%20pocessing.PNG)

###### *Documentation*

- [ ] EFS PUMP DATA SHEET!!!

-------------------

### MISCELLANEOUS
- [ ]
- [ ]
- [ ]
