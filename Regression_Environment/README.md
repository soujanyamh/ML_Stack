Dissolved oxygen prediction in river water
This dataset has data of the 5 indicators of river water quality from 8 consecutive stations of the state water monitoring system. It's should predict the value in the eighth station by the first seven stations. The numbering of stations in the dataset is done from the target station upstream, ie closest to it - first, upstream - second, etc.
Data are average monthly. The number of observations on stations is different (from 4 to about 20 years).

Training and test data are chosen so that the percentage of non-NA values on stations with long and short series data is approximately the same. Test data do not contain target column, as in the future it is planned to organize a competition to predict this data.
Indicators of river water quality in this dataset are:
•	Dissolved oxygen (O2) is measured in mgO2/cub. dm (ie milligrams of oxygen (O2) in the cubic decimeter);
•	Ammonium ions (NH4) concentration is measured in mg/cub. dm (ie milligrams in the cubic decimeter);
•	Nitrite ions (NO2) concentration is measured in mg/cub. dm (ie milligrams in the cubic decimeter);
•	Nitrate ions (NO3) concentration is measured in mg/cub. dm (ie milligrams in the cubic decimeter);
•	Biochemical oxygen demand, which is determined in 5 days ("BOD5" or "BOD"). BOD5 is measured in mgO/cub. dm (ie milligrams of oxygen in the cubic decimeter).
The minimum permissible value of O2 in Ukraine is 4 mgO2/cub. dm.
Id - the unique id of a given monthly averaged data;
target - a values of monthly averaged data of O2 in target station, mgO2/cub. dm;
1-7 - a values of monthly averaged data in stations 1-7 (in seven stations located from the target station upstream)
Inspiration

The most interesting are the following tasks:
1.	Analysis of data dependences, including EDA.
2.	Prediction the target data (water quaity in the target station) with the highest accuracy.
3.	Analysis of impact on the prediction accuracy of the first two stations (1-2) and the next five (3-7) stations separately.
