from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.section_('General')
config.General.requestName = 'STARlight_GammaGamma2MuMu_PbPb5TeV_XnXn_woPtCut_Reco_v1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_STARlight_GammaGamma_XnXn_Reco_cfg.py'
config.JobType.numCores = 2
config.JobType.maxMemoryMB = 3000
config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDataset = '/STARlight_GammaGamma2MuMu_PbPb5TeV/shuaiy-STARlight_GammaGamma2MuMu_PbPb5TeV_XnXn_woPtCut_Digi_v1-f5cdccc16b154eb39d7bf491b1016398/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.totalUnits = 100

config.Data.outLFNDirBase = '/store/user/%s/RiceHIN/STARlight/%s' % (getUsernameFromSiteDB(), config.General.requestName)
config.Data.publication = True
#config.Data.publication = False
config.Data.outputDatasetTag = config.General.requestName

config.section_('Site')
config.Data.ignoreLocality = True
config.Site.whitelist = ['T1_US_*','T2_US_*','T2_CH_CERN']
config.Site.storageSite = 'T2_US_MIT'
#config.Site.storageSite = 'T3_US_Rice'
