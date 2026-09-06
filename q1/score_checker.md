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
mermaid
graph TD
    A([START]) --> B[/INPUT score/]
    
    B --> C{score < 0 OR<br>score > 100?}
    C -- Yes --> D[DISPLAY "Invalid score"]
    C -- No --> E{score >= 90?}
    
    E -- Yes --> F[DISPLAY "Outstanding"]
    E -- No --> G{score >= 80?}
    
    G -- Yes --> H[DISPLAY "Very Satisfactory"]
    G -- No --> I{score >= 75?}
    
    I -- Yes --> J[DISPLAY "Satisfactory"]
    I -- No --> K[DISPLAY "Needs Improvement"]
    
    D --> L([END])
    F --> L
    H --> L
    J --> L
    K --> L

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
