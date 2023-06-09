# Checking for null values
bike.isnull().sum()

#checking for duplicates
bike_dup=bike
bike_dup.drop_duplicates(subset=None, inplace=True)
bike_dup.shape

#rename the columns
bike.rename(columns={'dteday':'Date','yr':'Year','mnth':'month','hum':'humidity','cnt':'count'},inplace =True)
bike.head()

#mapping the vars - season,month,weathersit,weekday
bike['season']=bike.season.map({1: 'spring', 2: 'summer',3:'fall', 4:'winter'})
bike['month']=bike.month.map({1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'June',7:'July',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'})
bike['weathersit']=bike.weathersit.map({1: 'Clear',2:'Mist + Cloudy',3:'Light Snow',4:'Snow + Fog'})
bike['weekday']=bike.weekday.map({0:'Sun',1:'Mon',2:'Tue',3:'Wed',4:'Thu',5:'Fri',6:'Sat'})
bike.head()


