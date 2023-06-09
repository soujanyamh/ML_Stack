Sleep Efficiency Prediction with Ridge Regression

About Dataset:
The dataset contains information about a group of test subjects and their sleep patterns. 
Each test subject is identified by a unique "Subject ID" and their age and gender are also recorded. 
The "Bedtime" and "Wakeup time" features indicate when each subject goes to bed and wakes up each day, and the "Sleep duration" feature records the total amount of time each subject slept in hours.
The "Sleep efficiency" feature is a measure of the proportion of time spent in bed that is actually spent asleep.
The "REM sleep percentage", "Deep sleep percentage", and "Light sleep percentage" features indicate the amount of time each subject spent in each stage of sleep. 
The "Awakenings" feature records the number of times each subject wakes up during the night.
Additionally, the dataset includes information about each subject's caffeine and alcohol consumption in the 24 hours prior to bedtime, their smoking status, and their exercise frequency.

Summary:
**-Goal of the project is to predict sleep efficiency with respective features

-Methods used : Linear Regression, Ridge Regression, Lasso Regression

-Performance of methods : Linear and Ridge Regression performed almost similar and Lasso could not perform well at all

-Verdict : Ridge Regression(alpha=15.0) performs best
