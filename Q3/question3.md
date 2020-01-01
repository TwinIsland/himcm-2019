As we shown above, for different places, for example, university and coffee shop. We should choose distinct models. In this part, we use an example of public place to describe how our model changes. We use university of MIT as an instance, to analyze the demand of the E-car charging station to satisfied 11376 students’ demands in charging. In addition, consider that approximately 80% student own their cars. Therefore, in the foundation that 21.6% people own E-car, we times it by 80%. For its P(x) function, because the attribute of university is belong to place of recreation, it is different to coffee shop. 

or government places, like university, the propose they provide free charging service is for meet the demand of student and professor, but nor for making money by attracting consumer though free charging service. Plus, the current plug-in is already satisfied students’ demand and the energy consuming for plug-in is relatively small compared to that of E-car charger. As the result, we neglect the factor of plug-in in this model.

P(x) =  $p_{\text {c-recreation }}(x)=0.02576 \mathrm{e}^{2.566 x}+2.244 \times 10^{-7} \mathrm{e}^{14.86 x}$

$C_{EVs} = 11376\times 0.216\times 0.7 \approx 1721$

$E_{e-car}(x) = \sum_{x=0}^{10}{\frac{1}{\sqrt{2 \pi} \times 0.1772} \mathrm{e}^{-\frac{(\frac{x}{10}-0.5137)^{2}}{2 \times 0.1772^{2}}}\times (0.02576 \mathrm{e}^{2.566 \frac{x}{10}}+2.244 \times 10^{-7} \mathrm{e}^{14.86 \frac{x}{10}})\times 1721\times 50\times \frac{x}{10}}$

=> E = 61473.54kW*h

![1573984865955](../../1573984865955.png)

After we get the energy consumption model, we can calculate the model 4.1

For university, it is not seem like that the people inside will change though time. Therefore, $C(t)\times P_{e-car} = 1721$

