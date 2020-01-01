# Introduction

for different places, it has the different variables. Nevertheless, the model is not changed. This part will show you a example about library, which has the consumer distribution shown below:

`[need graph]`

[  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0., 276.,438., 503., 528., 552., 579., 529., 383., 137.,  76.,   0.,   0., 0.,   0.]

## Energy consumption for E-car charging

According to the model 1, the coffee shop has the attribute of shop. Therefore, its p(x) should be:

$P_{x} = 0.02576 \mathrm{e}^{2.566 x}+2.244 \times 10^{-7} \mathrm{e}^{14.86 x}$

For the $P_{e-car}$, according to `Nanalyze`, there are approximately 21.6% of people who own electronic car.

For the constant variable: $C_{e-car}$, according to the graph, it should be: 

 $C_{e-car}$ = $\sum_{0}^{24}C(t)\times P_{e-car}=$ 4001$\times$ 21.6% $\approx$ 864

For the $T$, we use Tesla Model 3 as an example, its T = 50 kWh

Then, we can apply the p(x) function to model 3, which is:

$E_{e-car}(x) = \sum_{x=0}^{10}{\frac{1}{\sqrt{2 \pi} \times 0.1772} \mathrm{e}^{-\frac{(\frac{x}{10}-0.5137)^{2}}{2 \times 0.1772^{2}}}\times ( 0.02576 \mathrm{e}^{2.566 x}+2.244 \times 10^{-7} \mathrm{e}^{14.86 x})\times 78\times 50\times \frac{x}{10}}$

`[result]`



The change of the place will cause the change in variables. Nevertheless, the model will not be change. For example, if our research target is library, which is the recreation devices. the variables and function below will occur changes:

1. P(x)
2. C(t)
3. C

For example, if our research take place in NY national library, it

1. P(x) = $0.02576 \mathrm{e}^{2.566 x}+2.244 \times 10^{-7} \mathrm{e}^{14.86 x}$
2. C(t) `[graph]`
3. C: 4001