from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()
                                                                                                                              
config.General.requestName = 'crab_test1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../runForestAOD_pp_MC_75X.py'

config.Data.inputDataset = '/Pythia6_Dijet100_pp502/HINppWinter16DR-75X_mcRun2_asymptotic_ppAt5TeV_v3-v1/AODSIM'
config.Data.inputDBS ='global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/crabtest/' % (getUsernameFromSiteDB())
#config.Data.publication = True
config.Data.outputDatasetTag = 'crab_test1'

#config.JobType.inputFiles=['JPcalib_MC75X_ppqcd50.db']

config.Site.storageSite = 'T2_US_Purdue'  # or T2_CH_CERN

config.section_("Debug")
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']


