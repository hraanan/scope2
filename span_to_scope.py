# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 12:25:43 2018

@author: hraanan
"""


#import find_main_chain_of_microen
from find_main_chain_of_microen import get_main_chain
# create proteins and microenvironments lists

out_file=open('F:\scope2\microenvironments_scope_including_partoverlap.txt','w')
out_file.write('id\tscope\n')
microen_file=open('f:\Dropbox\postdoc\Results\Organic_cofactors\merge_metal_organic_chl_ca_10_md_3_rmsd_5_factor_correct_EC_1.4_1.3_1.15_no_ADE.txt','r')
microen_file.readline()
prot_dict={}
microen_list=[]
start_res=0
end_res=0
t=0
for line in microen_file:
    
    line =line.split('\t')
    prot=line[0].split('.')[0]
    chain=line[0].split('_')[1]
    res=line[0].split('_')[2]
    if prot not in prot_dict:
        prot_dict[prot]=[line[0]]
        continue
    microen_list=prot_dict.get(prot)
    microen_list.append(line[0])

#scope_file=open('F:\scope2\dir.cla.scope.2.07_test.txt','r')
scope_file=open('F:\scope2\dir.cla.scope.2.07.txt','r')
print(scope_file.readline())
print(scope_file.readline())
print(scope_file.readline())
print(scope_file.readline())
microen_chain_list=[]
full_overlap=0
part_overlap=0

for line in scope_file:
    microen_chain_list=[]
    microen_list=[]
    t=t+1
#   optional short test
#    if t==100: break
#   output counter
    
    if t % 1000 == 0:
        print(t)
        print(full_overlap,part_overlap)
    line=line.split('\t')
    #print (line)
    prot=line[1]
    chain=line[2].split(':')[0]
    domain_residues=''
    start_res=0
    end_res=0
    if len(line[2].split(':'))==1:
        domain_residues='all'
    if len(line[2].split(':'))>1:
        domain_residues=line[2].split(':')[1]
        try:
            if domain_residues[0]=='-':
                continue
            start_res=int(domain_residues.split('-')[0])
            end_res=int(domain_residues.split('-')[1])
        except:
            continue
    scope=line[3]
    if prot in prot_dict:
        microen_list=prot_dict.get(prot)
        microen_chain_list=[]
        for microen in microen_list:
            microen=microen.split('_')
            if microen[1]==chain:
                microen_chain_list.append(microen)
    for microen in microen_chain_list:
        main_chain=(get_main_chain('_'.join(microen)))
        #print(microen)
        #print(main_chain)
        '''
        if main_chain[1]=='err':
            print(microen,main_chain)
        
        if len(main_chain)>1:
            print(microen,main_chain)
        '''
        if main_chain[0]==True:
           continue
        if main_chain[1]=='err':
            continue
#        if start_res<0 or end_res<0:
#            continue       
        #try:
        #print(start_res,end_res)
        if main_chain[0]==False:
            if domain_residues=='all':
                full_overlap=full_overlap+1
                out_file.write('_'.join(microen)+'\t'+line[3]+'\n')
    #            print(line)
    #            print('_'.join(microen)+'\t'+line[3]+'\n')
                continue
                
            else:    
                if int(start_res)<=main_chain[2][0] and int(end_res)>=main_chain[2][1]:
                    full_overlap=full_overlap+1
                    out_file.write('_'.join(microen)+'\t'+line[3]+'\n')
    #                print(line)
    #                print('_'.join(microen)+'\t'+line[3]+'\n')
                    continue
                elif int(start_res)>main_chain[2][0] and int(end_res)>main_chain[2][1]:
                    part_overlap=part_overlap+1
                    out_file.write('_'.join(microen)+'\t'+line[3]+'\n')
                elif int(start_res)<main_chain[2][0] and int(end_res)<main_chain[2][1]:
                    part_overlap=part_overlap+1
                    out_file.write('_'.join(microen)+'\t'+line[3]+'\n')
        #if main_chain[0]==True:
        #except:
            
            
print(full_overlap,part_overlap)
out_file.close()