### HiForest Configuration
# Collisions: pp
# Type: MC
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

#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                            fileNames = cms.untracked.vstring(
														'/store/himc/HINppWinter16DR/Pythia6_bJet100_pp502/AODSIM/75X_mcRun2_asymptotic_ppAt5TeV_v3-v1/30000/06988FB5-3A0E-E611-9100-02163E011808.root'
        #"root://eoscms.cern.ch//eos/cms/store/cmst3/group/hintt/CMSSW_7_5_8_patch2/TTbar/RECO/Events_1.root"
#                           'file:step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_oldVtxParams.root')
                           #'/store/himc/HINppWinter16DR/Pythia6_bJet100_pp502/AODSIM/75X_mcRun2_asymptotic_ppAt5TeV_v3-v1/30000/06988FB5-3A0E-E611-9100-02163E011808.root')
			#'/store/user/kjung/Pythia8_ppMC_DigiReco_QCDJet_MuFiltered_loose2/ppMC_QCDJet_muFiltered_loose2_pt5GeV_pthat170/ppMC_QCDJet_muFiltered_loose2_pt5GeV_pthat170/crab_ppMC_QCDJet_muFiltered_loose2_pt5GeV_pthat170_DigiReco_muFiltered_loose2/171216_034802/0000/step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_10.root')
			#'/store/user/gsfs/Pythia8_Dijet80_pp_CUETP8M1_5020GeV/RECO__201711004/171004_122752/0000/step3_pp_RAW2DIGI_L1Reco_RECO_101.root'
			
			)
#			   eventsToProcess = cms.untracked.VEventRange('1:42101','1:52848')
)

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20))

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

from CondCore.DBCommon.CondDBSetup_cfi import *
##process.jpTagConds = cms.ESSource("PoolDBESSource", CondDBSetup,
##                connect = cms.string('sqlite_file:btagnew_pythia8MC75X_recalib2017.db'),
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

process.load("HeavyIonsAnalysis.JetAnalysis.FullJetSequence_nominalPP")

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
process.HiGenParticleAna.stableOnly = False
process.HiGenParticleAna.etaMax = cms.untracked.double(9e99)
process.HiGenParticleAna.ptMin = cms.untracked.double(-1)
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

process.load("HeavyIonsAnalysis.MuonAnalysis.hltMuTree_cfi")
process.hltMuTree.vertices = cms.InputTag("offlinePrimaryVertices")

####B-TAGGING#####

process.load('RecoBTag.CSVscikit.csvscikitTagJetTags_cfi')
process.load('RecoBTag.CSVscikit.csvscikitTaggerProducer_cfi')

process.ak4PFCombinedSecondaryVertexV2BJetTags = process.pfCSVscikitJetTags.clone()
process.ak4PFCombinedSecondaryVertexV2BJetTags.tagInfos=cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"), cms.InputTag("ak4PFSecondaryVertexTagInfos"))
process.CSVscikitTags.weightFile=cms.FileInPath('HeavyIonsAnalysis/JetAnalysis/data/TMVA_Btag_pp_BDTG.weights.xml')

################

#########################
# Main analysis list
#########################
process.ana_step = cms.Path(process.hltanalysis *
                            process.hiEvtAnalyzer *
                            process.HiGenParticleAna*
                            process.jetSequences +
                            #process.egmGsfElectronIDSequence + #Should be added in the path for VID module
                            #process.ggHiNtuplizer +
                            #process.ggHiNtuplizerGED +
#                            process.pfcandAnalyzer +
                            process.HiForest +
#			    process.trackSequencesPP +
			    process.hltMuTree +
                            process.runAnalyzer 
  #                          process.tupelPatSequence
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
process.ak4PFpatJetsWithBtagging.getJetMCFlavour = cms.bool(False)
process.akSoftDrop4PFpatJetsWithBtagging.getJetMCFlavour = cms.bool(False)
#process.akSoftDrop10PFpatJetsWithBtagging.getJetMCFlavour = cms.bool(False)
#process.akSoftDrop4PFz01b1patJetsWithBtagging.getJetMCFlavour = cms.bool(False)
#process.akSoftDrop4PFz005bm1patJetsWithBtagging.getJetMCFlavour = cms.bool(False)
#process.akSoftDrop4PFz005bm2patJetsWithBtagging.getJetMCFlavour = cms.bool(False)

process.ak4PFJetAnalyzer.doLifeTimeTaggingExtras = cms.untracked.bool(True)
process.ak4PFPatJetFlavourAssociation.groomedJets = cms.InputTag("akSoftDrop4PFJets")
process.ak4PFPatJetFlavourAssociation.doSubjets = cms.bool(True)
process.ak4PFJetAnalyzer.trackSelection = process.akSoftDrop4PFSubjetSecondaryVertexTagInfos.trackSelection
process.ak4PFJetAnalyzer.trackPairV0Filter = process.akSoftDrop4PFSubjetSecondaryVertexTagInfos.vertexCuts.v0Filter

process.akSoftDrop4PFPatJetFlavourAssociation.redoSubtraction = cms.bool(False)
process.akSoftDrop4PFPatJetFlavourAssociation.jets = cms.InputTag("ak4PFJets")
process.akSoftDrop4PFSubjetSecondaryVertexNegativeTagInfos.fatJets = cms.InputTag("ak4PFJets")
process.akSoftDrop4PFSubjetSecondaryVertexTagInfos.fatJets = cms.InputTag("ak4PFJets")
process.akSoftDrop4PFJetAnalyzer.doLifeTimeTaggingExtras = cms.untracked.bool(True)
process.akSoftDrop4PFJetAnalyzer.trackSelection = process.akSoftDrop4PFSubjetSecondaryVertexTagInfos.trackSelection
process.akSoftDrop4PFJetAnalyzer.trackPairV0Filter = process.akSoftDrop4PFSubjetSecondaryVertexTagInfos.vertexCuts.v0Filter

#process.akSoftDrop10PFJetAnalyzer.doLifeTimeTaggingExtras = cms.untracked.bool(True)
#process.akSoftDrop10PFJetAnalyzer.trackSelection = process.akSoftDrop4PFSubjetSecondaryVertexTagInfos.trackSelection
#process.akSoftDrop10PFJetAnalyzer.trackPairV0Filter = process.akSoftDrop4PFSubjetSecondaryVertexTagInfos.vertexCuts.v0Filter

#process.akSoftDrop4PFz01bm1JetAnalyzer.trackSelection = process.akSoftDrop4PFJetAnalyzer.trackSelection
#process.akSoftDrop4PFz01bm1JetAnalyzer.trackPairV0Filter = process.akSoftDrop4PFJetAnalyzer.trackPairV0Filter
#process.akSoftDrop4PFz01b1JetAnalyzer.trackSelection = process.akSoftDrop4PFJetAnalyzer.trackSelection
#process.akSoftDrop4PFz01b1JetAnalyzer.trackPairV0Filter = process.akSoftDrop4PFJetAnalyzer.trackPairV0Filter
#process.akSoftDrop4PFz005bm1JetAnalyzer.trackSelection = process.akSoftDrop4PFJetAnalyzer.trackSelection
#process.akSoftDrop4PFz005bm1JetAnalyzer.trackPairV0Filter = process.akSoftDrop4PFJetAnalyzer.trackPairV0Filter
#process.akSoftDrop4PFz005bm2JetAnalyzer.trackSelection = process.akSoftDrop4PFJetAnalyzer.trackSelection
#process.akSoftDrop4PFz005bm2JetAnalyzer.trackPairV0Filter = process.akSoftDrop4PFJetAnalyzer.trackPairV0Filter

#process.akSoftDrop4PFJetBtaggingSV *= process.akSoftDrop4PFSubjetJetTracksAssociatorAtVertex+process.akSoftDrop4PFSubjetImpactParameterTagInfos+process.akSoftDrop4PFSubjetJetProbabilityBJetTags+process.akSoftDrop4PFSubjetSecondaryVertexTagInfos+process.akSoftDrop4PFSubjetSecondaryVertexNegativeTagInfos+process.akSoftDrop4PFCombinedSubjetSecondaryVertexV2BJetTags+process.akSoftDrop4PFCombinedSubjetSecondaryVertexV2BJetTags+process.akSoftDrop4PFCombinedSubjetNegativeSecondaryVertexV2BJetTags

process.akSoftDrop4PFJetBtaggingSV *= process.akSoftDrop4PFSubjetJetTracksAssociatorAtVertex+process.akSoftDrop4PFSubjetImpactParameterTagInfos+process.akSoftDrop4PFSubjetJetProbabilityBJetTags+process.akSoftDrop4PFSubjetSecondaryVertexTagInfos+process.akSoftDrop4PFSubjetSecondaryVertexNegativeTagInfos+process.akSoftDrop4PFCombinedSubjetSecondaryVertexBJetTags+process.akSoftDrop4PFCombinedSubjetSecondaryVertexV2BJetTags+process.akSoftDrop4PFCombinedSubjetNegativeSecondaryVertexV2BJetTags

#process.akSoftDrop10PFJetBtaggingSV *= process.akSoftDrop10PFSubjetJetTracksAssociatorAtVertex+process.akSoftDrop10PFSubjetImpactParameterTagInfos+process.akSoftDrop10PFSubjetJetProbabilityBJetTags+process.akSoftDrop10PFSubjetSecondaryVertexTagInfos+process.akSoftDrop10PFSubjetSecondaryVertexNegativeTagInfos+process.akSoftDrop10PFCombinedSubjetSecondaryVertexBJetTags+process.akSoftDrop10PFCombinedSubjetSecondaryVertexV2BJetTags+process.akSoftDrop10PFCombinedSubjetNegativeSecondaryVertexV2BJetTags

#process.akSoftDrop4PFz01bm1JetBtaggingSV *= process.akSoftDrop4PFz01bm1SubjetJetTracksAssociatorAtVertex+process.akSoftDrop4PFz01bm1SubjetImpactParameterTagInfos+process.akSoftDrop4PFz01bm1SubjetJetProbabilityBJetTags+process.akSoftDrop4PFz01bm1SubjetSecondaryVertexTagInfos+process.akSoftDrop4PFz01bm1CombinedSubjetSecondaryVertexBJetTags+process.akSoftDrop4PFz01bm1CombinedSubjetSecondaryVertexV2BJetTags
#process.akSoftDrop4PFz01b1JetBtaggingSV *= process.akSoftDrop4PFz01b1SubjetJetTracksAssociatorAtVertex+process.akSoftDrop4PFz01b1SubjetImpactParameterTagInfos+process.akSoftDrop4PFz01b1SubjetJetProbabilityBJetTags+process.akSoftDrop4PFz01b1SubjetSecondaryVertexTagInfos+process.akSoftDrop4PFz01b1CombinedSubjetSecondaryVertexBJetTags+process.akSoftDrop4PFz01b1CombinedSubjetSecondaryVertexV2BJetTags
#process.akSoftDrop4PFz005bm1JetBtaggingSV *= process.akSoftDrop4PFz005bm1SubjetJetTracksAssociatorAtVertex+process.akSoftDrop4PFz005bm1SubjetImpactParameterTagInfos+process.akSoftDrop4PFz005bm1SubjetJetProbabilityBJetTags+process.akSoftDrop4PFz005bm1SubjetSecondaryVertexTagInfos+process.akSoftDrop4PFz005bm1CombinedSubjetSecondaryVertexBJetTags+process.akSoftDrop4PFz005bm1CombinedSubjetSecondaryVertexV2BJetTags
#process.akSoftDrop4PFz005bm2JetBtaggingSV *= process.akSoftDrop4PFz005bm2SubjetJetTracksAssociatorAtVertex+process.akSoftDrop4PFz005bm2SubjetImpactParameterTagInfos+process.akSoftDrop4PFz005bm2SubjetJetProbabilityBJetTags+process.akSoftDrop4PFz005bm2SubjetSecondaryVertexTagInfos+process.akSoftDrop4PFz005bm2CombinedSubjetSecondaryVertexBJetTags+process.akSoftDrop4PFz005bm2CombinedSubjetSecondaryVertexV2BJetTags

