# Introduction

Generally speak, to calculate the energy demand and the charging devices demand, we mainly consider two parts: the Electronic car charger(e-car) and the plug-in. In the later model, we will build a model to help the shop manager to estimate the energy consumption and the demand for charging devices.

# Assumption

1. People only use the plug in to charge their phone
2. The total electric quantity for phone and the e-car are the same for everybody.
3. No maintaining fee for the car charger and plug in
4. Everyone has one phone which have power of 3000mAh and 3.6v

# Part 1: the energy consumption for e-car and the device demand model

## Model 1: The relationship between SOC and the probability for people to charge their car

SOC mean the energy consumption percentage for a single car. Like if SOC=10%, it means that the user had already used 10% of the total electric quantity in car.  By fitting the data collected by the `NHTS2009`(National
Household Travel Survey 2009). It is easy for us to draw the graph which shows the relationship between *SOC* and *the probability that people charge their car* in various places, we define this function as $P(x)$, where $x$ represent *SOC*

![1573900955078](../../../AppData/Roaming/Typora/typora-user-images/1573900955078.png)

<center><i>data analyzed by Mr. Tao in Configuration Ratio for Distributed Electrical Vehicle
    Charging Infrastructures</i></center>

according to the fitting result from Mr. Tao, the joint probability density function are:

$p_{\mathrm{c}-\mathrm{work}}(x)=0.007483 \mathrm{e}^{-1.289 x}+0.0196 \mathrm{le}^{3.95 x}$

$p_{\mathrm{c}-\mathrm{shop}}(x)=0.01272 \mathrm{e}^{2.474 x}+1.528 \times 10^{-5} \mathrm{e}^{10.95 x}$

$p_{\text {c-recreation }}(x)=0.02576 \mathrm{e}^{2.566 x}+2.244 \times 10^{-7} \mathrm{e}^{14.86 x}$

## Model 2: The relationship between initial SOC and the probability

The US department of energy initiated the EV Project which make a statistics on the driving and charging pattern of electric vehicles. And the result of initial SOC is shown below, which is likely to be a normal distribution. We define it as $f(x)$

![1573871736642](../../../AppData/Roaming/Typora/typora-user-images/1573871736642.png)

Also, according to the fitting result from Mr. Tao, the joint probability density function are: $f(x)=\frac{1}{\sqrt{2 \pi} \times 0.1772} \mathrm{e}^{-\frac{(x-0.5137)^{2}}{2 \times 0.1772^{2}}}$

## Model 3: The Energy consumption model for E-car

### Variable

| Term              | description                              |
| ----------------- | ---------------------------------------- |
| C<sub>e-car</sub> | consumer who own e-car                   |
| T                 | electronic capacitor for an e-car        |
| x                 | SOC: the electricity that already used   |
| E<sub>e-car</sub> | energy consumption                       |
| t                 | time                                     |
| $B_{charger}$     | the building cost for single car charger |
| P<sub>e-car</sub> | probability that consumer own E-car      |

Firstly, we assume that the function of distribution graph for coffee bar is: $C(t)$ For different shops, we have different distribution function. After the model part, we will show a demo.

$C(t)$: The distribution for consumer number in different time

For the people who own the E-car, the probability they use the E-car can be simply describe as:

People use e-car charger = P<sub>(the SOC for car owner is x)</sub> $\times $ P<sub>(the E-car owner want to charge)</sub>$\times C_{e-car}$ = $f(x)\times p(x)\times C_{e-car}$

For the energy demand for a single car to charge from $(1-Soc)$ to the full-charged status, it can be describe as:

E<sub>for single car</sub> $= T\times x$

If we considered the demand for all the people, the function will be like:

$E_{e-car}(C_{e-car}) = {\sum_{x=0}^{10}{f(\frac{x}{10})\times p(\frac{x}{10})\times C_{e-car}\times T\times \frac{x}{10}}}$

For the $f(x)$. because it only depended on the individual willing for each car-owners, no matter where the statistic is taking place. However, for the function $p(x)$, it correlate with the place. Therefore, we can rewrite the E<sub>e-car</sub>function as: 

$E_{e-car}(C_{e-car}) = \sum_{x=0}^{10}{\frac{1}{\sqrt{2 \pi} \times 0.1772} \mathrm{e}^{-\frac{(\frac{x}{10}-0.5137)^{2}}{2 \times 0.1772^{2}}}\times p(\frac{x}{10})\times C_{e-car}\times T\times \frac{x}{10}}$

### Model 3.1: The costing model for E-car

The cost is made by two parts: the *Fixed costs* and *Variable cost*, which is:

$CE_{total} = CE_{fixed} + CE_{variable}$

For the $CE_{variable}$, it can be easily calculated by: $CE_{variable} = E_{e-car}\times F$, whereas $F$ there represent the cost for unit energy (W*h)

To find the $CE_{fixed}$, we need to know the total number of car charger: $Q_{e-car}$ that should be build, to get it, we build a model to represent the highest demand of car charge in a day, which can be described as:

$Q_{e-car} = {p(x)\times f(x)\times C(t)\times P_{e-car} | (f(x)\times p(x))' = 0, C(t)' = 0}$

Therefore, the $CE_{total}$ will be: 

$CE_{total} = Q_{e-car}\times B_{charger} + F\times E_{e-car}\times d$, whereas $d$ represent the day.

# Part 2: the energy consumption for plug-in and the devices demand model

## Model 4: The Energy consumption model for plug-in

According to the research by LG, when the phone’ s power is less than 20%, people will began to show the wonder of charging. Therefore, the probability that a consumer in a shop need to charge his/her phone is: 

P<sub>charge phone</sub> = P<sub>power less than 20%</sub> $\times$ P<sub>charge in public place</sub> 

For the P<sub>charge in public place</sub>. we can consider it as 100% since the coffee bar provide enough plug-in

To get the data from  P<sub>power less than 20%</sub>, we use the data collect from the charging behavior from a person in a whole day

![1573900664174](../../../AppData/Roaming/Typora/typora-user-images/1573900664174.png)

For the red part, it represent the situation that $charge<20%$, which take 25.21008% of the whole data. Therefore, P<sub>power less than 20%</sub> = 25.21008%

Assume that the total traffic per day is $C$. Them the total Energy consumption can be describe as:

$E_{plug-in} =$ P<sub>power less than 20%</sub> $\times$ P<sub>charge in public place</sub> $\times$ C $\times$ $T_{phone}\times$(1-20%) $\times(1+\sigma)$

For the $T_{phone}\times$(1-20%), it can be calculate by: 

$T_{phone}\times(1+\sigma)\times$(1-20%) = $\frac{3000mAh\times 1.8 \times 3.6v\times 0.8}{1000} = $ 0.015552 kWh, where as $\sigma$ there represent the energy loss when charging.

Then, the function of $E_{plug-in}$ can be write as:

$E_{plug-in} = 0.2521008 \times C \times 0.015552kWh = 0.004\times C$

### Model 4.1: The costing model for Plug-in

Similar to the model 3.1, we need to know the number of plug-in. To calculate that, considering the possible max plug-in usage which can be measured by:

$Q_{plug-in} = C(t) | PR(t)=0.2$, whereas $PR(t)$ represent the function which describe the relationship between charge and time​. Finally, we can modeling the total cost for plug-in: $CP_{total}$ as:

$CP_{total} = E_{plug-in}\times F\times d+ Q_{plug-in} \times B_{plug-in}$

# Apply

There is a coffee bar in the center of the city, which has the consumer traffic distribution shown below:

![1573886374781](../../../AppData/Roaming/Typora/typora-user-images/1573886374781.png)

<center><i>Data from a Starbuck in Switzerland.                   </i></center>
## Energy consumption for E-car charging

According to the model 1, the coffee shop has the attribute of shop. Therefore, its p(x) should be

$p(x)=0.01272 \mathrm{e}^{2.474 x}+1.528 \times 10^{-5} \mathrm{e}^{10.95 x}$

For the $P_{e-car}$, according to `Nanalyze`, there are approximately 21.6% of people who own electronic car.

For the constant variable: $C_{e-car}$, according to the graph, it should be: 

 $C_{e-car}$ = $\sum_{0}^{24}C(t)\times P_{e-car}=$ 363$\times$ 21.6% $\approx$ 78

For the $T$, we use Tesla Model 3 as an example, its T = 50 kWh

Then, we can apply the p(x) function to model 3, which is:

$E_{e-car}(x) = \sum_{x=0}^{10}{\frac{1}{\sqrt{2 \pi} \times 0.1772} \mathrm{e}^{-\frac{(\frac{x}{10}-0.5137)^{2}}{2 \times 0.1772^{2}}}\times (0.01272 \mathrm{e}^{\frac{2.474x}{10}}+1.528 \times 10^{-5} \mathrm{e}^{\frac{10.95x}{10}})\times 78\times 50\times \frac{x}{10}}$

=> E= 1903.946 kw*h

Which shown below.

![1573893691238](../../1573893691238.png)

`[breifly explain this graph]`

After we get the energy consumption model, we can calculate the model 4.1

According to our calculating, when t=18, C(t) raise to the max value, which is 44.

And when 777x=65.45(SOC = 0.6545), $f(x)\times g(x)' = 0$, and $f(x)\times g(x) = 0.1379595$

![1573975736148](../../../AppData/Roaming/Typora/typora-user-images/1573975736148.png)

Therefore, for the model 3.1, we can calculate its $Q_{charger}$

$Q_{e-car} = (p(x)\times f(x)\times C(t)\times  P_{e-car} | (f(x)\times p(x))' = 0, C(t)' = 0)=0.1379595\times 44\times 0.216 \approx 1.3$

which means to satisfied all the consumer’ s demand for charging their car, the number of e-car charger they have to build is 2

And for the F, we use the American electric charge: F=0.12 dollar/kWh, and for the $B_{charger}$, the most common charging devices cost: $1,000. Then, we can use model 3.1 to solve the cost out:

$CE_{total} = Q_{e-car}\times B_{charger} + F\times E_{e-car}\times d =1.3\times 1000 + 0.12\times 1903.946\times d = 1300 + 228.47352\times d$

**Conclusion:**

For the conclusion, to satisfied consumer’ s demand in charging e-car, the coffee bar should build 1.3 e-car charging station, approximately use 1903.946 kWh power. For the relationship between price and day, it can be describe as:  $CE_{total}=1300 + 228.47352\times d$. 

## Energy Consumption for plug-in

According to the $E_{plug-in} = 0.00048\times C$, we can easily calculate the Energy cost plug-in is: $0.004\times343 = 1.372kWh$

Then, to get the $Q_{plug-in}$, we use model 14.1, when PR(t)=0.2, t = 18 or t = 12. In these two situation, the C(t) = 22 and 44. To satisfied all the consumer’ s demand, we use 44 for our t. Therefore, $Q_{plug-in} = 44$

For F, we use 0.12

For the most common plug-in, it cost $10 t build one. Therefore, B=10

$CP_{total} = E_{plug-in}\times F\times d + Q_{plug-in} \times B_{plug-in} = 1.372\times 0.12\times d + 44\times 10 = 0.16464\times d + 440$

**Conclusion:**

For the conclusion, to satisfied all consumer’ s demand to charge their phone, the coffee bar should install 44 plug-in, and everyday,  those plug-in will cost them 1.372 kWh, and the cost function though time is: $CP_{total} = 0.16464\times d + 440$