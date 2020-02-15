from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.section_('General')
config.General.requestName = 'STARlight_GammaGamma2MuMu_PbPb5TeV_XnXn_woPtCut_GenSim_v1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.section_('JobType')
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'step1_STARlight_GammaGamma_XnXn_GenSim_cfg.py'
config.JobType.numCores = 2
config.JobType.maxMemoryMB = 2000
config.JobType.eventsPerLumi = 10000000
config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.outputPrimaryDataset = 'STARlight_GammaGamma2MuMu_PbPb5TeV'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10000
NJOBS = 300
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.outLFNDirBase = '/store/user/%s/RiceHIN/STARlight/%s' % (getUsernameFromSiteDB(), config.General.requestName)
config.Data.publication = True
#config.Data.publication = False
config.Data.outputDatasetTag = config.General.requestName

config.section_('Site')
config.Data.ignoreLocality = True
config.Site.whitelist = ['T1_US_*','T2_US_*','T2_CH_CERN']
config.Site.storageSite = 'T2_US_MIT'
#config.Site.storageSite = 'T3_US_Rice'
