import copy
value_dict = {}
ind = 'A'

def generatechild(puzzle,s):
    
    ans = copy.deepcopy(puzzle)
    for i in range(3):
        for j in range(3):
            if ans[i][j] == 0:
                indi = i
                indj = j
    if indi == 1 and indj == 1:
        child = 4
    elif (indi + indj) % 2 == 1:
        child = 3
    else:
        child = 2
    print(child)
    
    
    if child == 4:
        ans[indi][indj] = ans[indi-1][indj]
        ans[indi-1][indj] = 0
        
        if ans not in value_dict.values():
            value_dict[s] = ans
            s = chr(ord(s) + 1)
            generatechild(ans,s)
        ans = copy.deepcopy(puzzle)
        ans[indi][indj] = ans[indi+1][indj]
        ans[indi+1][indj] = 0
        
        if ans not in value_dict.values():
            value_dict[s] = ans
            s = chr(ord(s) + 1)
            generatechild(ans,s)
        ans = copy.deepcopy(puzzle)
        ans[indi][indj] = ans[indi][indj-1]
        ans[indi][indj-1] = 0
        
        if ans not in value_dict.values():
            value_dict[s] = ans
            s = chr(ord(s) + 1)
            generatechild(ans,s)
        ans = copy.deepcopy(puzzle)
        ans[indi][indj] = ans[indi][indj+1]
        ans[indi][indj+1] = 0
        
        ans = copy.deepcopy(puzzle)
        if ans not in value_dict.values():
            value_dict[s] = ans
            s = chr(ord(s) + 1)
            generatechild(ans,s)
            
    if child == 3:
        if indi == 0:
            ans[indi][indj] = ans[indi+1][indj]
            ans[indi+1][indj] = 0
            
            ans = copy.deepcopy(puzzle)
            if ans not in value_dict.values():
                value_dict[s] = ans
                s = chr(ord(s) + 1)
                generatechild(ans,s)
                print("next")
            ans[indi][indj] = ans[indi][indj+1]
            ans[indi][indj+1] = 0
            
            ans = copy.deepcopy(puzzle)
            if ans not in value_dict.values():
                value_dict[s] = ans
                s = chr(ord(s) + 1)
                generatechild(ans,s)
            ans[indi][indj] = ans[indi][indj-1]
            ans[indi][indj-1] = 0
            
            ans = copy.deepcopy(puzzle)
            if ans not in value_dict.values():
                value_dict[s] = ans
                s = chr(ord(s) + 1)
                generatechild(ans,s)
        elif indi == 2:
            ans[indi][indj] = ans[indi-1][indj]
            ans[indi-1][indj] = 0
            
            ans = copy.deepcopy(puzzle)
            if ans not in value_dict.values():
                value_dict[s] = ans
                s = chr(ord(s) + 1)
                generatechild(ans,s)
            ans[indi][indj] = ans[indi][indj+1]
            ans[indi][indj+1] = 0
            
            ans = copy.deepcopy(puzzle)
            if ans not in value_dict.values():
                value_dict[s] = ans
                s = chr(ord(s) + 1)
                generatechild(ans,s)
            ans[indi][indj] = ans[indi][indj-1]
            ans[indi][indj-1] = 0
            
            ans = copy.deepcopy(puzzle)
            if ans not in value_dict.values():
                value_dict[s] = ans
                s = chr(ord(s) + 1)
                generatechild(ans,s)
        elif indi == 1:
            ans[indi][indj] = ans[indi+1][indj]
            ans[indi+1][indj] = 0
                
            ans = copy.deepcopy(puzzle)
            if ans not in value_dict.values():
                value_dict[s] = ans
                s = chr(ord(s) + 1)
                generatechild(ans,s)
            ans[indi][indj] = ans[indi-1][indj]
            ans[indi-1][indj] = 0
                
            ans = copy.deepcopy(puzzle)
            if ans not in value_dict.values():
                value_dict[s] = ans
                s = chr(ord(s) + 1)
                generatechild(ans,s)
            if indj == 0:
                ans[indi][indj] = ans[indi][indj+1]
                ans[indi][indj+1] = 0
                
                ans = copy.deepcopy(puzzle)
                if ans not in value_dict.values():
                    value_dict[s] = ans
                    s = chr(ord(s) + 1)
                    generatechild(ans,s)
            else:
                ans[indi][indj] = ans[indi][indj-1]
                ans[indi][indj-1] = 0
                
                ans = copy.deepcopy(puzzle)
                if ans not in value_dict.values():
                    value_dict[s] = ans
                    s = chr(ord(s) + 1)
                    generatechild(ans,s)
                
    elif child == 2:
        if indi == 0:
            ans[indi][indj] = ans[indi+1][indj]
            ans[indi+1][indj] = 0
                
            ans = copy.deepcopy(puzzle)
            if ans not in value_dict.values():
                value_dict[s] = ans
                s = chr(ord(s) + 1)
                generatechild(ans,s)
            if indj == 0:
                ans[indi][indj] = ans[indi][indj+1]
                ans[indi][indj+1] = 0
                
                ans = copy.deepcopy(puzzle)
                if ans not in value_dict.values():
                    value_dict[s] = ans
                    s = chr(ord(s) + 1)
                    generatechild(ans,s)
            else:
                ans[indi][indj] = ans[indi][indj-1]
                ans[indi][indj-1] = 0
                
                ans = copy.deepcopy(puzzle)
                if ans not in value_dict.values():
                    value_dict[s] = ans
                    s = chr(ord(s) + 1)
                    generatechild(ans,s)
        else:
            ans[indi][indj] = ans[indi-1][indj]
            ans[indi-1][indj] = 0
                
            ans = copy.deepcopy(puzzle)
            if ans not in value_dict.values():
                value_dict[s] = ans
                s = chr(ord(s) + 1)
                generatechild(ans,s)
            if indj == 0:
                ans[indi][indj] = ans[indi][indj+1]
                ans[indi][indj+1] = 0
                
                ans = copy.deepcopy(puzzle)
                if ans not in value_dict.values():
                    value_dict[s] = ans
                    s = chr(ord(s) + 1)
                    generatechild(ans,s)
            else:
                ans[indi][indj] = ans[indi][indj-1]
                ans[indi][indj-1] = 0
                
                ans = copy.deepcopy(puzzle)
                if ans not in value_dict.values():
                    value_dict[s] = ans
                    s = chr(ord(s) + 1)
                    generatechild(ans,s)
    print(value_dict)
    return s

puzzle = [[2,8,3],[1,0,4],[7,6,5]]
ind = generatechild(puzzle,ind)

