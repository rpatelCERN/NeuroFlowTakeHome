# NeuroFlowTakeHome
A short coding exercise from Neuroflow on analytics and SQL queries.

# Part 1
This is definitely my favorite part because it features data and is more open ended!

"Given the information you have and any light research you’d like to do on the topic, what
insights can you draw? What assumptions have you made about the data? What are 2-3
additional pieces of information that would be important to collect?"

My findings for Part 1 are summarized in these slides, which also feature interactive charts made in Tableau and linked  in the slides [NeuroFlowSlides](NeuroFlowSlides.pdf)

Below I list a short summary of the answers.

## Part 1: Table Features and Assumptions
"What assumptions have you made about the data?"

**Dimensions or independent variables** are:

* Patient ID

* Evaluation Interval: determined as the time between when the patient was created and each date an evaluation was performed. This I measured in months, since evaluations are typically done once or twice a month.

* GAD-7 Severity score ranges: This is a definition based on [Reference Papers](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7306644/) and give the ranges for histogram bins (roughly a bin size of 5)

**Dependent variable or measures**

* GAD-7 score can be used to compute various quantities for each patient or over all patients

	* The maximum for each patient indicates if they ever had a moderate or severe anxiety score. For these patients, you can track how this score changes in new evaluations

	* The average (or mean) score is also useful in identifying patients who may have ranked high in anxiety scores (near a value of 10), and their score could increase or decrease in the next evaluation period. The average score for all patients is useful in seeing if they go down on average over the evaluation periods, and how low is the average toward later evaluation dates.

	* The mode, the most frequent score, is useful per patient to see the "stickiness" of a patient in a given GAD-score range (e.g. Does the patient have many evaluations in which they score moderate or severe? Does this mean a new intervention is necessary?)

	* The standard deviation of scores for each patient is interesting because it gives an idea of the range of GAD-7 scores over evaluations. These patients are interesting to highlight to find trends across evaluation periods (Do the scores peak at the beginning and then get small or in the middle period of evaluation? Do they oscillate between high and low? ).

**Assumptions**:
* Assume on average you should count the evaluations per month (instead of weeks), since on average most patients are evaluated once or twice a month.

* Assume the treatment plan changes according to patient GAD-7 score severity. I used [this reference](https://www.efficacy.org.uk/therapy/phq-9-and-gad-7/)

* Another assumption is that in an ideal dataset, where the company performance is optimal. The data would show not just the average GAD-7 score across all patients decreasing over time, but also the standard deviation is also decreasing.
  * If the same template is assigned for a given GAD-7 score, then the same time range of evaluations patients going through the same pathways should have similar severity labels.

  * Thus, over say a 6-month evaluation period, each patient gets the right treatment plan and completes exercises that allow them to reach the same anxiety score range as anyone else assisted by NeuroFlow.

## Part 1: Business and Therapy Impact
"The clinical purpose of these assessments is to help support clinicians in making a diagnosis, to
quantify anxiety symptoms, and to monitor changes over time to see if therapy is making a
difference. The provider can see this data too, building the basis of a conversation they can
have together."

The evolution of patient GAD-7 score over evaluations is the key piece of information and are shown in the following visualizations:

* [Decrease in average GAD-7 scores across all patients over 7 months of evaluation](https://public.tableau.com/views/NeuroFlowExcercise/AverageScore?:language=en&:display_count=y&:origin=viz_share_link)

* [Pie Chart Breakdown of GAD-7 Severity Labels for each Month of evaluation](https://public.tableau.com/shared/MHJN23PNY?:display_count=y&:origin=viz_share_link) **NOTE**: You can click through different evaluation periods

* [Precision: Std Dev. Over the Average GAD-7 Score](https://public.tableau.com/views/NeuroFlowExcercise/PrecisionScore?:language=en&:display_count=y&:origin=viz_share_link)

**Conclusions**:
* Aggregate quantities like the average GAD-7 score for all patients does decrease over evaluation periods: NeuroFlow and coordinated treatment work on average!

* Behavioral health data may not be like physics data and require a different measure of precision because the distributions are less symmetric: more measurements of high scores than low scores.


## Part 1: Therapy Impact and Data Insights

Instead of looking at the aggregate of all patient scores, look at the individual patient scores across months of evaluation. NeuroFlow can highlight both steady success in treatment for the provider and time periods of alert with a spike in the GAD-7 score. Alerts would motivate when to start a conversation with the provider.

Standard deviation of the GAD-7 Scores for each patient is a good way to separate patients with consistent scores from those with scores that vary over time.

I made an interactive chart to select a group of patients with at least one high GAD-7 score (>15) over a period of 7 months of evaluation. I also require the patient to have a large standard deviation in the GAD-7 scores (>5) to see possible trends over time. This chart can be used to see how many patients there are with a certain average GAD-7 score, a range of standard deviation, and a maximum score:
* [Selected Patients](https://public.tableau.com/views/NeuroFlowExcercise/HighlighingPatients?:language=en&:display_count=y&:origin=viz_share_link)

The number of evaluations in a given month, the average GAD-7 score, and the severity label for that month is shown for 20 patients that fit the above criteria in the chart below:

* [Patient GAD-7 trends](https://public.tableau.com/shared/YPRW6SQBG?:display_count=y&:origin=viz_share_link): This interactive chart allows to scroll through 20 patients and see trends in their GAD-7 score over a 7 month evaluation period.

	* Patient 477 shows a successful steady decrease in GAD-7 scores over 7 months

	* Pateint 3262 has a sudden spike in GAD-7 score after 4 months of evaluation, but it successfully decreases

	* Patient 6798 has a spike in score followed by months where the score is low. In the last 4 months, there is a sustained increase in the GAD-7 score in the severe range.

		* Comparing patient 6798 to patient 7868 in [Multiple Evaluations Per Month](https://public.tableau.com/views/NeuroFlowExcercise/MultiEvaluationMonths?:language=en&:display_count=y&publish=yes&:origin=viz_share_link) shows having multiple evaluations in one month for patient with a mild severity score can establish how "sticky" the score is. If a patient has multiple mild or low/minimal scores, this might mean that therapy adjustment is not necessary.

	* Patient 11861 shows a steady increase in GAD-7 scores from 3 mild evaluations increasing up to a severe scores. The first 3 months are a critical period where NeuroFlow exercise feedback should be analyzed and passed on to the provider, and the treatment should be adjusted.

**Key Insights** :

  * A key success of coordinating treatment with NeuroFlow is even if there is a sudden spike in GAD-7 score, the score can decrease within 2-3 months. Prompt adjustment of the treatment plan and NeuroFlow feedback is likely essential.

	* The number of evaluations per month should be adjusted when a patient has a mild severity score. This seems like a critical period for NeuroFlow feedback and to closely monitor the patient along with the provider.

  * Long periods of low scores followed by a spike in score begs for more information (What caused the increase?) Since providers are likely outpatient, they depend on NeuroFlow to understand patient behavior outside the provider setting. Can/Does NeuroFlow provide patient information on possible triggers for anxiety: substance abuse information, sudden withdrawal (no longer leaving the home), journal entries indicating irritability, or a sudden decline in activity (failure to complete a month of exercises?)

## Part 1: Additional Information

I think NeuroFlow builds a patient profile based on provider scores like GAD-7 and PHQ9. These surveys usually cover a set of common items that give a measure for anxiety: nervousness, irritability, restlessness, and levels of fear and worry.

Additional information from NeuroFlow highly complements and is correlated to the provider score:

* **Focus**: Each day, how many tasks can a patient complete. Rank them by how focused you feel from least focused activity to most.

* **Sleep**: Track length of sleep and quality, this can provide a measure of nervousness of irritability. Marking good or bad dreams is useful and complements journal entries about any ongoing fears or worries.

* **Leaving Home** : How often and how far does the patient leave home? In how many locations do they feel safe?

* **Number of Exercises**: Completing an exercise indicates motivation, while a lull in activity may indicate a mix of anxiety or depression. Also group exercises (if they are available) can establish a level of social anxiety (and likely there is a NeuroFlow template for this)

* **Journal Entry Trigger words**: I put this one last because I am least sure about it. Using patient journal entries may breach their privacy. Instead you can count how frequently certain sentiment words are present in patients with severe scores, and use them to flag patients with mild/moderate scores if these words become prevalent in their journals.

Given this information, you can use a Bayesian classification model or a different multi-classification machine learning algorithm to map the above patient information onto potential diagnoses. From this [study of an anxiety unit at Univ of Goettingen](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4610617/figure/DialoguesClinNeurosci-17-327-g001/), I pulled a few categories of diagnoses:

* Panic Disorder/Agoraphobia

* PTSD/Acute stress disorder

* Obsessive compulsive disorder

* Social Phobia

* Generalized anxiety Disorder

* Mixed anxiety and depression

The diagnosis profile can be used to more accurately suggest a personalized pathway of NeuroFlow exercises and recommend activities for the patient. For the provider, NeuroFlow can then provide detailed feedback on adjusting the treatment plan based on the patient diagnosis profile and see how the provider agrees with the measured profile. We (if you hire me!) can then adjust the learning algorithm based on provider feedback to  more accurately predict a diagnosis.

# Part 2
From Neuroflow:
"We’d like to see how you design and write SQL for the given questions. Often our business
counterparts will ask us for a quick query to answer a question. In this case, the questions are:
How many users completed an exercise in their first month grouped by the month of user
creation? Which organizations have the most severe patient population?"

In addition, I wrote a short python script to fill in data templates generated from [Mockaroo](https://www.mockaroo.com/).
The three tables needed are a Users Table, an Exercises Table, and an Organization/Provider table.
I use Mockaroo to fill the tables with random generated data like Organization names from Pharmaceutical company names,
provider ID from ISBN numbers etc.
I also create time interval data using datetime in Python, for example, the first question in Part 2 is to determine the
% of Users who finish an exercises within their first month.

Setting the patient creation time as a datetime object, allows to add a number of days based on a gaussian random number:
```
for datestr in SignupTimes:
	date_time_obj=datetime.strptime(datestr, '%m/%d/%Y')
	SignupTimeStamps.append(date_time_obj.isoformat())
	#### Use a gaussian random number with a mean of 30 and std dev of 60:
	date_time_obj=date_time_obj+timedelta(days=abs(int(random.gauss(mu,sigma))))
	### positive (always in the future) and integer number of days from creation to assignment completion
```
The input templates are in the folder Mockaroo/ and the output tables are
1. UsersTable.csv and ExcerciseTable.csv for Solutions 1. and 2.
2. PhQTable.csv and Mockaroo/OranizationProvider.csv for Solution 3. In this case I read out the provider ID from the Mockaroo Organizations table and insert a provider ID into the first 1000 entries of the data I received from NeuroFlow.

To run the script to create a mock data:
```
python CreateMockData.py
```

I have written out the solutions below and checked them in SQLite studio, and the SQL script is [NeuroFlowSQLTasks.sql](NeuroFlowSQLTasks.sql)


## Part 2. Solution 1:
"How many users completed an exercise in their first month per monthly cohort?"

```
SELECT u.MONTH AS CohortMonth,100.*c.ExcerciseCompleted/u.UsersCreated AS PercentAssignmentCompletion
FROM
(SELECT COUNT(Id) AS UsersCreated,strftime('%Y-%m',CreationTime) AS MONTH FROM UserID AS Users GROUP BY MONTH ) AS u JOIN
(SELECT COUNT(DISTINCT Id) AS ExcerciseCompleted,strftime('%Y-%m',CreationTime)
AS MONTH FROM (SELECT * FROM Excercises JOIN UserID ON Excercises.Id=UserID.Id) WHERE DATETIME(ExcerciseCompletion)<DATETIME(CreationTime,'+1 month')  GROUP BY MONTH )
AS c ON u.MONTH=c.MONTH
```
## Part 2. Solution 2:
"How many users completed a given amount of exercises?"

```
SELECT AmtExcercises,Count(Users) AS NumUsers
FROM (SELECT Id AS Users,COUNT(ExcerciseID)
AS AmtExcercises FROM Excercises  GROUP BY Id) GROUP BY AmtExcercises
```

## Part 2. Solution 3:
Which organizations have the most severe patient population?
```
SELECT Organization,Organization_Id,AVG(Score) FROM (PHQ JOIN Org ON Org.ProviderID=PHQ.ProviderID)
GROUP BY Organization_Id ORDER BY AVG(Score) DESC LIMIT 5
```
