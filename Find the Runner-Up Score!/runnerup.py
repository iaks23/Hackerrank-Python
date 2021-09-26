if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    mylist = list(set(arr))
    
    maximum = None 
    for x in mylist:
        if maximum is None or x > maximum:
            maximum = x 
            
    mylist.remove(maximum)
    
    var = max(mylist)
    print(var)
        
        
    
 
    
    

    
    
   
        
        
    



    
    
   
 