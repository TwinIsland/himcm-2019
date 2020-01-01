# Introduction

In this part, we will analyze the way to increase the revenue of each place that provide the free charger service. For us, we think there are mainly two kinds of solutions, which is 1. satisfied consumer’ s demand and increase the commodity price. 2. do not change the commodity price, but decrease the number free charger. For the three kinds of places we discussed above, there are three types: 1. build for public welfare, like airport 2. build for revenue, like coffee bar. For the situation 1, obviously, it has to use the solution 2, and for the situation 2, it is better to choose solution 2. In the later part, we gonna analyze each solutions.

## Solution 1: Change the price with satisfied demand

For the revenue, we consider it as:

$R = P\times C\times d - \Delta cost$

whereas the P there represent the price for unit commodity, d means days.

For the revenue function currently(after change the price), we can describe it as:

$R = P_{after}\times C_{after}\times d - Cost = P_{after}\times C_{after}\times d-Cost_{fixed}-Cost_{variable}$

Define $\sigma$ represent the (1-change ratio of C(t)), and it can be describe as:

$\sigma = 1-\frac{\Delta P}{P_{origin}}\times PE$

For the $P_{after}$, it is equal to $P_{origin} + \Delta P$ 

For $C_{after}$, it is equal to: $C_{origin}\times \sigma$

Because $C_{fixed}\propto C(t)$. Hence, $Cost_{fixed}=Cost_{fix-origin}\times \sigma$

Because $C_{variable}\propto C(t)$. Hence, $Cost_{variable}=Cost_{variable-origin}\times \sigma$

For the revenue before, we describe it as:

$R_{before} = P_{origin}\times C_{origin}\times d$

After we install the charing devices, the revenue will changed followed by the model below.

$R(P_{origin},\Delta P,d) = (P_{origin} + \Delta P)\times(C_{origin}\times\sigma)\times d-Cost_{fix-origin}\times \sigma-Cost_{variable-origin}\times \sigma \times d$

Then, the $\Delta R$ can be describe as:

$\Delta R = (P_{origin} + \Delta P)\times(C_{origin}\times\sigma)\times d-Cost_{fix-origin}\times \sigma-Cost_{variable-origin}\times \sigma \times d - P_{origin}\times C_{origin}\times d$

For the $Cost_{variable-origin}$ in the formula, it contain “Energy consumed by car” and “Energy consumed by plug-in”. In the apply part, the plug-in only consume 0.16464 energy per day which is a super small number compared to the \$228.47352 for e-car charger. Therefore,we neglect the $Cost_{variable-origin}$ for plug-in in order to simplified our model.

### Apply

For example, the coffee bar in the question 2 want to get their revenue after their free charing business runs for 100 day (d=100). 

Firstly, according to [opentextbc](https://opentextbc.ca/principlesofeconomics/chapter/5-3-elasticity-and-pricing/), we know that the price elastic of coffee is 0.3(PE=0.3), which means as the price increase by 10%, the consumer will decreased by 3%. 

Therefore, $\sigma=\frac{44-0.3\Delta P}{44}$

For the cost of ac up of coffee, we use $P_{origin} = 3$, and Profit = 1

According to the data we conduct in apply part, we can know that: 

$C_{origin} = 363$

$Cost_{fix-origin} = Cost_{fix-origin-car} + Cost_{fix-origin-plug-in} = (440+1300) =1740$

$Cost_{variable-origin} = Cost_{variable-origin-car} + Cost_{variable-origin-plug-in} = 228.47352 + 0.16464 = 228.63816$

Then, we can rewrite the formula as:

$\Delta R = (1+\Delta P)\times(363\sigma)\times 100-1740\sigma-228.63816\sigma\times 100 - 1\times 363\times 100$

 $\sigma=1 - \frac{\Delta P\times 0.03}{3\times 0.1}$