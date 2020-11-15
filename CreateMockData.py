import pandas as pd
from datetime import datetime
from datetime import timedelta
import random

Mockaroo_df=pd.read_csv("./Mockaroo/DataUserID.csv")
Excercise_table_df=Mockaroo_df.drop(["CreationTime"],axis=1)
User_table_df=Mockaroo_df[["id","CreationTime"]].copy()###

#### Fill Excercise table with more meaningful completion times
SignupTimes=User_table_df["CreationTime"].to_list()
SignupTimeStamps=[]
CompletionTimes=[]
Assignments={0:"JournalEntry", 1:"Meditation",2:"clinicalExam", 3:"PainManagement",4:"SleepSurvey"}
Excercise=[]
ExcerciseID=[]

mu=30 #### Avg number days for excercise completion
sigma=60##### Std Deviation + about 2 months
for datestr in SignupTimes:
	date_time_obj=datetime.strptime(datestr, '%m/%d/%Y')
	SignupTimeStamps.append(date_time_obj.isoformat())
	date_time_obj=date_time_obj+timedelta(days=abs(int(random.gauss(mu,sigma))))### positive and integer number of days from creation to assignment completion
	CompletionTimes.append(date_time_obj.isoformat())
	ExID=random.randint(0,4)###Here though each user completes only 1 Excercise
	ExcerciseID.append(ExID)
	Excercise.append(Assignments[ExID])

	#Excercise.append()
##### Remove the dummy completion date column
User_table_df.drop("CreationTime",axis=1,inplace=True)
User_table_df.insert(loc=User_table_df.shape[1],column="CreationTime",value=SignupTimeStamps)
User_table_df.to_csv("UsersTable.csv")


Excercise_table_df.drop("Excercise_Completion",axis=1,inplace=True)
Excercise_table_df.drop("ExcerciseID",axis=1,inplace=True)
Excercise_table_df.drop("Excercise",axis=1,inplace=True)

Excercise_table_df.insert(loc=Excercise_table_df.shape[1],column="Excercise_Completion",value=CompletionTimes)
Excercise_table_df.insert(loc=Excercise_table_df.shape[1],column="Excercise",value=Excercise)
Excercise_table_df.insert(loc=Excercise_table_df.shape[1],column="ExcerciseID",value=ExcerciseID)

### A USER can complete multiple excercises! This is the 2nd SQL question
UserId=Excercise_table_df['id'].to_list()
UsersExcercise=[]
CompletionTimePerExcercise=[]
for u in range(0, len(UserId)):
	ex=random.randint(0,4)### Random how many excercises a user completes
	for i in range(ex):###Fill the new columns
		date_time_obj=datetime.fromisoformat(CompletionTimes[u])
		date_time_obj=date_time_obj+timedelta(days=abs(int(random.gauss(3,7))))#### Shift around the completion times by 3 +/- 7 days
		Excercise_table_df = Excercise_table_df.append({'id': UserId[u],'Excercise_Completion':date_time_obj.isoformat(),'Excercise':Assignments[i],'ExcerciseID':i}, ignore_index=True)

Excercise_table_df.to_csv("ExcerciseTable.csv")

del Excercise_table_df
del User_table_df
del Mockaroo_df

Mockaroo_df=pd.read_csv("./Mockaroo/OranizationProvider.csv")### This is the Organization Table
ProviderId=Mockaroo_df["Provider_Id"].to_list()
Patient_df=pd.read_csv("GAD-7FromNeuroFlow.csv")####This is the Phq9 table from NeuroFlow
Patient_df=Patient_df.head(1000)### Don't need the full Data
Providers=[]
for i in range(Patient_df.shape[0]):###Should fill 1000 provider ID entries
	ran=random.randint(0,19)
	Providers.append(ProviderId[ran])
Patient_df.insert(loc=Patient_df.shape[1],column="Provider_Id",value=Providers)
Patient_df.to_csv("PhQTable.csv")
