# Programming Assignment 1 Tests
# This file includes a set of tests to make sure that your code behaves as
#    expected. These tests are not at all intended to be exhaustive. You
#    should design more tests for your code in addition to these. 


def twoToTheN(n):
    """ Calculates 2^n in log(n) time"""
    if(n==0):
        return 1;
    elif(n==1):
        return 2;
    elif(n%2 == 0):
        #if exponent is even then we know that 2^8 = 2^4 *2^4  
        #we can use this fact to only multiply up to 2^4 and then square it reducing the number of multiplications
        temp = twoToTheN(n/2)
        return square(temp);
    else:
        #if exponent is odd, we can use the same knowledge along with the extra fact
        # 2^9 = 2^8 * 2  
        temp = twoToTheN( (n-1) /2)
        return 2*square(temp)

def square(x):
    """ Calculates the square of x"""
    return x*x;


print "\nProblem 1: \n"
        
print "twoToTheN test case #1: " + str(twoToTheN(3) == 8)
print "twoToTheN test case #2: " + str(twoToTheN(0) == 1)
print "twoToTheN test case #3: " + str(twoToTheN(10) == 1024)




def sum(L):
    """ Calculates the sum of all the elements in a list"""
    temp=0;
    if (len(L) == 0):
        return 0;
    elif (len(L) == 1):
        return L[0];
    else:
        temp = L[0]+ sum(L[1:]);
        return temp;


def mean(L):
    """ Calculates the mean of all the elements in a list"""
    if(len(L)==0):
        return 0;
    elif(len(L)==1):
        return L[0]
    else:
        total = float(sum(L))
        length = float (len(L))
        return total/length;





def median(L):
    """ Calculates the median of all the elements in a list"""
    if(len(L)==0):
        return 0;
    elif(len(L)%2==0):
        while(len(L)>2):
            L.remove(max(L))
            L.remove(min(L))
        return mean(L);
    else:
        while(len(L)>1):
                L.remove(max(L))
                L.remove(min(L))
        return L[0];



    
print "\nProblem 2: \n"

w = [-1, 2, 2, -4]
x = [5,1,2,3,1] 
y = [5,1,2,3,1,4]
z = []


print "mean test case #1: " + str(mean(x) == float(12)/float(5))
print "mean test case #2: " + str(mean(y) == float(16)/float(6))
#empty list
print "mean test case #3: " + str(mean(z) == 0)
#negatives
print "mean test case #4: " + str(mean(w) == float(-1)/float(4))
print "median test case #1: " + str(median(x) == 2)
print "median test case #2: " + str(median(y) == 2.5)
#empty list
print "median test case #3: " + str(median(z) == 0)
#negatives
print "median test case #4: " + str(median(w) == 0.5)







def bfs(tree, elem):
    """ Searches for elem in a tree using a breadth first search"""
    #make sure first element of top list is not a list
    fringe =[]; #create FIFO queue for fringe
    if (isinstance(tree[0],list)):
        return -1;
    else:
        # 1. Add the initial state (root) to the <fringe>
        fringe.append(tree[0]) 
        if (fringe == []):
            return false;
        else:
            curr = fringe.pop()
            # 3. Is curr a goal state?
            print curr
            if (curr == elem):
                return True
            else:
                fringe = tree[1:]
    while True:
        if (fringe == []):
            return False;
        else:
            curr = fringe[0]
            fringe.remove(curr);
            if (isinstance(curr,list)):
                #if current is a list then add its 
                fringe.extend(curr[0:])
                            # 3. Is curr a goal state?
            else:
                print curr;
                if (curr == elem):
                    return True;
                # If so, SOLUTION  
                # If not, continue
                # 4. Expand curr by applying all possible actions (add
        # 5. Go to step 2

#def dfs(tree, elem):





#myTree = [4, [10, [33], [2]], [3], [14, [12]], [1]]
def dfs(tree, elem):
    """ Searches for elem in a tree using a depth first search"""
    #make sure first element of top list is not a list
    fringe =[]; #create LIFO stack for fringe
    if (isinstance(tree[0],list)):
        return -1;
    else:
        # 1. Add the initial state (root) to the <fringe>
        fringe.append(tree[0]) 
        if (fringe == []):
            return false;
        else:
            curr = fringe.pop()
            # 3. Is curr a goal state?
            print curr
            if (curr == elem):
                return True
            else:
                fringe = tree[1:]
    while True:
        if (fringe == []):
            return False;
        else:
            curr = fringe.pop()
            if (isinstance(curr,list)):
            #if current is a list then add its contents to the front of the stack 
                if (len(curr) < 1):
                    return -1
                else:
                    print curr[0]
                    if(curr[0]==elem):
                        return True
                    fringe.extend(curr[0:])
                # If so, SOLUTION  
                # If not, continue
                # 4. Expand curr by applying all possible actions (add
        # 5. Go to step 2












print "\nProblem 3: \n"

myTree = [4, [10, [33], [2]], [3], [14, [12]], [1]]
print "bfs test case #1: " + str(bfs(myTree, 1) == True)       + "\n"     
print "bfs test case #2: " + str(bfs(myTree, 7) == False)      + "\n" 
print "dfs test case #1: " + str(dfs(myTree, 1) == True)       + "\n" 
print "dfs test case #2: " + str(dfs(myTree, 7) == False)      + "\n" 






class TTTBoard:
    """This polygon class is here to show you how to use classes in python."""
    
    def __init__(self):      
            self.game = [    "*", "*", "*", 
                             "*", "*", "*",
                             "*", "*", "*"  ]

    def __str__(self):
            return " %s  " "  %s  " " %s \n %s  " "  %s  " " %s " "\n %s  " "  %s  " " %s " "  \n" % (self.game[0],self.game[1],self.game[2], self.game[3],self.game[4],self.game[5],self.game[6],self.game[7],self.game[8])

        
    def makeMove(self, player, pos):
        if(player == "X" or player == "O"):
            if (pos < 9 and pos >= 0):
                if (self.game[pos] == "*"):
                    self.game[pos] = player
                    return True
        return False        
    

    def hasWon(self,player):
        if(self.game[0]==player):
            if ((self.game[1]==player and self.game[2]==player) or (self.game[3]==player and self.game[6]==player) or (self.game[4]==player and self.game[8]==player)) :
                return True
        elif(self.game[1]==player):        
            if ((self.game[4]==player and self.game[7]==player)):
                return True
        elif(self.game[2]==player): 
            if ((self.game[4]==player and self.game[6]==player) or (self.game[5]==player and self.game[8]==player)):
                return True
        elif(self.game[3]==player):        
            if ((self.game[4]==player and self.game[5]==player)):
                return True
        elif(self.game[6]==player):        
            if ((self.game[7]==player and self.game[8]==player)):
                return True

        return False



    
        
    def gameOver(self): 
        if(self.hasWon("X") or self.hasWon("O")):
            return True
        else:
            for x in xrange(0,8):
                if(self.game[x]=="*"):
                    return False
                else:
                    return True

    def clear(self):
         for x in xrange(0,8):
                self.game[x]=="*"



print "\nProblem 4: \n"
            
myB = TTTBoard()
print myB

myB.makeMove("X", 8)
myB.makeMove("O", 7)
myB.makeMove("X", 5)
myB.makeMove("O", 6)
myB.makeMove("X", 2)
print myB

print "tic tac toe test case #1: " + str(myB.hasWon("X") == True)
print "tic tac toe test case #2: " + str(myB.hasWon("O") == False)




