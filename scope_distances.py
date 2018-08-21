# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 11:43:37 2018

@author: hraanan
"""

#import community
#import networkx as nx
#
#G=nx.Graph()

out_file=open('f:/scope2/groups_scope_ditances_matrix.txt','w')
out_file.write('source\ttarget\tdistance\n')
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
    for i,scope in enumerate(scope_list):
        group = line[0]+'_'+str(i)
        scope_dict[group]=scope 
i=0
j=0

for grp_1,scope_1 in scope_dict.items():
    scope_1=scope_1.split('.')
    for grp_2,scope_2 in scope_dict.items():
        if j<i:
            continue
        
        scope_2=scope_2.split('.')
        dis=0
        if scope_1[0]==scope_2[0]: dis=1  
        if scope_1[0]==scope_2[0] and scope_1[1]==scope_2[1]:dis=2
        if scope_1[0]==scope_2[0] and scope_1[1]==scope_2[1] and scope_1[2]==scope_2[2]:dis=3
        if scope_1[0]==scope_2[0] and scope_1[1]==scope_2[1] and scope_1[2]==scope_2[2] and scope_1[3]==scope_2[3]:dis=4
        out_file.write(grp_1+'\t'+grp_2+'\t'+'.'.join(scope_1)+'\t'+'.'.join(scope_2)+'\t'+str(dis)+'\n')
        j=j+1
    i=i+1


print('end')

out_file.close()