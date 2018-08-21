# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 11:43:37 2018

@author: hraanan
"""

import numpy


out_file=open('f:/scope2/groups_scope_name_list.txt','w')
out_file.write('group number\tgroup name\n')
in_file=open('f:/scope2/groups_scope.txt','r')
in_file.readline()
scope_dict={}

for line in in_file:
    line=line.split('\t')
    group = line[0]
    line[1]=line[1][:-1]
    scope_list=line[1].split(';')
    if len(scope_list)==1:
        scope_dict[line[0]]=line[1]
        
        continue
    for t,scope in enumerate(scope_list):
        group = line[0]+'_'+str(t)
        scope_dict[group]=scope 
        



i=1
j=0
for grp,scp in scope_dict.items():
    out_file.write(str(i)+'\t'+grp+'\n')
    i=i+1

#scope_matrix = numpy.zeros(shape=(440,440))
#
#i=1
#j=1
#for grp_1,scope_1 in scope_dict.items():
#    
#    scope_1=scope_1.split('.')
#    for grp_2,scope_2 in scope_dict.items():
##        if j<i:
##            continue
#        #print (grp_1,grp_2)
#        scope_2=scope_2.split('.')
#        dis=0
#        if scope_1[0]==scope_2[0]: dis=1  
#        if scope_1[0]==scope_2[0] and scope_1[1]==scope_2[1]:dis=2
#        if scope_1[0]==scope_2[0] and scope_1[1]==scope_2[1] and scope_1[2]==scope_2[2]:dis=3
#        if scope_1[0]==scope_2[0] and scope_1[1]==scope_2[1] and scope_1[2]==scope_2[2] and scope_1[3]==scope_2[3]:dis=4
#        #out_file.write(grp_1+'\t'+grp_2+'\t'+'.'.join(scope_1)+'\t'+'.'.join(scope_2)+'\t'+str(dis)+'\n')
#        scope_matrix[i][j]=dis
#        j=j+1
#    j=0
#    i=i+1


print('end')

out_file.close()