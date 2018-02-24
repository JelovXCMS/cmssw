from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'Data_pp5TeV_HiForest75X_BjtJESup_json_t2'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../runForestAOD_pp_DATA_75X_BjtJESup.py'

config.Data.inputDataset = '/HighPtJet80/Run2015E-PromptReco-v1/RECO'
config.Data.inputDBS ='global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/HiForest75X_BjtJESup/' % (getUsernameFromSiteDB())
#config.Data.publication = True
config.Data.outputDatasetTag = 'Data_pp5TeV_HiForest75X_BjtJESup_json_t2'

config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/5TeV/Cert_262081-262328_5TeV_PromptReco_Collisions15_25ns_JSON.txt'


#config.JobType.inputFiles=['JPcalib_MC75X_ppqcd50.db']
config.JobType.inputFiles=['fout_qcd.root','fout_bjt.root']



config.Site.storageSite = 'T2_US_Purdue'  # or T2_CH_CERN

config.section_("Debug")
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']

