Electric Feed System
======================

An exploratory project looking into the possibility of using electric fuel & oxidizer pumps
to generate the inlet pressure required to provide propellant to the existing Liquid Fuelled
Engine (LFE), which requires a theoretical chamber pressure of ~375 psi.

!["Block Diagram of proposed electric feed system"](Documentation/Images/BlockDiagram.png)


Project requirements
--------------------

1. Design a custom inverter/power supply system.
2. Design and ground test a prototype electric pump system that delivers a reasonable NPSH
   at ~0.04 ft^3/s flow rate of IPA and ~0.03 ft^3/s flow rate of LOX.
	* This is not a flight system, however, future iterations will be, so make design
	  decisions with future weight optimization in mind.
3. Design for the existing LFE (with a design chamber pressure of ~375psi)
   (this chamber pressure will be confirmed by hot fire test ASAP).
4. The pump must be constructed from COTS components.
5. Work in parallel with the Carbon Fiber Propellant Tanks (CFPT) team to optimize the pressure
   requirements for both groups. Pump must successfully suppress cavitation at whatever pressure
   the CFPT team is able to deliver to us.
6. Produce the following documents:
	1. LOX Handling Procedures
	2. SOP
	3. Design Methodology & Process
	4. Analytical design comparison between Blowdown System and Electric Feed System in
	   order to determine the validity of pursuing the EFS technology.
7. Complete a design tool that will define a pump based on specific input parameters.
8. Make a far superior pump than Boston U.

### Erin’s Hopes & Dreams:

1. A test apparatus that is compatible with the existing LFETS
2. Live sensors and safety emergency shutdown provisions.
3. Prototype testing performed (if there is time):
	1. Cold flow test w/ water.
	2. Cold flow test w/ LN2.
	3. HOT FIRE!!! ((super secret hidden bonus level))
	
# Experiment design:
## Component checklist:
### Structure:
- [x] Test platform 
- [x] Battery box
- [ ] Tank stand
### Pump unit:
- [ ] Test Impellers
- [ ] Impeller dowel
- [ ] Impeller shaft
- [ ] Bearing plate
- [ ] Housing base
- [ ] Housing center
- [ ] ] Housing top
- [ ] Seal plates
- [ ] Motor mount
- [ ] Shaft coupler
- [ ] Various fasteners
- [ ] Seals and bearings
### Electrical:
- [x] Motor
- [x] ESC
- [x] Batteries
- [ ] Assembled wiring harness
- [ ] DAQ system
- [ ] Assembled sensor array
### Plumbing:
- [ ] Water tank
- [x] Pressurant (air) tank
- [ ] Fittings and piping

# Important links

 - [Cache of NASA 8000-series Special Publication mongoraphs](https://drive.google.com/folderview?id=0B5irBl_D7OtgMHlDUzJMNnBrSWM&usp=sharing)
   (not publically accessible as of 20170325)
