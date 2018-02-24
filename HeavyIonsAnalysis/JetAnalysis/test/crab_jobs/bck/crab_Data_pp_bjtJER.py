from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'Data_pp5TeV_HiForest75X_BjtJER'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../runForestAOD_pp_DATA_75X_BjtJER.py'

config.Data.inputDataset = '/HighPtJet80/Run2015E-PromptReco-v1/RECO'
config.Data.inputDBS ='global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 3
config.Data.outLFNDirBase = '/store/user/%s/HiForest75X_BjtJER/' % (getUsernameFromSiteDB())
#config.Data.publication = True
config.Data.outputDatasetTag = 'Data_pp5TeV_HiForest75X_BjtJER'

#config.JobType.inputFiles=['JPcalib_MC75X_ppqcd50.db']
config.JobType.inputFiles=['fout_qcd.root','fout_bjt.root']



config.Site.storageSite = 'T2_US_Purdue'  # or T2_CH_CERN

config.section_("Debug")
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']

