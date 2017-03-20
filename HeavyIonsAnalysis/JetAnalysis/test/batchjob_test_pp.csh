#!/bin/csh
# Lxplus Batch Job Script
#set CMSSW_PROJECT_SRC="cmssw_projects/13X/cmssw131hlt6/src"
set CFG_FILE="test_runForestAOD_pp_MC_Pythia6_75X.py"
set OUTPUT_FILE="Test_HiForestAOD_pp_MC_PYTHIA6_bjet30.root"
set TOP="$PWD"

cd /home/peng43/work/Project/HiHFJet2017/MC_study/Pythia6/CMSSW_7_5_8_patch3/src
eval `scramv1 runtime -csh`
cd $TOP
cmsRun $CFG_FILE
#rfcp Analyzer_Output.root /castor/cern.ch/user/s/ssimon/$OUTPUT_FILE
rfcp Test_HiForestAOD_pp_MC_PYTHIA6_bjet30.root /home/peng43/work/Project/HiHFJet2017/MC_study/Pythia6/CMSSW_7_5_8_patch3/src/HeavyIonsAnalysis/JetAnalysis/test/$OUTPUT_FILE

