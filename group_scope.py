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
out_file=open('f:/scope2/groups_with_scope.txt','w')
#out_file.write(groups_file.readline())

#in_file.readline()


microen_groups={}

prot=[]
for line in in_file:
    line=line.split('\t')
    microen_groups[line[0]]=line[1]
group_scope_dict={}
scope_file=open('f:/scope2/microenvironments_scope.txt','r')
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
group_file=open('F:\Dropbox\postdoc\Results\Organic_cofactors\groups_description_merge_metal_organic_chl_ca_10_md_3_rmsd_5_factor_1-4_1-3_1-15_with_ECs.csv','r')
titel=str(group_file.readline())[:-1]
out_file.write(titel+'\t'+'scope\n')
for line in group_file:
    group=line.split('\t')[0]
    scope=group_scope_dict.get(group)
    
    try:
        
        if len(scope)>1:
            #print(len(scope))
            line=line.split('\t')
            
            i=0
            for i,scp in enumerate(scope):
                print(i)
                line[0]=group+'_'+str(i)
                out_file.write('\t'.join(line)[:-1]+'\t'+scp+'\n')
        else:
            out_file.write(line[:-1]+'\t'+scp+'\n')
    except TypeError:
        continue
#for grp,scope in group_scope_dict.items():
#    out_file.write(grp+'\t'+';'.join(scope)+'\n')

out_file.close()
print('end')


