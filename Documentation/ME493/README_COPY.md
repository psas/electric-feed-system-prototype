---
layout: Project
title: Electric Feed System
sponsor: Portland State Aerospace Society
sponsor_url: https://github.com/psas
document-date: 20 May 2017
---

# Electric Feed System

![](https://github.com/psas/electric-feed-system/blob/master/Documentation/Images/team5.PNG)

### Objective:

The objective of the EFS project is to design, build, and test an electric feed system using COTS parts and in-house manufacturing for the PSAS LV4 liquid fueled bi-propellant rocket engine prototype by June 6, 2017.

### Project Team Members:

Name                | GitHub Username | Current Role
--------------------|-----------------|-----------------------------------
Jordan Roland       | @JSRoland       | Project Coordinator
Johnny C. Froehlich | @JordParma      | Design Engineer; Testing
Mimi Shang          | @mimishang      | Control Systems Engineer
Johnathan Talik     | @jtalik         | Manufacturing Engineer
Rawand Rasheed      | @rawand12       | Control Systems Engineer
James Luce          | @luceja         | Thermal/fluids Engineer

### EFS Requirements:

1. Design and bench test a technology development platform for the electric pump system.
2. Design and test a custom power system for EFS motor and system controls.
3. Design for the existing LV4 liquid fuel engine (target chamber pressure of 350 - 400 psi)
4. The pump must be constructed from COTS components.
5. Parallel work with Carbon Fiber Propellant Tank (CFPT) team to optimize vehicle integration.
6. IPython design tool to generate pump requirements based on engine/vehicle level parameters.    
7. Produce the following documentation:
    - EFS testing, handling, and troubleshooting procedures
	- EFS Design Methodology & Design Process
    - Complete bill of materials

    #### Stretch Goals:
    - Integration with existing Liquid Fuelled Engine Test Stand (LFETS)
    - Completed live health monitoring and emergency shutdown provisions
    - Cold fire LN2 testing
    - Cold fire LOX testing
    - Hot  fire LOX testing

### Design Challenges:

The EFS pump can be described as a semi-open, partial emissions impeller type and is exemplified as highly unorthodox. Reasons exist, however, to break with conventional design practice to meet objectives which would otherwise be difficult to achieve. These difficult to achieve objectives include a pump capable of high-head low-flow processes at high shaft rotational speeds. Intentionally flaunting the rules, in fact, may provide a pump design that can equal or exceed the performance of conventional pumps in the head-flow design range for which it is intended and for which it is best suited. An overview of some of the many challenges involved in producing such a pump are listed below;

To name a few...
1. Need for a simple, lightweight, and easily manufactured pump suited to produce high heads at low flow  rates.


2. Engine/vehicle requirements define the need for a feed system that is a radical departure from conventional design.


3. Using an unorthodox Barske open impeller design.


4. Hardware is physically small.


5. Shaft deflection, key stresses, fits for mounted components, and rotor dynamics must be seriously considered.


6. Simplifying a detailed fabrication process.

### Outcomes:

The expected outcomes of the PSAS EFS capstone project are as follows;

1. Detailed design explanation.

This document is geared towards leaving fellow PSAS engineers with a complete overview of the detailed design process for further work and scaling. This document includes the theory that when into developing the EFS system

2. EFS technology development platform.

The EFS technology development platform is to serve as a completed unit for future development of the electric feed system. The platform, which includes the EFS pump and test apparatus allows for the continued testing of EFS, scaled EFS pumps and modification to EFS components and subsystems.

3. Manufacturing/controls/testing procedures.


4. Completed EFS water test assembly with part drawings and 3-axis CNC machine code for reproducibility.


5. Evaluation of pump performance and accompanying documentation e.g., Performance curves, BEP, spec sheets, future work.

The EFS pump performance curves will Identify the best operating point (BEP) of the system. Complete and reliable performance curves will allow for the evaluation of the EFS system, more importantly it will allow for the use of pump scaling laws (affinity laws) which otherwise would be inapplicable. The use of scaling laws will allow PSAS to take the EFS pump and scale it up for larger rockets in the future.


6. Open Source GitHub repository.



![Figure: ](https://github.com/psas/electric-feed-system/blob/master/Documentation/Images/Impellers.PNG)
