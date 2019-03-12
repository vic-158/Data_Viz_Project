## Readme File for Victor's files
Originally, we were interested in looking at FAFSA (Free Application for Federal Student Aid) Data to see how changes in federal grants to universities impact their standing/ graduation rates/ etc. However, the available federal loan data for each school only reflected the number of awards and not the overall grant value. Therefore, the data was not included in the final analysis.
* Data_Viz_Proj_DatabySchool_CSVCreator was used to create usable csvs to be read as pandas df from the xlsx files from FAFSA.
* Data_Viz_Project_Data_Munging_FAFSA_bySChool was used to aggregate all of the individual xlsx files into dataframes per application cycle since each csv from the xlsx files only reflected one of six quarters.

Once the FAFSA data aspect was abandoned, I focused on assisting Brendan with the Census API pull.
* Data_Viz_Project_Census_Data_County used a code base provided by Brendan to query the census for povery, income, population, and age data by the counties for each of the schools identified by Leslie as the top 10 movers up and down in the rankings.
