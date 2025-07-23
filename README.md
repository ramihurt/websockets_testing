Recently, I have been working for a new OEM developing some end to end testing procedures for testing in-car customer 
features. The OEM has proprietary hardware used in conjunction with a software solution called CANoe to mock the ECU and
multimedia platforms which we can then use to simulate certain actions. However, all of this is a manual process which 
can take over a week to fully test all functionalities when a new firmware update is released thus prompting an
automation strategy. As part of the process, I started developing a new python POC project to automate communications
between the user and the test hardware. 

For this starter POC, I had 2 goals. The first was to establish proper ABD communications to the hardware and to send it
remote commands or execute scripts. The second goal was to attach a simple UI interface. For the UI interface, I wanted
to integrate some sort of live logging which would return prints and results from the background processes. After 
testing several solutions using RESTful APIs and websockets, I found websockets' behavior favorable. The open socket 
stream could remain open between a UI and the backend. The final solution's stack was composed of a python flask backend
with a simple reactjs frontend. This article will mostly focus on the backend architecture and an overview of all
packages and components and how they communicate with each other. 
