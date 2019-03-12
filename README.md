#### While answering the overall question regarding the economic impacts of changes in college ranking, we divided the work as follows:
* Leslie focused on visualizing the change in the overall rankings and also cleaning the data for the changes in rank as well as putting together slides for the presentation.
* Brendan focused on aggregating the Census API data and creating the line plots to vizualize change over time.
* Victor originally focused on integrating the FAFSA data with the ranking data, which mid-way was abandoned, as it did not work towards the main question. At which point, the focus was shifted to creating box-plots to vizualize the change in each parameter across both groups.
* Sirui worked on the google maps API integration to vizualize the data geographically.

In order to determine the link between economic impacts and changes in college rank, we compared the 10 universities that moved up the most in the rankings between 2009-2015 and the 10 universities the moved down in the rankings the most between 2009 - 2015.

As indicators of economic impact, we were interested in changes in income (both per capita and household), though the data are linked, so it was highly unlikely that they would move in opposite directions (i.e. there would be an increase in per capita income but an overall decrease in household income and vice-versa). We also explored changes in population as well as poverty rate.

We looked at county-level data for these measures, as schools occasionally spanned multiple zip-codes. With respect to income, there did not seem to be a statistically significant difference in the change in average income, both household and per capita, between 2009 and 2015 for the communities represented by the 10 schools that improved in ranking and those 10 that fell the most in the rankings. It appears that the communities represented by the schools that fell the most have a much larger distribution in income change. This is also reflected in the comparison in the poverty rate between the two populations. The top 10 schools see on average a ~2% increase in poverty rate, as do the bottom 10 schools, but the change in poverty rate across the communities represented by the latter group varies much more greatly.

