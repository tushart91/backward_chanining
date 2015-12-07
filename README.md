backward_chanining
==================
```
Backward Chaining for First Order Logic.
Only AND,=> operator supported.
```

###Format of input for solver:
```
Query
No of lines in KB
Statement(s) to be put in KB (in Horn form)
```

###Example:
```
Diagnosis(John,Infected)
6
HasSymptom(x,Diarrhea)=>LostWeight(x)
LostWeight(x)&Diagnosis(x,LikelyInfected)=>Diagnosis(x,Infected)
HasTraveled(x,Tiberia)&HasFever(x)=>Diagnosis(x,LikelyInfected)
HasTraveled(John,Tiberia)
HasFever(John)
HasSymptom(John,Diarrhea)
```

###Output
```
The output is either TRUE or FALSE in the output.txt file.
TRUE if a substitution can be made and the query can be infered through substituion and FALSE if NOT.
To see the substitution change DEBUG = False to True in solver.py
```
