import FWCore.ParameterSet.Config as cms

process = cms.Process("AlcarecoAnalysis")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
process.load("Configuration.StandardSequences.Services_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("CondCore.DBCommon.CondDBCommon_cfi")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = '102X_upgrade2018_realistic_v10'

import CalibTracker.Configuration.Common.PoolDBESSource_cfi  

#process.conditionsInTrackerAlignmentRcd = CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone(
#     connect = cms.string('sqlite_file:/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/mp2837/jobData/jobm/alignments_MP.db'),
#     #connect = cms.string('sqlite_file:alignments_MP.db'),
#     toGet = cms.VPSet(cms.PSet(record = cms.string('TrackerAlignmentRcd'),
#                               tag = cms.string('Alignments')
#                               )
#                      )
#    )
#
#process.prefer_conditionsInTrackerAlignmentRcd = cms.ESPrefer("PoolDBESSource", "conditionsInTrackerAlignmentRcd")

process.GlobalTag.toGet = cms.VPSet(
   cms.PSet(record = cms.string('TrackerAlignmentRcd'),
            tag = cms.string('TrackerAlignment_MC2018_v1'),
            connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
            ),
)


process.source = cms.Source ("PoolSource",
	fileNames =  cms.untracked.vstring(
		'file:FC020B1E-E8B4-E811-9A24-FA163E5A0019.root'
	)
)
###################################################################
# The TrackRefitter
###################################################################
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
import RecoTracker.TrackProducer.TrackRefitters_cff
process.TrackRefitter1 = process.TrackRefitterP5.clone(
    src =  'ALCARECOTkAlZMuMu', #'AliMomConstraint1',
    TrajectoryInEvent = True,
    TTRHBuilder = "WithAngleAndTemplate",
    NavigationSchool = "",
    #constraint = 'momentum', ### SPECIFIC FOR CRUZET
    #srcConstr='AliMomConstraint1' ### SPECIFIC FOR CRUZET$works only with tag V02-10-02 TrackingTools/PatternTools / or CMSSW >=31X
    )

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.myanalysis = cms.EDAnalyzer("TkAlDiMuonValidation",
                                    #TkTag = cms.string ('ALCARECOTkAlZMuMu'),
                                    TkTag = cms.string ('TrackRefitter1'),
                                    maxMass = cms.double(80),
                                    minMass = cms.double(120)
                                    )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('myTkAlDiMuonValidation_output.root')
                                   )

process.MessageLogger = cms.Service("MessageLogger",
                                    destinations = cms.untracked.vstring("cout"),
                                    cout = cms.untracked.PSet(threshold = cms.untracked.string('DEBUG'),
                                                              INFO = cms.untracked.PSet(reportEvery = cms.untracked.int32(10000))),
                                    
                                    )

process.p1 = cms.Path(process.offlineBeamSpot*
                      process.TrackRefitter1*
                      process.myanalysis)
