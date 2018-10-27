import numpy as np

# To find orientation/Direction of points A, B and C. 
#The function returns following a value which can indicate
#1 --> Clockwise
#2 --> Counterclockwise
#3 -->  A, B and C are colinear

def Dir(A, B, C):

	val = (B['y'] - A['y']) * (C['x'] - B['x']) - (B['x'] - A['x']) * (C['y'] - B['y']) 
	return val

# Given three colinear points A, B, C, the function checks if 
# point B lies on line segment 'AC'
def OnSegment(A, B, C):

	if(B['x'] <= max(A['x'], C['x']) and B['x'] >= min(A['x'], C['x']) and B['y'] <= max(A['y'], C['y']) and B['y'] >= min(A['y'], C['y'])):

		return True
	
	return False

#The main function that returns true if line segment (x1, x2) and (x3, x4) overlap. 
def LinearIntersect(A, B, C, D):
    #Find the four orientations/directions needed for general and 
    #special cases 
    d1 = Dir(A, B, C); 
    d2 = Dir(A, B, D); 
    d3 = Dir(C, D, A); 
    d4 = Dir(C, D, B); 
  
    #General case 
    if d1 != d2 and d3 != d4:
    	return True
    #Special Cases 
    #A, B and C are colinear and C lies on segment AB 
    if (d1 == 0 and OnSegment(A, C, B)):
    	return True 
  
    #A, B and D are colinear and D lies on segment AB 
    if (d2 == 0 and OnSegment(A, D, B)):
     	return True
  
    #C, D and A are colinear and A lies on segment CD 
    if (d3 == 0 and OnSegment(C, A, D)):
    	 return True
  
    #C, D and B are colinear and B lies on segment CD 
    if (d4 == 0 and OnSegment(C, B, D)):
    	 return True 
  
    return False #Doesn't fall in any of the above cases

# Testing the program

# Positive Test
A = {'x':1, 'y':0}
B = {'x':0, 'y':5}
C = {'x':2, 'y':0}
D = {'x':0, 'y':6}

if LinearIntersect(A, B, C, D):
	print('The two lines are overlaped')
else:
	print('The two lines are not overlaped')

# Negative Test
A = {'x':-5, 'y':-5}
B = {'x':0, 'y':0}
C = {'x':1, 'y':1}
D = {'x':10, 'y':10}

if LinearIntersect(A, B, C, D):
	print('The two lines are overlaped')
else:
	print('The two lines are not overlaped')