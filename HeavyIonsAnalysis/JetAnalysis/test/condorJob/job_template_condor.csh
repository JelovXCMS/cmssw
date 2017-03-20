#!/bin/csh
#
# ---------------------------------------------------------
#

#Name of job
setenv ARG1 $1

#Number of events
setenv ARG2 $2
setenv MAX_EVENTS ${ARG2}

#index of job
setenv ARG3 $3

set SKIP_EVENTS = 0
@ SKIP_EVENTS = ${MAX_EVENTS} * (${ARG3} - 1)


setenv basename ${ARG1}_${ARG3}
setenv fname ${basename}.job
echo Job file will be ${fname}

#create condor job submission file
cat - > condor_${fname} <<EOF
#===============================================================================
#
# condor_submit condor_job
#
#===============================================================================
#universe             = vanilla
universe             = grid
executable           = ${fname}
#arguments            = 60
initialdir           = /home/peng43/work/Project/HiHFJet2017/MC_study/Pythia6/CMSSW_7_5_8_patch3/src
gateway              = hadoop-osg.rcac.purdue.edu
jobmanager           = jobmanager-condor
should_Transfer_Files = NO
#===============================================================================

# Grid
grid_resource        = gt2 \$(gateway)/\$(jobmanager)

#=============================================================================== 
output               = ${basename}.out
error                = ${basename}.err
log                  = ${basename}.log
#===============================================================================
requirements = (Arch == "X86_64")||regexp("cms",Name)
globus_rsl = (condor_submit=(requirements 'regexp(\"cms-*\",Machine)'))
#===============================================================================

+CMSJob = True
#+LENGTH="SHORT"

queue

EOF

#create job executable file
cat - > ${fname} <<EOF
#!/bin/csh -f
set nonomatch

echo ""
echo "----------------------------------------------------"
echo "Job started on `date`"
echo "Job is running on \`uname -a\`"
if ( \${OSTYPE} == "linux" ) then
  set processor = \`sort /proc/cpuinfo | uniq | gawk -F: '(substr(\$1,1,10)=="model name"){print \$2}'\`
  set rate = \`sort /proc/cpuinfo | uniq | gawk -F: '(substr(\$1,1,7)=="cpu MHz"){print substr(\$2,1,6)}'\`
  echo "Processor info : " \$processor \$rate "MHz"
endif
set start = \`date\`
echo "Job started on \`date\`"
echo ""

echo "Job working folder is " $PWD
echo "----------------------------------------------------"

#
#----------------------------------------------------------
# s e t   t h e   r u n t i m e   e n v i r o n m e n t
#----------------------------------------------------------
#
setenv PATH /usr/local/bin:/usr/bin:/bin
setenv CMS_PATH /cvmfs/cms.cern.ch/

setenv CMSSW_RELEASE CMSSW_7_5_8_patch3
setenv SCRAM_ARCH slc6_amd64_gcc491

source \${CMS_PATH}/cmsset_default.csh
setenv SRCDIR   /home/peng43/work/Project/HiHFJet2017/MC_study/Pythia6/CMSSW_7_5_8_patch3/
setenv OUTDIR   /home/peng43/work/Project/HiHFJet2017/MC_study/Pythia6/CMSSW_7_5_8_patch3/src/HeavyIonsAnalysis/JetAnalysis/test/condorJob

echo " "
echo "Output directory is : " \$OUTDIR
echo " "

#
#----------------------------------------------------------
# s e t   t h e   r u n t i m e   e n v i r o n m e n t
#----------------------------------------------------------
#

cd \${SRCDIR}/src/
eval \`scramv1 runtime -csh\` 

#  Print environment available on worker node
echo "----------------------------------------------------"
echo "Environment variables available on WN "
echo "----------------------------------------------------"
env
echo "----------------------------------------------------"


#
#----------------------------------------------------------
# c o p y   e x e   a n d   c o n f i g    f i l e s
#----------------------------------------------------------
#
setenv WORKDIR \`mktemp -d /tmp/foo_XXXXXX\` 
rm -f -r \${WORKDIR}

#Change to workdir
mkdir -p \${WORKDIR}
cd \${WORKDIR}

#
#----------------------------------------------------------
# set CMSSW environment
#----------------------------------------------------------
#

/bin/rm -f job.py

#Create job option file
cat > job.py <<@EOF

import FWCore.ParameterSet.Config as cms
process = cms.Process("Demo")
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.categories.append('Demo')
process.MessageLogger.cerr.INFO = cms.untracked.PSet(
limit = cms.untracked.int32(-1)
)
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

#Number of events to process
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(${MAX_EVENTS}) )

process.source = cms.Source("PoolSource",
# replace 'myfile.root' with the source file you want to use
fileNames = cms.untracked.vstring('file:/mnt/hadoop//store/mc/HC/GenericTTbar/GEN-SIM-RECO/CMSSW_7_0_4_START70_V7-v1/00000/BC370B30-F1CC-E311-BA37-02163E00E79D.root'),

#Number of events to skip
skipEvents=cms.untracked.uint32(${SKIP_EVENTS})
)

process.demo = cms.EDAnalyzer('DemoAnalyzer'
)

process.p = cms.Path(process.demo)


@EOF

echo "----contents of job.py------------------------------"
cat job.py
echo "----------------------------------------------------"

#
#----------------------------------------------------------
# e x e c u t e   j o b
#----------------------------------------------------------
#

 echo "Processing Event Collection : $basename  " 

 /usr/bin/time -f "%e %U %S %x" -o x cmsRun -p job.py
 uptime

 set rtime = \`tail -1 x | cut -f 1 -d " "\`
 set utime = \`tail -1 x | cut -f 2 -d " "\`
 set stime = \`tail -1 x | cut -f 3 -d " "\`
 set stat  = \`tail -1 x | cut -f 4 -d " "\`

#
#----------------------------------------------------------
# c o p y   o u t p u t
#----------------------------------------------------------
#
#  if ( \${status} != 0 ) cp \${WORKDIR}/*.root \${OUTDIR}/${basename}.root
#    cp \${WORKDIR}/*.root \${OUTDIR}/${basename}.root
   
#
# show what is being left behind...
#
  echo ""
  echo "Current directory:"
  pwd
  echo \`ls -lrtAFh\`
#
  set end = \`date\`
  echo ""
  echo "Job end \`date\`"
  echo ""
#
#
rm -r \${WORKDIR}
exit \${status}
EOF

#make it executable
chmod +x ${fname}
