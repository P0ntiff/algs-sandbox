





fixed_length_window(arr)
 - initialise:
    - l, r = 0, 0
    - some data structure for window info 
    - current best to 0 
 - while we can grow the window  (r < len(arr))
    - increase the window (update data structure & increase r) 
    - if the window is at size (r - l == k)
        update current best 
        update the data structure 
        shrink the window (update data structure & increase l)
 - return answer 

reset_length_window(arr)
 - initialise:
    - l, r = 0, 0
    - data structure to track window info 
    - answer 
 - while r < len(arr)
     if can grow window (window is still valid with one more element, which is at r)
        grow window (update data structure and increase r)
        update answer 
     else:
        reset window to the position after the problematic element
- return answer 