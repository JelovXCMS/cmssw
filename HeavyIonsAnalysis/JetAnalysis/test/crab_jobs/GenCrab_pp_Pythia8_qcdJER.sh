#!/bin/sh

## generae crab py

INFILELIST=pp_Pythia8MC_qcd.lis
echo $INFILELIST


while read line                                                                                                               
do
INFILENAME=$line


echo "INFILENAME :" $INFILENAME


cat > crab_${INFILENAME}_qcdJER.py <<EOF


from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = '${INFILENAME}_HiForest75X_QCDJER'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../runForestAOD_pp_MC_75X_QCDJER.py'

config.Data.inputDataset = '/${INFILENAME}/HINppWinter16DR-75X_mcRun2_asymptotic_ppAt5TeV_v3-v1/AODSIM'
config.Data.inputDBS ='global'                                                                                                
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/HiForest75X_QCDJER/' % (getUsernameFromSiteDB())
#config.Data.publication = True
config.Data.outputDatasetTag = '${INFILENAME}_HiForest75X_QCDJER'

#config.JobType.inputFiles=['JPcalib_MC75X_ppqcd50.db']
config.JobType.inputFiles=['fout_qcd.root','fout_bjt.root']



config.Site.storageSite = 'T2_US_Purdue'  # or T2_CH_CERN

config.section_("Debug")
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']

EOF

crab submit crab_${INFILENAME}_qcdJER.py

done<$INFILELIST


