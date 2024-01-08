def change_date(today):
    today = today[::-1]
    i = 0 
    j = 0
    new_today =""
    while ( j < len(today)):
        if ( today[j] == '-'):
            for k in range(j-1,i-1,-1):
                new_today += today[k]
            new_today += '-'
            i = j +1
            j += 1 
        else:
            j+=1
    for k in range( j-1,i-1,-1):
        new_today += today[k]  
    today = new_today
    
    return today