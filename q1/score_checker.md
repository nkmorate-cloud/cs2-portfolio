# Clean Decision Code Makeover: Student Score Checker 
**Name:** NEIDGEL KATE MORATE
**Section:** 8-Dahlia
--- 
## Activity Overview 
In this activity, I improved a Student Score Checker program by applying proper coding standards and selection structures. 
The program accepts a student score from 0 to 100 and determines the appropriate classification. 
The classifications are: 
| Score | Classification | 
|---:|---| 
| 90–100 | Outstanding | 
| 80–89 | Very satisfactory | 
| 75-79 | Satisfactory | 
| 0–74 | Needs Improvement | 
| Scores below 0 or above 100 | considered invalid. |
--- 

# 1
Input: What information does the program need?  
* The student's score (or numbers representing their score)

Boundary: What is the minimum valid score?
* 0

Boundary: What is the maximum valid score?
* 100

Possible Outputs: What outcomes can the program produce? 
* Invalid score (for scores below 0 and above 100),  Outstanding (for scores between 90 and 100), Very satisfactory (for scores between 80 and 89), Satisfactory (for scores between 75 and 79), Needs improvement (for scores below 75)

Selection Pattern: Which part uses a boundary condition?
* (if score < 0 or score > 100:) uses boundary conditions 

Selection Pattern: Which part uses multiple decision paths?
* (elif score >= 90: ... elif score >= 80: ... else:) uses multiple decision paths

# 2
* [ START ]
*           │
*           ▼
*     / INPUT score /
*           │
*           ▼
*     /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
*    < score < 0 OR > 100?    > ─── Yes ───► [ DISPLAY "Invalid score" ]
*     \______________________/                       │
*           │ No                                     │
*           ▼                                        │
*     /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\                       │
*    <      score >= 90?      > ─── Yes ───► [ DISPLAY "Outstanding" ]
*     \______________________/                       │
*           │ No                                     │
*           ▼                                        │
*     /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\                       │
*    <      score >= 80?      > ─── Yes ───► [ DISPLAY "Very Satisfactory" ]
*     \______________________/                       │
*           │ No                                     │
*           ▼                                        │
*     /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\                       │
*    <      score >= 75?      > ─── Yes ───► [ DISPLAY "Satisfactory" ]
*     \______________________/                       │
*           │ No                                     │
*           ▼                                        │
*    [ DISPLAY "Needs Improvement" ]                 │
*           │                                        │
*           ▼                                        ▼
*           └───────────────────────────────────────►[ END ]


# 3
* START
* INPUT score

* IF score < 0 OR score > 100 THEN
*    DISPLAY "Invalid score"
* ELSE IF score >= 90 THEN
*    DISPLAY "Outstanding"
* ELSE IF score >= 80 THEN
*    DISPLAY "Very Satisfactory"
* ELSE IF score >= 75 THEN
*    DISPLAY "Satisfactory"
* ELSE
*    DISPLAY "Needs Improvement"
* END

# 4
[Score Checker Source Code](./q1/score_checker.py) 

# 5
| Test | Input | Purpose | Expected Output | Actual Output | Result | |---|---:|---|---|---|---| 
| 1 | -1 | Below minimum | | | | 
| 2 | 0 | Minimum boundary | | | | 
| 3 | 74 | Below Satisfactory boundary | | | | 
| 4 | 75 | Satisfactory boundary | | | | 
| 5 | 80 | Very Satisfactory boundary | | | | 
| 6 | 90 | Outstanding boundary | | | | 
| 7 | 100 | Maximum boundary | | | | 
| 8 | 101 | Above maximum | | | | 

