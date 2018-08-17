

from Bio import PDB
import math
import numpy
from Bio.PDB import *

######initial variabels############# 
rootdir ='f:/microfolds_8_2018/all/' # folder of the pdb original filesdownladed form the pdb
 
AA=['PHE','TRP','TYR','ALA','CYS','ASP','GLU','GLY','HIS','ILE','LYS','LEU','MET','ASN','PRO','GLN','ARG','SER','THR','VAL']
chl=['BCB','CLA','CHL','BCL','CL0','PMR','PHO'] #chlorophyll cofactors list
heme=['HEA','HAS','2FH','522','89R','DDH','DHE','HES','HDD','HDE','HDM','HEB','HEC','HEM','HEO','HEV','HP5','MH0','N7H','NTE','OBV','SRM','VER']
pyr_atom_list=['C3A','C3B','C3C','C3D']

#####################
organic_cofactors_list=[]
cofactors_dict={}
organic_cofactors_pdb_file=open('manual_cofactor_list_with_quinone.txt','r')
for line in organic_cofactors_pdb_file:
    line=line.split('\t')
    organic_cofactors_list.append(line[1])
    if line[1] not in cofactors_dict:
        if len(line[4])>1:
            cofactors_dict[line[1]]=[line[3],line[4][:-1]]
        else:
            cofactors_dict[line[1]]=[line[3]]

pdbl=PDB.PDBList()



def get_center(residue,al): # get the geometric centar of list of atom coordinatins 
    coord = []
    for atom in residue:
        
        if atom.name in al or al==['all']:
        #   print(atom.coord)
           at=atom.coord
           x=at[0]
           y=at[1]
           z=at[2]
           atcord=[x,y,z]
           coord.append(atcord)
    x=0
    y=0
    z=0
    i=0
    for point in coord:
        i=i+1
        x=x+point[0]
        y=y+point[1]
        z=z+point[2]
    x=x/i
    y=y/i
    z=z/i
    center=numpy.array([x,y,z])    
    return center;



def get_main_chain(microen):
    
    neighbors_res_range=[0,0]
    neighbors_chain_list=[]
    neighbors_list=[]
    multi=False        
    try:
        protein=microen[0:4]
        microen='_'.join(microen.split('_')[:-2])
        cof=microen.split('_')[0].split('.')[1]
        parser = PDB.PDBParser(PERMISSIVE=1,get_header=1,QUIET=1)
        structure = parser.get_structure(protein,rootdir+cof+'/'+microen+'.pdb')
        model = structure[0]
        chain = model[microen.split('_')[1]]
        for residue in chain:
            if residue.id[1]==int(microen.split('_')[2]) and residue.get_resname()==cof:
                atom_list = Selection.unfold_entities(model, 'A') # A for atoms
                ns = NeighborSearch(atom_list)
                lig=[]
                if residue.resname in cofactors_dict:
                     al=cofactors_dict[residue.resname][0]
                     al=al.split(';')
                    
                
                elif residue.resname in chl or residue.resname in heme:
                    al=pyr_atom_list
                    
                else:
                    al=['all'] 
                center = get_center(residue,al)
                all_neighbors = ns.search(center, 5.0,"R") # 15.0 for distance in angstrom
                neighbors_chain_list=[]
                neighbors_res_list=[]
                i=0
                for res in all_neighbors:
                    
                    if res.id[1]!=int(microen.split('_')[2]): 
                        i=i+1
                        if res.get_parent().id not in neighbors_chain_list:
                            neighbors_chain_list.append(res.get_parent().id)
                if i==0:
                    neighbors_chain_list='err'
                    continue
                start_res=10000000
                end_res=0
                neighbors_res_range=[0,0]
                multi=False
                if len(neighbors_chain_list)>1:
                    multi=True             
                else:
                    for res in all_neighbors:
                        if res.resname in AA:
                            #print(res)
                            if res.id[1]<start_res:
                                start_res=res.id[1]
                            if res.id[1]>end_res:
                                end_res=res.id[1]
                    neighbors_res_range=[start_res,end_res]
    except:
        neighbors_chain_list='err'
   
    return [multi,neighbors_chain_list,neighbors_res_range]
                                                 
                    
#print(get_main_chain('11gs.GSH_B_210_transferase_2.5.1.18'))