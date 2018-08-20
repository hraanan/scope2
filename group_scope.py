# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 12:42:08 2018

@author: hraanan
"""

from collections import defaultdict

dates_dict = defaultdict(list)
in_file_name="merge_metal_organic_chl_ca_10_md_3_rmsd_5_factor_correct_EC_1.4_1.3_1.15_no_ADE.txt"
in_file=open(in_file_name,"r")
in_file.readline()
#groups_file=open('groups_description_merge_metal_organic_chl_ca_10_md_3_rmsd_5_factor_1-4_1-3_1-15.csv','r')
out_file=open('f:/scope2/groups_scope.txt','w')
#out_file.write(groups_file.readline())

#in_file.readline()
out_file.write('ID\tscope\n')

microen_groups={}

prot=[]
for line in in_file:
    line=line.split('\t')
    microen_groups[line[0]]=line[1]
group_scope_dict={}
scope_file=open('f:/scope2/microenvironments_scope_test.txt','r')
scope_file.readline()
for line in scope_file:
    line=line.split('\t')
    group=microen_groups.get(line[0])
    if group not in group_scope_dict:
        group_scope_dict[group]=[line[1][:-1]]
        continue
    scope=group_scope_dict.get(group)
    scope.append(line[1][:-1])
    group_scope_dict[group]=list(set(scope))

for grp,scope in group_scope_dict.items():
    out_file.write(grp+'\t'+';'.join(scope)+'\n')

out_file.close()
print('end')








#x=0
#y=0

#groups={}
#for line in in_file:
#    ecs=[]
#    line=line.split("\t")
#    groups.setdefault(line[1],[])#.append(line[5])
#    ecs=groups.get(line[1])
#    if line[5] not in ecs:
#        if line[5]=="-":
#            continue
#        ecs.append(line[5])
        
        #groups.setdefault(line[1],[]).append(prot_meta_dict.get(line[5]))
#for key,value in groups.items():
#    groups[key]=list(set(value))              
#    

#for line in in_file:
#    line=line.split("\t")
#    in_prot=line[0][0:4]
#    #in_prot=in_prot[0]
#    groups_list=[]
#    metabolism_file=open(metabolism_file_name,'r')
#    x=x+1    
#    for metline in metabolism_file:
#        metline=metline.split("\t")
#        prot=metline[2].lower()
#              
#        if prot==in_prot:
#            #line='\t'.join(line)
#            y=y+1            
#            
#            out_file.write('\t'.join(line)[:-1]+'\t'+metline[0]+'\n')
#out_file.close()
#
#max_age=0  
#in_file=open('metabolism_'+in_file_name,"r")
#
#groups={}
#in_file.readline()
#for line in in_file:
#    line=line.split("\t")
#    groups.setdefault(line[1],[]).append(line[24][:-1])    

#for key,value in groups.items():
#    groups[key]=list(set(value))        
#for line in groups_file:
#    line=line.split("\t")
#    #print(len(groups.get(line[0])))
#    #print(groups.get(line[0]))
#    ecs_tree=[]
#    ecs_number=0
#    grplen=0
#    try:
#        grplen=(len(groups.get(line[0])))
#    except:
#        groups[line[0]]=""
#    if groups.get(line[0])!="":
#        for ec in groups.get(line[0]):
#           if '-' not in ec:
#               ecs_number=ecs_number+1
#               #ec=ec.split('.')
#               ecs_tree.append(ec)
#               ec=ec[:-2]
#               if ec not in ecs_tree:
#                   ecs_tree.append(ec)
#               ec=ec[:-2]
#               if ec not in ecs_tree:
#                   ecs_tree.append(ec)
#               ec=ec[:-2]
#               if ec not in ecs_tree:
#                   ecs_tree.append(ec)
#               
#        for ec in groups.get(line[0]):  
#           if '-' in ec:
#               ec=ec[:-2]
#           if '-' in ec:
#               ec=ec[:-2]
#           if '-' in ec:
#               ec=ec[:-2]
#           if ec not in ecs_tree:
#              ecs_tree.append(ec)
#              ecs_number=ecs_number+1
#               
##        groups[line[0]]=""
#    out_file.write('\t'.join(line)[:-1]+'\t'+';'.join(groups.get(line[0]))+'\t'+str(grplen)+'\t'+str(ecs_number)+'\n')
#out_file.close()
#print('end')