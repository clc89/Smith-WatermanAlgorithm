import re, cStringIO

#Enumeration for scoring values
class Scores():
    MATCH = 1
    MISMATCH = -1
    GAP_PENALTY = -2 
 
#Enumeration for determining direction when tracing matrix    
class Direction():
    END = 0
    UP = 1
    LEFT = 2 
    DIAGONAL = 3        


def calculateAlignment(seq1, seq2):
    m = len(seq1)
    n = len(seq2)  
    
    #create score table with initial values of zero.
    score = []
    for i in xrange(m+1):
        score.append([])
        for j in xrange(n+1):
            score[-1].append(0)
            
    #create trace table with initial values of zero.        
    tracePointer = []
    for i in xrange(m+1):
        tracePointer.append([])
        for j in xrange(n+1):
            tracePointer[-1].append(0)
            
    max_score = 0
    # fill score matrix and trace matrix
    for i in xrange(1, m + 1):
        for j in xrange(1, n + 1):
            
            select = 0;
            if (seq1[i-1] == seq2[j-1]):
                select = Scores.MATCH 
            elif(seq1[i-1] == '-' or seq2[j-1] == '-'):
                select = Scores.GAP_PENALTY
            else:
                select = Scores.MISMATCH 
                              
            diag = score[i-1][j-1] + select
            score_up = score[i][j-1] + Scores.GAP_PENALTY
            score_left = score[i-1][j] + Scores.GAP_PENALTY
            score[i][j] = max(0, score_left, score_up, diag)
            if score[i][j] == 0:
                tracePointer[i][j] = Direction.END
            if score[i][j] == score_up:
                tracePointer[i][j] = Direction.UP                
            if score[i][j] == score_left:
                tracePointer[i][j] = Direction.LEFT
            if score[i][j] == diag:
                tracePointer[i][j] = Direction.DIAGONAL 
            if score[i][j] >= max_score:
                max_i = i
                max_j = j
                max_score = score[i][j];
    
    #aligned sequences
    seqA, seqB = '', '' 
    
    
    # perform trace through matrix
    i,j = max_i,max_j    
    #loop until it reaches the end.
    while tracePointer[i][j] != Direction.END:
        #diagonal move
        if tracePointer[i][j] == Direction.DIAGONAL:
            seqA += seq1[i-1]
            seqB += seq2[j-1]
            i -= 1
            j -= 1
        #move left
        elif tracePointer[i][j] == Direction.LEFT:
            seqA += '-'
            seqB += seq2[j-1]
            j -= 1
        #move up
        elif tracePointer[i][j] == Direction.UP:
            seqA += seq1[i-1]
            seqB += '-'
            i -= 1

    # Because the sequence were traversed backwards they must
    # be reversed.
    seqA = seqA[::-1]
    seqB = seqB[::-1]    
    
    i,j = 0,0
    
    score = 0
    fancyLineString = '' #the fancy lines used in the output to show matches.
    
    # Loop through sequences and set the appropriate 
    # line for each match.
    for i in xrange(0,len(seqA)):
        if seqA[i] == seqB[i]:                
            fancyLineString = fancyLineString + "|"
            s2 = 0;
            if (seqA[i] == seqB[i]):
                s2 = Scores.MATCH 
            elif(seqA[i] == '-' or seqB[i] == '-'):
                s2 = Scores.GAP_PENALTY
            else:
                s2 = Scores.MISMATCH 
            score += s2
    
        elif seqA[i] != seqB[i] and seqA[i] != '-' and seqB[i] != '-': 
            if (seqA[i] == seqB[i]):
                s2 = Scores.MATCH 
            elif(seqA[i] == '-' or seqB[i] == '-'):
                s2 = Scores.GAP_PENALTY
            else:
                s2 = Scores.MISMATCH 
            score += s2
            fancyLineString += ' '
    
        elif seqA[i] == '-' or seqB[i] == '-':          
            fancyLineString += ' '
            score += Scores.GAP_PENALTY
    
    

    #add newlines so that sequences can be properly displayed
    seqA = re.sub("(.{60})", "\\1\n", seqA, 0, re.DOTALL)   
    seqB = re.sub("(.{60})", "\\1\n", seqB, 0, re.DOTALL)
    fancyLineString = re.sub("(.{60})", "\\1\n", fancyLineString, 0, re.DOTALL)
    seqAArray = seqA.split('\n')
    seqBArray = seqB.split('\n')
    fancyLineArray = fancyLineString.split('\n')
    text_file = open("results", "w")

    #display formated sequences and output results to file.
    for i in xrange(0, len(seqAArray)):
        print seqAArray[i]
        text_file.write(seqAArray[i])
        text_file.write('\n')
        print fancyLineArray[i]
        text_file.write(fancyLineArray[i]) 
        text_file.write('\n')   
        print seqBArray[i]
        text_file.write(seqBArray[i])
        text_file.write('\n')
        print '\n'
        text_file.write('\n')
        
    #show score
    print 'Score =', max_score
    text_file.write("Score: {0}".format(max_score))
    text_file.close()
    