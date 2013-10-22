import sys
firstSequence = sys.argv[1]
secondSequence = sys.argv[2]
sequence=['']*2
match = 1;
mismatch = -1;
gap = -2;

#A parser for fasta format. Returns the order (first line) followed by the sequence by line.
def parse_fasta(fasta): 
	sequences=''
	sep=''
	with open(fasta) as f:
			next(f)
			for line in f:
				
					sequences += (line.strip())
					sep='\n'
	return sequences
#   x=file(fasta)
#   order = []
#   sequences = {}
#      
#   for line in x:
#     if line.startswith('>'):
#       name = line[1:].rstrip('\n')
#       name = name.replace('_', ' ')
#       order.append(name)
#       sequences[name] = ''
#     else:
#       sequences[name] += line.rstrip('\n').rstrip('*')
#              
#   print "%d sequences found" % len(order)
#   return order, sequences

#possible issue-double blanks returns gap
def match_score(a, b):
    if a == b:
        return match
    elif a == '-' or b == '-':
        return gap
    else:
        return mismatch

def finalize(align1, align2):
    align1 = align1[::-1] #reverse sequence 1
    align2 = align2[::-1]
    i,j = 0,0;
    symbol = ''
    found = 0
    score = 0
    identity = 0
    length=min(len(align1),len(align2))
    for i in range(0,length):
		if align1[i] == align2[i]:
			symbol = symbol + align1[i]
			identity = identity + 1
			score += match_score(align1[i], align2[i])
    
	# if they are not identical and none of them is gap
		elif align1[i] != align2[i] and align1[i] != '-' and align2[i] != '-': 
			score += match_score(align1[i], align2[i])
			symbol += ' '
			found = 0
    
        #if one of them is a gap, output a space
		elif align1[i] == '-' or align2[i] == '-':          
			symbol += ' '
			score += gap_penalty

		identity = float(identity) / len(align1) * 100
    
    print 'Identity =', "%3.3f" % identity, 'percent'
    print 'Score =', score
    print align1
    print symbol
    print align2
	
def generate_matrix(length1,length2):
	return [[0]*length1 for i in xrange(length2)]

def score_matrix(matrix,seq1,seq2):
	
	highestScore=0
	bestLocation=(0,0)
	
	for i in xrange(1,len(seq1)+1):
		for j in xrange(1,len(seq2)+1):
			matrix[i][j] = max(
			#case 1, pointing left
				matrix[i][j-1] + gap,
			#pointing up
				matrix[i-1][j] + gap,
			#diagonal up 
				matrix[i-1][j-1] + match_score(x[i-1], y[j-1])
            )
			if A[i][j] >= best:
				highestScore = matrix[i][j]
                bestLocation = (i,j)
	
	return highestScore,bestLocation
	
	
#def main():
sequence[0]= parse_fasta(firstSequence)
sequence[1]= parse_fasta(secondSequence)
finalize(sequence[0], sequence[1])
