import numpy as np
import os
import sys
from rings_gen_options_msd import genoptions_msd
from rings_gen_options import genoptions
from rings_setup_MgO import MgO
from rings_setup_SiO import SiO
from pathlib import Path
#
truncate=5000#HOW MANY ITERATIONS TO TRUNCATE FROM TRAJECTORY
print(' Go rings');sys.stdout.flush()
data=np.loadtxt("input.txt", dtype=np.str)
for i in range(data.shape[0]):
        task=data[i]
        task1=data[i]
        task2=data[i]+"_ext"
        CWD=os.getcwd()
        catcmd='cat '+task1+"/movie.xyz "+task2+"/movie.xyz > "+task2+"/cat_movie.xyz"
        os.system(catcmd)
        contpath=Path(CWD+"/"+task2)
        filedir=Path(CWD+"/"+task2+"/rings")
        datadir=Path(CWD+"/"+task2+"/rings/data")
        olddatafile=Path(CWD+"/"+task2+"/out.xyz")
        newdatafile=Path(CWD+"/"+task2+"/rings/data/out.xyz")
        os.chdir(contpath)#move into task directory
        #Read xyz file
        print(" reading file movie.xyz  ....");sys.stdout.flush()
        #
        f = open('cat_movie.xyz','r')
        data_list = f.readlines()
        f.close()#close input xyz file
        #get number of atoms
        s1 = data_list[0]
        natoms = int(s1)
        if truncate > 0:
                #determine number of iterations
                numiter = len(data_list)
                numiter = int(numiter)
                niter = int(numiter / (natoms+2))
                #determine how many lines to truncate
                trunc = int(truncate*(natoms+2))
                trunciter = int(trunc / (natoms+2))
                print('\n there are',natoms,'atoms and',niter,'iterations\n truncating the first'\
                    ,trunciter,'iterations (',trunc,'lines from total',numiter,')...');sys.stdout.flush()
                del data_list[0:trunc]
                #write new output
                print(' writing file out.xyz ...');sys.stdout.flush()
                fout = open('out.xyz','w')
                fout.writelines(data_list)
                fout.close()         
        else:
                os.system('cp movie.xyz out.xyz')
        # Create target directory & all intermediate directories if don't exist
        if not os.path.exists(datadir):
            os.makedirs(datadir)
            print("Creating Directory " , datadir);sys.stdout.flush()
        else:    
            print("Creating Directory " , datadir ,  " ... already exists");sys.stdout.flush()
        # move trajectory file
        if  os.path.exists(newdatafile):
            os.remove(newdatafile)
            os.rename(olddatafile,newdatafile)
        else:    
            os.rename(olddatafile,newdatafile)
        
        os.chdir(filedir)#move into directory to run rings
        ##############################################
        ### CALCULATE SIO COORDINATION ENVIORNMENT ###
        ##############################################
        genoptions_msd()
        SiO('input-CN-SiO',contpath,natoms)
        oldbondfile=Path(CWD+"/"+task2+"/rings/bonds/bond-prop.dat")
        newbondfile=Path(CWD+"/"+task2+"/rings/bonds/bond-prop-SiO.dat") #RENAME BOND PROP FILE
        if  os.path.exists(newbondfile):
            os.remove(newbondfile)
            os.rename(oldbondfile,newbondfile)
        else:    
            os.rename(oldbondfile,newbondfile)
        ##############################################
        ### CALCULATE MgO COORDINATION ENVIRONMENT ###
        ##############################################
        genoptions()#Generate new options file:calculation of partials and MSD already done
        MgO('input-CN-MgO',contpath,natoms)
        newbondfile=Path(CWD+"/"+task2+"/rings/bonds/bond-prop-MgO.dat") #RENAME BOND PROP FILE
        if  os.path.exists(newbondfile):
            os.remove(newbondfile)
            os.rename(oldbondfile,newbondfile)
        else:    
            os.rename(oldbondfile,newbondfile)                 
        os.chdir(CWD)#move back to original directory  
