def SiO(filename,contpath,natoms):
    import os
    from pathlib import Path
    import sys
    print(' Reading CONTCAR...');sys.stdout.flush()
    cont = Path(str(contpath)+"/CONTCAR")
    f = open(cont)
    lines=f.readlines()
    f.close()
    boxlen, *rest = lines[2].rstrip().split('0.0')
    length=round(float(boxlen),9)
    print (' Box length =',length,'Angstrom');sys.stdout.flush()
    inp="#####################################\n"
    inp=inp+"#       R.I.N.G.S. input file       #\n"
    inp=inp+"#####################################\n"
    inp=inp+"MSH                                 #\n"
    inp=inp+str(natoms)+"                                 #\n"
    inp=inp+"3                                   #\n"
    inp=inp+"Mg  O  Si                        #\n"
    inp=inp+"40000                               #\n"
    inp=inp+"1                                   #\n"
    inp=inp+str(length)+" 0 0                    #\n"
    inp=inp+"0 "+str(length)+" 0                    #\n"
    inp=inp+"0 0 "+str(length)+"                    #\n"
    inp=inp+"1                                   #\n"
    inp=inp+"ANI                                 #\n"
    inp=inp+"out.xyz                             #\n"
    inp=inp+"300                                 #\n"
    inp=inp+"1000                                #\n"
    inp=inp+"25                                  #\n"
    inp=inp+"0.125                               #\n"
    inp=inp+"90                                  #\n"
    inp=inp+"20                                  #\n"
    inp=inp+"10                                  #\n"
    inp=inp+"15                                  #\n"
    inp=inp+"#####################################\n"
    inp=inp+"Mg Mg   0.1                         #\n"
    inp=inp+"Mg Si   0.1                         #\n"
    inp=inp+"Mg O    0.1                         #\n"
    inp=inp+"Si Si   0.1                         #\n"
    inp=inp+"Si O    2.22                        #\n"
    inp=inp+"O O     0.1                         #\n"
    inp=inp+"Grtot   2.22                        #\n"
    inp=inp+"#####################################"
    file=open(filename,'w')
    file.write(inp)
    file.close()
    print("\n Running R.I.N.G.S. \n");sys.stdout.flush()
    cmd = 'rings '+str(filename)
    os.system(cmd)
