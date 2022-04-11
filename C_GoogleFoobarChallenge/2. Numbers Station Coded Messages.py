  '''
  My inital code - a brute force checker - took too long to run, which failed the hidden edge cases. 
  
  So, I had to rework it to get a faster, more linear runtime. 
  
  The difference in code is minimal; however, the use of a generator and while-loop drastically improved performance.
  '''
  #ORIGINAL CODE:  
  def solution(a, t_Num):
    for i in a: 
        total = 0             #Restart at 0
        for j in range(i, len(a)):
            total += a[j]
            if total == t_Num:          # if params are equal...
                return i, j             # Send the beg. & end. indexes
            if total > t_Num:           # if total is larger...
                break                   # Stop and go to next    
    return -1, -1                       # If neither, then nothing found. 
  
  #FASTER CODE: (Passed the inital 5 exams. Scored 50% overall 😢)
  def solution(a, t_Num):
    rBeg = rEnd = 0
    
    while rBeg <= rEnd and rEnd < len(a):
        repo = sum(a[rBeg:rEnd+1])    # Generator use to save time
        if repo == t_Num:
            return [rBeg, rEnd]
        elif repo < t_Num:
            rEnd += 1
        else:
            rBeg += 1
            rEnd = max(rBeg, rEnd)
    return [-1,-1]
    
    

    
