CREATE TABLE UserID(
    Ind INTEGER,
    Id TEXT,
    CreationTime DATE
)
CREATE TABLE Excercises(
    Ind INTEGER,
    Id TEXT,
    ExcerciseCompletion DATE,
        Excercise TEXT,
    ExcerciseID INTEGER
)


/* How many users in each cohort? Denominator 
SELECT COUNT(Id) AS UsersCreated,strftime('%Y-%m',CreationTime) AS MONTH FROM UserID AS Users GROUP BY MONTH  */

/* How many distinct users completed their excercise within their first month? Numerator
SELECT COUNT(DISTINCT Id) AS CreationTime,strftime('%Y-%m',CreationTime) AS MONTH FROM (SELECT * FROM Excercises JOIN UserID ON Excercises.Id=UserID.Id)
AS CompletedAssignment
WHERE DATETIME(ExcerciseCompletion)<DATETIME(CreationTime,'+1 month') GROUP BY MONTH
*/
 
/* Divide Numerator by Denominator and multiply by 100 ANSWER TO SQL Problem 1:*/
/*How many users completed an exercise in their first month per monthly cohort? What percentage*/
SELECT u.MONTH AS CohortMonth,100.*c.ExcerciseCompleted/u.UsersCreated AS PercentAssignmentCompletion 
FROM 
(SELECT COUNT(Id) AS UsersCreated,strftime('%Y-%m',CreationTime) AS MONTH FROM UserID AS Users GROUP BY MONTH ) AS u JOIN 
(SELECT COUNT(DISTINCT Id) AS ExcerciseCompleted,strftime('%Y-%m',CreationTime) 
AS MONTH FROM (SELECT * FROM Excercises JOIN UserID ON Excercises.Id=UserID.Id) WHERE DATETIME(ExcerciseCompletion)<DATETIME(CreationTime,'+1 month')  GROUP BY MONTH )
AS c ON u.MONTH=c.MONTH

/* How many users completed a given amount of exercises?*/
SELECT AmtExcercises,Count(Users) AS NumUsers 
FROM (SELECT Id AS Users,COUNT(ExcerciseID) 
AS AmtExcercises FROM Excercises  GROUP BY Id) GROUP BY AmtExcercises

CREATE TABLE PHQ(
    Ind INTEGER,
    date DATE,
    patient_id INTEGER,
    type TEXT,
    patient_date_created DATE,
    score INTEGER,
    ProviderID TEXT
)
CREATE TABLE Org(
    Organization TEXT,
    Organization_Id TEXT,
    ProviderID TEXT
)
SELECT * FROM PHQ WHERE patient_id=8214
/* Which organizations have the most severe patient population? */
SELECT AVG(Score) FROM (PHQ JOIN Org ON Org.ProviderID=PHQ.ProviderID) GROUP BY Organization_Id ORDER BY AVG(Score) DESC