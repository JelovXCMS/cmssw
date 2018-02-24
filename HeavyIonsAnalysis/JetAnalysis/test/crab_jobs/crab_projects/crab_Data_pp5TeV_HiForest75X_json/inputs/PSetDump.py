import FWCore.ParameterSet.Config as cms

process = cms.Process("HiForest")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/data/Run2015E/HighPtJet80/AOD/PromptReco-v1/000/262/173/00000/3E8293B5-9894-E511-90E8-02163E011FA1.root')
)
process.HBHENoiseFilterResultProducer = cms.EDProducer("HBHENoiseFilterResultProducer",
    IgnoreTS4TS5ifJetInLowBVRegion = cms.bool(True),
    defaultDecision = cms.string('HBHENoiseFilterResultRun1'),
    minHPDHits = cms.int32(17),
    minHPDNoOtherHits = cms.int32(10),
    minIsolatedNoiseSumE = cms.double(50.0),
    minIsolatedNoiseSumEt = cms.double(25.0),
    minNumIsolatedNoiseChannels = cms.int32(10),
    minZeros = cms.int32(9999),
    noiselabel = cms.InputTag("hcalnoise")
)


process.Njettiness = cms.EDProducer("NjettinessAdder",
    Njets = cms.vuint32(1, 2, 3, 4),
    R0 = cms.double(0.8),
    Rcutoff = cms.double(-999.0),
    akAxesR0 = cms.double(-999.0),
    axesDefinition = cms.uint32(6),
    beta = cms.double(1.0),
    measureDefinition = cms.uint32(0),
    nPass = cms.int32(-999),
    src = cms.InputTag("ak8PFJetsCHS")
)


process.ak3PFCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"), cms.InputTag("ak3PFSecondaryVertexTagInfos"))
)


process.ak3PFCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"), cms.InputTag("ak3PFSecondaryVertexTagInfos"))
)


process.ak3PFImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("ak3PFJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.ak3PFJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"))
)


process.ak3PFJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("ak3CaloJets"),
    useRecHits = cms.bool(True)
)


process.ak3PFJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"))
)


process.ak3PFJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("ak3PFJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.ak3PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.3),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak3PFNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"), cms.InputTag("ak3PFSecondaryVertexNegativeTagInfos"))
)


process.ak3PFNegativeCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"), cms.InputTag("ak3PFSecondaryVertexNegativeTagInfos"))
)


process.ak3PFNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFSecondaryVertexNegativeTagInfos"))
)


process.ak3PFNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFSecondaryVertexNegativeTagInfos"))
)


process.ak3PFNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFSoftPFMuonsTagInfos"))
)


process.ak3PFNjettiness = cms.EDProducer("NjettinessAdder",
    Njets = cms.vuint32(1, 2, 3, 4),
    R0 = cms.double(0.3),
    Rcutoff = cms.double(-999.0),
    akAxesR0 = cms.double(-999.0),
    axesDefinition = cms.uint32(6),
    beta = cms.double(1.0),
    measureDefinition = cms.uint32(0),
    nPass = cms.int32(-999),
    src = cms.InputTag("ak3PFJets")
)


process.ak3PFPatJetFlavourAssociation = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("ak3PFPatJetPartons","bHadrons"),
    cHadrons = cms.InputTag("ak3PFPatJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak3PFJets"),
    leptons = cms.InputTag("ak3PFPatJetPartons","leptons"),
    partons = cms.InputTag("ak3PFPatJetPartons","algorithmicPartons"),
    rParam = cms.double(0.3)
)


process.ak3PFPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("ak3PFPatJetPartonAssociationLegacy")
)


process.ak3PFPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak3PFJets"),
    partons = cms.InputTag("myPartons")
)


process.ak3PFPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.ak3PFPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"), cms.InputTag("ak3PFSecondaryVertexTagInfos"))
)


process.ak3PFPositiveCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"), cms.InputTag("ak3PFSecondaryVertexTagInfos"))
)


process.ak3PFPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFSoftPFMuonsTagInfos"))
)


process.ak3PFSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("ak3PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.ak3PFSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("ak3PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.ak3PFSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFSecondaryVertexTagInfos"))
)


process.ak3PFSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFSecondaryVertexTagInfos"))
)


process.ak3PFSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFSoftPFMuonsTagInfos"))
)


process.ak3PFSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFSoftPFMuonsTagInfos"))
)


process.ak3PFSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFSoftPFMuonsTagInfos"))
)


process.ak3PFSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("ak3PFJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.ak3PFTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"))
)


process.ak3PFTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak3PFImpactParameterTagInfos"))
)


process.ak3PFcorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AK3PF_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak3PFJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.ak3PFmatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak3GenJets"),
    maxDeltaR = cms.double(0.3),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak3PFJets")
)


process.ak3PFmatchGroomed = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak3GenJets"),
    maxDeltaR = cms.double(0.3),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak3GenJets")
)


process.ak3PFparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak3PFJets")
)


process.ak3PFpatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("ak3PFPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("ak3PFPatJetFlavourAssociation"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("ak3PFSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("ak3PFSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("ak3PFCombinedSecondaryVertexBJetTags"), cms.InputTag("ak3PFCombinedSecondaryVertexV2BJetTags"), cms.InputTag("ak3PFJetBProbabilityBJetTags"), 
        cms.InputTag("ak3PFJetProbabilityBJetTags"), cms.InputTag("ak3PFTrackCountingHighEffBJetTags"), cms.InputTag("ak3PFTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("ak3PFmatch"),
    genPartonMatch = cms.InputTag("ak3PFparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak3PFcorr")),
    jetIDMap = cms.InputTag("ak3PFJetID"),
    jetSource = cms.InputTag("ak3PFJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak3PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("", "ak3PFNjettiness:tau1", "ak3PFNjettiness:tau2", "ak3PFNjettiness:tau3")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.ak4CaloCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"), cms.InputTag("ak4CaloSecondaryVertexTagInfos"))
)


process.ak4CaloCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"), cms.InputTag("ak4CaloSecondaryVertexTagInfos"))
)


process.ak4CaloImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("ak4CaloJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.ak4CaloJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"))
)


process.ak4CaloJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("ak4CaloJets"),
    useRecHits = cms.bool(True)
)


process.ak4CaloJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"))
)


process.ak4CaloJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("ak4CaloJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.ak4CaloNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"), cms.InputTag("ak4CaloSecondaryVertexNegativeTagInfos"))
)


process.ak4CaloNegativeCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"), cms.InputTag("ak4CaloSecondaryVertexNegativeTagInfos"))
)


process.ak4CaloNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloSecondaryVertexNegativeTagInfos"))
)


process.ak4CaloNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloSecondaryVertexNegativeTagInfos"))
)


process.ak4CaloNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloSoftPFMuonsTagInfos"))
)


process.ak4CaloNjettiness = cms.EDProducer("NjettinessAdder",
    Njets = cms.vuint32(1, 2, 3, 4),
    R0 = cms.double(0.4),
    Rcutoff = cms.double(-999.0),
    akAxesR0 = cms.double(-999.0),
    axesDefinition = cms.uint32(6),
    beta = cms.double(1.0),
    measureDefinition = cms.uint32(0),
    nPass = cms.int32(-999),
    src = cms.InputTag("ak4CaloJets")
)


process.ak4CaloPatJetFlavourAssociation = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("ak4CaloPatJetPartons","bHadrons"),
    cHadrons = cms.InputTag("ak4CaloPatJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak4CaloJets"),
    leptons = cms.InputTag("ak4CaloPatJetPartons","leptons"),
    partons = cms.InputTag("ak4CaloPatJetPartons","algorithmicPartons"),
    rParam = cms.double(0.4)
)


process.ak4CaloPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("ak4CaloPatJetPartonAssociationLegacy")
)


process.ak4CaloPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak4CaloJets"),
    partons = cms.InputTag("myPartons")
)


process.ak4CaloPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.ak4CaloPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"), cms.InputTag("ak4CaloSecondaryVertexTagInfos"))
)


process.ak4CaloPositiveCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"), cms.InputTag("ak4CaloSecondaryVertexTagInfos"))
)


process.ak4CaloPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloSoftPFMuonsTagInfos"))
)


process.ak4CaloSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("ak4CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.ak4CaloSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("ak4CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.ak4CaloSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloSecondaryVertexTagInfos"))
)


process.ak4CaloSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloSecondaryVertexTagInfos"))
)


process.ak4CaloSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloSoftPFMuonsTagInfos"))
)


process.ak4CaloSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloSoftPFMuonsTagInfos"))
)


process.ak4CaloSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloSoftPFMuonsTagInfos"))
)


process.ak4CaloSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("ak4CaloJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.ak4CaloTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"))
)


process.ak4CaloTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4CaloImpactParameterTagInfos"))
)


process.ak4Calocorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AK4Calo_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak4CaloJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.ak4Calomatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4GenJets"),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak4CaloJets")
)


process.ak4CalomatchGroomed = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4GenJets"),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak4GenJets")
)


process.ak4Caloparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak4CaloJets")
)


process.ak4CalopatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("ak4CaloPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("ak4CaloPatJetFlavourAssociation"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("ak4CaloSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("ak4CaloSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("ak4CaloCombinedSecondaryVertexBJetTags"), cms.InputTag("ak4CaloCombinedSecondaryVertexV2BJetTags"), cms.InputTag("ak4CaloJetBProbabilityBJetTags"), 
        cms.InputTag("ak4CaloJetProbabilityBJetTags"), cms.InputTag("ak4CaloTrackCountingHighEffBJetTags"), cms.InputTag("ak4CaloTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("ak4Calomatch"),
    genPartonMatch = cms.InputTag("ak4Caloparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak4Calocorr")),
    jetIDMap = cms.InputTag("ak4CaloJetID"),
    jetSource = cms.InputTag("ak4CaloJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak4CaloJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("", "ak4CaloNjettiness:tau1", "ak4CaloNjettiness:tau2", "ak4CaloNjettiness:tau3")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.ak4PFCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"), cms.InputTag("ak4PFSecondaryVertexTagInfos"))
)


process.ak4PFCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"), cms.InputTag("ak4PFSecondaryVertexTagInfos"))
)


process.ak4PFImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("ak4PFJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.ak4PFJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"))
)


process.ak4PFJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("ak4CaloJets"),
    useRecHits = cms.bool(True)
)


process.ak4PFJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"))
)


process.ak4PFJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("ak4PFJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.ak4PFNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"), cms.InputTag("ak4PFSecondaryVertexNegativeTagInfos"))
)


process.ak4PFNegativeCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"), cms.InputTag("ak4PFSecondaryVertexNegativeTagInfos"))
)


process.ak4PFNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFSecondaryVertexNegativeTagInfos"))
)


process.ak4PFNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFSecondaryVertexNegativeTagInfos"))
)


process.ak4PFNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFSoftPFMuonsTagInfos"))
)


process.ak4PFNjettiness = cms.EDProducer("NjettinessAdder",
    Njets = cms.vuint32(1, 2, 3, 4),
    R0 = cms.double(0.4),
    Rcutoff = cms.double(-999.0),
    akAxesR0 = cms.double(-999.0),
    axesDefinition = cms.uint32(6),
    beta = cms.double(1.0),
    measureDefinition = cms.uint32(0),
    nPass = cms.int32(-999),
    src = cms.InputTag("ak4PFJets")
)


process.ak4PFPatJetFlavourAssociation = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("ak4PFPatJetPartons","bHadrons"),
    cHadrons = cms.InputTag("ak4PFPatJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak4PFJets"),
    leptons = cms.InputTag("ak4PFPatJetPartons","leptons"),
    partons = cms.InputTag("ak4PFPatJetPartons","algorithmicPartons"),
    rParam = cms.double(0.4)
)


process.ak4PFPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("ak4PFPatJetPartonAssociationLegacy")
)


process.ak4PFPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak4PFJets"),
    partons = cms.InputTag("myPartons")
)


process.ak4PFPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.ak4PFPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"), cms.InputTag("ak4PFSecondaryVertexTagInfos"))
)


process.ak4PFPositiveCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"), cms.InputTag("ak4PFSecondaryVertexTagInfos"))
)


process.ak4PFPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFSoftPFMuonsTagInfos"))
)


process.ak4PFSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("ak4PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.ak4PFSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("ak4PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.ak4PFSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFSecondaryVertexTagInfos"))
)


process.ak4PFSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFSecondaryVertexTagInfos"))
)


process.ak4PFSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFSoftPFMuonsTagInfos"))
)


process.ak4PFSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFSoftPFMuonsTagInfos"))
)


process.ak4PFSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFSoftPFMuonsTagInfos"))
)


process.ak4PFSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("ak4PFJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"))
)


process.ak4PFTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"))
)


process.ak4PFcorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute', 
        'L2L3Residual'),
    payload = cms.string('AK4PF_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak4PFJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.ak4PFmatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4GenJets"),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak4PFJets")
)


process.ak4PFmatchGroomed = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4GenJets"),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak4GenJets")
)


process.ak4PFparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak4PFJets")
)


process.ak4PFpatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("ak4PFPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("ak4PFPatJetFlavourAssociation"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("ak4PFSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("ak4PFSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("ak4PFCombinedSecondaryVertexBJetTags"), cms.InputTag("ak4PFCombinedSecondaryVertexV2BJetTags"), cms.InputTag("ak4PFJetBProbabilityBJetTags"), 
        cms.InputTag("ak4PFJetProbabilityBJetTags"), cms.InputTag("ak4PFTrackCountingHighEffBJetTags"), cms.InputTag("ak4PFTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("ak4PFmatch"),
    genPartonMatch = cms.InputTag("ak4PFparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak4PFcorr")),
    jetIDMap = cms.InputTag("ak4PFJetID"),
    jetSource = cms.InputTag("ak4PFJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak4PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("", "ak4PFNjettiness:tau1", "ak4PFNjettiness:tau2", "ak4PFNjettiness:tau3")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.ak5JetExtender = cms.EDProducer("JetExtender",
    coneSize = cms.double(0.5),
    jet2TracksAtCALO = cms.InputTag("ak5JetTracksAssociatorAtCaloFace"),
    jet2TracksAtVX = cms.InputTag("ak5JetTracksAssociatorAtVertex"),
    jets = cms.InputTag("ak5CaloJets")
)


process.ak5JetTracksAssociatorAtCaloFace = cms.EDProducer("JetTracksAssociatorAtCaloFace",
    coneSize = cms.double(0.5),
    extrapolations = cms.InputTag("trackExtrapolator"),
    jets = cms.InputTag("ak5CaloJets"),
    trackQuality = cms.string('goodIterative'),
    tracks = cms.InputTag("generalTracks")
)


process.ak5JetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("ak5CaloJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)


process.ak5JetTracksAssociatorAtVertexPF = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("ak5PFJetsCHS"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)


process.ak5JetTracksAssociatorExplicit = cms.EDProducer("JetTracksAssociatorExplicit",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("ak5PFJetsCHS"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)


process.ak5PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.5),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akSoftDrop4PFCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFImpactParameterTagInfos"), cms.InputTag("akSoftDrop4PFSecondaryVertexTagInfos"))
)


process.akSoftDrop4PFCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFImpactParameterTagInfos"), cms.InputTag("akSoftDrop4PFSecondaryVertexTagInfos"))
)


process.akSoftDrop4PFCombinedSubjetNegativeSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFSubjetImpactParameterTagInfos"), cms.InputTag("akSoftDrop4PFSubjetSecondaryVertexNegativeTagInfos"))
)


process.akSoftDrop4PFCombinedSubjetSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFSubjetImpactParameterTagInfos"), cms.InputTag("akSoftDrop4PFSubjetSecondaryVertexTagInfos"))
)


process.akSoftDrop4PFCombinedSubjetSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFSubjetImpactParameterTagInfos"), cms.InputTag("akSoftDrop4PFSubjetSecondaryVertexTagInfos"))
)


process.akSoftDrop4PFImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akSoftDrop4PFJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akSoftDrop4PFJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFImpactParameterTagInfos"))
)


process.akSoftDrop4PFJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("akSoftDrop4CaloJets"),
    useRecHits = cms.bool(True)
)


process.akSoftDrop4PFJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFImpactParameterTagInfos"))
)


process.akSoftDrop4PFJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akSoftDrop4PFJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.akSoftDrop4PFJets = cms.EDProducer("SoftDropJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    R0 = cms.double(0.4),
    Rho_EtaMax = cms.double(4.4),
    beta = cms.double(0.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useOnlyCharged = cms.bool(False),
    useSoftDrop = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True),
    zcut = cms.double(0.1)
)


process.akSoftDrop4PFNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFImpactParameterTagInfos"), cms.InputTag("akSoftDrop4PFSecondaryVertexNegativeTagInfos"))
)


process.akSoftDrop4PFNegativeCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFImpactParameterTagInfos"), cms.InputTag("akSoftDrop4PFSecondaryVertexNegativeTagInfos"))
)


process.akSoftDrop4PFNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFSecondaryVertexNegativeTagInfos"))
)


process.akSoftDrop4PFNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFSecondaryVertexNegativeTagInfos"))
)


process.akSoftDrop4PFNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFSoftPFMuonsTagInfos"))
)


process.akSoftDrop4PFNjettiness = cms.EDProducer("NjettinessAdder",
    Njets = cms.vuint32(1, 2, 3, 4),
    R0 = cms.double(0.4),
    Rcutoff = cms.double(-999.0),
    akAxesR0 = cms.double(-999.0),
    axesDefinition = cms.uint32(6),
    beta = cms.double(1.0),
    measureDefinition = cms.uint32(0),
    nPass = cms.int32(-999),
    src = cms.InputTag("akSoftDrop4PFJets")
)


process.akSoftDrop4PFPatJetFlavourAssociation = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("akSoftDrop4PFPatJetPartons","bHadrons"),
    cHadrons = cms.InputTag("akSoftDrop4PFPatJetPartons","cHadrons"),
    doSubjets = cms.bool(True),
    ghostRescaling = cms.double(1e-18),
    groomedJets = cms.InputTag("akSoftDrop4PFJets"),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("akSoftDrop4PFJets"),
    leptons = cms.InputTag("akSoftDrop4PFPatJetPartons","leptons"),
    partons = cms.InputTag("akSoftDrop4PFPatJetPartons","algorithmicPartons"),
    rParam = cms.double(0.4),
    redoSubtraction = cms.bool(True),
    subjets = cms.InputTag("akSoftDrop4PFJets","SubJets")
)


process.akSoftDrop4PFPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("akSoftDrop4PFPatJetPartonAssociationLegacy")
)


process.akSoftDrop4PFPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akSoftDrop4PFJets"),
    partons = cms.InputTag("myPartons")
)


process.akSoftDrop4PFPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.akSoftDrop4PFPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFImpactParameterTagInfos"), cms.InputTag("akSoftDrop4PFSecondaryVertexTagInfos"))
)


process.akSoftDrop4PFPositiveCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFImpactParameterTagInfos"), cms.InputTag("akSoftDrop4PFSecondaryVertexTagInfos"))
)


process.akSoftDrop4PFPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFSoftPFMuonsTagInfos"))
)


process.akSoftDrop4PFSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akSoftDrop4PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akSoftDrop4PFSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akSoftDrop4PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akSoftDrop4PFSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFSecondaryVertexTagInfos"))
)


process.akSoftDrop4PFSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFSecondaryVertexTagInfos"))
)


process.akSoftDrop4PFSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFSoftPFMuonsTagInfos"))
)


process.akSoftDrop4PFSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFSoftPFMuonsTagInfos"))
)


process.akSoftDrop4PFSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFSoftPFMuonsTagInfos"))
)


process.akSoftDrop4PFSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("akSoftDrop4PFJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.akSoftDrop4PFSubjetImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akSoftDrop4PFSubjetJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akSoftDrop4PFSubjetJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFSubjetImpactParameterTagInfos"))
)


process.akSoftDrop4PFSubjetJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorExplicit",
    jets = cms.InputTag("akSoftDrop4PFJets","SubJets"),
    tracks = cms.InputTag("highPurityTracks")
)


process.akSoftDrop4PFSubjetSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    fatJets = cms.InputTag("akSoftDrop4PFJets"),
    groomedFatJets = cms.InputTag("akSoftDrop4PFJets"),
    jetAlgorithm = cms.string('AntiKt'),
    minimumTrackWeight = cms.double(0.5),
    rParam = cms.double(0.4),
    trackIPTagInfos = cms.InputTag("akSoftDrop4PFSubjetImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    useSVClustering = cms.bool(True),
    useSVMomentum = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.1),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akSoftDrop4PFSubjetSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    fatJets = cms.InputTag("akSoftDrop4PFJets"),
    groomedFatJets = cms.InputTag("akSoftDrop4PFJets"),
    jetAlgorithm = cms.string('AntiKt'),
    minimumTrackWeight = cms.double(0.5),
    rParam = cms.double(0.4),
    trackIPTagInfos = cms.InputTag("akSoftDrop4PFSubjetImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    useSVClustering = cms.bool(True),
    useSVMomentum = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.1),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akSoftDrop4PFTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFImpactParameterTagInfos"))
)


process.akSoftDrop4PFTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akSoftDrop4PFImpactParameterTagInfos"))
)


process.akSoftDrop4PFcorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute', 
        'L2L3Residual'),
    payload = cms.string('AK4PF_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akSoftDrop4PFJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akSoftDrop4PFmatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4GenJets"),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akSoftDrop4PFJets")
)


process.akSoftDrop4PFmatchGroomed = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4GenJets"),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akSoftDrop4GenJets")
)


process.akSoftDrop4PFparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akSoftDrop4PFJets")
)


process.akSoftDrop4PFpatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akSoftDrop4PFPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akSoftDrop4PFPatJetFlavourAssociation"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("akSoftDrop4PFSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("akSoftDrop4PFSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("akSoftDrop4PFCombinedSecondaryVertexBJetTags"), cms.InputTag("akSoftDrop4PFCombinedSecondaryVertexV2BJetTags"), cms.InputTag("akSoftDrop4PFJetBProbabilityBJetTags"), 
        cms.InputTag("akSoftDrop4PFJetProbabilityBJetTags"), cms.InputTag("akSoftDrop4PFTrackCountingHighEffBJetTags"), cms.InputTag("akSoftDrop4PFTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akSoftDrop4PFmatch"),
    genPartonMatch = cms.InputTag("akSoftDrop4PFparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akSoftDrop4PFcorr")),
    jetIDMap = cms.InputTag("akSoftDrop4PFJetID"),
    jetSource = cms.InputTag("akSoftDrop4PFJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("akSoftDrop4PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("", "akSoftDrop4PFNjettiness:tau1", "akSoftDrop4PFNjettiness:tau2", "akSoftDrop4PFNjettiness:tau3", "akSoftDrop4PFJets:sym")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("", "akSoftDrop4PFJets:droppedBranches")
        )
    )
)


process.bToCharmDecayVertexMerged = cms.EDProducer("BtoCharmDecayVertexMerger",
    maxDRUnique = cms.double(0.4),
    maxPtreltomerge = cms.double(7777.0),
    maxvecSumIMifsmallDRUnique = cms.double(5.5),
    minCosPAtomerge = cms.double(0.99),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("inclusiveSecondaryVerticesFiltered")
)


process.candidateVertexArbitrator = cms.EDProducer("CandidateVertexArbitrator",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    dLenFraction = cms.double(0.333),
    dRCut = cms.double(0.4),
    distCut = cms.double(0.04),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("candidateVertexMerger"),
    sigCut = cms.double(5),
    trackMinLayers = cms.int32(4),
    trackMinPixels = cms.int32(1),
    trackMinPt = cms.double(0.4),
    tracks = cms.InputTag("particleFlow")
)


process.candidateVertexArbitratorCtagL = cms.EDProducer("CandidateVertexArbitrator",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    dLenFraction = cms.double(0.333),
    dRCut = cms.double(0.4),
    distCut = cms.double(0.04),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("candidateVertexMergerCtagL"),
    sigCut = cms.double(5),
    trackMinLayers = cms.int32(4),
    trackMinPixels = cms.int32(1),
    trackMinPt = cms.double(0.4),
    tracks = cms.InputTag("particleFlow")
)


process.candidateVertexMerger = cms.EDProducer("CandidateVertexMerger",
    maxFraction = cms.double(0.7),
    minSignificance = cms.double(2),
    secondaryVertices = cms.InputTag("inclusiveCandidateVertexFinder")
)


process.candidateVertexMergerCtagL = cms.EDProducer("CandidateVertexMerger",
    maxFraction = cms.double(0.7),
    minSignificance = cms.double(2),
    secondaryVertices = cms.InputTag("inclusiveCandidateVertexFinderCtagL")
)


process.combinedInclusiveSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderTagInfos"))
)


process.combinedInclusiveSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderTagInfos"))
)


process.combinedMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedMVAComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.combinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"))
)


process.combinedSecondaryVertexSoftLeptonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexSoftLeptonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.combinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"))
)


process.doubleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('doubleVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("inclusiveSecondaryVertexFinderFilteredTagInfos"))
)


process.egmGsfElectronIDs = cms.EDProducer("VersionedGsfElectronIdProducer",
    physicsObjectIDs = cms.VPSet(cms.PSet(
        idDefinition = cms.PSet(
            cutFlow = cms.VPSet(cms.PSet(
                cutName = cms.string('MinPtCut'),
                isIgnored = cms.bool(False),
                minPt = cms.double(5.0),
                needsAdditionalProducts = cms.bool(False)
            ), 
                cms.PSet(
                    allowedEtaRanges = cms.VPSet(cms.PSet(
                        maxEta = cms.double(1.479),
                        minEta = cms.double(0.0)
                    ), 
                        cms.PSet(
                            maxEta = cms.double(2.5),
                            minEta = cms.double(1.479)
                        )),
                    cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False),
                    useAbsEta = cms.bool(True)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleDEtaInCut'),
                    dEtaInCutValueEB = cms.double(0.0105),
                    dEtaInCutValueEE = cms.double(0.00814),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleDPhiInCut'),
                    dPhiInCutValueEB = cms.double(0.115),
                    dPhiInCutValueEE = cms.double(0.182),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                    full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0103),
                    full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0301),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleHadronicOverEMCut'),
                    hadronicOverEMCutValueEB = cms.double(0.104),
                    hadronicOverEMCutValueEE = cms.double(0.0897),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleDxyCut'),
                    dxyCutValueEB = cms.double(0.0261),
                    dxyCutValueEE = cms.double(0.118),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                    vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleDzCut'),
                    dzCutValueEB = cms.double(0.41),
                    dzCutValueEE = cms.double(0.822),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                    vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                    eInverseMinusPInverseCutValueEB = cms.double(0.102),
                    eInverseMinusPInverseCutValueEE = cms.double(0.126),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                    effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
                    isIgnored = cms.bool(False),
                    isRelativeIso = cms.bool(True),
                    isoCutEBHighPt = cms.double(0.0893),
                    isoCutEBLowPt = cms.double(0.0893),
                    isoCutEEHighPt = cms.double(0.121),
                    isoCutEELowPt = cms.double(0.121),
                    needsAdditionalProducts = cms.bool(True),
                    ptCutOff = cms.double(20.0),
                    rho = cms.InputTag("fixedGridRhoFastjetAll")
                ), 
                cms.PSet(
                    beamspotSrc = cms.InputTag("offlineBeamSpot"),
                    conversionSrc = cms.InputTag("allConversions"),
                    conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                    cutName = cms.string('GsfEleConversionVetoCut'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleMissingHitsCut'),
                    isIgnored = cms.bool(False),
                    maxMissingHitsEB = cms.uint32(2),
                    maxMissingHitsEE = cms.uint32(1),
                    needsAdditionalProducts = cms.bool(False)
                )),
            idName = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-loose')
        ),
        idMD5 = cms.string('4fab9e4d09a2c1a36cbbd2279deb3627'),
        isPOGApproved = cms.untracked.bool(True)
    ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInCut'),
                        dEtaInCutValueEB = cms.double(0.0103),
                        dEtaInCutValueEE = cms.double(0.00733),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0336),
                        dPhiInCutValueEE = cms.double(0.114),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0101),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0283),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0876),
                        hadronicOverEMCutValueEE = cms.double(0.0678),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDxyCut'),
                        dxyCutValueEB = cms.double(0.0118),
                        dxyCutValueEE = cms.double(0.0739),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDzCut'),
                        dzCutValueEB = cms.double(0.373),
                        dzCutValueEE = cms.double(0.602),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0174),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0898),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0766),
                        isoCutEBLowPt = cms.double(0.0766),
                        isoCutEEHighPt = cms.double(0.0678),
                        isoCutEELowPt = cms.double(0.0678),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-medium')
            ),
            idMD5 = cms.string('aa291aba714c148fcba156544907c440'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInCut'),
                        dEtaInCutValueEB = cms.double(0.00926),
                        dEtaInCutValueEE = cms.double(0.00724),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0336),
                        dPhiInCutValueEE = cms.double(0.0918),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0101),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0279),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0597),
                        hadronicOverEMCutValueEE = cms.double(0.0615),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDxyCut'),
                        dxyCutValueEB = cms.double(0.0111),
                        dxyCutValueEE = cms.double(0.0351),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDzCut'),
                        dzCutValueEB = cms.double(0.0466),
                        dzCutValueEE = cms.double(0.417),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.012),
                        eInverseMinusPInverseCutValueEE = cms.double(0.00999),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0354),
                        isoCutEBLowPt = cms.double(0.0354),
                        isoCutEEHighPt = cms.double(0.0646),
                        isoCutEELowPt = cms.double(0.0646),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-tight')
            ),
            idMD5 = cms.string('4e13b87c0573d3c8ebf91d446fa1d90f'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInCut'),
                        dEtaInCutValueEB = cms.double(0.0152),
                        dEtaInCutValueEE = cms.double(0.0113),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.216),
                        dPhiInCutValueEE = cms.double(0.237),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0114),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0352),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.181),
                        hadronicOverEMCutValueEE = cms.double(0.116),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDxyCut'),
                        dxyCutValueEB = cms.double(0.0564),
                        dxyCutValueEE = cms.double(0.222),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDzCut'),
                        dzCutValueEB = cms.double(0.472),
                        dzCutValueEE = cms.double(0.921),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.207),
                        eInverseMinusPInverseCutValueEE = cms.double(0.174),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.126),
                        isoCutEBLowPt = cms.double(0.126),
                        isoCutEEHighPt = cms.double(0.144),
                        isoCutEELowPt = cms.double(0.144),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-veto')
            ),
            idMD5 = cms.string('202030579ee3eec90fdc2d236ba3de7e'),
            isPOGApproved = cms.untracked.bool(True)
        )),
    physicsObjectSrc = cms.InputTag("gedGsfElectrons")
)


process.electronMVAValueMapProducer = cms.EDProducer("ElectronMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(cms.PSet(
        mvaName = cms.string('ElectronMVAEstimatorRun2Phys14NonTrig'),
        mvaTag = cms.string('25nsV1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
    ), 
        cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            conversionsAOD = cms.InputTag("allConversions"),
            conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
            mvaName = cms.string('ElectronMVAEstimatorRun2Spring15NonTrig'),
            mvaTag = cms.string('25nsV1'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
        )),
    src = cms.InputTag("gedGsfElectrons"),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.electronRegressionValueMapProducer = cms.EDProducer("ElectronRegressionValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    src = cms.InputTag("gedGsfElectrons"),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
    useFull5x5 = cms.bool(False)
)


process.ghostTrackBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('ghostTrackComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("ghostTrackVertexTagInfos"))
)


process.ghostTrackVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(1),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('gtvr'),
        fitType = cms.string('RefitGhostTrackWithVertices'),
        maxFitChi2 = cms.double(10.0),
        mergeThreshold = cms.double(3.0),
        primcut = cms.double(2.0),
        seccut = cms.double(4.0)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.impactParameterMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('impactParameterMVAComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.impactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.inclusiveCandidateSecondaryVertices = cms.EDProducer("CandidateVertexMerger",
    maxFraction = cms.double(0.2),
    minSignificance = cms.double(10.0),
    secondaryVertices = cms.InputTag("candidateVertexArbitrator")
)


process.inclusiveCandidateSecondaryVerticesCtagL = cms.EDProducer("CandidateVertexMerger",
    maxFraction = cms.double(0.2),
    minSignificance = cms.double(10.0),
    secondaryVertices = cms.InputTag("candidateVertexArbitratorCtagL")
)


process.inclusiveCandidateVertexFinder = cms.EDProducer("InclusiveCandidateVertexFinder",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterizer = cms.PSet(
        clusterMaxDistance = cms.double(0.05),
        clusterMaxSignificance = cms.double(4.5),
        clusterMinAngleCosine = cms.double(0.5),
        distanceRatio = cms.double(20),
        seedMax3DIPSignificance = cms.double(9999.0),
        seedMax3DIPValue = cms.double(9999.0),
        seedMin3DIPSignificance = cms.double(1.2),
        seedMin3DIPValue = cms.double(0.005)
    ),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxNTracks = cms.uint32(30),
    maximumLongitudinalImpactParameter = cms.double(0.3),
    minHits = cms.uint32(8),
    minPt = cms.double(0.8),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("particleFlow"),
    useDirectVertexFitter = cms.bool(True),
    useVertexReco = cms.bool(True),
    vertexMinAngleCosine = cms.double(0.95),
    vertexMinDLen2DSig = cms.double(2.5),
    vertexMinDLenSig = cms.double(0.5),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        primcut = cms.double(1.0),
        seccut = cms.double(3),
        smoothing = cms.bool(True)
    )
)


process.inclusiveCandidateVertexFinderCtagL = cms.EDProducer("InclusiveCandidateVertexFinder",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterizer = cms.PSet(
        clusterMaxDistance = cms.double(0.05),
        clusterMaxSignificance = cms.double(4.5),
        clusterMinAngleCosine = cms.double(0.5),
        distanceRatio = cms.double(10),
        seedMax3DIPSignificance = cms.double(9999.0),
        seedMax3DIPValue = cms.double(9999.0),
        seedMin3DIPSignificance = cms.double(1.0),
        seedMin3DIPValue = cms.double(0.005)
    ),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxNTracks = cms.uint32(30),
    maximumLongitudinalImpactParameter = cms.double(0.3),
    minHits = cms.uint32(8),
    minPt = cms.double(0.8),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("particleFlow"),
    useDirectVertexFitter = cms.bool(True),
    useVertexReco = cms.bool(True),
    vertexMinAngleCosine = cms.double(0.95),
    vertexMinDLen2DSig = cms.double(1.25),
    vertexMinDLenSig = cms.double(0.25),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        primcut = cms.double(1.0),
        seccut = cms.double(3),
        smoothing = cms.bool(True)
    )
)


process.inclusiveSecondaryVertexFinderFilteredNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("bToCharmDecayVertexMerged"),
    extSVDeltaRToJet = cms.double(-0.4),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-2.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.inclusiveSecondaryVertexFinderFilteredTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("bToCharmDecayVertexMerged"),
    extSVDeltaRToJet = cms.double(0.4),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.inclusiveSecondaryVertexFinderNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveSecondaryVertices"),
    extSVDeltaRToJet = cms.double(-0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-2.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.inclusiveSecondaryVertexFinderTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.inclusiveSecondaryVertices = cms.EDProducer("VertexMerger",
    maxFraction = cms.double(0.2),
    minSignificance = cms.double(10.0),
    secondaryVertices = cms.InputTag("trackVertexArbitrator")
)


process.inclusiveVertexFinder = cms.EDProducer("InclusiveVertexFinder",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterizer = cms.PSet(
        clusterMaxDistance = cms.double(0.05),
        clusterMaxSignificance = cms.double(4.5),
        clusterMinAngleCosine = cms.double(0.5),
        distanceRatio = cms.double(20),
        seedMax3DIPSignificance = cms.double(9999.0),
        seedMax3DIPValue = cms.double(9999.0),
        seedMin3DIPSignificance = cms.double(1.2),
        seedMin3DIPValue = cms.double(0.005)
    ),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxNTracks = cms.uint32(30),
    maximumLongitudinalImpactParameter = cms.double(0.3),
    minHits = cms.uint32(8),
    minPt = cms.double(0.8),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useDirectVertexFitter = cms.bool(True),
    useVertexReco = cms.bool(True),
    vertexMinAngleCosine = cms.double(0.95),
    vertexMinDLen2DSig = cms.double(2.5),
    vertexMinDLenSig = cms.double(0.5),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        primcut = cms.double(1.0),
        seccut = cms.double(3),
        smoothing = cms.bool(True)
    )
)


process.jetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.jetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.muonHLTL1Match = cms.EDProducer("HLTL1MuonMatcher",
    fallbackToME1 = cms.bool(False),
    l1PhiOffset = cms.double(0.0218166156499),
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltL1extraParticles")'),
    maxDeltaEta = cms.double(99),
    maxDeltaPhi = cms.double(6),
    maxDeltaR = cms.double(0.5),
    resolveAmbiguities = cms.bool(True),
    setPropLabel = cms.string('propagatedToM2'),
    sortBy = cms.string('pt'),
    src = cms.InputTag("muons"),
    useSimpleGeometry = cms.bool(True),
    useState = cms.string('atVertex'),
    useTrack = cms.string('tracker'),
    writeExtraInfo = cms.bool(True)
)


process.muonL1Info = cms.EDProducer("L1MuonMatcher",
    fallbackToME1 = cms.bool(False),
    l1PhiOffset = cms.double(0.0218166156499),
    matched = cms.InputTag("l1extraParticles"),
    maxDeltaEta = cms.double(99),
    maxDeltaPhi = cms.double(6),
    maxDeltaR = cms.double(0.5),
    preselection = cms.string('bx == 0'),
    setL1Label = cms.string('l1'),
    setPropLabel = cms.string('propagated'),
    sortBy = cms.string('pt'),
    src = cms.InputTag("muons"),
    useSimpleGeometry = cms.bool(True),
    useState = cms.string('atVertex'),
    useTrack = cms.string('tracker'),
    writeExtraInfo = cms.bool(True)
)


process.muonMatchHLTCtfTrack = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltMuTrackJpsiCtfTrackCands")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTCtfTrack2 = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltMuTrackJpsiEffCtfTrackCands")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTL1 = cms.EDProducer("HLTL1MuonMatcher",
    fallbackToME1 = cms.bool(False),
    l1PhiOffset = cms.double(0.0218166156499),
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltL1extraParticles")'),
    maxDeltaEta = cms.double(99),
    maxDeltaPhi = cms.double(6),
    maxDeltaR = cms.double(0.5),
    resolveAmbiguities = cms.bool(True),
    setPropLabel = cms.string('propagatedToM2'),
    sortBy = cms.string('pt'),
    src = cms.InputTag("patMuonsWithoutTrigger"),
    useSimpleGeometry = cms.bool(True),
    useState = cms.string('atVertex'),
    useTrack = cms.string('tracker'),
    writeExtraInfo = cms.bool(True)
)


process.muonMatchHLTL2 = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltL2MuonCandidates")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.3),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTL3 = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltHIL3MuonCandidates")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTL3T = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltGlbTrkMuonCands")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTTrackMu = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltMuTkMuJpsiTrackerMuonCands")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchL1 = cms.EDProducer("HLTL1MuonMatcher",
    fallbackToME1 = cms.bool(False),
    l1PhiOffset = cms.double(0.0218166156499),
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltL1extraParticles")'),
    maxDeltaEta = cms.double(99),
    maxDeltaPhi = cms.double(6),
    maxDeltaR = cms.double(0.5),
    resolveAmbiguities = cms.bool(True),
    setPropLabel = cms.string('propagatedToM2'),
    sortBy = cms.string('pt'),
    src = cms.InputTag("patMuonsWithoutTrigger"),
    useSimpleGeometry = cms.bool(True),
    useState = cms.string('atVertex'),
    useTrack = cms.string('tracker'),
    writeExtraInfo = cms.bool(True)
)


process.muonTriggerMatchHLT = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string(''),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.negativeCombinedInclusiveSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderNegativeTagInfos"))
)


process.negativeCombinedInclusiveSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderNegativeTagInfos"))
)


process.negativeCombinedMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedMVAComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderNegativeTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.negativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexNegativeTagInfos"))
)


process.negativeCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexNegativeTagInfos"))
)


process.negativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.negativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.negativeSimpleInclusiveSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("inclusiveSecondaryVertexFinderFilteredNegativeTagInfos"))
)


process.negativeSimpleInclusiveSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("inclusiveSecondaryVertexFinderFilteredNegativeTagInfos"))
)


process.negativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexNegativeTagInfos"))
)


process.negativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexNegativeTagInfos"))
)


process.negativeSoftPFElectronBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFElectronComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.negativeSoftPFElectronByIP2dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFElectronByIP2dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.negativeSoftPFElectronByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFElectronByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.negativeSoftPFElectronByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFElectronByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.negativeSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.negativeSoftPFMuonByIP2dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByIP2dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.negativeSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.negativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.negativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.negativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.patElectrons = cms.EDProducer("PATElectronProducer",
    addEfficiencies = cms.bool(False),
    addElectronID = cms.bool(True),
    addGenMatch = cms.bool(True),
    addPFClusterIso = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    efficiencies = cms.PSet(

    ),
    electronIDSources = cms.PSet(
        eidLoose = cms.InputTag("eidLoose"),
        eidRobustHighEnergy = cms.InputTag("eidRobustHighEnergy"),
        eidRobustLoose = cms.InputTag("eidRobustLoose"),
        eidRobustTight = cms.InputTag("eidRobustTight"),
        eidTight = cms.InputTag("eidTight")
    ),
    electronSource = cms.InputTag("gedGsfElectrons"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedGsfElectronCore = cms.bool(True),
    embedGsfTrack = cms.bool(True),
    embedHighLevelSelection = cms.bool(True),
    embedPFCandidate = cms.bool(True),
    embedPflowBasicClusters = cms.bool(True),
    embedPflowPreshowerClusters = cms.bool(True),
    embedPflowSuperCluster = cms.bool(True),
    embedPreshowerClusters = cms.bool(True),
    embedRecHits = cms.bool(True),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    embedTrack = cms.bool(True),
    genParticleMatch = cms.InputTag("electronMatch"),
    isoDeposits = cms.PSet(

    ),
    pfCandidateMap = cms.InputTag("particleFlow","electrons"),
    pfElectronSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    resolutions = cms.PSet(

    ),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patJetCorrFactors = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute'),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak4PFJetsCHS"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetFlavourAssociation = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak4PFJetsCHS"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","algorithmicPartons"),
    rParam = cms.double(0.4)
)


process.patJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacy")
)


process.patJetGenJetMatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4GenJets"),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak4PFJetsCHS")
)


process.patJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak4PFJetsCHS"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak4PFJetsCHS")
)


process.patJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.patJetPartonsLegacy = cms.EDProducer("PartonSelector",
    src = cms.InputTag("genParticles"),
    withLeptons = cms.bool(False)
)


process.patJets = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("combinedSecondaryVertexBJetTags"), cms.InputTag("pfJetBProbabilityBJetTags"), cms.InputTag("pfJetProbabilityBJetTags"), cms.InputTag("pfTrackCountingHighPurBJetTags"), cms.InputTag("pfTrackCountingHighEffBJetTags"), 
        cms.InputTag("pfSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("pfSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("pfCombinedSecondaryVertexV2BJetTags"), cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"), cms.InputTag("softPFMuonBJetTags"), 
        cms.InputTag("softPFElectronBJetTags"), cms.InputTag("pfCombinedMVABJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatch"),
    genPartonMatch = cms.InputTag("patJetPartonMatch"),
    getJetMCFlavour = cms.bool(True),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactors")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak4PFJetsCHS"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patMuonsWithTrigger = cms.EDProducer("PATTriggerMatchMuonEmbedder",
    matches = cms.VInputTag(cms.InputTag("muonMatchHLTL2"), cms.InputTag("muonMatchHLTL3"), cms.InputTag("muonMatchHLTL3T"), cms.InputTag("muonMatchHLTCtfTrack"), cms.InputTag("muonMatchHLTCtfTrack2"), 
        cms.InputTag("muonMatchHLTTrackMu")),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.patMuonsWithoutTrigger = cms.EDProducer("PATMuonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    caloMETMuonCorrs = cms.InputTag("muonMETValueMapProducer","muCorrData"),
    efficiencies = cms.PSet(

    ),
    embedCaloMETMuonCorrs = cms.bool(False),
    embedCombinedMuon = cms.bool(True),
    embedDytMuon = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedHighLevelSelection = cms.bool(True),
    embedMuonBestTrack = cms.bool(True),
    embedPFCandidate = cms.bool(False),
    embedPfEcalEnergy = cms.bool(False),
    embedPickyMuon = cms.bool(False),
    embedStandAloneMuon = cms.bool(True),
    embedTcMETMuonCorrs = cms.bool(False),
    embedTpfmsMuon = cms.bool(False),
    embedTrack = cms.bool(True),
    embedTunePMuonBestTrack = cms.bool(True),
    forceBestTrackEmbedding = cms.bool(False),
    genParticleMatch = cms.InputTag("muonMatch"),
    isoDeposits = cms.PSet(

    ),
    muonSource = cms.InputTag("muons"),
    pfMuonSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    resolutions = cms.PSet(

    ),
    tcMETMuonCorrs = cms.InputTag("muonTCMETValueMapProducer","muCorrData"),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag(cms.InputTag("muonL1Info"))
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag()
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag(cms.InputTag("muonL1Info","deltaR"))
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag(cms.InputTag("muonL1Info","quality"))
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patPhotons = cms.EDProducer("PATPhotonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(True),
    addPFClusterIso = cms.bool(False),
    addPhotonID = cms.bool(True),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    efficiencies = cms.PSet(

    ),
    electronSource = cms.InputTag("gedGsfElectrons"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedPreshowerClusters = cms.bool(True),
    embedRecHits = cms.bool(True),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    genParticleMatch = cms.InputTag("photonMatch"),
    isoDeposits = cms.PSet(

    ),
    photonIDSources = cms.PSet(
        PhotonCutBasedIDLoose = cms.InputTag("PhotonIDProdGED","PhotonCutBasedIDLoose"),
        PhotonCutBasedIDTight = cms.InputTag("PhotonIDProdGED","PhotonCutBasedIDTight")
    ),
    photonSource = cms.InputTag("gedPhotons"),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    resolutions = cms.PSet(

    ),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patTrigger = cms.EDProducer("TriggerObjectFilterByCollection",
    collections = cms.vstring('hltL1extraParticles', 
        'hltL2MuonCandidates', 
        'hltGlbTrkMuonCands', 
        'hltMuTrackJpsiCtfTrackCands', 
        'hltMuTrackJpsiEffCtfTrackCands', 
        'hltMuTkMuJpsiTrackerMuonCands', 
        'hltHIL3MuonCandidates'),
    src = cms.InputTag("patTriggerFull")
)


process.patTriggerFull = cms.EDProducer("PATTriggerProducer",
    l1GtReadoutRecordInputTag = cms.InputTag("gtDigis","","RECO"),
    onlyStandAlone = cms.bool(True),
    processName = cms.string('HLT')
)


process.pfBoostedDoubleSecondaryVertexAK8BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexAK8Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosAK8"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAK8"), cms.InputTag("softPFMuonsTagInfosAK8"), cms.InputTag("softPFElectronsTagInfosAK8"))
)


process.pfBoostedDoubleSecondaryVertexCA15BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexCA15Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosCA15"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosCA15"), cms.InputTag("softPFMuonsTagInfosCA15"), cms.InputTag("softPFElectronsTagInfosCA15"))
)


process.pfCombinedInclusiveSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"))
)


process.pfCombinedInclusiveSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"))
)


process.pfCombinedMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedMVAComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfSecondaryVertexTagInfos"))
)


process.pfCombinedSecondaryVertexSoftLeptonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedSecondaryVertexSoftLeptonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfCombinedSecondaryVertexSoftLeptonCtagLJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedSecondaryVertexSoftLeptonCtagLComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCtagLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfSecondaryVertexTagInfos"))
)


process.pfImpactParameterTagInfos = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("particleFlow"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak4PFJetsCHS"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosAK8 = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("particleFlow"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PFJetsCHS"),
    maxDeltaR = cms.double(0.8),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosCA15 = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("particleFlow"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ca15PFJetsCHS"),
    maxDeltaR = cms.double(1.5),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfInclusiveSecondaryVertexFinderCtagLNegativeTagInfos = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveCandidateSecondaryVerticesCtagL"),
    extSVDeltaRToJet = cms.double(-0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-2.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderCtagLTagInfos = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveCandidateSecondaryVerticesCtagL"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(1.5),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderNegativeTagInfos = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveCandidateSecondaryVertices"),
    extSVDeltaRToJet = cms.double(-0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-2.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfos = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveCandidateSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosAK8 = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveCandidateSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.8),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAK8"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.8),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosCA15 = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveCandidateSecondaryVertices"),
    extSVDeltaRToJet = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosCA15"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(1.5),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(1.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfNegativeCombinedInclusiveSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderNegativeTagInfos"))
)


process.pfNegativeCombinedInclusiveSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderNegativeTagInfos"))
)


process.pfNegativeCombinedMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeCombinedMVAComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderNegativeTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfSecondaryVertexNegativeTagInfos"))
)


process.pfNegativeCombinedSecondaryVertexSoftLeptonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeCombinedSecondaryVertexSoftLeptonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderNegativeTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfNegativeCombinedSecondaryVertexSoftLeptonCtagLJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeCombinedSecondaryVertexSoftLeptonCtagLComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCtagLNegativeTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfNegativeCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfSecondaryVertexNegativeTagInfos"))
)


process.pfNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateSimpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfSecondaryVertexNegativeTagInfos"))
)


process.pfNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateSimpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfSecondaryVertexNegativeTagInfos"))
)


process.pfNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfPositiveCombinedInclusiveSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"))
)


process.pfPositiveCombinedInclusiveSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"))
)


process.pfPositiveCombinedMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveCombinedMVAComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfSecondaryVertexTagInfos"))
)


process.pfPositiveCombinedSecondaryVertexSoftLeptonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveCombinedSecondaryVertexSoftLeptonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfPositiveCombinedSecondaryVertexSoftLeptonCtagLJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveCombinedSecondaryVertexSoftLeptonCtagLComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCtagLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfPositiveCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfSecondaryVertexTagInfos"))
)


process.pfPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfSecondaryVertexNegativeTagInfos = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfSecondaryVertexTagInfos = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateSimpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfSecondaryVertexTagInfos"))
)


process.pfSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateSimpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfSecondaryVertexTagInfos"))
)


process.pfTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.positiveCombinedInclusiveSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderTagInfos"))
)


process.positiveCombinedInclusiveSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderTagInfos"))
)


process.positiveCombinedMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedMVAComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.positiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"))
)


process.positiveCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"))
)


process.positiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.positiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.positiveSoftPFElectronBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFElectronComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.positiveSoftPFElectronByIP2dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFElectronByIP2dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.positiveSoftPFElectronByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFElectronByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.positiveSoftPFElectronByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFElectronByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.positiveSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.positiveSoftPFMuonByIP2dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByIP2dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.positiveSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.positiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.secondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.secondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.siPixelRecHits = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("siPixelClusters")
)


process.siPixelRecHitsPreSplitting = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("siPixelClustersPreSplitting")
)


process.simpleInclusiveSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("inclusiveSecondaryVertexFinderFilteredTagInfos"))
)


process.simpleInclusiveSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("inclusiveSecondaryVertexFinderFilteredTagInfos"))
)


process.simpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfos"))
)


process.simpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfos"))
)


process.softMuonTagInfos = cms.EDProducer("SoftLepton",
    jets = cms.InputTag("ak4PFJetsCHS"),
    leptonCands = cms.InputTag(""),
    leptonChi2Cut = cms.double(9999.0),
    leptonDeltaRCut = cms.double(0.4),
    leptonId = cms.InputTag(""),
    leptons = cms.InputTag("muons"),
    muonSelection = cms.uint32(1),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    refineJetAxis = cms.uint32(0)
)


process.softPFElectronBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFElectronComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.softPFElectronByIP2dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFElectronByIP2dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.softPFElectronByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFElectronByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.softPFElectronByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFElectronByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.softPFElectronsTagInfos = cms.EDProducer("SoftPFElectronTagInfoProducer",
    DeltaRElectronJet = cms.double(0.4),
    MaxSip3D = cms.double(200),
    electrons = cms.InputTag("gedGsfElectrons"),
    jets = cms.InputTag("ak4PFJetsCHS"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.softPFElectronsTagInfosAK8 = cms.EDProducer("SoftPFElectronTagInfoProducer",
    DeltaRElectronJet = cms.double(0.8),
    MaxSip3D = cms.double(200),
    electrons = cms.InputTag("gedGsfElectrons"),
    jets = cms.InputTag("ak8PFJetsCHS"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.softPFElectronsTagInfosCA15 = cms.EDProducer("SoftPFElectronTagInfoProducer",
    DeltaRElectronJet = cms.double(1.5),
    MaxSip3D = cms.double(200),
    electrons = cms.InputTag("gedGsfElectrons"),
    jets = cms.InputTag("ca15PFJetsCHS"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.softPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.softPFMuonByIP2dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP2dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.softPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.softPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.softPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("ak4PFJetsCHS"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.softPFMuonsTagInfosAK8 = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("ak8PFJetsCHS"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.softPFMuonsTagInfosCA15 = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("ca15PFJetsCHS"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.towersAboveThreshold = cms.EDProducer("CaloTowerCandidateCreator",
    minimumE = cms.double(3.0),
    minimumEt = cms.double(0.0),
    src = cms.InputTag("towerMaker"),
    verbose = cms.untracked.int32(0)
)


process.trackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.trackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.trackVertexArbitrator = cms.EDProducer("TrackVertexArbitrator",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    dLenFraction = cms.double(0.333),
    dRCut = cms.double(0.4),
    distCut = cms.double(0.04),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("vertexMerger"),
    sigCut = cms.double(5),
    trackMinLayers = cms.int32(4),
    trackMinPixels = cms.int32(1),
    trackMinPt = cms.double(0.4),
    tracks = cms.InputTag("generalTracks")
)


process.vertexMerger = cms.EDProducer("VertexMerger",
    maxFraction = cms.double(0.7),
    minSignificance = cms.double(2),
    secondaryVertices = cms.InputTag("inclusiveVertexFinder")
)


process.NoScraping = cms.EDFilter("FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False),
    numtrack = cms.untracked.uint32(10),
    thresh = cms.untracked.double(0.25)
)


process.PAprimaryVertexFilter = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && abs(z) <= 25 && position.Rho <= 2 && tracksSize >= 2'),
    filter = cms.bool(True),
    src = cms.InputTag("offlinePrimaryVertices")
)


process.bVertexFilter = cms.EDFilter("BVertexFilter",
    minVertices = cms.int32(0),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("secondaryVertices"),
    useVertexKinematicAsJetAxis = cms.bool(True),
    vertexFilter = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.1),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    )
)


process.clusterCompatibilityFilter = cms.EDFilter("HIClusterCompatibilityFilter",
    cluscomSrc = cms.InputTag("hiClusterCompatibility"),
    clusterPars = cms.vdouble(0.0, 0.0045),
    clusterTrunc = cms.double(2.0),
    maxZ = cms.double(20.05),
    minZ = cms.double(-20.0),
    nhitsTrunc = cms.int32(150)
)


process.fHBHEIsoNoiseFilterResult = cms.EDFilter("BooleanFlagFilter",
    inputLabel = cms.InputTag("HBHENoiseFilterResultProducer","HBHEIsoNoiseFilterResult"),
    reverseDecision = cms.bool(False)
)


process.fHBHENoiseFilterResult = cms.EDFilter("BooleanFlagFilter",
    inputLabel = cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResult"),
    reverseDecision = cms.bool(False)
)


process.fHBHENoiseFilterResultRun1 = cms.EDFilter("BooleanFlagFilter",
    inputLabel = cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun1"),
    reverseDecision = cms.bool(False)
)


process.fHBHENoiseFilterResultRun2Loose = cms.EDFilter("BooleanFlagFilter",
    inputLabel = cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun2Loose"),
    reverseDecision = cms.bool(False)
)


process.fHBHENoiseFilterResultRun2Tight = cms.EDFilter("BooleanFlagFilter",
    inputLabel = cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun2Tight"),
    reverseDecision = cms.bool(False)
)


process.hfNegFilter = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegFilter2 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(2),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegFilter3 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(3),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegFilter4 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(4),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegFilter5 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(5),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegTowers = cms.EDFilter("EtaPtMinCandSelector",
    etaMax = cms.double(-3.0),
    etaMin = cms.double(-6.0),
    ptMin = cms.double(0),
    src = cms.InputTag("towersAboveThreshold")
)


process.hfPosFilter = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosFilter2 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(2),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosFilter3 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(3),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosFilter4 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(4),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosFilter5 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(5),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosTowers = cms.EDFilter("EtaPtMinCandSelector",
    etaMax = cms.double(6.0),
    etaMin = cms.double(3.0),
    ptMin = cms.double(0),
    src = cms.InputTag("towersAboveThreshold")
)


process.hiTracks = cms.EDFilter("TrackSelector",
    cut = cms.string('quality("highPurity")'),
    src = cms.InputTag("hiGeneralTracks")
)


process.highPurityTracks = cms.EDFilter("TrackSelector",
    cut = cms.string('quality("highPurity")'),
    src = cms.InputTag("generalTracks")
)


process.hltLevel1GTSeed = cms.EDFilter("HLTLevel1GTSeed",
    L1CollectionsTag = cms.InputTag("l1extraParticles"),
    L1GtObjectMapTag = cms.InputTag("l1GtObjectMap"),
    L1GtReadoutRecordTag = cms.InputTag("gtDigis"),
    L1MuonCollectionTag = cms.InputTag("l1extraParticles"),
    L1NrBxInEvent = cms.int32(3),
    L1SeedsLogicalExpression = cms.string(''),
    L1TechTriggerSeeding = cms.bool(False),
    L1UseAliasesForSeeding = cms.bool(True),
    L1UseL1TriggerObjectMaps = cms.bool(True),
    saveTags = cms.bool(False)
)


process.hltPixelClusterShapeFilter = cms.EDFilter("HLTPixelClusterShapeFilter",
    clusterPars = cms.vdouble(0, 0.0045),
    clusterTrunc = cms.double(2),
    inputTag = cms.InputTag("siPixelRecHits"),
    maxZ = cms.double(20.05),
    minZ = cms.double(-20),
    nhitsTrunc = cms.int32(150),
    saveTags = cms.bool(False),
    zStep = cms.double(0.2)
)


process.inclusiveSecondaryVerticesFiltered = cms.EDFilter("BVertexFilter",
    minVertices = cms.int32(0),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("inclusiveSecondaryVertices"),
    useVertexKinematicAsJetAxis = cms.bool(True),
    vertexFilter = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.1),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    )
)


process.noBSChalo = cms.EDFilter("HLTLevel1GTSeed",
    L1CollectionsTag = cms.InputTag("l1extraParticles"),
    L1GtObjectMapTag = cms.InputTag("l1GtObjectMap"),
    L1GtReadoutRecordTag = cms.InputTag("gtDigis"),
    L1MuonCollectionTag = cms.InputTag("l1extraParticles"),
    L1NrBxInEvent = cms.int32(3),
    L1SeedsLogicalExpression = cms.string('NOT (36 OR 37 OR 38 OR 39)'),
    L1TechTriggerSeeding = cms.bool(True),
    L1UseAliasesForSeeding = cms.bool(True),
    L1UseL1TriggerObjectMaps = cms.bool(True),
    saveTags = cms.bool(False)
)


process.pileupVertexFilterCutE = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(True),
    doDzNtrkCut = cms.bool(False),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutEandG = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(True),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutG = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGloose = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 4.5, 3.2, 3.0, 1.8, 
        1.8, 1.35, 0.9),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGplus = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(0.05),
    dzCutByNtrk = cms.vdouble(999.0, 999.0, 999.0, 3.0, 2.0, 
        1.6, 1.4, 1.2, 1.1, 1.0, 
        0.9, 0.8, 0.7, 0.7, 0.6, 
        0.6, 0.5, 0.5, 0.4, 0.4, 
        0.4, 0.3, 0.3, 0.3, 0.3, 
        0.3, 0.2, 0.2, 0.2, 0.2, 
        0.0),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGplusNV = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 999.0, 999.0, 3.0, 2.0, 
        1.6, 1.4, 1.2, 1.1, 1.0, 
        0.9, 0.8, 0.7, 0.7, 0.6, 
        0.6, 0.5, 0.5, 0.4, 0.4, 
        0.4, 0.3, 0.3, 0.3, 0.3, 
        0.3, 0.2, 0.2, 0.2, 0.2, 
        0.0),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGplusUpsPP = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 999.0, 1.5, 1.0, 0.8, 
        0.6, 0.5, 0.4, 0.3, 0.2, 
        0.2, 0.2, 0.2, 0.2, 0.2, 
        0.2, 0.0),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGplusplus = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(False),
    doSurfaceCut = cms.bool(True),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(0.05),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(28.593, -1.525, 2.636788, -1.5e-05, 200.0, 
        0.0),
    surfaceFunctionString = cms.string('[0]*exp([1]*(x-([3]*(y-[4])**2+[5])))+[2]'),
    surfaceMinDzEval = cms.double(0.0),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGtight = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 2.0, 1.6, 1.333, 0.8, 
        0.8, 0.6, 0.4),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutW = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(False),
    doSurfaceCut = cms.bool(True),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutWplus = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(False),
    doSurfaceCut = cms.bool(True),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(0.05),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.primaryVertexFilter = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && abs(z) <= 25 && position.Rho <= 2 && tracksSize >= 2'),
    filter = cms.bool(True),
    src = cms.InputTag("hiSelectedVertex")
)


process.HiForest = cms.EDAnalyzer("HiForestInfo",
    GlobalTagLabel = cms.string('75X_dataRun2_v13'),
    HiForestVersion = cms.string('CMSSW_7_5_8_patch3-633-gc86a77d\n'),
    inputLines = cms.vstring('HiForest V3', 
        "\'JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK4Calo_offline\'")
)


process.ak3PFJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('ak3PF'),
    doExtendedFlavorTagging = cms.untracked.bool(False),
    doGenSubJets = cms.untracked.bool(False),
    doGenSym = cms.untracked.bool(False),
    doGenTaus = cms.untracked.bool(False),
    doHiJetID = cms.untracked.bool(True),
    doJetConstituents = cms.untracked.bool(False),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doNewJetVars = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(False),
    doTower = cms.untracked.bool(False),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genDroppedBranches = cms.InputTag("ak3GenJets","droppedBranches"),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(5),
    genSym = cms.InputTag("ak3GenJets","sym"),
    genTau1 = cms.InputTag("ak3GenNjettiness","tau1"),
    genTau2 = cms.InputTag("ak3GenNjettiness","tau2"),
    genTau3 = cms.InputTag("ak3GenNjettiness","tau3"),
    genjetTag = cms.InputTag("ak3GenJets"),
    groomedJets = cms.InputTag("ak3PFJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    isPythia6 = cms.untracked.bool(False),
    jetFlavourInfos = cms.InputTag("ak3PFPatJetFlavourAssociation"),
    jetIDWeight = cms.untracked.string('HeavyIonsAnalysis/JetAnalysis/data/JetID_TMVAClassification_BDTG_weights.xml'),
    jetName = cms.untracked.string('ak3PF'),
    jetPtMin = cms.double(5.0),
    jetTag = cms.InputTag("ak3PFpatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlow"),
    rParam = cms.double(0.3),
    subjetFlavourInfos = cms.InputTag("ak3PFPatJetFlavourAssociation","SubJets"),
    subjetGenTag = cms.untracked.InputTag("ak3GenJets"),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("generalTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.ak4CaloJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('ak4Calo'),
    doExtendedFlavorTagging = cms.untracked.bool(False),
    doGenSubJets = cms.untracked.bool(False),
    doGenSym = cms.untracked.bool(False),
    doGenTaus = cms.untracked.bool(False),
    doHiJetID = cms.untracked.bool(True),
    doJetConstituents = cms.untracked.bool(False),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doNewJetVars = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(False),
    doTower = cms.untracked.bool(False),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genDroppedBranches = cms.InputTag("ak4GenJets","droppedBranches"),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(5),
    genSym = cms.InputTag("ak4GenJets","sym"),
    genTau1 = cms.InputTag("ak4GenNjettiness","tau1"),
    genTau2 = cms.InputTag("ak4GenNjettiness","tau2"),
    genTau3 = cms.InputTag("ak4GenNjettiness","tau3"),
    genjetTag = cms.InputTag("ak4GenJets"),
    groomedJets = cms.InputTag("ak4CaloJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    isPythia6 = cms.untracked.bool(False),
    jetFlavourInfos = cms.InputTag("ak4CaloPatJetFlavourAssociation"),
    jetIDWeight = cms.untracked.string('HeavyIonsAnalysis/JetAnalysis/data/JetID_TMVAClassification_BDTG_weights.xml'),
    jetName = cms.untracked.string('ak4Calo'),
    jetPtMin = cms.double(5.0),
    jetTag = cms.InputTag("ak4CalopatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlow"),
    rParam = cms.double(0.4),
    subjetFlavourInfos = cms.InputTag("ak4CaloPatJetFlavourAssociation","SubJets"),
    subjetGenTag = cms.untracked.InputTag("ak4GenJets"),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("generalTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.ak4PFJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('ak4PF'),
    doExtendedFlavorTagging = cms.untracked.bool(False),
    doGenSubJets = cms.untracked.bool(False),
    doGenSym = cms.untracked.bool(False),
    doGenTaus = cms.untracked.bool(False),
    doHiJetID = cms.untracked.bool(True),
    doJetConstituents = cms.untracked.bool(False),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doNewJetVars = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(False),
    doTower = cms.untracked.bool(False),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genDroppedBranches = cms.InputTag("ak4GenJets","droppedBranches"),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(5),
    genSym = cms.InputTag("ak4GenJets","sym"),
    genTau1 = cms.InputTag("ak4GenNjettiness","tau1"),
    genTau2 = cms.InputTag("ak4GenNjettiness","tau2"),
    genTau3 = cms.InputTag("ak4GenNjettiness","tau3"),
    genjetTag = cms.InputTag("ak4GenJets"),
    groomedJets = cms.InputTag("ak4PFJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    isPythia6 = cms.untracked.bool(False),
    jetFlavourInfos = cms.InputTag("ak4PFPatJetFlavourAssociation"),
    jetIDWeight = cms.untracked.string('HeavyIonsAnalysis/JetAnalysis/data/JetID_TMVAClassification_BDTG_weights.xml'),
    jetName = cms.untracked.string('ak4PF'),
    jetPtMin = cms.double(5.0),
    jetTag = cms.InputTag("ak4PFpatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlow"),
    rParam = cms.double(0.4),
    subjetFlavourInfos = cms.InputTag("ak4PFPatJetFlavourAssociation","SubJets"),
    subjetGenTag = cms.untracked.InputTag("ak4GenJets"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackQuality = cms.untracked.string('highPurity'),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackTag = cms.InputTag("generalTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.akSoftDrop4PFJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('akSoftDrop4PF'),
    doExtendedFlavorTagging = cms.untracked.bool(False),
    doGenSubJets = cms.untracked.bool(False),
    doGenSym = cms.untracked.bool(False),
    doGenTaus = cms.untracked.bool(False),
    doHiJetID = cms.untracked.bool(True),
    doJetConstituents = cms.untracked.bool(False),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(True),
    doNewJetVars = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(True),
    doTower = cms.untracked.bool(False),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genDroppedBranches = cms.InputTag("akSoftDrop4GenJets","droppedBranches"),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(5),
    genSym = cms.InputTag("akSoftDrop4GenJets","sym"),
    genTau1 = cms.InputTag("akSoftDrop4GenNjettiness","tau1"),
    genTau2 = cms.InputTag("akSoftDrop4GenNjettiness","tau2"),
    genTau3 = cms.InputTag("akSoftDrop4GenNjettiness","tau3"),
    genjetTag = cms.InputTag("ak4GenJets"),
    groomedJets = cms.InputTag("akSoftDrop4PFJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    isPythia6 = cms.untracked.bool(False),
    jetFlavourInfos = cms.InputTag("akSoftDrop4PFPatJetFlavourAssociation"),
    jetIDWeight = cms.untracked.string('HeavyIonsAnalysis/JetAnalysis/data/JetID_TMVAClassification_BDTG_weights.xml'),
    jetName = cms.untracked.string('akSoftDrop4PF'),
    jetPtMin = cms.double(5.0),
    jetTag = cms.InputTag("akSoftDrop4PFpatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlow"),
    rParam = cms.double(0.4),
    subjetFlavourInfos = cms.InputTag("akSoftDrop4PFPatJetFlavourAssociation","SubJets"),
    subjetGenTag = cms.untracked.InputTag("akSoftDrop4GenJets"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackQuality = cms.untracked.string('highPurity'),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackTag = cms.InputTag("generalTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.anaTrack = cms.EDAnalyzer("TrackAnalyzer",
    associatorMap = cms.InputTag("tpRecoAssocHiGeneralTracks"),
    beamSpotSrc = cms.untracked.InputTag("offlineBeamSpot"),
    doMVA = cms.untracked.bool(True),
    doPFMatching = cms.untracked.bool(True),
    doSimTrack = cms.untracked.bool(False),
    doSimVertex = cms.untracked.bool(False),
    fillSimTrack = cms.untracked.bool(False),
    mvaSrc = cms.InputTag("hiGeneralTracks","MVAVals"),
    particleSrc = cms.InputTag("genParticles"),
    pfCandSrc = cms.InputTag("particleFlowTmp"),
    qualityString = cms.untracked.string('highPurity'),
    qualityStrings = cms.untracked.vstring('highPurity', 
        'tight', 
        'loose'),
    simTrackPtMin = cms.untracked.double(0.4),
    tpEffSrc = cms.untracked.InputTag("mix","MergedTrackTruth"),
    tpFakeSrc = cms.untracked.InputTag("mix","MergedTrackTruth"),
    trackPtMin = cms.untracked.double(0.49),
    trackSrc = cms.InputTag("hiGeneralTracks"),
    useQuality = cms.untracked.bool(False),
    vertexSrc = cms.vstring('hiSelectedVertex')
)


process.ggHiNtuplizer = cms.EDAnalyzer("ggHiNtuplizer",
    VtxLabel = cms.InputTag("offlinePrimaryVertices"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversions = cms.InputTag("allConversions"),
    doElectronVID = cms.bool(True),
    doGenParticles = cms.bool(False),
    doPfIso = cms.bool(True),
    doVsIso = cms.bool(False),
    effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
    electronLooseID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-loose"),
    electronMediumID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-medium"),
    electronTightID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-tight"),
    electronVetoID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-veto"),
    genParticleSrc = cms.InputTag("genParticles"),
    gsfElectronLabel = cms.InputTag("gedGsfElectrons"),
    particleFlowCollection = cms.InputTag("particleFlow"),
    pileupCollection = cms.InputTag("addPileupInfo"),
    recoMuonSrc = cms.InputTag("muons"),
    recoPhotonHiIsolationMap = cms.InputTag("photonIsolationHIProducerpp"),
    recoPhotonSrc = cms.InputTag("photons"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    runOnParticleGun = cms.bool(False),
    useValMapIso = cms.bool(True),
    voronoiBackgroundCalo = cms.InputTag("voronoiBackgroundCalo"),
    voronoiBackgroundPF = cms.InputTag("voronoiBackgroundPF")
)


process.ggHiNtuplizerGED = cms.EDAnalyzer("ggHiNtuplizer",
    VtxLabel = cms.InputTag("offlinePrimaryVertices"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversions = cms.InputTag("allConversions"),
    doElectronVID = cms.bool(True),
    doGenParticles = cms.bool(False),
    doPfIso = cms.bool(True),
    doVsIso = cms.bool(False),
    effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
    electronLooseID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-loose"),
    electronMediumID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-medium"),
    electronTightID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-tight"),
    electronVetoID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-veto"),
    genParticleSrc = cms.InputTag("genParticles"),
    gsfElectronLabel = cms.InputTag("gedGsfElectrons"),
    particleFlowCollection = cms.InputTag("particleFlow"),
    pileupCollection = cms.InputTag("addPileupInfo"),
    recoMuonSrc = cms.InputTag("muons"),
    recoPhotonHiIsolationMap = cms.InputTag("photonIsolationHIProducerppGED"),
    recoPhotonSrc = cms.InputTag("gedPhotons"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    runOnParticleGun = cms.bool(False),
    useValMapIso = cms.bool(True),
    voronoiBackgroundCalo = cms.InputTag("voronoiBackgroundCalo"),
    voronoiBackgroundPF = cms.InputTag("voronoiBackgroundPF")
)


process.hiEvtAnalyzer = cms.EDAnalyzer("HiEvtAnalyzer",
    CentralityBinSrc = cms.InputTag("centralityBin","HFtowers"),
    CentralitySrc = cms.InputTag("hiCentrality"),
    EvtPlane = cms.InputTag("hiEvtPlane"),
    EvtPlaneFlat = cms.InputTag("hiEvtPlaneFlat"),
    HiMC = cms.InputTag("heavyIon"),
    Vertex = cms.InputTag("offlinePrimaryVertices"),
    doCentrality = cms.bool(False),
    doEvtPlane = cms.bool(False),
    doEvtPlaneFlat = cms.bool(False),
    doHiMC = cms.bool(False),
    doMC = cms.bool(False),
    doVertex = cms.bool(True),
    evtPlaneLevel = cms.int32(0),
    useHepMC = cms.bool(False)
)


process.hltMuTree = cms.EDAnalyzer("HLTMuTree",
    doGen = cms.untracked.bool(False),
    doReco = cms.untracked.bool(True),
    genparticle = cms.InputTag("hiGenParticles"),
    muons = cms.InputTag("muons"),
    simtrack = cms.InputTag("mergedtruth","MergedTrackTruth"),
    vertices = cms.InputTag("offlinePrimaryVertices")
)


process.hltanalysis = cms.EDAnalyzer("HLTBitAnalyzer",
    HLTProcessName = cms.string('HLT'),
    RunParameters = cms.PSet(
        HistogramFile = cms.untracked.string('hltbitanalysis.root')
    ),
    UseTFileService = cms.untracked.bool(True),
    dummyBranches = cms.untracked.vstring('HLT_PixelTracks_Multiplicity60_v1', 
        'HLT_PixelTracks_Multiplicity60_v2', 
        'HLT_PixelTracks_Multiplicity60_v3', 
        'HLT_PixelTracks_Multiplicity85_v1', 
        'HLT_PixelTracks_Multiplicity85_v2', 
        'HLT_PixelTracks_Multiplicity110_v1', 
        'HLT_PixelTracks_Multiplicity110_v2', 
        'HLT_PixelTracks_Multiplicity135_v1', 
        'HLT_PixelTracks_Multiplicity135_v2', 
        'HLT_PixelTracks_Multiplicity160_v1', 
        'HLT_PixelTracks_Multiplicity160_v2', 
        'HLT_Physics_v1', 
        'HLT_Physics_v2', 
        'HLT_Random_v1', 
        'HLT_EcalCalibration_v1', 
        'HLT_HcalCalibration_v1', 
        'HLT_L1Tech6_BPTX_MinusOnly_v1', 
        'HLT_L1Tech5_BPTX_PlusOnly_v1', 
        'HLT_L1Tech5_BPTX_PlusOnly_v2', 
        'HLT_L1Tech7_NoBPTX_v1', 
        'HLT_L1TOTEM1_MinBias_v1', 
        'HLT_L1TOTEM2_ZeroBias_v1', 
        'HLT_L1MinimumBiasHF1OR_v1', 
        'HLT_L1MinimumBiasHF2OR_v1', 
        'HLT_L1MinimumBiasHF1AND_v1', 
        'HLT_L1MinimumBiasHF2AND_v1', 
        'HLT_L1MinimumBiasHF2ORNoBptxGating_v1', 
        'HLT_ZeroBias_v1', 
        'HLT_ZeroBias_v2', 
        'HLT_ZeroBias_part0_v1', 
        'HLT_ZeroBias_part0_v2', 
        'HLT_ZeroBias_part1_v1', 
        'HLT_ZeroBias_part1_v2', 
        'HLT_ZeroBias_part2_v1', 
        'HLT_ZeroBias_part2_v2', 
        'HLT_ZeroBias_part3_v1', 
        'HLT_ZeroBias_part3_v2', 
        'HLT_ZeroBias_part4_v1', 
        'HLT_ZeroBias_part4_v2', 
        'HLT_ZeroBias_part5_v1', 
        'HLT_ZeroBias_part5_v2', 
        'HLT_ZeroBias_part6_v1', 
        'HLT_ZeroBias_part6_v2', 
        'HLT_ZeroBias_part7_v1', 
        'HLT_ZeroBias_part7_v2', 
        'HLT_ZeroBias_part8_v1', 
        'HLT_ZeroBias_part8_v2', 
        'HLT_ZeroBias_part9_v1', 
        'HLT_ZeroBias_part9_v2', 
        'HLT_ZeroBias_part10_v1', 
        'HLT_ZeroBias_part10_v2', 
        'HLT_ZeroBias_part11_v1', 
        'HLT_ZeroBias_part11_v2', 
        'HLT_ZeroBias_part12_v1', 
        'HLT_ZeroBias_part12_v2', 
        'HLT_ZeroBias_part13_v1', 
        'HLT_ZeroBias_part13_v2', 
        'HLT_ZeroBias_part14_v1', 
        'HLT_ZeroBias_part14_v2', 
        'HLT_ZeroBias_part15_v1', 
        'HLT_ZeroBias_part15_v2', 
        'HLT_ZeroBias_part16_v1', 
        'HLT_ZeroBias_part16_v2', 
        'HLT_ZeroBias_part17_v1', 
        'HLT_ZeroBias_part17_v2', 
        'HLT_ZeroBias_part18_v1', 
        'HLT_ZeroBias_part18_v2', 
        'HLT_ZeroBias_part19_v1', 
        'HLT_ZeroBias_part19_v2', 
        'HLT_AK4CaloJet40_Eta5p1_v1', 
        'HLT_AK4CaloJet60_Eta5p1_v1', 
        'HLT_AK4CaloJet80_Eta5p1_v1', 
        'HLT_AK4CaloJet100_Eta5p1_v1', 
        'HLT_AK4CaloJet110_Eta5p1_v1', 
        'HLT_AK4CaloJet120_Eta5p1_v1', 
        'HLT_AK4CaloJet150_v1', 
        'HLT_AK4PFJet40_Eta5p1_v1', 
        'HLT_AK4PFJet60_Eta5p1_v1', 
        'HLT_AK4PFJet80_Eta5p1_v1', 
        'HLT_AK4PFJet100_Eta5p1_v1', 
        'HLT_AK4PFJet110_Eta5p1_v1', 
        'HLT_AK4PFJet120_Eta5p1_v1', 
        'HLT_AK4CaloJet80_Jet35_Eta1p1_v1', 
        'HLT_AK4CaloJet80_Jet35_Eta0p7_v1', 
        'HLT_AK4CaloJet100_Jet35_Eta1p1_v1', 
        'HLT_AK4CaloJet100_Jet35_Eta0p7_v1', 
        'HLT_AK4CaloJet80_45_45_Eta2p1_v1', 
        'HLT_HISinglePhoton10_Eta1p5_v1', 
        'HLT_HISinglePhoton15_Eta1p5_v1', 
        'HLT_HISinglePhoton20_Eta1p5_v1', 
        'HLT_HISinglePhoton30_Eta1p5_v1', 
        'HLT_HISinglePhoton40_Eta1p5_v1', 
        'HLT_HISinglePhoton50_Eta1p5_v1', 
        'HLT_HISinglePhoton60_Eta1p5_v1', 
        'HLT_HISinglePhoton10_Eta3p1_v1', 
        'HLT_HISinglePhoton15_Eta3p1_v1', 
        'HLT_HISinglePhoton20_Eta3p1_v1', 
        'HLT_HISinglePhoton30_Eta3p1_v1', 
        'HLT_HISinglePhoton40_Eta3p1_v1', 
        'HLT_HISinglePhoton50_Eta3p1_v1', 
        'HLT_HISinglePhoton60_Eta3p1_v1', 
        'HLT_HIDoublePhoton15_Eta1p5_Mass50_1000_v1', 
        'HLT_HIDoublePhoton15_Eta1p5_Mass50_1000_R9HECut_v1', 
        'HLT_HIDoublePhoton15_Eta2p1_Mass50_1000_R9Cut_v1', 
        'HLT_HIDoublePhoton15_Eta2p5_Mass50_1000_R9SigmaHECut_v1', 
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet40Eta2p1_v1', 
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet60Eta2p1_v1', 
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet80Eta2p1_v1', 
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet100Eta2p1_v1', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton10Eta1p5_v1', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton15Eta1p5_v1', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton20Eta1p5_v1', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton30Eta1p5_v1', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton40Eta1p5_v1', 
        'HLT_HIL1DoubleMu0_v1', 
        'HLT_HIL1DoubleMu10_v1', 
        'HLT_HIL2DoubleMu0_NHitQ_v1', 
        'HLT_HIL3DoubleMu0_OS_m2p5to4p5_v1', 
        'HLT_HIL3DoubleMu0_OS_m7to14_v1', 
        'HLT_HIL2Mu3_NHitQ10_v1', 
        'HLT_HIL3Mu3_NHitQ15_v1', 
        'HLT_HIL2Mu5_NHitQ10_v1', 
        'HLT_HIL3Mu5_NHitQ15_v1', 
        'HLT_HIL2Mu7_NHitQ10_v1', 
        'HLT_HIL3Mu7_NHitQ15_v1', 
        'HLT_HIL2Mu15_v1', 
        'HLT_HIL3Mu15_v1', 
        'HLT_HIL2Mu20_v1', 
        'HLT_HIL3Mu20_v1', 
        'HLT_FullTrack18ForPPRef_v1', 
        'HLT_FullTrack18ForPPRef_v2', 
        'HLT_FullTrack18ForPPRef_v3', 
        'HLT_FullTrack24ForPPRef_v1', 
        'HLT_FullTrack24ForPPRef_v2', 
        'HLT_FullTrack24ForPPRef_v3', 
        'HLT_FullTrack34ForPPRef_v1', 
        'HLT_FullTrack34ForPPRef_v2', 
        'HLT_FullTrack34ForPPRef_v3', 
        'HLT_FullTrack34ForPPRef_v4', 
        'HLT_FullTrack45ForPPRef_v1', 
        'HLT_FullTrack45ForPPRef_v2', 
        'HLT_FullTrack45ForPPRef_v3', 
        'HLT_FullTrack53ForPPRef_v1', 
        'HLT_FullTrack53ForPPRef_v2', 
        'HLT_FullTrack53ForPPRef_v3', 
        'HLT_HIUPCL1DoubleMuOpenNotHF2_v1', 
        'HLT_HIUPCDoubleMuNotHF2Pixel_SingleTrack_v1', 
        'HLT_HIUPCL1MuOpen_NotMinimumBiasHF2_AND_v1', 
        'HLT_HIUPCMuOpen_NotMinimumBiasHF2_ANDPixel_SingleTrack_v1', 
        'HLT_HIUPCL1NotMinimumBiasHF2_AND_v1', 
        'HLT_HIUPCNotMinimumBiasHF2_ANDPixel_SingleTrack_v1', 
        'HLT_HIUPCL1ZdcOR_BptxAND_v1', 
        'HLT_HIUPCZdcOR_BptxANDPixel_SingleTrack_v1', 
        'HLT_HIUPCL1ZdcXOR_BptxAND_v1', 
        'HLT_HIUPCZdcXOR_BptxANDPixel_SingleTrack_v1', 
        'HLT_HIUPCL1NotZdcOR_BptxAND_v1', 
        'HLT_HIUPCNotZdcOR_BptxANDPixel_SingleTrack_v1', 
        'HLT_HIL1CastorMediumJet_v1', 
        'HLT_HICastorMediumJetPixel_SingleTrack_v1', 
        'HLT_DmesonPPTrackingGlobal_Dpt8_v1', 
        'HLT_DmesonPPTrackingGlobal_Dpt15_v1', 
        'HLT_DmesonPPTrackingGlobal_Dpt20_v1', 
        'HLT_DmesonPPTrackingGlobal_Dpt30_v1', 
        'HLT_DmesonPPTrackingGlobal_Dpt40_v1', 
        'HLT_DmesonPPTrackingGlobal_Dpt50_v1', 
        'HLT_DmesonPPTrackingGlobal_Dpt60_v1', 
        'HLT_L1MinimumBiasHF1OR_part0_v1', 
        'HLT_L1MinimumBiasHF1OR_part1_v1', 
        'HLT_L1MinimumBiasHF1OR_part2_v1', 
        'HLT_L1MinimumBiasHF1OR_part3_v1', 
        'HLT_L1MinimumBiasHF1OR_part4_v1', 
        'HLT_L1MinimumBiasHF1OR_part5_v1', 
        'HLT_L1MinimumBiasHF1OR_part6_v1', 
        'HLT_L1MinimumBiasHF1OR_part7_v1', 
        'HLT_L1MinimumBiasHF1OR_part8_v1', 
        'HLT_L1MinimumBiasHF1OR_part9_v1', 
        'HLT_L1MinimumBiasHF1OR_part10_v1', 
        'HLT_L1MinimumBiasHF1OR_part11_v1', 
        'HLT_L1MinimumBiasHF1OR_part12_v1', 
        'HLT_L1MinimumBiasHF1OR_part13_v1', 
        'HLT_L1MinimumBiasHF1OR_part14_v1', 
        'HLT_L1MinimumBiasHF1OR_part15_v1', 
        'HLT_L1MinimumBiasHF1OR_part16_v1', 
        'HLT_L1MinimumBiasHF1OR_part17_v1', 
        'HLT_L1MinimumBiasHF1OR_part18_v1', 
        'HLT_L1MinimumBiasHF1OR_part19_v1', 
        'HLT_AK4PFBJetBCSV60_Eta2p1_v1', 
        'HLT_AK4PFBJetBCSV80_Eta2p1_v1', 
        'HLT_AK4PFDJet60_Eta2p1_v1', 
        'HLT_AK4PFDJet80_Eta2p1_v1', 
        'HLT_AK4PFBJetBSSV60_Eta2p1_v1', 
        'HLT_AK4PFBJetBSSV80_Eta2p1_v1'),
    hltresults = cms.InputTag("TriggerResults","","HLT"),
    l1GctHFBitCounts = cms.InputTag("gctDigis"),
    l1GctHFRingSums = cms.InputTag("gctDigis"),
    l1GtObjectMapRecord = cms.InputTag("hltL1GtObjectMap","","HLT"),
    l1GtReadoutRecord = cms.InputTag("gtDigis"),
    l1extramc = cms.string('l1extraParticles'),
    l1extramu = cms.string('l1extraParticles')
)


process.hltbitanalysis = cms.EDAnalyzer("HLTBitAnalyzer",
    HLTProcessName = cms.string('HLT'),
    RunParameters = cms.PSet(
        HistogramFile = cms.untracked.string('hltbitanalysis.root')
    ),
    UseTFileService = cms.untracked.bool(True),
    hltresults = cms.InputTag("TriggerResults","","HLT"),
    l1GctHFBitCounts = cms.InputTag("hltGctDigis"),
    l1GctHFRingSums = cms.InputTag("hltGctDigis"),
    l1GtObjectMapRecord = cms.InputTag("hltL1GtObjectMap","","HLT"),
    l1GtReadoutRecord = cms.InputTag("hltGtDigis","","HLT"),
    l1extramc = cms.string('hltL1extraParticles'),
    l1extramu = cms.string('hltL1extraParticles')
)


process.hltobject = cms.EDAnalyzer("TriggerObjectAnalyzer",
    processName = cms.string('HLT'),
    treeName = cms.string('JetTriggers'),
    triggerEvent = cms.InputTag("hltTriggerSummaryAOD","","HLT"),
    triggerNames = cms.vstring('HLT_AK4CaloJet100_Eta5p1_v', 
        'HLT_AK4CaloJet100_Jet35_Eta0p7_v', 
        'HLT_AK4CaloJet100_Jet35_Eta1p1_v', 
        'HLT_AK4CaloJet110_Eta5p1_v', 
        'HLT_AK4CaloJet120_Eta5p1_v', 
        'HLT_AK4CaloJet150_v', 
        'HLT_AK4CaloJet40_Eta5p1_v', 
        'HLT_AK4CaloJet60_Eta5p1_v', 
        'HLT_AK4CaloJet80_45_45_Eta2p1_v', 
        'HLT_AK4CaloJet80_Eta5p1_v', 
        'HLT_AK4CaloJet80_Jet35_Eta0p7_v', 
        'HLT_AK4CaloJet80_Jet35_Eta1p1_v', 
        'HLT_AK4PFBJetBCSV60_Eta2p1_v', 
        'HLT_AK4PFBJetBCSV80_Eta2p1_v', 
        'HLT_AK4PFBJetBSSV60_Eta2p1_v', 
        'HLT_AK4PFBJetBSSV80_Eta2p1_v', 
        'HLT_AK4PFDJet60_Eta2p1_v', 
        'HLT_AK4PFDJet80_Eta2p1_v', 
        'HLT_AK4PFJet100_Eta5p1_v', 
        'HLT_AK4PFJet110_Eta5p1_v', 
        'HLT_AK4PFJet120_Eta5p1_v', 
        'HLT_AK4PFJet40_Eta5p1_v', 
        'HLT_AK4PFJet60_Eta5p1_v', 
        'HLT_AK4PFJet80_Eta5p1_v', 
        'HLT_HIL1DoubleMu0_v', 
        'HLT_HIL1DoubleMu10_v', 
        'HLT_HIL2DoubleMu0_NHitQ_v', 
        'HLT_HIL2Mu15_v', 
        'HLT_HIL2Mu20_v', 
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet100Eta2p1_v', 
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet40Eta2p1_v', 
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet60Eta2p1_v', 
        'HLT_HIL2Mu3Eta2p5_AK4CaloJet80Eta2p1_v', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton10Eta1p5_v', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton15Eta1p5_v', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton20Eta1p5_v', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton30Eta1p5_v', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton40Eta1p5_v', 
        'HLT_HIL2Mu3_NHitQ10_v', 
        'HLT_HIL2Mu5_NHitQ10_v', 
        'HLT_HIL2Mu7_NHitQ10_v', 
        'HLT_HIL3DoubleMu0_OS_m2p5to4p5_v', 
        'HLT_HIL3DoubleMu0_OS_m7to14_v', 
        'HLT_HIL3Mu15_v', 
        'HLT_HIL3Mu20_v', 
        'HLT_HIL3Mu3_NHitQ15_v', 
        'HLT_HIL3Mu5_NHitQ15_v', 
        'HLT_HIL3Mu7_NHitQ15_v', 
        'HLT_HISinglePhoton10_Eta1p5_v', 
        'HLT_HISinglePhoton10_Eta3p1_v', 
        'HLT_HISinglePhoton15_Eta1p5_v', 
        'HLT_HISinglePhoton15_Eta3p1_v', 
        'HLT_HISinglePhoton20_Eta1p5_v', 
        'HLT_HISinglePhoton20_Eta3p1_v', 
        'HLT_HISinglePhoton30_Eta1p5_v', 
        'HLT_HISinglePhoton30_Eta3p1_v', 
        'HLT_HISinglePhoton40_Eta1p5_v', 
        'HLT_HISinglePhoton40_Eta3p1_v', 
        'HLT_HISinglePhoton50_Eta1p5_v', 
        'HLT_HISinglePhoton50_Eta3p1_v', 
        'HLT_HISinglePhoton60_Eta1p5_v', 
        'HLT_HISinglePhoton60_Eta3p1_v', 
        'HLT_FullTrack18ForPPRef_v', 
        'HLT_FullTrack24ForPPRef_v', 
        'HLT_FullTrack34ForPPRef_v', 
        'HLT_FullTrack45ForPPRef_v', 
        'HLT_DmesonPPTrackingGlobal_Dpt8_v', 
        'HLT_DmesonPPTrackingGlobal_Dpt15_v', 
        'HLT_DmesonPPTrackingGlobal_Dpt20_v', 
        'HLT_DmesonPPTrackingGlobal_Dpt30_v', 
        'HLT_DmesonPPTrackingGlobal_Dpt40_v', 
        'HLT_DmesonPPTrackingGlobal_Dpt50_v', 
        'HLT_DmesonPPTrackingGlobal_Dpt60_v'),
    triggerResults = cms.InputTag("TriggerResults","","HLT")
)


process.inclusiveJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    doGenSym = cms.untracked.bool(False),
    doGenTaus = cms.untracked.bool(False),
    doHiJetID = cms.untracked.bool(True),
    doJetConstituents = cms.untracked.bool(False),
    doLifeTimeTagging = cms.untracked.bool(False),
    doNewJetVars = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(False),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genjetTag = cms.InputTag("iterativeCone5HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HLT'),
    isMC = cms.untracked.bool(False),
    jetIDWeight = cms.untracked.string('HeavyIonsAnalysis/JetAnalysis/data/JetID_TMVAClassification_BDTG_weights.xml'),
    jetPtMin = cms.double(5.0),
    jetTag = cms.InputTag("icPu5patJets"),
    matchTag = cms.untracked.InputTag("akPu3PFpatJets"),
    rParam = cms.double(0.5),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.pixelTrack = cms.EDAnalyzer("TrackAnalyzer",
    associatorMap = cms.InputTag("tpRecoAssocHiGeneralTracks"),
    beamSpotSrc = cms.untracked.InputTag("offlineBeamSpot"),
    doMVA = cms.untracked.bool(True),
    doPFMatching = cms.untracked.bool(True),
    doSimTrack = cms.untracked.bool(False),
    doSimVertex = cms.untracked.bool(False),
    fillSimTrack = cms.untracked.bool(False),
    mvaSrc = cms.InputTag("hiGeneralTracks","MVAVals"),
    particleSrc = cms.InputTag("genParticles"),
    pfCandSrc = cms.InputTag("particleFlowTmp"),
    qualityString = cms.untracked.string('highPurity'),
    qualityStrings = cms.untracked.vstring('highPurity'),
    simTrackPtMin = cms.untracked.double(0.4),
    tpEffSrc = cms.untracked.InputTag("mix","MergedTrackTruth"),
    tpFakeSrc = cms.untracked.InputTag("mix","MergedTrackTruth"),
    trackPtMin = cms.untracked.double(0.4),
    trackSrc = cms.InputTag("hiGeneralAndPixelTracks"),
    useQuality = cms.untracked.bool(False),
    vertexSrc = cms.vstring('hiSelectedVertex')
)


process.ppTrack = cms.EDAnalyzer("TrackAnalyzer",
    associatorMap = cms.InputTag("tpRecoAssocHiGeneralTracks"),
    beamSpotSrc = cms.untracked.InputTag("offlineBeamSpot"),
    doMVA = cms.untracked.bool(True),
    doPFMatching = cms.untracked.bool(True),
    doSimTrack = cms.untracked.bool(False),
    doSimVertex = cms.untracked.bool(False),
    fillSimTrack = cms.untracked.bool(False),
    mvaSrc = cms.InputTag("generalTracks","MVAVals"),
    particleSrc = cms.InputTag("genParticles"),
    pfCandSrc = cms.InputTag("particleFlow"),
    qualityString = cms.untracked.string('highPurity'),
    qualityStrings = cms.untracked.vstring('highPurity', 
        'tight', 
        'loose'),
    simTrackPtMin = cms.untracked.double(0.4),
    tpEffSrc = cms.untracked.InputTag("mix","MergedTrackTruth"),
    tpFakeSrc = cms.untracked.InputTag("mix","MergedTrackTruth"),
    trackPtMin = cms.untracked.double(0.49),
    trackSrc = cms.InputTag("generalTracks"),
    useQuality = cms.untracked.bool(False),
    vertexSrc = cms.vstring('offlinePrimaryVertices')
)


process.skimanalysis = cms.EDAnalyzer("FilterAnalyzer",
    hltresults = cms.InputTag("TriggerResults","","HiForest"),
    superFilters = cms.vstring('')
)


process.tupel = cms.EDAnalyzer("Tupel",
    CalojetLabel = cms.untracked.InputTag("ak4CalopatJets"),
    elecMatch = cms.string('elecTriggerMatchHLTElecs'),
    electronSrc = cms.untracked.InputTag("patElectrons"),
    genSrc = cms.untracked.InputTag("genParticles"),
    gjetSrc = cms.untracked.InputTag("ak4GenJets"),
    jetSrc = cms.untracked.InputTag("ak4PFpatJetsWithBtagging"),
    lheSource = cms.untracked.InputTag("source"),
    metSource = cms.VInputTag("slimmedMETs", "slimmedMETs", "slimmedMETs", "slimmedMETs"),
    metSrc = cms.untracked.InputTag("patMETsPF"),
    muonMatch = cms.string('muonTriggerMatchHLTMuons'),
    muonMatch2 = cms.string('muonTriggerMatchHLTMuons2'),
    muonSrc = cms.untracked.InputTag("patMuonsWithTrigger"),
    photonSrc = cms.untracked.InputTag("patPhotons"),
    trigger = cms.InputTag("patTrigger"),
    vtxSrc = cms.untracked.InputTag("offlinePrimaryVertices")
)


process.patTriggerMatchers1Mu = cms.Sequence(process.muonMatchHLTL2+process.muonMatchHLTL3+process.muonMatchHLTL3T)


process.ak4CaloJetBtaggingMu = cms.Sequence(process.ak4CaloSoftPFMuonsTagInfos+process.ak4CaloSoftPFMuonBJetTags+process.ak4CaloSoftPFMuonByIP3dBJetTags+process.ak4CaloSoftPFMuonByPtBJetTags+process.ak4CaloNegativeSoftPFMuonByPtBJetTags+process.ak4CaloPositiveSoftPFMuonByPtBJetTags)


process.trackSequencesPbPb = cms.Sequence(process.anaTrack)


process.patJetFlavourIdLegacy = cms.Sequence(process.patJetPartonsLegacy+process.patJetPartonAssociationLegacy+process.patJetFlavourAssociationLegacy)


process.ak4PFJetBtaggingIP = cms.Sequence(process.ak4PFImpactParameterTagInfos+process.ak4PFTrackCountingHighEffBJetTags+process.ak4PFTrackCountingHighPurBJetTags+process.ak4PFJetProbabilityBJetTags+process.ak4PFJetBProbabilityBJetTags)


process.patJetFlavourId = cms.Sequence(process.patJetPartons+process.patJetFlavourAssociation)


process.ak5JTA = cms.Sequence(process.ak5JetTracksAssociatorAtVertexPF+process.ak5JetTracksAssociatorAtVertex+process.ak5JetTracksAssociatorAtCaloFace+process.ak5JetExtender)


process.ak4PFJetBtaggingNegSV = cms.Sequence(process.ak4PFImpactParameterTagInfos+process.ak4PFSecondaryVertexNegativeTagInfos+process.ak4PFNegativeSimpleSecondaryVertexHighEffBJetTags+process.ak4PFNegativeSimpleSecondaryVertexHighPurBJetTags+process.ak4PFNegativeCombinedSecondaryVertexBJetTags+process.ak4PFPositiveCombinedSecondaryVertexBJetTags+process.ak4PFNegativeCombinedSecondaryVertexV2BJetTags+process.ak4PFPositiveCombinedSecondaryVertexV2BJetTags)


process.ak4CaloJetBtaggingIP = cms.Sequence(process.ak4CaloImpactParameterTagInfos+process.ak4CaloTrackCountingHighEffBJetTags+process.ak4CaloTrackCountingHighPurBJetTags+process.ak4CaloJetProbabilityBJetTags+process.ak4CaloJetBProbabilityBJetTags)


process.inclusiveCandidateVertexing = cms.Sequence(process.inclusiveCandidateVertexFinder+process.candidateVertexMerger+process.candidateVertexArbitrator+process.inclusiveCandidateSecondaryVertices)


process.ak4PFJetBtaggingMu = cms.Sequence(process.ak4PFSoftPFMuonsTagInfos+process.ak4PFSoftPFMuonBJetTags+process.ak4PFSoftPFMuonByIP3dBJetTags+process.ak4PFSoftPFMuonByPtBJetTags+process.ak4PFNegativeSoftPFMuonByPtBJetTags+process.ak4PFPositiveSoftPFMuonByPtBJetTags)


process.akSoftDrop4PFPatJetFlavourId = cms.Sequence(process.akSoftDrop4PFPatJetPartons+process.akSoftDrop4PFPatJetFlavourAssociation)


process.akSoftDrop4PFJetBtaggingSV = cms.Sequence(process.akSoftDrop4PFImpactParameterTagInfos+process.akSoftDrop4PFSecondaryVertexTagInfos+process.akSoftDrop4PFSimpleSecondaryVertexHighEffBJetTags+process.akSoftDrop4PFSimpleSecondaryVertexHighPurBJetTags+process.akSoftDrop4PFCombinedSecondaryVertexBJetTags+process.akSoftDrop4PFCombinedSecondaryVertexV2BJetTags+process.akSoftDrop4PFSubjetJetTracksAssociatorAtVertex+process.akSoftDrop4PFSubjetImpactParameterTagInfos+process.akSoftDrop4PFSubjetJetProbabilityBJetTags+process.akSoftDrop4PFSubjetSecondaryVertexTagInfos+process.akSoftDrop4PFCombinedSubjetSecondaryVertexV2BJetTags+process.akSoftDrop4PFSubjetSecondaryVertexNegativeTagInfos+process.akSoftDrop4PFCombinedSubjetNegativeSecondaryVertexV2BJetTags)


process.ak4CaloJetBtaggingNegSV = cms.Sequence(process.ak4CaloImpactParameterTagInfos+process.ak4CaloSecondaryVertexNegativeTagInfos+process.ak4CaloNegativeSimpleSecondaryVertexHighEffBJetTags+process.ak4CaloNegativeSimpleSecondaryVertexHighPurBJetTags+process.ak4CaloNegativeCombinedSecondaryVertexBJetTags+process.ak4CaloPositiveCombinedSecondaryVertexBJetTags+process.ak4CaloNegativeCombinedSecondaryVertexV2BJetTags+process.ak4CaloPositiveCombinedSecondaryVertexV2BJetTags)


process.pfBTagging = cms.Sequence(process.pfImpactParameterTagInfos+process.pfTrackCountingHighEffBJetTags+process.pfTrackCountingHighPurBJetTags+process.pfJetProbabilityBJetTags+process.pfJetBProbabilityBJetTags+process.pfSecondaryVertexTagInfos+process.pfSimpleSecondaryVertexHighEffBJetTags+process.pfSimpleSecondaryVertexHighPurBJetTags+process.pfCombinedSecondaryVertexBJetTags+process.pfCombinedSecondaryVertexV2BJetTags+process.inclusiveCandidateVertexing+process.pfInclusiveSecondaryVertexFinderTagInfos+process.pfCombinedInclusiveSecondaryVertexV2BJetTags+process.softPFMuonsTagInfos+process.softPFMuonBJetTags+process.softPFElectronsTagInfos+process.softPFElectronBJetTags+process.pfCombinedMVABJetTags+process.pfCombinedSecondaryVertexSoftLeptonBJetTags)


process.ak3PFJetBtaggingIP = cms.Sequence(process.ak3PFImpactParameterTagInfos+process.ak3PFTrackCountingHighEffBJetTags+process.ak3PFTrackCountingHighPurBJetTags+process.ak3PFJetProbabilityBJetTags+process.ak3PFJetBProbabilityBJetTags)


process.ak4CaloJetBtaggingSV = cms.Sequence(process.ak4CaloImpactParameterTagInfos+process.ak4CaloSecondaryVertexTagInfos+process.ak4CaloSimpleSecondaryVertexHighEffBJetTags+process.ak4CaloSimpleSecondaryVertexHighPurBJetTags+process.ak4CaloCombinedSecondaryVertexBJetTags+process.ak4CaloCombinedSecondaryVertexV2BJetTags)


process.ak3PFJetBtaggingMu = cms.Sequence(process.ak3PFSoftPFMuonsTagInfos+process.ak3PFSoftPFMuonBJetTags+process.ak3PFSoftPFMuonByIP3dBJetTags+process.ak3PFSoftPFMuonByPtBJetTags+process.ak3PFNegativeSoftPFMuonByPtBJetTags+process.ak3PFPositiveSoftPFMuonByPtBJetTags)


process.ak4PFPatJetFlavourIdLegacy = cms.Sequence(process.ak4PFPatJetPartonAssociationLegacy+process.ak4PFPatJetFlavourAssociationLegacy)


process.hfCoincFilter4 = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter4+process.hfNegFilter4)


process.hfCoincFilter5 = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter5+process.hfNegFilter5)


process.hfCoincFilter2 = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter2+process.hfNegFilter2)


process.hfCoincFilter3 = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter3+process.hfNegFilter3)


process.patTriggerMatchers2Mu = cms.Sequence(process.muonMatchHLTCtfTrack+process.muonMatchHLTCtfTrack2+process.muonMatchHLTTrackMu)


process.ak4CaloPatJetFlavourId = cms.Sequence(process.ak4CaloPatJetPartons+process.ak4CaloPatJetFlavourAssociation)


process.ak3PFPatJetFlavourId = cms.Sequence(process.ak3PFPatJetPartons+process.ak3PFPatJetFlavourAssociation)


process.inclusiveCandidateVertexingCtagL = cms.Sequence(process.inclusiveCandidateVertexFinderCtagL+process.candidateVertexMergerCtagL+process.candidateVertexArbitratorCtagL+process.inclusiveCandidateSecondaryVerticesCtagL)


process.ak4CaloPatJetFlavourIdLegacy = cms.Sequence(process.ak4CaloPatJetPartonAssociationLegacy+process.ak4CaloPatJetFlavourAssociationLegacy)


process.hfCoincFilter = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter+process.hfNegFilter)


process.hfnegTowers = cms.Sequence(process.towersAboveThreshold+process.hfNegTowers)


process.hfnegFilter2 = cms.Sequence(process.hfnegTowers+process.hfNegFilter2)


process.hfnegFilter3 = cms.Sequence(process.hfnegTowers+process.hfNegFilter3)


process.akSoftDrop4PFJetBtaggingMu = cms.Sequence(process.akSoftDrop4PFSoftPFMuonsTagInfos+process.akSoftDrop4PFSoftPFMuonBJetTags+process.akSoftDrop4PFSoftPFMuonByIP3dBJetTags+process.akSoftDrop4PFSoftPFMuonByPtBJetTags+process.akSoftDrop4PFNegativeSoftPFMuonByPtBJetTags+process.akSoftDrop4PFPositiveSoftPFMuonByPtBJetTags)


process.hfnegFilter4 = cms.Sequence(process.hfnegTowers+process.hfNegFilter4)


process.hfnegFilter5 = cms.Sequence(process.hfnegTowers+process.hfNegFilter5)


process.inclusiveVertexing = cms.Sequence(process.inclusiveVertexFinder+process.vertexMerger+process.trackVertexArbitrator+process.inclusiveSecondaryVertices)


process.legacyBTagging = cms.Sequence(process.impactParameterTagInfos+process.trackCountingHighEffBJetTags+process.trackCountingHighPurBJetTags+process.jetProbabilityBJetTags+process.jetBProbabilityBJetTags+process.secondaryVertexTagInfos+process.simpleSecondaryVertexHighEffBJetTags+process.simpleSecondaryVertexHighPurBJetTags+process.combinedSecondaryVertexBJetTags+process.inclusiveSecondaryVertexFinderTagInfos+process.combinedInclusiveSecondaryVertexV2BJetTags+process.ghostTrackVertexTagInfos+process.ghostTrackBJetTags+process.softPFMuonsTagInfos+process.softPFMuonBJetTags+process.softPFElectronsTagInfos+process.softPFElectronBJetTags+process.combinedMVABJetTags)


process.hfnegFilter = cms.Sequence(process.hfnegTowers+process.hfNegFilter)


process.patElectronSequence = cms.Sequence(process.patElectrons)


process.ak3PFJetBtaggingSV = cms.Sequence(process.ak3PFImpactParameterTagInfos+process.ak3PFSecondaryVertexTagInfos+process.ak3PFSimpleSecondaryVertexHighEffBJetTags+process.ak3PFSimpleSecondaryVertexHighPurBJetTags+process.ak3PFCombinedSecondaryVertexBJetTags+process.ak3PFCombinedSecondaryVertexV2BJetTags)


process.patPhotonSequence = cms.Sequence(process.patPhotons)


process.akSoftDrop4PFPatJetFlavourIdLegacy = cms.Sequence(process.akSoftDrop4PFPatJetPartonAssociationLegacy+process.akSoftDrop4PFPatJetFlavourAssociationLegacy)


process.ak4PFJetBtaggingSV = cms.Sequence(process.ak4PFImpactParameterTagInfos+process.ak4PFSecondaryVertexTagInfos+process.ak4PFSimpleSecondaryVertexHighEffBJetTags+process.ak4PFSimpleSecondaryVertexHighPurBJetTags+process.ak4PFCombinedSecondaryVertexBJetTags+process.ak4PFCombinedSecondaryVertexV2BJetTags)


process.ak5JTAExplicit = cms.Sequence(process.ak5JetTracksAssociatorExplicit)


process.ak3PFJetBtaggingNegSV = cms.Sequence(process.ak3PFImpactParameterTagInfos+process.ak3PFSecondaryVertexNegativeTagInfos+process.ak3PFNegativeSimpleSecondaryVertexHighEffBJetTags+process.ak3PFNegativeSimpleSecondaryVertexHighPurBJetTags+process.ak3PFNegativeCombinedSecondaryVertexBJetTags+process.ak3PFPositiveCombinedSecondaryVertexBJetTags+process.ak3PFNegativeCombinedSecondaryVertexV2BJetTags+process.ak3PFPositiveCombinedSecondaryVertexV2BJetTags)


process.egmGsfElectronIDSequence = cms.Sequence(process.electronMVAValueMapProducer+process.egmGsfElectronIDs+process.electronRegressionValueMapProducer)


process.akSoftDrop4PFJetBtaggingNegSV = cms.Sequence(process.akSoftDrop4PFImpactParameterTagInfos+process.akSoftDrop4PFSecondaryVertexNegativeTagInfos+process.akSoftDrop4PFNegativeSimpleSecondaryVertexHighEffBJetTags+process.akSoftDrop4PFNegativeSimpleSecondaryVertexHighPurBJetTags+process.akSoftDrop4PFNegativeCombinedSecondaryVertexBJetTags+process.akSoftDrop4PFPositiveCombinedSecondaryVertexBJetTags+process.akSoftDrop4PFNegativeCombinedSecondaryVertexV2BJetTags+process.akSoftDrop4PFPositiveCombinedSecondaryVertexV2BJetTags)


process.hfposTowers = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers)


process.ak4PFPatJetFlavourId = cms.Sequence(process.ak4PFPatJetPartons+process.ak4PFPatJetFlavourAssociation)


process.ak4CaloJetBtagging = cms.Sequence(process.ak4CaloJetBtaggingIP+process.ak4CaloJetBtaggingSV+process.ak4CaloJetBtaggingNegSV)


process.akSoftDrop4PFJetBtaggingIP = cms.Sequence(process.akSoftDrop4PFImpactParameterTagInfos+process.akSoftDrop4PFTrackCountingHighEffBJetTags+process.akSoftDrop4PFTrackCountingHighPurBJetTags+process.akSoftDrop4PFJetProbabilityBJetTags+process.akSoftDrop4PFJetBProbabilityBJetTags)


process.akSoftDrop4PFJetBtagging = cms.Sequence(process.akSoftDrop4PFJetBtaggingIP+process.akSoftDrop4PFJetBtaggingSV+process.akSoftDrop4PFJetBtaggingNegSV)


process.trackSequencesPP = cms.Sequence(process.ppTrack)


process.ak3PFPatJetFlavourIdLegacy = cms.Sequence(process.ak3PFPatJetPartonAssociationLegacy+process.ak3PFPatJetFlavourAssociationLegacy)


process.patTriggerMatching = cms.Sequence(process.patTriggerFull+process.patTrigger+process.patTriggerMatchers1Mu+process.patTriggerMatchers2Mu+process.patMuonsWithTrigger)


process.patMuonsWithTriggerSequence = cms.Sequence(process.muonL1Info+process.patMuonsWithoutTrigger+process.patTriggerMatching)


process.ak3PFJetBtagging = cms.Sequence(process.ak3PFJetBtaggingIP+process.ak3PFJetBtaggingSV+process.ak3PFJetBtaggingNegSV)


process.ak3PFJetSequence_mc = cms.Sequence(process.ak3PFmatch+process.ak3PFparton+process.ak3PFcorr+process.ak3PFPatJetFlavourId+process.ak3PFJetTracksAssociatorAtVertex+process.ak3PFJetBtagging+process.ak3PFNjettiness+process.ak3PFpatJetsWithBtagging+process.ak3PFJetAnalyzer)


process.tupelPatSequence = cms.Sequence(process.patMuonsWithTriggerSequence+process.patPhotonSequence+process.patElectronSequence+process.tupel)


process.pfCTagging = cms.Sequence(process.inclusiveCandidateVertexingCtagL+process.pfInclusiveSecondaryVertexFinderCtagLTagInfos+process.pfCombinedSecondaryVertexSoftLeptonCtagLJetTags)


process.hfposFilter = cms.Sequence(process.hfposTowers+process.hfPosFilter)


process.btagging = cms.Sequence(process.legacyBTagging+process.pfBTagging)


process.ak4CaloJetSequence_mc = cms.Sequence(process.ak4Calomatch+process.ak4Caloparton+process.ak4Calocorr+process.ak4CaloPatJetFlavourId+process.ak4CaloJetTracksAssociatorAtVertex+process.ak4CaloJetBtagging+process.ak4CaloNjettiness+process.ak4CalopatJetsWithBtagging+process.ak4CaloJetAnalyzer)


process.ak4CaloJetSequence_data = cms.Sequence(process.ak4Calocorr+process.ak4CaloJetTracksAssociatorAtVertex+process.ak4CaloJetBtagging+process.ak4CaloNjettiness+process.ak4CalopatJetsWithBtagging+process.ak4CaloJetAnalyzer)


process.akSoftDrop4PFJetSequence_data = cms.Sequence(process.akSoftDrop4PFcorr+process.akSoftDrop4PFJetTracksAssociatorAtVertex+process.akSoftDrop4PFJetBtagging+process.akSoftDrop4PFNjettiness+process.akSoftDrop4PFpatJetsWithBtagging+process.akSoftDrop4PFJetAnalyzer)


process.ak4PFJetBtagging = cms.Sequence(process.ak4PFJetBtaggingIP+process.ak4PFJetBtaggingSV+process.ak4PFJetBtaggingNegSV)


process.ak4PFJetSequence_mc = cms.Sequence(process.ak4PFmatch+process.ak4PFparton+process.ak4PFcorr+process.ak4PFPatJetFlavourId+process.ak4PFJetTracksAssociatorAtVertex+process.ak4PFJetBtagging+process.ak4PFNjettiness+process.ak4PFpatJetsWithBtagging+process.ak4PFJetAnalyzer)


process.ak4PFJetSequence_mb = cms.Sequence(process.ak4PFJetSequence_mc)


process.akSoftDrop4PFJetSequence_mc = cms.Sequence(process.akSoftDrop4PFmatch+process.akSoftDrop4PFparton+process.akSoftDrop4PFcorr+process.akSoftDrop4PFPatJetFlavourId+process.akSoftDrop4PFJetTracksAssociatorAtVertex+process.akSoftDrop4PFJetBtagging+process.akSoftDrop4PFNjettiness+process.akSoftDrop4PFpatJetsWithBtagging+process.akSoftDrop4PFJetAnalyzer)


process.ak3PFJetSequence_jec = cms.Sequence(process.ak3PFJetSequence_mc)


process.collisionEventSelectionAOD = cms.Sequence(process.hfCoincFilter3+process.primaryVertexFilter+process.clusterCompatibilityFilter)


process.ak4PFJetSequence_data = cms.Sequence(process.ak4PFcorr+process.ak4PFJetTracksAssociatorAtVertex+process.ak4PFJetBtagging+process.ak4PFNjettiness+process.ak4PFpatJetsWithBtagging+process.ak4PFJetAnalyzer)


process.akSoftDrop4PFJetSequence = cms.Sequence(process.akSoftDrop4PFJetSequence_data)


process.collisionEventSelection = cms.Sequence(process.hfCoincFilter3+process.primaryVertexFilter+process.siPixelRecHits+process.hltPixelClusterShapeFilter)


process.hfposFilter3 = cms.Sequence(process.hfposTowers+process.hfPosFilter3)


process.hfposFilter4 = cms.Sequence(process.hfposTowers+process.hfPosFilter4)


process.hfposFilter5 = cms.Sequence(process.hfposTowers+process.hfPosFilter5)


process.hfposFilter2 = cms.Sequence(process.hfposTowers+process.hfPosFilter2)


process.ak3PFJetSequence_data = cms.Sequence(process.ak3PFcorr+process.ak3PFJetTracksAssociatorAtVertex+process.ak3PFJetBtagging+process.ak3PFNjettiness+process.ak3PFpatJetsWithBtagging+process.ak3PFJetAnalyzer)


process.ak4PFJetSequence = cms.Sequence(process.ak4PFJetSequence_data)


process.ak4CaloJetSequence_mb = cms.Sequence(process.ak4CaloJetSequence_mc)


process.akSoftDrop4PFJetSequence_mb = cms.Sequence(process.akSoftDrop4PFJetSequence_mc)


process.ak3PFJetSequence_mb = cms.Sequence(process.ak3PFJetSequence_mc)


process.ak4PFJetSequence_jec = cms.Sequence(process.ak4PFJetSequence_mc)


process.ak4CaloJetSequence = cms.Sequence(process.ak4CaloJetSequence_data)


process.ak3PFJetSequence = cms.Sequence(process.ak3PFJetSequence_data)


process.akSoftDrop4PFJetSequence_jec = cms.Sequence(process.akSoftDrop4PFJetSequence_mc)


process.jetSequences = cms.Sequence(process.akSoftDrop4PFJets+process.highPurityTracks+process.ak4PFJetSequence+process.akSoftDrop4PFJetSequence)


process.ak4CaloJetSequence_jec = cms.Sequence(process.ak4CaloJetSequence_mc)


process.ana_step = cms.Path(process.hltanalysis+process.hltobject+process.hiEvtAnalyzer+process.jetSequences+process.hltMuTree+process.HiForest)


process.pHBHENoiseFilterResultProducer = cms.Path(process.HBHENoiseFilterResultProducer)


process.HBHENoiseFilterResult = cms.Path(process.fHBHENoiseFilterResult)


process.HBHENoiseFilterResultRun1 = cms.Path(process.fHBHENoiseFilterResultRun1)


process.HBHENoiseFilterResultRun2Loose = cms.Path(process.fHBHENoiseFilterResultRun2Loose)


process.HBHENoiseFilterResultRun2Tight = cms.Path(process.fHBHENoiseFilterResultRun2Tight)


process.HBHEIsoNoiseFilterResult = cms.Path(process.fHBHEIsoNoiseFilterResult)


process.pPAprimaryVertexFilter = cms.Path(process.PAprimaryVertexFilter)


process.pBeamScrapingFilter = cms.Path(process.NoScraping)


process.pVertexFilterCutG = cms.Path(process.pileupVertexFilterCutG)


process.pVertexFilterCutGloose = cms.Path(process.pileupVertexFilterCutGloose)


process.pVertexFilterCutGtight = cms.Path(process.pileupVertexFilterCutGtight)


process.pVertexFilterCutGplus = cms.Path(process.pileupVertexFilterCutGplus)


process.pVertexFilterCutE = cms.Path(process.pileupVertexFilterCutE)


process.pVertexFilterCutEandG = cms.Path(process.pileupVertexFilterCutEandG)


process.pAna = cms.EndPath(process.skimanalysis)


process.DQMStore = cms.Service("DQMStore",
    LSbasedMode = cms.untracked.bool(False),
    collateHistograms = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(False),
    forceResetOnBeginLumi = cms.untracked.bool(False),
    referenceFileName = cms.untracked.string(''),
    verbose = cms.untracked.int32(0),
    verboseQT = cms.untracked.int32(0)
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    famosSimHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    siTrackerGaussianSmearingRecHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('HiForestAOD.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer")


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(18268),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.SteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAlong'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(18268)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.candidateBoostedDoubleSecondaryVertexAK8Computer = cms.ESProducer("CandidateBoostedDoubleSecondaryVertexESProducer",
    R0 = cms.double(0.8),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(0.7),
    weightFile = cms.FileInPath('RecoBTag/SecondaryVertex/data/BoostedDoubleSV_AK8_BDT.weights.xml.gz')
)


process.candidateBoostedDoubleSecondaryVertexCA15Computer = cms.ESProducer("CandidateBoostedDoubleSecondaryVertexESProducer",
    R0 = cms.double(1.5),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(1.3),
    weightFile = cms.FileInPath('RecoBTag/SecondaryVertex/data/BoostedDoubleSV_CA15_BDT.weights.xml.gz')
)


process.candidateCombinedMVAComputer = cms.ESProducer("CombinedMVAJetTagESProducer",
    calibrationRecord = cms.string('CombinedMVA'),
    jetTagComputers = cms.VPSet(cms.PSet(
        discriminator = cms.bool(True),
        jetTagComputer = cms.string('candidateJetProbabilityComputer'),
        variables = cms.bool(False)
    ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('candidateCombinedSecondaryVertexV2Computer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('softPFMuonComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('softPFElectronComputer'),
            variables = cms.bool(False)
        )),
    useCategories = cms.bool(False)
)


process.candidateCombinedSecondaryVertexComputer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidateCombinedSecondaryVertexSoftLeptonComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLepton', 
        'CombinedSVPseudoVertexNoSoftLepton', 
        'CombinedSVNoVertexNoSoftLepton', 
        'CombinedSVRecoVertexSoftMuon', 
        'CombinedSVPseudoVertexSoftMuon', 
        'CombinedSVNoVertexSoftMuon', 
        'CombinedSVRecoVertexSoftElectron', 
        'CombinedSVPseudoVertexSoftElectron', 
        'CombinedSVNoVertexSoftElectron'),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidateCombinedSecondaryVertexSoftLeptonCtagLComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonCtagLESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLeptonCtagL', 
        'CombinedSVPseudoVertexNoSoftLeptonCtagL', 
        'CombinedSVNoVertexNoSoftLeptonCtagL', 
        'CombinedSVRecoVertexSoftMuonCtagL', 
        'CombinedSVPseudoVertexSoftMuonCtagL', 
        'CombinedSVNoVertexSoftMuonCtagL', 
        'CombinedSVRecoVertexSoftElectronCtagL', 
        'CombinedSVPseudoVertexSoftElectronCtagL', 
        'CombinedSVNoVertexSoftElectronCtagL'),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidateCombinedSecondaryVertexV2Computer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidateJetBProbabilityComputer = cms.ESProducer("CandidateJetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateJetProbabilityComputer = cms.ESProducer("CandidateJetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeCombinedMVAComputer = cms.ESProducer("CombinedMVAJetTagESProducer",
    calibrationRecord = cms.string('CombinedMVA'),
    jetTagComputers = cms.VPSet(cms.PSet(
        discriminator = cms.bool(True),
        jetTagComputer = cms.string('candidateNegativeOnlyJetProbabilityComputer'),
        variables = cms.bool(False)
    ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('candidateNegativeCombinedSecondaryVertexComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('negativeSoftPFMuonComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('negativeSoftPFElectronComputer'),
            variables = cms.bool(False)
        )),
    useCategories = cms.bool(False)
)


process.candidateNegativeCombinedSecondaryVertexComputer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.candidateNegativeCombinedSecondaryVertexSoftLeptonComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLepton', 
        'CombinedSVPseudoVertexNoSoftLepton', 
        'CombinedSVNoVertexNoSoftLepton', 
        'CombinedSVRecoVertexSoftMuon', 
        'CombinedSVPseudoVertexSoftMuon', 
        'CombinedSVNoVertexSoftMuon', 
        'CombinedSVRecoVertexSoftElectron', 
        'CombinedSVPseudoVertexSoftElectron', 
        'CombinedSVNoVertexSoftElectron'),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.candidateNegativeCombinedSecondaryVertexSoftLeptonCtagLComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonCtagLESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLeptonCtagL', 
        'CombinedSVPseudoVertexNoSoftLeptonCtagL', 
        'CombinedSVNoVertexNoSoftLeptonCtagL', 
        'CombinedSVRecoVertexSoftMuonCtagL', 
        'CombinedSVPseudoVertexSoftMuonCtagL', 
        'CombinedSVNoVertexSoftMuonCtagL', 
        'CombinedSVRecoVertexSoftElectronCtagL', 
        'CombinedSVPseudoVertexSoftElectronCtagL', 
        'CombinedSVNoVertexSoftElectronCtagL'),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.candidateNegativeCombinedSecondaryVertexV2Computer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.candidateNegativeOnlyJetBProbabilityComputer = cms.ESProducer("CandidateJetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeOnlyJetProbabilityComputer = cms.ESProducer("CandidateJetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeTrackCounting3D2ndComputer = cms.ESProducer("CandidateNegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeTrackCounting3D3rdComputer = cms.ESProducer("CandidateNegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.candidatePositiveCombinedMVAComputer = cms.ESProducer("CombinedMVAJetTagESProducer",
    calibrationRecord = cms.string('CombinedMVA'),
    jetTagComputers = cms.VPSet(cms.PSet(
        discriminator = cms.bool(True),
        jetTagComputer = cms.string('candidatePositiveOnlyJetProbabilityComputer'),
        variables = cms.bool(False)
    ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('candidatePositiveCombinedSecondaryVertexComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('positiveSoftPFMuonComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('positiveSoftPFElectronComputer'),
            variables = cms.bool(False)
        )),
    useCategories = cms.bool(False)
)


process.candidatePositiveCombinedSecondaryVertexComputer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidatePositiveCombinedSecondaryVertexSoftLeptonComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLepton', 
        'CombinedSVPseudoVertexNoSoftLepton', 
        'CombinedSVNoVertexNoSoftLepton', 
        'CombinedSVRecoVertexSoftMuon', 
        'CombinedSVPseudoVertexSoftMuon', 
        'CombinedSVNoVertexSoftMuon', 
        'CombinedSVRecoVertexSoftElectron', 
        'CombinedSVPseudoVertexSoftElectron', 
        'CombinedSVNoVertexSoftElectron'),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidatePositiveCombinedSecondaryVertexSoftLeptonCtagLComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonCtagLESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLeptonCtagL', 
        'CombinedSVPseudoVertexNoSoftLeptonCtagL', 
        'CombinedSVNoVertexNoSoftLeptonCtagL', 
        'CombinedSVRecoVertexSoftMuonCtagL', 
        'CombinedSVPseudoVertexSoftMuonCtagL', 
        'CombinedSVNoVertexSoftMuonCtagL', 
        'CombinedSVRecoVertexSoftElectronCtagL', 
        'CombinedSVPseudoVertexSoftElectronCtagL', 
        'CombinedSVNoVertexSoftElectronCtagL'),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidatePositiveCombinedSecondaryVertexV2Computer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidatePositiveOnlyJetBProbabilityComputer = cms.ESProducer("CandidateJetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidatePositiveOnlyJetProbabilityComputer = cms.ESProducer("CandidateJetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateSimpleSecondaryVertex2TrkComputer = cms.ESProducer("CandidateSimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.candidateSimpleSecondaryVertex3TrkComputer = cms.ESProducer("CandidateSimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.candidateTrackCounting3D2ndComputer = cms.ESProducer("CandidateTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.candidateTrackCounting3D3rdComputer = cms.ESProducer("CandidateTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.combinedMVAComputer = cms.ESProducer("CombinedMVAJetTagESProducer",
    calibrationRecord = cms.string('CombinedMVA'),
    jetTagComputers = cms.VPSet(cms.PSet(
        discriminator = cms.bool(True),
        jetTagComputer = cms.string('jetProbabilityComputer'),
        variables = cms.bool(False)
    ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('softPFMuonComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('softPFElectronComputer'),
            variables = cms.bool(False)
        )),
    useCategories = cms.bool(False)
)


process.combinedSecondaryVertexComputer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.combinedSecondaryVertexSoftLeptonComputer = cms.ESProducer("CombinedSecondaryVertexSoftLeptonESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLepton', 
        'CombinedSVPseudoVertexNoSoftLepton', 
        'CombinedSVNoVertexNoSoftLepton', 
        'CombinedSVRecoVertexSoftMuon', 
        'CombinedSVPseudoVertexSoftMuon', 
        'CombinedSVNoVertexSoftMuon', 
        'CombinedSVRecoVertexSoftElectron', 
        'CombinedSVPseudoVertexSoftElectron', 
        'CombinedSVNoVertexSoftElectron'),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.combinedSecondaryVertexV2Computer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.doubleVertex2TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    minVertices = cms.uint32(2),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.ghostTrackComputer = cms.ESProducer("GhostTrackESProducer",
    calibrationRecords = cms.vstring('GhostTrackRecoVertex', 
        'GhostTrackPseudoVertex', 
        'GhostTrackNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True)
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    appendToDataLabel = cms.string(''),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.impactParameterMVAComputer = cms.ESProducer("GenericMVAJetTagESProducer",
    calibrationRecord = cms.string('ImpactParameterMVA'),
    useCategories = cms.bool(False)
)


process.jetBProbabilityComputer = cms.ESProducer("JetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.jetProbabilityComputer = cms.ESProducer("JetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.l1GtTriggerMaskTechTrig = cms.ESProducer("L1GtTriggerMaskTechTrigTrivialProducer",
    TriggerMask = cms.vuint32(0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0)
)


process.negativeCombinedMVAComputer = cms.ESProducer("CombinedMVAJetTagESProducer",
    calibrationRecord = cms.string('CombinedMVA'),
    jetTagComputers = cms.VPSet(cms.PSet(
        discriminator = cms.bool(True),
        jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
        variables = cms.bool(False)
    ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('negativeSoftPFMuonComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('negativeSoftPFElectronComputer'),
            variables = cms.bool(False)
        )),
    useCategories = cms.bool(False)
)


process.negativeCombinedSecondaryVertexComputer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.negativeCombinedSecondaryVertexV2Computer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.negativeOnlyJetBProbabilityComputer = cms.ESProducer("JetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.negativeOnlyJetProbabilityComputer = cms.ESProducer("JetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.negativeSoftPFElectronByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(False)
)


process.negativeSoftPFElectronByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(True)
)


process.negativeSoftPFElectronByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('negative')
)


process.negativeSoftPFElectronComputer = cms.ESProducer("ElectronTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFElectron_TMVA420_BDT_74X_v1'),
    ipSign = cms.string('negative'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)


process.negativeSoftPFMuonByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(False)
)


process.negativeSoftPFMuonByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(True)
)


process.negativeSoftPFMuonByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('negative')
)


process.negativeSoftPFMuonComputer = cms.ESProducer("MuonTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFMuon_TMVA420_BDT_74X_v1'),
    ipSign = cms.string('negative'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)


process.negativeTrackCounting3D2ndComputer = cms.ESProducer("NegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.negativeTrackCounting3D3rdComputer = cms.ESProducer("NegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.positiveCombinedMVAComputer = cms.ESProducer("CombinedMVAJetTagESProducer",
    calibrationRecord = cms.string('CombinedMVA'),
    jetTagComputers = cms.VPSet(cms.PSet(
        discriminator = cms.bool(True),
        jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
        variables = cms.bool(False)
    ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('positiveSoftPFMuonComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('positiveSoftPFElectronComputer'),
            variables = cms.bool(False)
        )),
    useCategories = cms.bool(False)
)


process.positiveCombinedSecondaryVertexComputer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.positiveCombinedSecondaryVertexV2Computer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.positiveOnlyJetBProbabilityComputer = cms.ESProducer("JetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.positiveOnlyJetProbabilityComputer = cms.ESProducer("JetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.positiveSoftPFElectronByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(False)
)


process.positiveSoftPFElectronByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(True)
)


process.positiveSoftPFElectronByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('positive')
)


process.positiveSoftPFElectronComputer = cms.ESProducer("ElectronTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFElectron_TMVA420_BDT_74X_v1'),
    ipSign = cms.string('positive'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)


process.positiveSoftPFMuonByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(False)
)


process.positiveSoftPFMuonByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(True)
)


process.positiveSoftPFMuonByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('positive')
)


process.positiveSoftPFMuonComputer = cms.ESProducer("MuonTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFMuon_TMVA420_BDT_74X_v1'),
    ipSign = cms.string('positive'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(cms.PSet(
        Label = cms.untracked.string(''),
        NormalizationFactor = cms.untracked.double(1.0),
        Record = cms.string('SiStripApvGainRcd')
    ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.simpleSecondaryVertex2TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.simpleSecondaryVertex3TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.softPFElectronByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(False)
)


process.softPFElectronByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(True)
)


process.softPFElectronByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('any')
)


process.softPFElectronComputer = cms.ESProducer("ElectronTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFElectron_TMVA420_BDT_74X_v1'),
    ipSign = cms.string('any'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)


process.softPFMuonByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(False)
)


process.softPFMuonByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(True)
)


process.softPFMuonByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('any')
)


process.softPFMuonComputer = cms.ESProducer("MuonTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFMuon_TMVA420_BDT_74X_v1'),
    ipSign = cms.string('any'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackCounting3D2ndComputer = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.trackCounting3D3rdComputer = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.BTagRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('JetTagComputerRecord')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    ),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('75X_dataRun2_v13'),
    toGet = cms.VPSet()
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.L1GtTriggerMaskTechTrigRcdSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1GtTriggerMaskTechTrigRcd')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HERecalibration = cms.bool(False),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalibration = cms.bool(False),
    HcalReLabel = cms.PSet(
        RelabelHits = cms.untracked.bool(False),
        RelabelRules = cms.untracked.PSet(
            CorrectPhi = cms.untracked.bool(False),
            Eta1 = cms.untracked.vint32(1, 2, 2, 2, 3, 
                3, 3, 3, 3, 3, 
                3, 3, 3, 3, 3, 
                3, 3, 3, 3),
            Eta16 = cms.untracked.vint32(1, 1, 2, 2, 2, 
                2, 2, 2, 2, 3, 
                3, 3, 3, 3, 3, 
                3, 3, 3, 3),
            Eta17 = cms.untracked.vint32(1, 1, 2, 2, 3, 
                3, 3, 4, 4, 4, 
                4, 4, 5, 5, 5, 
                5, 5, 5, 5)
        )
    ),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    ),
    iLumi = cms.double(-1.0),
    toGet = cms.untracked.vstring('GainWidths')
)


process.jec = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0)
    ),
    timetype = cms.string('runnumber'),
    toGet = cms.VPSet(cms.PSet(
        connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
        label = cms.untracked.string('AK1Calo_offline'),
        record = cms.string('JetCorrectionsRecord'),
        tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK1Calo_offline')
    ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK1PF_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK1PF_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK2Calo_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK2Calo_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK2PF_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK2PF_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK3Calo_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK3Calo_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK3PF_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK3PF_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK4Calo_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK4Calo_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK4PF_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK4PF_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK5Calo_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK5Calo_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK5PF_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK5PF_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK6Calo_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK6Calo_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK6PF_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK6PF_offline')
        ))
)


process.prefer("es_hardcode")

process.prefer("jec")

process.CondDBCommon = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    ),
    connect = cms.string('protocol://db/schema')
)

process.CondDBSetup = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    )
)

process.HcalReLabel = cms.PSet(
    RelabelHits = cms.untracked.bool(False),
    RelabelRules = cms.untracked.PSet(
        CorrectPhi = cms.untracked.bool(False),
        Eta1 = cms.untracked.vint32(1, 2, 2, 2, 3, 
            3, 3, 3, 3, 3, 
            3, 3, 3, 3, 3, 
            3, 3, 3, 3),
        Eta16 = cms.untracked.vint32(1, 1, 2, 2, 2, 
            2, 2, 2, 2, 3, 
            3, 3, 3, 3, 3, 
            3, 3, 3, 3),
        Eta17 = cms.untracked.vint32(1, 1, 2, 2, 3, 
            3, 3, 4, 4, 4, 
            4, 4, 5, 5, 5, 
            5, 5, 5, 5)
    )
)

process.JetIDParams = cms.PSet(
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    useRecHits = cms.bool(True)
)

process.combinedSecondaryVertexCommon = cms.PSet(
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)

process.ghostTrackCommon = cms.PSet(
    charmCut = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig')
)

process.ghostTrackVertexRecoBlock = cms.PSet(
    vertexReco = cms.PSet(
        finder = cms.string('gtvr'),
        fitType = cms.string('RefitGhostTrackWithVertices'),
        maxFitChi2 = cms.double(10.0),
        mergeThreshold = cms.double(3.0),
        primcut = cms.double(2.0),
        seccut = cms.double(4.0)
    )
)

process.j2tParametersCALO = cms.PSet(
    coneSize = cms.double(0.4),
    extrapolations = cms.InputTag("trackExtrapolator"),
    trackQuality = cms.string('goodIterative'),
    tracks = cms.InputTag("generalTracks")
)

process.j2tParametersVX = cms.PSet(
    coneSize = cms.double(0.4),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(200)
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_producer_config = cms.PSet(
    mvaName = cms.string('ElectronMVAEstimatorRun2Phys14NonTrig'),
    mvaTag = cms.string('25nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(-0.253, 0.081, -0.081, 0.965, 0.917, 
            0.683),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-PHYS14-PU20bx25-nonTrig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(False)
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(-0.483, -0.267, -0.323, 0.933, 0.825, 
            0.337),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-PHYS14-PU20bx25-nonTrig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(False)
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_producer_config = cms.PSet(
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversionsAOD = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    mvaName = cms.string('ElectronMVAEstimatorRun2Spring15NonTrig'),
    mvaTag = cms.string('25nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(0.287435, 0.221846, -0.303263, 0.967083, 0.929117, 
            0.726311),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(-0.083313, -0.235222, -0.67099, 0.913286, 0.805013, 
            0.358969),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.options = cms.untracked.PSet(

)

process.softPFElectronCommon = cms.PSet(
    gbrForestLabel = cms.string('btag_SoftPFElectron_TMVA420_BDT_74X_v1'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)

process.softPFMuonCommon = cms.PSet(
    gbrForestLabel = cms.string('btag_SoftPFMuon_TMVA420_BDT_74X_v1'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)

process.trackPseudoSelectionBlock = cms.PSet(
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)

process.trackSelectionBlock = cms.PSet(
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)

process.variableJTAPars = cms.PSet(
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5)
)

process.vertexCutsBlock = cms.PSet(
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    )
)

process.vertexRecoBlock = cms.PSet(
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    )
)

process.vertexSelectionBlock = cms.PSet(
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)

process.vertexTrackSelectionBlock = cms.PSet(
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    )
)

process.mvaConfigsForEleProducer = cms.VPSet(cms.PSet(
    mvaName = cms.string('ElectronMVAEstimatorRun2Phys14NonTrig'),
    mvaTag = cms.string('25nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
), 
    cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        conversionsAOD = cms.InputTag("allConversions"),
        conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
        mvaName = cms.string('ElectronMVAEstimatorRun2Spring15NonTrig'),
        mvaTag = cms.string('25nsV1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
    ))

