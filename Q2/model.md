## Variable

| Term | description                            |
| ---- | -------------------------------------- |
| C    | consumer who own e-car                 |
| T    | elctronic capatior for an e-car        |
| X    | SOC: the electrocity that already used |
| t    | time(0~24)                             |
| E    | energy consumption                     |

## Model

**model 1: the distribution for initial  SOC:**

$f_{\mathrm{c}}(x)=\frac{1}{\sqrt{2 \pi} \times 0.1772} \mathrm{e}^{-\frac{(x-0.5137)^{2}}{2 \times 0.1772^{2}}}$

**model 2: the distribution for charing demand probability**

$p_{\mathrm{c}-\mathrm{shop}}(x)=0.01272 \mathrm{e}^{2.474 x}+1.528 \times 10^{-5} \mathrm{e}^{10.95 x}$

**model 3: the distribution for  consumer popular time**

*Assume it adapt the normal distribution, then:*

$C(t,\mu,\sigma)=\frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{(t-\mu)^{2}}{2 \sigma^{2}}}$

for the variable $\mu$ and $\sigma$, it depend on each shop’s real situation, which can be easily calculated. Later, we will show a DEMO.

**model 4: the energy demand function:**

For: P<sub>(the SOC for car owner is x)</sub> $\cup$ P(the E-car owner want to charge), we can briefly describe as:

$f_c(x)\times p_{x-shop}(x)$

and for the number of people, it is:

$f_c(x)\times p_{x-shop}(x)times C$

then, for the energy consumption for a singer car, it can be describe as:

$E_{total} = T\times X$

Finally, considering the time distribution which shows in *model 3* and for the e-car owner with different SOC, we can build the *energy consumption model by*: 

$E = \sum_{t=0}^{24}{\int_{0}^1{f_c(x)\times p_{x-shop}(x)\times C(t)\times X\times T}}$

or it can also be write as:

$E = \sum_{t=0}^{24}{\int_{0}^1{\frac{1}{\sqrt{2 \pi} \times 0.1772} \mathrm{e}^{-\frac{(x-0.5137)^{2}}{2 \times 0.1772^{2}}}\times (0.01272 \mathrm{e}^{2.474 x}+1.528 \times 10^{-5} \mathrm{e}^{10.95 x})\times \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{(t-\mu)^{2}}{2 \sigma^{2}}}\times X\times T}}$

however, to simplify as model solving procedural, we can consider the *consumer popular time* as a single variable. That is, we turn $C(t)$ to a constant *P* which describe the total consumers in a shop in a single day. Subsequently, we can rewrite our model like:

$E = \int_{0}^1{\frac{1}{\sqrt{2 \pi} \times 0.1772} \mathrm{e}^{-\frac{(x-0.5137)^{2}}{2 \times 0.1772^{2}}}\times (0.01272 \mathrm{e}^{2.474 x}+1.528 \times 10^{-5} \mathrm{e}^{10.95 x})\times X\times T}$