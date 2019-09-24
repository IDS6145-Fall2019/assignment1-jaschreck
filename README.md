# Assignment 1 
Jacquelyn Schreck
Topic: Escalators efficiency


# General Introduction
# Part 1: Designing a Model - Subway System

Motivation: A lot of major cities use subways as their main mode of transportation, no matter where they’re going. It would be best to optimize the space so that people can circulate through as quickly as possible. In this case I am referring to how the escalators run.

Examples: Someone going to work has to get onto the subway, but they are stuck in a long line and can’t get to their train on time to get to work. Now they have to wait an additional 10-15 minutes before they have another train, and they’ll be late for work.

Context and solutions: In the past some subway systems have tried many different things. Changing direction of escalators depending on hour, making it mandatory for stationary riders to stay on the left while the walkers go to the right, etc.


## (Part 1.1): Requirements (Experimental Design) **(10%)**
Problems: The escalator isn’t moving as many people as efficiently as it should be. It blocks the space and makes causes people to be late to where they’re going, or they have to show up way earlier. 

Hypothetical solutions (Hypotheses): Make it mandatory to not walk. Make it mandatory to stay to the left if you don’t want to walk. Add more escalators (if there’s room). Add more stairs for those who want to walk (if there’s room). Change direction of escalators depending on time of day. Change speed. 

System objective: To make the subway experience as efficient as possible by being able to cycle people through quickly. This means everything thing needs to keep moving and escalators can slow people down.

System inputs: The escalator will be wide enough to accommodate people who want to walk and room on the side for people who don’t want to walk. People will be able to get on the escalator without having to wait, they will be able to walk on immediately.

System function: Move people along as quickly as possible. 

System outputs: Lessen amount of time on the escalator. Lessen wait time to get on the escalator


## (Part 1.2) Subway (My Problem) Model **(10%)**

In uploaded files:
Behavior Diagram.png
Object Diagram.png
Class Diagram.png


## (Part 1.3) Subway (My Problem) Simulation **(10%)**

Simulation type: Agent-based simulation since it is a crowd of people

Inputs: The escalator will be wide enough to accommodate people who want to walk and room on the side for people who don’t want to walk. People will be able to get on the escalator without having to wait, they will be able to walk on immediately.

Outputs: Lessen amount of time on the escalator. Lessen wait time to get on the escalator

How it will help to analyze: Understanding the inputs and outputs gives us more of an understanding of the independent and dependent variables (more on this in 1.5). When we understand our variables, we’re able to run the proper analyses to test our hypotheses. If we do not understand our data we are not going to be able to test our hypotheses and your work will become incomprehensible. In this case, we would want to see how many people are getting efficient use of the escalators on day one, where the conditions aren’t changed, and on day 2, when conditions are changed. That way we can see which day had better efficiency, and then implement the changes that need to be made if it shows that the changes were better for efficiency. This could be visualized with a simple bar chart.


## (Part 1.4) Subway City (My Problem) Model **(10%)**

In uploaded files:
Assignment1SimTech.py

## (Part 1.5) Specifying the Inputs to a System **(10%)**

Independent: How many people, how wide is the elevator, how many elevators, are people allowed to walk, which way are the elevators going, can the direction be changed, and can the speed be changed. 

Dependent: How long people wait to get on the escalator and how long the escalator ride is. 

Where the data is from: Online open source

Statistics for input: Important statistics are going to be the means and standard deviations. 

Analyses and visualization: The means and standard deviations are printed. There will be bar charts for the means as well. There will also be bar charts showing the raw data.

Infographic: An infographic could be having a map showing routes, and each route has a differnt width and/or color based on efficiency.


# Part 2: Creating a Model from Code

In uploaded files:
POTS Diagram.png


# Part 3: Data Analysis

## (Part 3.1) - Real Data **(10%)**

The dataset is not actually a real dataset. I looked up 5 individual stations that told me how many people they have each day of the week and how long the average wait time is. I could not find this kind of information on escalators specifically so that is why I chose this data instead. It still fits in the overall topic of the subway system though because this shows how efficient each subway system is as a whole. 

First, station one has an average of 4700 people per day with an average wait time for the train of 16 minutes. Station one is much more efficient than station two becasue even though it has fewer people (M= 3140), it has a longer average wait time (M= 19.2). Station three seems to be doing better than station two, but is still behind station one in efficiency. Station three average wait time is 14.2 minutes with an average of 1560 people per day. Stationsfour and five seem to be equally efficient. Station four has an average of 2320 people per day and an average wait time of 9.2 minutes, while station five has slightly more people on average (M= 3040), and a slightly longer wait time (M= 11.2). Stations one, four, and five seem to be almost equally efficient. I would not say that I could easily say one is better than the other.

This can all be seen in the graphs.

In uploaded files:
Assignment1SimTech.py
(Various CSV files because that was the easiest way to split up the stations.)

## (Part 3.2) -  Plotting 2D Random Number Generators **(15%)**

Quasi is less random and more symmetrical. The colorful charts are the pseudo random generated and the blue charts are quasi random generated. 

In uploaded files:
Assignment1SimTech.py

## (Part 3.3) -  Plotting 1D Random Distributions **(15%)**

The quasi histograms look the most similar to the uniform histograms, but they are a little more symmetrical since quasi number generators are never truly random.

In uploaded files:
Assignment1SimTech.py

