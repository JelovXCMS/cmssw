### HiForest Configuration
# Collisions: pp
# Type: MC
# Input: AOD

import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')
process.options = cms.untracked.PSet(

#	SkipEvent = cms.untracked.vstring('ProductNotFound') # see the following reason to add this. 
)

## add for avoid Fatal Exception by : ProductNotFound
##   [0] Processing run: 1 lumi: 1751 event: 1798308
##	    [1] Running path 'ana_step'
##			   [2] Calling event method for module Tupel/'tupel'
##				 Exception Message:
##				 Principal::getByLabel: Found zero products matching all criteria
##				 Looking for a container with elements of type: pat::Jet
##				 Looking for module label: ak4PFpatJetsWithBtagging
##				 Looking for productInstanceName:
##     [a] If you wish to continue processing events after a ProductNotFound exception,
##		 add "SkipEvent = cms.untracked.vstring('ProductNotFound')" to the "options" PSet in the configuration.

process.Timing = cms.Service("Timing",
      summaryOnly = cms.untracked.bool(True)
			)
			


#####################################################################################
# HiForest labelling info
#####################################################################################

process.load("HeavyIonsAnalysis.JetAnalysis.HiForest_cff")
process.HiForest.inputLines = cms.vstring("HiForest V3",)
import subprocess
version = subprocess.Popen(["(cd $CMSSW_BASE/src && git describe --tags)"], stdout=subprocess.PIPE, shell=True).stdout.read()
if version == '':
    version = 'no git info'
process.HiForest.HiForestVersion = cms.string(version)

#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                            fileNames = cms.untracked.vstring(
#                                "file:test_sample/pp_MC_PYTHIA6_bjet30.root"
#																"file:test_sample/pp_MC_PYTHIA6_bjet120.root"

 "root://cms-xrd-global.cern.ch//store/himc/HINppWinter16DR/Pythia6_bJet120_pp502/AODSIM/75X_mcRun2_asymptotic_ppAt5TeV_v3-v1/00000/5270484A-9D07-E611-B734-34E6D7BDDEE8.root" #bjet_pthat120_pp 1st, n23711
,
"root://cms-xrd-global.cern.ch///store/himc/HINppWinter16DR/Pythia6_bJet120_pp502/AODSIM/75X_mcRun2_asymptotic_ppAt5TeV_v3-v1/30000/2EF3FB1C-1F0F-E611-B00B-0025905D1D60.root" #bjet_pthat120_pp 3st, n42125

#" root://xrootd-cms.infn.it//store/himc/HINppWinter16DR/Pythia6_bJet120_pp502/AODSIM/75X_mcRun2_asymptotic_ppAt5TeV_v3-v1/00000/5270484A-9D07-E611-B734-34E6D7BDDEE8.root" #bjet_pthat120_pp


#"root://cms-xrd-global.cern.ch//store/himc/HINppWinter16DR/Pythia6_Dijet120_pp502/AODSIM/75X_mcRun2_asymptotic_ppAt5TeV_v3-v1/30000/16CDD81D-660F-E611-A0D4-0090FAA573F0.root" #dijet_pthat120_pp
                            )
)

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
#    input = cms.untracked.int32(1000))
    input = cms.untracked.int32(-1))


#####################################################################################
# Load Global Tag, Geometry, etc.
#####################################################################################

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_mcRun2_asymptotic_ppAt5TeV_v3', '')
process.HiForest.GlobalTagLabel = process.GlobalTag.globaltag


# Customization
from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import overrideJEC_pp5020
process = overrideJEC_pp5020(process)

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string(
#																	 "Test.root"
#                                  "Test_HiForestAOD_pp_MC_PYTHIA6_bjet120_n1000.root"
																	 "Test_HiForestAOD_pp_MC_PYTHIA6_bjet120_n65000.root"
#																	 "Test_HiForestAOD_pp_MC_PYTHIA6_Dijet120.root"
																	 ))

#####################################################################################
# Additional Reconstruction and Analysis: Main Body
#####################################################################################

####################################################################################

#############################
# Jets
#############################

process.load("HeavyIonsAnalysis.JetAnalysis.FullJetSequence_nominalPP")
#process.ak3PFJetAnalyzer.isPythia6 = cms.untracked.bool(True)
process.ak4PFJetAnalyzer.isPythia6 = cms.untracked.bool(True)
process.ak5PFJetAnalyzer.isPythia6 = cms.untracked.bool(False)
process.ak4CaloJetAnalyzer.isPythia6 = cms.untracked.bool(False)
process.akSoftDrop4PFJetAnalyzer.isPythia6 = cms.untracked.bool(True)
#process.akSoftDrop4PFJetAnalyzer.doJetConstituents = cms.untracked.bool(True)
#process.akSoftDrop4PFJetAnalyzer.doNewJetVars = cms.untracked.bool(True)
process.akSoftDrop5PFJetAnalyzer.isPythia6 = cms.untracked.bool(False)


process.ak4PFJetAnalyzer.doGhostFlavorMatch = cms.untracked.bool(True)
process.akSoftDrop4PFJetAnalyzer.doGhostFlavorMatch = cms.untracked.bool(True)
#process.akSoftDrop4PFJetAnalyzer.doGhostSubJetFlavor = cms.untracked.bool(True)



process.akSoftDrop4PFPatJetFlavourAssociation.jets="ak4PFJets"
process.akSoftDrop4PFPatJetFlavourAssociation.groomedJets=cms.InputTag("akSoftDrop4PFJets")
process.akSoftDrop4PFPatJetFlavourAssociation.subjets= cms.InputTag('akSoftDrop4PFJets','SubJets')
process.akSoftDrop4PFJets.useSoftDrop = True
process.akSoftDrop4PFpatJetsWithBtagging.getJetMCFlavour = cms.bool(False)

process.akSoftDrop4PFJetAnalyzer.jetFlavourInfos=cms.InputTag("akSoftDrop4PFPatJetFlavourAssociation")
process.akSoftDrop4PFJetAnalyzer.subjetFlavourInfos = cms.InputTag("akSoftDrop4PFPatJetFlavourAssociation","SubJets")
process.akSoftDrop4PFJetAnalyzer.groomedJets        = cms.InputTag("akSoftDrop4PFJets")


# for ak4PFJets
process.ak4PFPatJetFlavourAssociation.jets="ak4PFJets"
#process.ak4PFPatJetFlavourAssociation.groomedJets=cms.InputTag("akSoftDrop4PFJets")
#process.ak4PFPatJetFlavourAssociation.subjets= cms.InputTag('akSoftDrop4PFJets','SubJets')
#process.ak4PFJets.useSoftDrop = False
process.ak4PFpatJetsWithBtagging.getJetMCFlavour = cms.bool(False)

process.ak4PFJetAnalyzer.jetFlavourInfos=cms.InputTag("ak4PFPatJetFlavourAssociation")
#process.ak4PFJetAnalyzer.subjetFlavourInfos = cms.InputTag("akSoftDrop4PFPatJetFlavourAssociation","SubJets")
#process.ak4PFJetAnalyzer.groomedJets        = cms.InputTag("akSoftDrop4PFJets")




#                                                     subjetFlavourInfos = cms.InputTag("akSoftDrop4PFPatJetFlavourAssociation","SubJets"),
#                                                     groomedJets        = cms.InputTag("akSoftDrop4PFJets"),




# Include this to turn on storing the jet constituents and new jet variables for q/g separation
#process.ak4PFJetAnalyzer.doJetConstituents = cms.untracked.bool(True)
#process.ak4PFJetAnalyzer.doNewJetVars = cms.untracked.bool(True)
# Use this version for JEC
#process.load("HeavyIonsAnalysis.JetAnalysis.FullJetSequence_JECPP")

#####################################################################################

############################
# Event Analysis
############################
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi') #use data version to avoid PbPb MC
process.hiEvtAnalyzer.Vertex = cms.InputTag("offlinePrimaryVertices")
process.hiEvtAnalyzer.doCentrality = cms.bool(False)
process.hiEvtAnalyzer.doEvtPlane = cms.bool(False)
process.hiEvtAnalyzer.doMC = cms.bool(True) #general MC info
process.hiEvtAnalyzer.doHiMC = cms.bool(False) #HI specific MC info

process.load('HeavyIonsAnalysis.JetAnalysis.HiGenAnalyzer_cfi')
process.HiGenParticleAna.genParticleSrc = cms.untracked.InputTag("genParticles")
process.HiGenParticleAna.doHI = False
process.load('HeavyIonsAnalysis.EventAnalysis.runanalyzer_cff')
process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzer_pp_cfi")
process.pfcandAnalyzer.skipCharged = False
process.pfcandAnalyzer.pfPtMin = 0
process.pfcandAnalyzer.pfCandidateLabel = cms.InputTag("particleFlow")
process.pfcandAnalyzer.doVS = cms.untracked.bool(False)
process.pfcandAnalyzer.doUEraw_ = cms.untracked.bool(False)
process.pfcandAnalyzer.genLabel = cms.InputTag("genParticles")

#####################################################################################

#########################
# Track Analyzer
#########################
process.load('HeavyIonsAnalysis.JetAnalysis.ExtraTrackReco_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_cff')

# Use this instead for track corrections
## process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_Corr_cff')

#####################################################################################

#####################
# photons
######################
process.load('HeavyIonsAnalysis.PhotonAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.gsfElectronLabel   = cms.InputTag("gedGsfElectrons")
process.ggHiNtuplizer.recoPhotonHiIsolationMap = cms.InputTag('photonIsolationHIProducerpp')
process.ggHiNtuplizer.VtxLabel           = cms.InputTag("offlinePrimaryVertices")
process.ggHiNtuplizer.particleFlowCollection = cms.InputTag("particleFlow")
process.ggHiNtuplizer.doVsIso            = cms.bool(False)
process.ggHiNtuplizer.doElectronVID      = cms.bool(True)
process.ggHiNtuplizerGED = process.ggHiNtuplizer.clone(recoPhotonSrc = cms.InputTag('gedPhotons'),
                                                       recoPhotonHiIsolationMap = cms.InputTag('photonIsolationHIProducerppGED'))

####################################################################################
#####################
# Electron ID
#####################

from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
# turn on VID producer, indicate data format to be processed
# DataFormat.AOD or DataFormat.MiniAOD
dataFormat = DataFormat.AOD
switchOnVIDElectronIdProducer(process, dataFormat)

# define which IDs we want to produce. Check here https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2#Recipe_for_regular_users_for_7_4
my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Spring15_25ns_V1_cff']

#add them to the VID producer
for idmod in my_id_modules:
    setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)
####################################################################################


#####################
# tupel and necessary PAT sequences
#####################

process.load("HeavyIonsAnalysis.VectorBosonAnalysis.tupelSequence_pp_mc_cff")

#####################################################################################

#########################
# Main analysis list
#########################
process.ana_step = cms.Path(process.hltanalysis *
                            process.hiEvtAnalyzer *
                            process.HiGenParticleAna*
                            process.jetSequences +
                            process.egmGsfElectronIDSequence + #Should be added in the path for VID module
                            process.ggHiNtuplizer +
                            process.ggHiNtuplizerGED +
                            process.pfcandAnalyzer +
                            process.HiForest +
			    process.trackSequencesPP +
                            process.runAnalyzer +
                            process.tupelPatSequence
)

#####################################################################################

#########################
# Event Selection
#########################

process.load('HeavyIonsAnalysis.JetAnalysis.EventSelection_cff')
process.pHBHENoiseFilterResultProducer = cms.Path( process.HBHENoiseFilterResultProducer )
process.HBHENoiseFilterResult = cms.Path(process.fHBHENoiseFilterResult)
process.HBHENoiseFilterResultRun1 = cms.Path(process.fHBHENoiseFilterResultRun1)
process.HBHENoiseFilterResultRun2Loose = cms.Path(process.fHBHENoiseFilterResultRun2Loose)
process.HBHENoiseFilterResultRun2Tight = cms.Path(process.fHBHENoiseFilterResultRun2Tight)
process.HBHEIsoNoiseFilterResult = cms.Path(process.fHBHEIsoNoiseFilterResult)

process.PAprimaryVertexFilter = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && abs(z) <= 25 && position.Rho <= 2 && tracksSize >= 2"),
    filter = cms.bool(True), # otherwise it won't filter the events
)

process.NoScraping = cms.EDFilter("FilterOutScraping",
 applyfilter = cms.untracked.bool(True),
 debugOn = cms.untracked.bool(False),
 numtrack = cms.untracked.uint32(10),
 thresh = cms.untracked.double(0.25)
)

process.pPAprimaryVertexFilter = cms.Path(process.PAprimaryVertexFilter)
process.pBeamScrapingFilter=cms.Path(process.NoScraping)

process.load("HeavyIonsAnalysis.VertexAnalysis.PAPileUpVertexFilter_cff")

process.pVertexFilterCutG = cms.Path(process.pileupVertexFilterCutG)
process.pVertexFilterCutGloose = cms.Path(process.pileupVertexFilterCutGloose)
process.pVertexFilterCutGtight = cms.Path(process.pileupVertexFilterCutGtight)
process.pVertexFilterCutGplus = cms.Path(process.pileupVertexFilterCutGplus)
process.pVertexFilterCutE = cms.Path(process.pileupVertexFilterCutE)
process.pVertexFilterCutEandG = cms.Path(process.pileupVertexFilterCutEandG)

process.pAna = cms.EndPath(process.skimanalysis)

# Customization

#process.akSoftDrop4PFPatJetFlavourAssociation.jets="ak4PFJets"
#process.akSoftDrop4PFPatJetFlavourAssociation.groomedJets=cms.InputTag("akSoftDrop4PFJets")
#process.akSoftDrop4PFPatJetFlavourAssociation.subjets= cms.InputTag('akSoftDrop4PFJets','SubJets')
#process.akSoftDrop4PFJets.useSoftDrop = True
#process.akSoftDrop4PFpatJetsWithBtagging.getJetMCFlavour = cms.bool(False)

#process.printEventAKSoftDrop4PFJets = cms.EDAnalyzer("printJetFlavourInfo",
#                                                     jetFlavourInfos    = cms.InputTag("akSoftDrop4PFPatJetFlavourAssociation"),
#                                                     subjetFlavourInfos = cms.InputTag("akSoftDrop4PFPatJetFlavourAssociation","SubJets"),
#                                                     groomedJets        = cms.InputTag("akSoftDrop4PFJets"),
#                                                     )


#process.ana_step *= process.printEventAKSoftDrop4PFJets


