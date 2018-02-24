### HiForest Configuration
# Collisions: pp
# Type: Data
# Input: AOD

import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')
process.options = cms.untracked.PSet()

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


#####################################
# Timing Module 
#####################################

#process.Timing = cms.Service("Timing",
#      summaryOnly = cms.untracked.bool(False),
#      useJobReport = cms.untracked.bool(True)
#    )

#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                '/store/data/Run2015E/HighPtJet80/AOD/PromptReco-v1/000/262/173/00000/3E8293B5-9894-E511-90E8-02163E011FA1.root'                        
# '/store/data/Run2015E/HighPtJet80/AOD/PromptReco-v1/000/262/173/00000/3E8293B5-9894-E511-90E8-02163E011FA1.root'                                #'/store/data/Run2015E/HighPtJet80/AOD/PromptReco-v1/000/262/272/00000/803A4255-7696-E511-B178-02163E0142DD.root'
                            )
)

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50))


#####################################################################################
# Load Global Tag, Geometry, etc.
#####################################################################################

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
process.HiForest.GlobalTagLabel = process.GlobalTag.globaltag

from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import overrideJEC_pp5020
process = overrideJEC_pp5020(process)

from CondCore.DBCommon.CondDBSetup_cfi import *
##process.jpTagConds = cms.ESSource("PoolDBESSource", CondDBSetup,
##                connect = cms.string('sqlite_file:btagnew_data75X_recalib2017.db'),
##                toGet = cms.VPSet(         # overide Global Tag use EcalTBWeights_EBEE_offline
##                        cms.PSet(
##                                record = cms.string('BTagTrackProbability2DRcd') ,
##                                tag = cms.string('probBTagPDF2D_tag_mc')
##                                ),
##                        cms.PSet(
##                                record = cms.string('BTagTrackProbability3DRcd') ,
##                                tag = cms.string('probBTagPDF3D_tag_mc')
##                                )
##                        )
##                )
##process.es_prefer_jpTagConds = cms.ESPrefer("PoolDBESSource","jpTagConds")

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("HiForestAOD.root"))

#####################################################################################
# Additional Reconstruction and Analysis: Main Body
#####################################################################################

####################################################################################

#############################
# Jets
#############################

### PP RECO does not include R=3 or R=5 jets.
### re-RECO is only possible for PF, RECO is missing calotowers
from RecoJets.JetProducers.ak5PFJets_cfi import ak5PFJets
ak5PFJets.doAreaFastjet = True
process.ak5PFJets = ak5PFJets
process.ak3PFJets = ak5PFJets.clone(rParam = 0.3)

process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak4CaloJetSequence_pp_data_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak3PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak4PFJetSequence_pp_data_cff')

#process.load('HeavyIonsAnalysis.JetAnalysis.jets.akCs4PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akSoftDrop4PFJetSequence_pp_data_cff')

process.highPurityTracks = cms.EDFilter("TrackSelector",
                                        src = cms.InputTag("generalTracks"),
                                        cut = cms.string('quality("highPurity")')
                                        )

#process.load('RecoJets.JetProducers.akCs4PFJets_cfi')

#KT jets and rho estimators
#process.load('RecoJets.JetProducers.kt4PFJets_cfi') 
#process.load('RecoHI.HiJetAlgos.hiFJRhoProducer') 
#process.load('RecoHI.HiJetAlgos.hiFJGridEmptyAreaCalculator_cff') 
#process.kt4PFJets.src = cms.InputTag('particleFlow')
#process.kt4PFJets.doAreaFastjet = True
#process.kt4PFJets.jetPtMin      = cms.double(0.0)
#process.kt4PFJets.GhostArea     = cms.double(0.005)
#process.hiFJGridEmptyAreaCalculator.doCentrality = cms.bool(False)
#process.hiFJGridEmptyAreaCalculator.pfCandSource = cms.InputTag("particleFlow")

#CS jets
#process.akCs4PFJets.rho      = cms.InputTag('hiFJGridEmptyAreaCalculator','mapToRhoCorr1Bin')
#process.akCs4PFJets.rhom      = cms.InputTag('hiFJGridEmptyAreaCalculator','mapToRhoMCorr1Bin')
#process.akCs4PFJets.src = cms.InputTag('particleFlow')

#SoftDrop PF jets
from RecoJets.JetProducers.PFJetParameters_cfi import *
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *
process.akSoftDrop4PFJets = cms.EDProducer(
    "SoftDropJetProducer",
    PFJetParameters,
    AnomalousCellParameters,
    jetAlgorithm = cms.string("AntiKt"),
    rParam       = cms.double(0.4),
    useSoftDrop = cms.bool(True),
    zcut = cms.double(0.1),
    beta = cms.double(0.0),
    R0   = cms.double(0.4),
    JESpt0 = cms.double(0.02),
    JESpt1 = cms.double(0.02),
    JER = cms.bool(False),
    isBjet = cms.bool(True),
    useOnlyCharged = cms.bool(False),
    useExplicitGhosts = cms.bool(True),
    writeCompound = cms.bool(True),
    jetCollInstanceName=cms.string("SubJets")
)
#process.akSoftDrop5PFJets = process.akSoftDrop4PFJets.clone(rParam = cms.double(0.5), R0 = cms.double(0.5))

process.jetSequences = cms.Sequence(
    #process.ak3PFJets +
    #process.ak5PFJets +
 #   process.kt4PFJets +
  #  process.hiFJRhoProducer +
  #  process.hiFJGridEmptyAreaCalculator +
#    process.akCs4PFJets +
    process.akSoftDrop4PFJets +
    process.highPurityTracks +
    #process.ak4CaloJetSequence +
    #process.ak3PFJetSequence +
    process.ak4PFJetSequence +
    #process.akCs4PFJetSequence +
    process.akSoftDrop4PFJetSequence 
    #process.ak5PFJetSequence
    )

# How to turn on the jet constituents 
#process.ak4PFJetAnalyzer.doJetConstituents = cms.untracked.bool(True)
#process.ak4PFJetAnalyzer.doNewJetVars = cms.untracked.bool(True)


#####################################################################################

############################
# Event Analysis
############################
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hltobject_cfi')
process.hiEvtAnalyzer.Vertex = cms.InputTag("offlinePrimaryVertices")
process.hiEvtAnalyzer.doCentrality = cms.bool(False)
process.hiEvtAnalyzer.doEvtPlane = cms.bool(False)

process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
from HeavyIonsAnalysis.EventAnalysis.dummybranches_cff import addHLTdummybranchesForPP
addHLTdummybranchesForPP(process)

#process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzer_cfi")
#process.pfcandAnalyzer.skipCharged = False
#process.pfcandAnalyzer.pfPtMin = 0
#process.pfcandAnalyzer.pfCandidateLabel = cms.InputTag("particleFlow")
#process.pfcandAnalyzer.doVS = cms.untracked.bool(False)
#process.pfcandAnalyzer.doUEraw_ = cms.untracked.bool(False)
#process.pfcandAnalyzer.genLabel = cms.InputTag("genParticles")
#process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzerCS_cfi")
#process.pfcandAnalyzerCS.skipCharged = False
#process.pfcandAnalyzerCS.pfPtMin = 0
#process.pfcandAnalyzerCS.pfCandidateLabel = cms.InputTag("particleFlow")
#process.pfcandAnalyzerCS.doVS = cms.untracked.bool(False)
#process.pfcandAnalyzerCS.doUEraw_ = cms.untracked.bool(False)
#process.pfcandAnalyzerCS.genLabel = cms.InputTag("genParticles")
#process.load("HeavyIonsAnalysis.JetAnalysis.hcalNoise_cff")

#####################################################################################

#########################
# Track Analyzer
#########################
process.load('HeavyIonsAnalysis.JetAnalysis.ExtraTrackReco_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_cff')

####################################################################################

#####################
# Photons
#####################
process.load('HeavyIonsAnalysis.PhotonAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.gsfElectronLabel   = cms.InputTag("gedGsfElectrons")
process.ggHiNtuplizer.recoPhotonHiIsolationMap = cms.InputTag('photonIsolationHIProducerpp')
process.ggHiNtuplizer.VtxLabel  = cms.InputTag("offlinePrimaryVertices")
process.ggHiNtuplizer.particleFlowCollection = cms.InputTag("particleFlow")
process.ggHiNtuplizer.doVsIso   = cms.bool(False)
process.ggHiNtuplizer.doGenParticles = False
process.ggHiNtuplizer.doElectronVID = cms.bool(True)
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

#####################################################################################

process.load("HeavyIonsAnalysis.MuonAnalysis.hltMuTree_cfi")
process.hltMuTree.vertices = cms.InputTag("offlinePrimaryVertices")

#####################
# tupel and necessary PAT sequences
#####################

process.load("HeavyIonsAnalysis.VectorBosonAnalysis.tupelSequence_pp_cff")

#####################################################################################

#########################
# Main analysis list
#########################


process.ana_step = cms.Path(process.hltanalysis *
			    process.hltobject *
                            process.hiEvtAnalyzer *
                            process.jetSequences +
#                            process.egmGsfElectronIDSequence + #Should be added in the path for VID module
#                            process.ggHiNtuplizer +
#                            process.ggHiNtuplizerGED +
#                            process.pfcandAnalyzer +
#		            process.pfcandAnalyzerCS +
			    process.hltMuTree +
                            process.HiForest 
#                            process.trackSequencesPP +
#                            process.tupelPatSequence
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

process.akSoftDrop4PFJets.useSoftDrop = True
#process.akSoftDrop4PFJetAnalyzer.doExtendedFlavorTagging = cms.untracked.bool(True)
process.akSoftDrop4PFJetAnalyzer.groomedJets        = cms.InputTag("akSoftDrop4PFJets")
process.akSoftDrop4PFJetAnalyzer.doSubJets = cms.untracked.bool(True)
process.akSoftDrop4PFJetAnalyzer.doLifeTimeTaggingExtras = cms.untracked.bool(True)

process.ak4PFJetAnalyzer.trackSelection = process.akSoftDrop4PFSubjetSecondaryVertexTagInfos.trackSelection
process.ak4PFJetAnalyzer.trackPairV0Filter = process.akSoftDrop4PFSubjetSecondaryVertexTagInfos.vertexCuts.v0Filter

#process.akCs4PFJetAnalyzer.trackSelection = process.akSoftDrop4PFSubjetSecondaryVertexTagInfos.trackSelection
#process.akCs4PFJetAnalyzer.trackPairV0Filter = process.akSoftDrop4PFSubjetSecondaryVertexTagInfos.vertexCuts.v0Filter

process.akSoftDrop4PFJetAnalyzer.trackSelection = process.akSoftDrop4PFSubjetSecondaryVertexTagInfos.trackSelection
process.akSoftDrop4PFJetAnalyzer.trackPairV0Filter = process.akSoftDrop4PFSubjetSecondaryVertexTagInfos.vertexCuts.v0Filter

process.akSoftDrop4PFJetBtaggingSV *= process.akSoftDrop4PFSubjetJetTracksAssociatorAtVertex+process.akSoftDrop4PFSubjetImpactParameterTagInfos+process.akSoftDrop4PFSubjetJetProbabilityBJetTags+process.akSoftDrop4PFSubjetSecondaryVertexTagInfos+process.akSoftDrop4PFCombinedSubjetSecondaryVertexV2BJetTags+process.akSoftDrop4PFSubjetSecondaryVertexNegativeTagInfos+process.akSoftDrop4PFCombinedSubjetNegativeSecondaryVertexV2BJetTags

