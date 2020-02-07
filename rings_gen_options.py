def genoptions():
    filename = "options"
    inp="######################################\n"
    inp=inp+"    R.I.N.G.S. options file          #\n"
    inp=inp+"######################################\n"
    inp=inp+"PBC             .true.               #\n"
    inp=inp+"Frac            .false.              #\n"
    inp=inp+"g(r)            .false.               #\n"
    inp=inp+"S(q)            .false.               #\n"
    inp=inp+"S(k)            .false.              #\n"
    inp=inp+"gfft(r)         .false.              #\n"
    inp=inp+"MSD             .false.               #\n"
    inp=inp+"atMSD           .false.              #\n"
    inp=inp+"Bonds           .true.               #\n"
    inp=inp+"Angles          .true.               #\n"
    inp=inp+"Chains          .false.              #\n"
    inp=inp+"----- ! Chain statistics options ! -----\n"
    inp=inp+"Species           0                  #\n"
    inp=inp+"AAAA            .false.              #\n"
    inp=inp+"ABAB            .false.              #\n"
    inp=inp+"1221            .false.              #\n"
    inp=inp+"---------------------------------------\n"
    inp=inp+"Rings           .false.               #\n"
    inp=inp+"----- ! Ring statistics options ! -----\n"
    inp=inp+"Species           0                  #\n"
    inp=inp+"ABAB            .false.              #\n"
    inp=inp+"Rings0          .false.              #\n"
    inp=inp+"Rings1          .false.              #\n"
    inp=inp+"Rings2          .false.              #\n"
    inp=inp+"Rings3          .false.              #\n"
    inp=inp+"Rings4          .false.              #\n"
    inp=inp+"Prim_Rings      .false.              #\n"
    inp=inp+"Str_Rings       .false.              #\n"
    inp=inp+"BarycRings      .false.              #\n"
    inp=inp+"Prop-1          .false.              #\n"
    inp=inp+"Prop-2          .false.              #\n"
    inp=inp+"Prop-3          .false.              #\n"
    inp=inp+"Prop-4          .false.              #\n"
    inp=inp+"Prop-5          .false.              #\n"
    inp=inp+"---------------------------------------\n"
    inp=inp+"Vacuum          .false.              #\n"
    inp=inp+"######################################\n"
    inp=inp+"        Outputting options           #\n"
    inp=inp+"######################################\n"
    inp=inp+"Evol            .false.              #\n"
    inp=inp+"Dxout           .false.              #\n"
    inp=inp+"-- ! OpenDX visualization options !  --\n"
    inp=inp+"RadOut          .false.              #\n"
    inp=inp+"RingsOut        .false.              #\n"
    inp=inp+"DRngOut         .false.              #\n"
    inp=inp+"VoidsOut        .false.              #\n"
    inp=inp+"TetraOut        .false.              #\n"
    inp=inp+"TrajOut         .false.              #\n"
    inp=inp+"---------------------------------------\n" 
    inp=inp+"Output        my-output.out          #\n"
    inp=inp+"######################################" 
    file=open(filename, 'w')
    file.write(inp)
    file.close()
