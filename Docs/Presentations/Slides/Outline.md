## Story: 

1. **Brief team introduction** 
- [ ] Title Slide, Team members introduce stuff

---

2. **Problem description** @luceja

##### Slides:

- [x] The problem: getting rockets to go higher (the rocket equation)
- [x] normally solid fuel, and problems with liquid fuel solutions
- [x] electric motor pump a good solution (battery energy density, etc)

---

3. **Key Customer requirements** @JordParma

- Show just the most important customer requirements
- Make sure that the customer requirements are not only important, but clearly understandable to the (smart, professional)   audience

##### Slides:

- [ ] Outline high level reqs. (Words in tables)
- [ ] What makes them important to the success of the project. 


---

4. **Key performance metrics** @JordParma

- How did we measure design outcomes so that it meets customer requirements

##### Slides:

> Combine with #3

- [ ] Outline upper and lower limits on meeting reqs. (Words in tables)

> Add yes/no or checkmark for reqs. ONLY. Performance vs. requirments happens in #9

---
5. **Final Design and Subsystems breakdown** @jtalik

##### Slides:

Final design:
- [ ] High Level
	-  Flow Diagram of the testing apparatus - Diagram 
	-  Actual testing assembly - Hig-res photo

Subsystems breakdown:
- [ ] Pump 
	- Bearing
	- Seals 
	- Hydraulic assembly (volute, impeller, difusser)
		-Highlight the modular design for testing
	- Shaft / Coupling
	- Motor Dynomometer
	- Motor / ESC / Batteries / motor control 

	- [ ] inlcude quater section - CAD (one on poster)
	- [ ] include photo of pump w/ casing + motor mount
	- [ ] include photo of motor control - High res photo (one on poster)

- [ ] Testing
	- Testing Apparatus
	- Sensing 
		- Pressure, Flow, RPM, Torque, ect... 
	- Data Aquisition 
		- Ardunino and excel 

	- [ ] Include diagram of testing -  Diagram
	- [ ] Include high-res photo of testing apparatus - Photo
	- [ ] Include high res photo of the control / measurement apparatus - Photo 
---

6. **Design concepts** @JordParma

- Give an example of your creative thinking in generating concepts
- Provide some evidence of how you selected viable concepts
- Show conceptually how your design works

##### Slides:

- [ ] What is our engineering methodology? Make smart/concrete decisions and smart/concrete guesses. DISAGREE AND COMMIT!
      fail and fail again until we get what we want. Lets be a little romantic here. People love that shit

> Can maybe group these three into one or two slides or just the general idea.

- [ ] Use IPyNb to demonstrate how we guided ourselves into the realm of our req engine/vehicle performance
- [ ] Use IPyNb to demonstrate selecting viable impeller concept (Maybe move to #5)
- [ ] Use IPyNb to demonstrate determining power requirments

- [ ] Show a high level conceptual slide of how the pump works. Pressure/flow transfer etc. (I FUGGIN GOT DIS BOIS)
 
---

7. **Final performance vs. Key Customer requirements** @JordParma

- Show how, or to what degree, your design meets the key requirements. This is the second half of the climax of your talk.
- Show proof of how well you have solved your problem

##### Slides:

- [ ] Let the data drop cause the shit is fire! Go easy on em though. 

> I need some time to plot.

- [ ] What does it mean? Did we hit our mark?

---
8. **Biggest challenges and solutions** @luceja
- Show one or at most two big problems that you overcame

PROBLEM: Designing, manufacturing, and testing a pump in-house

##### Slides:

- [x] Requirements meant that off shelf designs or parts (impellers, etc) wouldn't be usable.. have to make everything (graphic of parts that we had to make)
- [ ] The level of precision (concentricity and lengths) was critical (rpms, loads, vibration)... graphic series of impeller and housing > shaft > everything
- [ ] Casing Design  
	Problems: 
	- High RPMS / High Pressure
	- Alignment / Clearances / Fits 
	- Percision execution

	Solutions: 
	- Bearing Arrangment and Selection
		- Canteliever Bearing Arragnement 
		A double row, angular contact bearing fixed  in the housing and the shaft, towards the drive side of the saft provides axial and radial support for the shaft. 
		A single row, deep groove bearing fixed to the shaft, but with axial displacement enabled, provides radial support of the shaft. Due to the enabled axial displacment, angluar dislacement is elminatied, while shaft displacement can be accounted for, minimizing the stesses in the shaft. 

	- In-House Manufacturing 
		- Learning techniques for achieving alignment: Jig 
		- CAM software: Mastercam
		- CNC: 3 axis and Lathe
		
	- [ ] Include the picture of the quarter section
	- [ ] Include the picture of John and Kris on the CNC Hass
	- [ ] Include picture of James on the CNC Lathe 
			
- [ ] Controls / Measurement
	Problems:
	- Motor control 
	- Sensing and measuring for preformance curves
		- 3 x Pressure, Temperature, RPM, Torque, Flowrates
		
	Solutions:
	- Rigged the quadcotper control with tricking the reciever/transiever
	- Arduino DAQ

	- [ ] include picture of the Motor Controller 
	
---

9. **Conclusion – Recap your story** @jtalik

- Where you started – Customer requirements
- Where you ended – proof of satisfying customer requirements

##### Slides:

- [ ] 
- [ ] 
- [ ] 

---

10. **Recommendations for next steps** @both

- Any unfinished pieces?
- What you learned
- What should be done next

##### Slides:

- [ ] Note about ongoing testing and results to come.
- [ ] What we learned? COT DAMN. We need to compress this.

- [ ] Future work slide
	- Further performance improvement investigation. Speed, impeller trim, etc,.
	- Revamp for cryo LN2 tests
	- Integrate with liquid engine test stand for LOX testing
	- VFD
	- 8 kN scaling
---


## Notes:

#### Possible Questions from audience:

1. Why use centrifugal pump (vs other high head / low flow like piston)
2. 
3. 

