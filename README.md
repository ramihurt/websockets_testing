# DSC Testing Tool

This is a simple example package. You can use
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## Overview

[Skip the boring stuff] (#design)

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

## What is a websocket.

## Why a websocket
Allows for a live logging system like someone would expect from a classical terminal. Tests can be complex and run for
several minutes at a time waiting for requests and responses from the mock hardware and the OEM's backend solution. With
a traditional API, the stateful-focused approach would deliver logs in batch and provide almost no progress updates or
test tracking. With the websocket, test modules can use a centralized websocket utility within the backend to send live
messages to the user on the front end. The websocket can also use the subject parameter to elicit specific behaviors 
from the backend system by listening for certain keywords, much like a traditional API would do, but in a stateless
fashion. 

## Design
One of the goals was to have a centralized mechanism which could be shared amongst the test modules I am developing.
Although this may change in the future, at this time, only one connection is needed because it's a single instance of
the frontend connecting to a single instance of the backend and only one websocket connection is needed. I experimented 
with a few different approaches, like a static class, for example, but I didn't like this unregulated open access to the
websocket. I wanted it to be more controlled. The final solution was to create a basic socketio object wrapped around an 
interface class which can then be passed to the different test classes.

## Emitter and sender
My MessageEmitter class is the starting point. This class implements and invokes the low-level emit method from socketIo. The 
init method for this class requires a socketio object (which holds the active connection) and is saved within the object.
The MessageSender class constructor then takes a MessageEmitter object (which still holds our websocket connection) and
adds additional business logic or message data manipulation before it is emitted. The question arises, why wrap the Sender
around the Emitter. This is for scalability and reduced coupling. In the future, I can create different MessageSender-type
classes which accept a common MessageEmitter object but can implement its own logic to further customize messages and logic 
for a specific test module. For example, the current MessageSender class has methods for producing a JSON payload with
different color schemes for the limited tests I currently have. In the future, however, maybe one of the future testing 
modules needs a completely different color scheme or needs to aggregate data before it is emitted. This could be achieved
by creating a new sender class with this custom logic but still re-use the same websocket connection.

## The frontend
Admittedly, I employed the help of LLMs to help me draft a ReactJS frontend. This simply helped me reduce the amount of 
time spent on building a minimal UI which could connect to the backend websocket and accept/send messages using the
websocket. I added a few customizations after the initial outline was generated. But, since frontend development is not 
my forte, this was extremely helpful to save me time which could be used on the more important aspect of this POC. With 
that, the front end has just a few simple buttons to connect to and disconnect from the backend. The other buttons are
dedicated to emit messages from the frontend to the backend to launch test functions. 

## Breaking down the code

## Final thoughts