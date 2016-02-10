'''
p8_MultiplicationTable.py
Dylan House
Python 3.2.5.1
2/8/2016
Display a multiplaction table for 0.1, 0.2, and 0.3
while controlling formatting / spacing.
'''

# establish format
print( "\t0.1\t0.2\t0.3\n")

# 0.1 set
print( "0.1\t%.2f" %(0.1*0.1) + "\t%.2f" %(0.1*0.2) + "\t%.2f" %(0.1*0.3))
# 0.2 set
print( "\n0.2\t%.2f" %(0.2*0.1) + "\t%.2f" %(0.2*0.2) + "\t%.2f" %(0.2*0.3))
# 0.3 set
print( "\n0.3\t%.2f" %(0.3*0.1) + "\t%.2f" %(0.3*0.2) + "\t%.2f" %(0.3*0.3))

'''
>>> ================================ RESTART ================================
>>> 
	0.1	0.2	0.3

0.1	0.01	0.02	0.03

0.2	0.02	0.04	0.06

0.3	0.03	0.06	0.09
>>> 
'''
