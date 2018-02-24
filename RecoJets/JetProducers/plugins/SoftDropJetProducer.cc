#include "FWCore/Framework/interface/MakerMacros.h"
#include "RecoJets/JetProducers/plugins/SoftDropJetProducer.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "RecoJets/JetProducers/interface/JetSpecific.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/Common/interface/AssociationVector.h"
#include "DataFormats/JetReco/interface/JetCollection.h"
#include "DataFormats/Common/interface/Ref.h"
#include "DataFormats/Common/interface/RefToBase.h"
#include "DataFormats/Common/interface/RefVector.h"

#include "fastjet/contrib/SoftDrop.hh"

#include <iostream>
#include <memory>
#include <algorithm>
#include <limits>
#include <cmath>

#include "FWCore/ParameterSet/interface/FileInPath.h"
#include <TFile.h>
#include <TH1.h>
#include <TH1F.h>
#include <TH2F.h>
#include <TMath.h>

#include <TRandom3.h>

#include "fastjet/ClusterSequence.hh"
#include "fastjet/ClusterSequenceArea.hh"
#include "fastjet/contrib/ConstituentSubtractor.hh"


using namespace std;
using namespace reco;
using namespace edm;
using namespace cms;



SoftDropJetProducer::SoftDropJetProducer(edm::ParameterSet const& iConfig):
  VirtualJetProducer( iConfig ),
  zCut_(-1.0),
  beta_(-1.0),
  R0_(-1.0),
//	JES_(0.0),
//	JER_(false),
//	isBjet_(false),	
  useOnlyCharged_(false)
{
  //get soft drop settings
  zCut_ = iConfig.getParameter<double>("zcut");
  beta_ = iConfig.getParameter<double>("beta");
  R0_ = iConfig.getParameter<double>("R0");
  useOnlyCharged_ = iConfig.getParameter<bool>("useOnlyCharged");

	JESpt0_=0.0; 
	JESpt1_=0.0;
	JERpt0_=0.0;
	JERpt1_=0.0;
	JER_=false;
	isBjet_=false;

	if (iConfig.exists("JESpt0"))	JESpt0_ = iConfig.getParameter<double>("JESpt0");
	if (iConfig.exists("JESpt1"))	JESpt1_ = iConfig.getParameter<double>("JESpt1");
  if (iConfig.exists("JERpt0")) JERpt0_ = iConfig.getParameter<double>("JERpt0");
  if (iConfig.exists("JERpt1")) JERpt1_ = iConfig.getParameter<double>("JERpt1");
	if (iConfig.exists("JER")) JER_ = iConfig.getParameter<bool>("JER");
	if (iConfig.exists("isBjet")) isBjet_ = iConfig.getParameter<bool>("isBjet"); 

	debug_= false;

  input_candidateview_token_SD_ = consumes<reco::CandidateView>(src_);
  input_candidatefwdptr_token_SD_ = consumes<std::vector<edm::FwdPtr<reco::PFCandidate> > >(src_);
  input_packedcandidatefwdptr_token_SD_ = consumes<std::vector<edm::FwdPtr<pat::PackedCandidate> > >(src_);

  produces<edm::ValueMap<float> > ("sym");
  produces<edm::ValueMap<int> > ("droppedBranches");
  //produces<edm::ValueMap<std::vector<double>> > ("droppedSym");
  //produces<edm::AssociationVector<reco::JetRefBaseProd,std::vector<double>> > ("droppedSym");
  //produces<edm::AssociationVector<std::vector<double> > ("droppedSym"); 

}

//______________________________________________________________________________
void SoftDropJetProducer::produce( edm::Event & iEvent, const edm::EventSetup & iSetup )
{
	if(gRandom) delete gRandom;
	gRandom = new TRandom3(0);
	gRandom->SetSeed(0);

  // use the default production from one collection
  //VirtualJetProducer::produce( iEvent, iSetup );

  // If requested, set the fastjet random seed to a deterministic function
  // of the run/lumi/event.
  // NOTE!!! The fastjet random number sequence is a global singleton.
  // Thus, we have to create an object and get access to the global singleton
  // in order to change it.
  if ( useDeterministicSeed_ ) {
    fastjet::GhostedAreaSpec gas;
    std::vector<int> seeds(2);
    unsigned int runNum_uint = static_cast <unsigned int> (iEvent.id().run());
    unsigned int evNum_uint = static_cast <unsigned int> (iEvent.id().event());
    seeds[0] = std::max(runNum_uint,minSeed_ + 3) + 3 * evNum_uint;
    seeds[1] = std::max(runNum_uint,minSeed_ + 5) + 5 * evNum_uint;
    gas.set_random_status(seeds);
  }

  LogDebug("SoftDropJetProducer") << "Entered produce\n";
  //determine signal vertex2
  vertex_=reco::Jet::Point(0,0,0);
  if ( (makeCaloJet(jetTypeE) || makePFJet(jetTypeE)) &&doPVCorrection_) {
    LogDebug("SoftDropJetProducer") << "Adding PV info\n";
    edm::Handle<reco::VertexCollection> pvCollection;
    iEvent.getByToken(input_vertex_token_ , pvCollection);
    if (pvCollection->size()>0) vertex_=pvCollection->begin()->position();
  }

  // For Pileup subtraction using offset correction:
  // set up geometry map
  if ( doPUOffsetCorr_ ) {
     subtractor_->setupGeometryMap(iEvent, iSetup);
  }

  // clear data
  LogDebug("SoftDropJetProducer") << "Clear data\n";
  fjInputs_.clear();
  fjJets_.clear();
  inputs_.clear();

  // get inputs and convert them to the fastjet format (fastjet::PeudoJet)
  edm::Handle<reco::CandidateView> inputsHandle;

  edm::Handle< std::vector<edm::FwdPtr<reco::PFCandidate> > > pfinputsHandleAsFwdPtr;
  edm::Handle< std::vector<edm::FwdPtr<pat::PackedCandidate> > > packedinputsHandleAsFwdPtr;


  bool isView = iEvent.getByToken(input_candidateview_token_SD_, inputsHandle);

  if ( isView ) {
    if ( verbosity_ >= 1 ) {
      std::cout << "found inputs in event" << std::endl; }
    for (size_t i = 0; i < inputsHandle->size(); ++i) {
      inputs_.push_back(inputsHandle->ptrAt(i));
      // if ( verbosity_ >= 1 ) {
      //   std::cout << "input particle " << i << " pt = " << inputs_[i]->pt() << " phi: " << inputs_[i]->phi() << " eta: " << inputs_[i]->eta() << " " << std::endl;
      // }
    }
  } else {
    bool isPF = iEvent.getByToken(input_candidatefwdptr_token_SD_, pfinputsHandleAsFwdPtr);
    if ( isPF ) {
      for (size_t i = 0; i < pfinputsHandleAsFwdPtr->size(); ++i) {
        if ( (*pfinputsHandleAsFwdPtr)[i].ptr().isAvailable() ) {
          inputs_.push_back( (*pfinputsHandleAsFwdPtr)[i].ptr() );
        }
        else if ( (*pfinputsHandleAsFwdPtr)[i].backPtr().isAvailable() ) {
          inputs_.push_back( (*pfinputsHandleAsFwdPtr)[i].backPtr() );
        }
      }
    } else {
      iEvent.getByToken(input_packedcandidatefwdptr_token_SD_, packedinputsHandleAsFwdPtr);
      for (size_t i = 0; i < packedinputsHandleAsFwdPtr->size(); ++i) {
        if ( (*packedinputsHandleAsFwdPtr)[i].ptr().isAvailable() ) {
          inputs_.push_back( (*packedinputsHandleAsFwdPtr)[i].ptr() );
        }
        else if ( (*packedinputsHandleAsFwdPtr)[i].backPtr().isAvailable() ) {
          inputs_.push_back( (*packedinputsHandleAsFwdPtr)[i].backPtr() );
        }
      }
    }
  }
  LogDebug("SoftDropJetProducer") << "Got inputs\n";

  // Convert candidates to fastjet::PseudoJets.
  // Also correct to Primary Vertex. Will modify fjInputs_
  // and use inputs_
  fjInputs_.reserve(inputs_.size());
  inputTowers();
  LogDebug("VirtualJetProducer") << "Inputted towers\n";

  // Run algorithm. Will modify fjJets_ and allocate fjClusterSeq_.
  // This will use fjInputs_
  runAlgorithm( iEvent, iSetup );

  // Write the output jets.
  // This will (by default) call the member function template
  // "writeJets", but can be overridden.
  // this will use inputs_
  output( iEvent, iSetup );

  

  //use write function of this class
  //writeSoftDropJets<reco::PFJet>( iEvent, iSetup );

  
  //use runAlgorithm of this class
  //runAlgorithm(iEvent,iSetup);

  // fjClusterSeq_ retains quite a lot of memory - about 1 to 7Mb at 200 pileup
  // depending on the exact configuration; and there are 24 FastjetJetProducers in the
  // sequence so this adds up to about 60 Mb. It's allocated every time runAlgorithm
  // is called, so safe to delete here.
  fjClusterSeq_.reset();
  fjClusterSeqRecluster_.reset();

  // Clear the work vectors so that memory is free for other modules.
  // Use the trick of swapping with an empty vector so that the memory
  // is actually given back rather than silently kept.
  decltype(fjInputs_)().swap(fjInputs_);
  decltype(fjJets_)().swap(fjJets_);
  decltype(inputs_)().swap(inputs_);
}

//______________________________________________________________________________
void SoftDropJetProducer::output( edm::Event & iEvent, const edm::EventSetup & iSetup )
{
  //use write function of this class
  if ( writeCompound_ ) {
    // Write jets and subjets
    switch( jetTypeE ) {
    case JetType::CaloJet :
      writeSoftDropJets<reco::CaloJet>( iEvent, iSetup );
      break;
    case JetType::PFJet :
      writeSoftDropJets<reco::PFJet>( iEvent, iSetup );
      break;
    case JetType::GenJet :
      writeSoftDropJets<reco::GenJet>( iEvent, iSetup );
      break;
    case JetType::BasicJet :
      writeSoftDropJets<reco::BasicJet>( iEvent, iSetup );
      break;
    default:
      throw cms::Exception("InvalidInput") << "invalid jet type in SoftDropJetProducer\n";
      break;
    };
  }
  
  //  writeSoftDropJets<reco::PFJet>( iEvent, iSetup );

}

//______________________________________________________________________________
void SoftDropJetProducer::runAlgorithm( edm::Event & iEvent, edm::EventSetup const& iSetup)
{


//    string defName="RecoJets/JetProducers/plugins/fout.root";
//		string defName="HeavyIonsAnalysis/JetAnalysis/test/fout_qcd.root";
//    edm::FileInPath f(defName);
//    TFile *fin= TFile::Open(f.fullPath().c_str(),"read");

//   string defName="root://cms-xrd-global.cern.ch//store/user/chengchi/HIHFJet2017/fout_qcd.root";
	 string defName="fout_bjt.root";
	 if(isBjet_==false){defName="fout_qcd.root";}
   TFile *fin= TFile::Open(defName.c_str(),"read");

	 const int nPtBins=2;
	 const int nZgBins=8;
   double ZgMin=0.1;
   double ZgBinWidth=(0.5-ZgMin)/nZgBins;
   double ZgBins[nZgBins];
	
	for(int iZgBins=0; iZgBins<nZgBins; iZgBins++){
		ZgBins[iZgBins]=ZgMin+(double)iZgBins*ZgBinWidth;
	}


	 TH2F *h2[nPtBins][nZgBins];
	 TH1F *h1[nPtBins];

	 TF1 *f1[nPtBins];

	 for(int iPtBins=0; iPtBins<nPtBins; iPtBins++){
			h1[iPtBins]=(TH1F*)fin->Get(Form("h_jetJER_pt%i",iPtBins));
			f1[iPtBins]=new TF1(Form("f1_%i",iPtBins),"gaus",0,5);
			f1[iPtBins]->SetParameters(10000,1,0.0);
		for(int iZgBins=0; iZgBins<nZgBins; iZgBins++){
			h2[iPtBins][iZgBins]=(TH2F*)fin->Get(Form("h2_Sj1Sj2_jet_CorrPt_Pt%i_Zg%i",iPtBins,iZgBins));
		}
	 }
	 	 f1[0]->SetParameter(2,JERpt0_);
     f1[1]->SetParameter(2,JERpt1_);


//   TH1F *h1=(TH1F*)fin->Get("h_de_subjet1pt_over_de_jetpt_Zg3");



  //std::cout << "<SoftDropJetProducer::runAlgorithm (moduleLabel = " << moduleLabel_ << ")>:" << std::endl;
  
  if ( !doAreaFastjet_ && !doRhoFastjet_) {
    fjClusterSeq_ = ClusterSequencePtr( new fastjet::ClusterSequence( fjInputs_, *fjJetDefinition_ ) );
  } else if (voronoiRfact_ <= 0) {
    fjClusterSeq_ = ClusterSequencePtr( new fastjet::ClusterSequenceArea( fjInputs_, *fjJetDefinition_ , *fjAreaDefinition_ ) );
  } else {
    fjClusterSeq_ = ClusterSequencePtr( new fastjet::ClusterSequenceVoronoiArea( fjInputs_, *fjJetDefinition_ , fastjet::VoronoiAreaSpec(voronoiRfact_) ) );
  }
  
  std::vector<fastjet::PseudoJet> origJets = fastjet::sorted_by_pt(fjClusterSeq_->inclusive_jets(jetPtMin_));
  // fastjet::contrib::SoftDrop * sdr = new fastjet::contrib::SoftDrop(beta_, zCut_, R0_ );
  // sdr->set_verbose_structure(true);
  
  // for ( std::vector<fastjet::PseudoJet>::const_iterator ijet = origJets.begin(),
  //         ijetEnd = origJets.end(); ijet != ijetEnd; ++ijet ) {
  //   fastjet::PseudoJet transformedJet = *ijet;
  //   if ( transformedJet == 0 ) continue;
  //   transformedJet = (*sdr)(transformedJet);
  //   //fjJets_.push_back( transformedJet );

  //   double sym = transformedJet.structure_of<fastjet::contrib::SoftDrop>().symmetry();
  //   std::cout << "sym: " << sym << std::endl;
  //   int ndrop = transformedJet.structure_of<fastjet::contrib::SoftDrop>().dropped_count();
  //   std::cout << "#dropped branches: " << ndrop << std::endl;
  //   std::vector<double> dropped_symmetry = transformedJet.structure_of<fastjet::contrib::SoftDrop>().dropped_symmetry();
  //   std::cout << "dropped_symmetry.size() " << dropped_symmetry.size() << std::endl;
  //   for ( std::vector<double>::const_iterator dsym = dropped_symmetry.begin();
  //           dsym != dropped_symmetry.end(); ++dsym )
  //     std::cout << "dropped symmetry: " << (*dsym) << std::endl;
  // }

  //std::cout << "recluster manual" << std::endl;

  //select requested particle types and recluster with CA infinite radius
  //fjJetDefinitionRecluster_ = JetDefPtr(new fastjet::JetDefinition(fastjet::antikt_algorithm,rParam_));
  //fjJetDefinitionRecluster_ = JetDefPtr(new fastjet::JetDefinition(fastjet::cambridge_algorithm,999.));
      
  fjJets_.clear();
  clusterSequences.clear();
  jetDefinitions.clear();
  lSym.clear();
  lDroppedBranches.clear();
  lDroppedSym.clear();
 

	if(debug_==true) std::cout<<"\n   -------   \n"<<endl;
 
  static const reco::PFCandidate dummySinceTranslateIsNotStatic;
  // clusterSequence_coll clusterSequences;
  // jetDefinition_coll jetDefinitions;
  for ( std::vector<fastjet::PseudoJet>::const_iterator ijet = origJets.begin(),
          ijetEnd = origJets.end(); ijet != ijetEnd; ++ijet ) {

		unsigned ijet_fromIt= ijet-origJets.begin();

  if(debug_==true)	std::cout<<"ijet_fromIt = "<<ijet_fromIt<<endl;

    fjClusterSeqRecluster_.reset();
    std::vector<fastjet::PseudoJet> inputsRecluster;
    //    inputsRecluster.clear();
    std::vector<fastjet::PseudoJet> particles, ghosts;
    fastjet::SelectorIsPureGhost().sift(ijet->constituents(), ghosts, particles);
    //std::cout << "#particles in jet " << particles.size() << std::endl;
    for ( std::vector<fastjet::PseudoJet>::const_iterator ipart = particles.begin();
          ipart != particles.end(); ++ipart ) {
      auto orig = inputs_[(*ipart).user_index()];
      auto id = dummySinceTranslateIsNotStatic.translatePdgIdToType(orig->pdgId());
      
      bool passed  = false;
      if(useOnlyCharged_) {
        if(id==1) passed = true;
      } else
        passed = true;
      //if(passed) std::cout << "id: " << id << " pdfId: " << orig->pdgId() << std::endl;
      if(passed) inputsRecluster.push_back(*ipart);
    }
    //    std::cout << "inputsRecluster.size() " << inputsRecluster.size() << std::endl;

    //recluster with selected particles
    fjJetDefinitionRecluster_ = JetDefPtr(new fastjet::JetDefinition(fastjet::cambridge_algorithm,999.));
    //fjJetDefinitionRecluster_ = JetDefPtr(new fastjet::JetDefinition(fastjet::cambridge_algorithm,fastjet::JetDefinition::max_allowable_R));
    if ( !doAreaFastjet_ && !doRhoFastjet_) {
      fjClusterSeqRecluster_ = ClusterSequencePtr( new fastjet::ClusterSequence( inputsRecluster, *fjJetDefinitionRecluster_ ) );
    } else if (voronoiRfact_ <= 0) {
      fjClusterSeqRecluster_ = ClusterSequencePtr( new fastjet::ClusterSequenceArea( inputsRecluster, *fjJetDefinitionRecluster_ , *fjAreaDefinition_ ) );
    } else {
      fjClusterSeqRecluster_ = ClusterSequencePtr( new fastjet::ClusterSequenceVoronoiArea( inputsRecluster, *fjJetDefinitionRecluster_ , fastjet::VoronoiAreaSpec(voronoiRfact_) ) );
    }
    clusterSequences.push_back(fjClusterSeqRecluster_);
    jetDefinitions.push_back(fjJetDefinitionRecluster_);

    std::vector<fastjet::PseudoJet> tempJets = fastjet::sorted_by_pt(fjClusterSeqRecluster_->inclusive_jets(jetPtMin_));
    //std::vector<fastjet::PseudoJet> tempJets = fastjet::sorted_by_pt(clusterSequences[clusterSequences.size()]->inclusive_jets(jetPtMin_));
    if(tempJets.size()<1) continue;
    //std::cout << "got reclusted CA jet" << std::endl;
    //std::cout << "tempJets.size() " << tempJets.size() << std::endl;   
 
    fastjet::contrib::SoftDrop * sd = new fastjet::contrib::SoftDrop(beta_, zCut_, R0_ );
    sd->set_verbose_structure(true);

    fastjet::PseudoJet transformedJet = tempJets[0];
    if ( transformedJet == 0 ) {
      //fjClusterSeqRecluster_->delete_self_when_unused();
      if(sd) { delete sd; sd = 0;}
      continue;
    }
    // if(!transformedJet.has_valid_cluster_sequence()) {
    //   std::cout << "transformedJet does not have a valid cluster sequence" << std::endl;
    // }
    //std::cout << "orig jet pt: " << transformedJet.perp() << std::endl;
    transformedJet = (*sd)(transformedJet);
//
    double sym = transformedJet.structure_of<fastjet::contrib::SoftDrop>().symmetry();
    int ndrop = transformedJet.structure_of<fastjet::contrib::SoftDrop>().dropped_count();
    std::vector<double> dropped_symmetry = transformedJet.structure_of<fastjet::contrib::SoftDrop>().dropped_symmetry();


    if(JESpt0_==0.0 && JESpt1_==0.0 && JER_==false) {
//			cout<<"default SD"<<endl;
			fjJets_.push_back( transformedJet );} //put CA reclusterd jet after softDrop into vector which will be written to event
		else{
//			cout<<"JES SD"<<endl;
/* 
    fastjet::PseudoJet TRANsubjet1, TRANsubjet2;
        if(transformedJet.has_parents(TRANsubjet1,TRANsubjet2)){
					cout<<"--- transformedJet subjet1 pt = "<< TRANsubjet1.perp()<<" ,  subjet2 pt= "<<TRANsubjet2.perp()<<endl;
					}
*/
 
//    std::cout<<"test start from here"<<endl;
		// test 1 , read TH2


//		string defName="RecoJets/JetProducers/plugins/fout.root";
//		edm::FileInPath f(defName);

//		TFile *fin= new TFile(f.fullPath().c_str(),"read");
//		TH1F *h1=(TH1F*)fin->Get("h_de_subjet1pt_over_de_jetpt_Zg10");
//		cout<<"h1 random 1 = "<<h1->GetRandom()<<endl;
//    cout<<"h1 random 2 = "<<h1->GetRandom()<<endl;


		// test 2 , manually run SD
		
		// recluster by CA , not needed.
/*
		std::vector<fastjet::PseudoJet> tempJetsParticles=tempJets[0].constituents();

		fastjet::JetDefinition CAJetDef(fastjet::cambridge_algorithm,9);
		fastjet::ClusterSequence SeCA(tempJetsParticles,CAJetDef);

		vector<fastjet::PseudoJet> tempJetsCA=SeCA.inclusive_jets();
*/


		fastjet::PseudoJet MaSDjet = tempJets[0];

	  fastjet::PseudoJet MaSDsubjet1, MaSDsubjet2; 
    if ( MaSDjet == 0 ) {
      //fjClusterSeqRecluster_->delete_self_when_unused();
      if(sd) { delete sd; sd = 0;}
      continue;
    }

		// SD drop
		double Zgcut=zCut_;

		double SJ1pt=0;
		double SJ2pt=0;
		double Zgtest=0;
		int JetPtBin=0;
		int JetZgBin=0;

		double JES=0.05;
		double JES_SJ1=0;
		double JES_SJ2=0;	

		if(tempJets[0].perp()<160) {
			JetPtBin=0;
//			JES=0.054;
//			JES=0.016;
			JES=JESpt0_;
			if(JER_==true){JES=h1[0]->GetRandom()-h1[0]->GetMean();}
			if(JER_==true && JERpt0_!=0.0){ JES=f1[0]->GetRandom()-1; }
		}else{
			JetPtBin=1;
//			JES=0.049;
//			JES=0.016;
			JES=JESpt1_;	
      if(JER_==true){JES=h1[1]->GetRandom()-h1[1]->GetMean();}
      if(JER_==true && JERpt1_!=0.0){ JES=f1[1]->GetRandom()-1; }
		}



		if(MaSDjet.has_parents(MaSDsubjet1,MaSDsubjet2)){

		// determine variation here
				Zgtest=((TMath::Min(MaSDsubjet1.perp(),MaSDsubjet2.perp()))/(MaSDsubjet1.perp()+MaSDsubjet2.perp() ));
				if(MaSDsubjet1.perp()>=MaSDsubjet2.perp()){
					SJ1pt=MaSDsubjet1.perp(); SJ2pt=MaSDsubjet2.perp();					
				}else{
					SJ2pt=MaSDsubjet1.perp(); SJ1pt=MaSDsubjet2.perp();					
				}
				JetZgBin=0;	
				for(int iZgBins=0; iZgBins<nZgBins; iZgBins++){
					if(Zgtest>ZgBins[iZgBins] && Zgtest<=(ZgBins[iZgBins]+ZgBinWidth)){
					JetZgBin=iZgBins;
					}
				}							
				h2[JetPtBin][JetZgBin]->GetRandom2(JES_SJ1,JES_SJ2);
				SJ1pt=SJ1pt*(1+JES_SJ1*JES);
				SJ2pt=SJ2pt*(1+JES_SJ2*JES);
			  Zgtest=SJ2pt/(SJ2pt+SJ1pt);

			while( Zgtest <Zgcut){
				MaSDjet=MaSDsubjet1;
				if(MaSDjet.has_parents(MaSDsubjet1,MaSDsubjet2)){
        Zgtest=((TMath::Min(MaSDsubjet1.perp(),MaSDsubjet2.perp()))/(MaSDsubjet1.perp()+MaSDsubjet2.perp() ));
        if(MaSDsubjet1.perp()>=MaSDsubjet2.perp()){
          SJ1pt=MaSDsubjet1.perp(); SJ2pt=MaSDsubjet2.perp();
        }else{
          SJ2pt=MaSDsubjet1.perp(); SJ1pt=MaSDsubjet2.perp();
//					cout<<"SJ pt swap"<<endl;
        }
        JetZgBin=0;
        for(int iZgBins=0; iZgBins<nZgBins; iZgBins++){
          if(Zgtest>ZgBins[iZgBins] && Zgtest<=(ZgBins[iZgBins]+ZgBinWidth)){
          JetZgBin=iZgBins;
          }
        }
        h2[JetPtBin][JetZgBin]->GetRandom2(JES_SJ1,JES_SJ2);
        SJ1pt=SJ1pt*(1+JES_SJ1*JES);
        SJ2pt=SJ2pt*(1+JES_SJ2*JES);
        Zgtest=SJ2pt/(SJ2pt+SJ1pt);

				}else{break;}
			} // end while zgcut
		} // end if has parents

	  fjJets_.push_back( MaSDjet );

//		cout<<"MaSDsubjet1.px() = "<<MaSDsubjet1.px()<<" ,MaSDsubjet1.py() = "<<MaSDsubjet1.py()<<endl;
//    cout<<"MaSDsubjet2.px() = "<<MaSDsubjet2.px()<<" ,MaSDsubjet2.py() = "<<MaSDsubjet2.py()<<endl;
 if(debug_==true)		cout<<"Zg = "<<((SJ2pt)/(SJ1pt+SJ2pt))<<" , SJ1pt = "<<SJ1pt<<" ,SJ2pt = "<<SJ2pt<<endl;

		SjJES[ijet_fromIt][0]=JES_SJ1*JES;
		SjJES[ijet_fromIt][1]=JES_SJ2*JES;

		}// end if else JES JER SD

 //// force to be the same structure of SD0

/*
    fastjet::contrib::SoftDrop * sd0 = new fastjet::contrib::SoftDrop(beta_, 0, R0_ );
    sd0->set_verbose_structure(true);

    if ( MaSDjet == 0 ) {
      //fjClusterSeqRecluster_->delete_self_when_unused();
      if(sd0) { delete sd0; sd0 = 0;}
      continue;
    }
    // if(!transformedJet.has_valid_cluster_sequence()) {
    //   std::cout << "transformedJet does not have a valid cluster sequence" << std::endl;
    // }
    //std::cout << "orig jet pt: " << transformedJet.perp() << std::endl;
    MaSDjet = (*sd0)(MaSDjet);

        if(MaSDjet.has_parents(MaSDsubjet1,MaSDsubjet2)){
          cout<<"ori subjet1 pt ="<<MaSDsubjet1.perp()<<" , subjet2 pt = "<<MaSDsubjet2.perp()<<" Jet pt = "<<MaSDjet.perp()<<endl;
          SJ1pt=MaSDsubjet1.perp(); SJ2pt=MaSDsubjet2.perp();
          cout<<"before JES, Zg = "<<((SJ2pt)/(SJ1pt+SJ2pt))<<" , SJ1pt = "<<SJ1pt<<" ,SJ2pt = "<<SJ2pt<<endl;
          SJ1pt=SJ1pt*(1+JES_SJ1*JES);
          SJ2pt=SJ2pt*(1+JES_SJ2*JES);
					cout<<"JES1 = "<< (1+JES_SJ1*JES)<<" , JES2 = "<<(1+JES_SJ2*JES)<<endl;
          cout<<"after SD0, Zg = "<<((SJ2pt)/(SJ1pt+SJ2pt))<<" , SJ1pt = "<<SJ1pt<<" ,SJ2pt = "<<SJ2pt<<endl;
				}


    fastjet::PseudoJet check0_MaSDsubjet1, check0_MaSDsubjet2;
    MaSDjet.has_parents(check0_MaSDsubjet1,check0_MaSDsubjet2);
    cout<<" before push MaSDsubjet1 pt = "<<check0_MaSDsubjet1.perp()<<" , MaSDsubjet2 pt = "<<check0_MaSDsubjet2.perp()<<endl;
    cout<<" ###### MaSDjet pt = "<<MaSDjet.perp()<<" ,# of constituents "<<MaSDjet.constituents().size()<<endl;


    fjJets_.push_back( MaSDjet );

	  fastjet::PseudoJet check_MaSDsubjet1, check_MaSDsubjet2; 
		MaSDjet.has_parents(check_MaSDsubjet1,check_MaSDsubjet2);
		cout<<"MaSDsubjet1 pt = "<<check_MaSDsubjet1.perp()<<" , MaSDsubjet2 pt = "<<check_MaSDsubjet2.perp()<<endl;
	  cout<<" ###### MaSDjet pt = "<<MaSDjet.perp()<<" ,# of constituents "<<MaSDjet.constituents().size()<<endl;


 /// end force SD0
*/




    // //DEBUGGING BEGIN 
    // std::cout << "SoftDropProducer: " << moduleLabel_ << std::endl; 
    // std::cout << "sym: " << sym << std::endl;
    // std::cout << "#dropped branches: " << ndrop << std::endl;
    // std::cout << "dropped_symmetry.size() " << dropped_symmetry.size() << std::endl;
    // for ( std::vector<double>::const_iterator dsym = dropped_symmetry.begin();
    //       dsym != dropped_symmetry.end(); ++dsym )
    //   std::cout << "dropped symmetry: " << (*dsym) << std::endl;
    
    // std::vector<fastjet::PseudoJet> constituents;
    // if ( transformedJet.has_pieces() )
    //   constituents = transformedJet.pieces();
    // std::vector<fastjet::PseudoJet>::const_iterator itSubJetBegin = constituents.begin(), itSubJet = itSubJetBegin, itSubJetEnd = constituents.end();
    // for (; itSubJet != itSubJetEnd; ++itSubJet ){
    //   fastjet::PseudoJet const & subjet = *itSubJet;
    //   std::cout << "subjet # " << (itSubJet - itSubJetBegin) << ": Pt = " << subjet.pt() << std::endl;
    // }
    // //DEBUGGING END

    lSym.push_back(sym);
    lDroppedBranches.push_back(ndrop);
    lDroppedSym.push_back(dropped_symmetry);
    
    if(sd) { delete sd; sd = 0;}
    //    fjClusterSeqRecluster_->delete_self_when_unused();
    
  }//anti-kt original jet loop
  
  //fjJets_ = fastjet::sorted_by_pt(fjClusterSeq_->inclusive_jets(jetPtMin_));
  
  // fastjet::RecursiveSymmetryCutBase rc(fastjet::SymmetryMeasure::scalar_z,  // the default SymmetryMeasure
  //                                      std::numeric_limits<double>::infinity(), // default is no mass drop
  //                                      fastjet::RecursionChoice::larger_pt, // the default RecursionChoice
  //                                      subtractor);
  // rc.set_grooming_mode();

  //  PseudoJet piece1, piece2;
  //  while (subjet.has_parents(piece1, piece2)) {
  //  double sym;
  //  double pt1 = piece1.pt();
  //  double pt2 = piece2.pt();
  //  make sure denominator is non-zero
  //  sym = pt1 + pt2;
  //  if (sym == 0) return PseudoJet(); 
  //  sym = std::min(pt1, pt2) / sym;
  // }

  //std::cout << "SoftDropProducer::runAlgorithm end" << std::endl;


   for(int iPtBins=0; iPtBins<nPtBins; iPtBins++){
			delete h1[iPtBins];
			delete f1[iPtBins];
    for(int iZgBins=0; iZgBins<nZgBins; iZgBins++){
      delete h2[iPtBins][iZgBins];
    }
   }


	delete fin;
  
}

/// function template to write out the outputs
template< class T>
void SoftDropJetProducer::writeSoftDropJets(  edm::Event & iEvent, edm::EventSetup const& iSetup)
{
  //VirtualJetProducer::writeJetsWithConstituents(iEvent,iSetup);
  if ( verbosity_ >= 1 ) {
    std::cout << "<SoftDropJetProducer::writeSoftDropJets (moduleLabel = " << moduleLabel_ << ")>:" << std::endl;
  }
  //  std::cout << "<SoftDropJetProducer::writeSoftDropJets (moduleLabel = " << moduleLabel_ << ")>:" << std::endl;

  // get a list of output jets
  std::auto_ptr<reco::BasicJetCollection>  jetCollection( new reco::BasicJetCollection() );
  // get a list of output subjets
  std::auto_ptr<std::vector<T> >  subjetCollection( new std::vector<T>() );

  // This will store the handle for the subjets after we write them
  edm::OrphanHandle< std::vector<T> > subjetHandleAfterPut;
  // this is the mapping of subjet to hard jet
  std::vector< std::vector<int> > indices;
  // this is the list of hardjet 4-momenta
  std::vector<math::XYZTLorentzVector> p4_hardJets;
  // this is the hardjet areas
  std::vector<double> area_hardJets;

  // Loop over the hard jets
  //std::cout << "N hard jets: " << fjJets_.size() << std::endl;

  std::vector<fastjet::PseudoJet>::const_iterator it = fjJets_.begin(),
    iEnd = fjJets_.end(),
    iBegin = fjJets_.begin();
  indices.resize( fjJets_.size() );
	

  for ( ; it != iEnd; ++it ) {


    fastjet::PseudoJet const & localJet = *it;
    unsigned int jetIndex = it - iBegin;
    // Get the 4-vector for the hard jet

    p4_hardJets.push_back( math::XYZTLorentzVector(localJet.px(), localJet.py(), localJet.pz(), localJet.e() ));
    double localJetArea = 0.0;
    if ( doAreaFastjet_ && localJet.has_area() ) {
      localJetArea = localJet.area();
    }
    area_hardJets.push_back( localJetArea );

    // create the subjet/constituent list
    std::vector<fastjet::PseudoJet> constituents,ghosts;
    if ( it->has_pieces() ) {
//			cout<<"has_piece"<<endl;
      constituents = it->pieces();
    } else if ( it->has_constituents() ) {
      //constituents = it->constituents();
//			cout<<"no piece, has_constituents"<<endl;
      fastjet::SelectorIsPureGhost().sift(it->constituents(), ghosts, constituents); //filter out ghosts
    }

/*
		cout<<" local jet pt ="<<localJet.perp()<<" , # of constituents = "<<localJet.constituents().size()<<endl;

	  fastjet::PseudoJet check_localsubjet1, check_localsubjet2; 
		localJet.has_parents(check_localsubjet1,check_localsubjet2);
		cout<<"localsubjet1 pt = "<<check_localsubjet1.perp()<<" , localsubjet2 pt = "<<check_localsubjet2.perp()<<endl;

		// test local jet has parents
		fastjet::PseudoJet MaSDsubjet1, MaSDsubjet2;
		if (localJet.has_parents(MaSDsubjet1,MaSDsubjet2)){
			cout<<"\n local jet has parents"<<endl;
			cout<<"subjet1 pt = "<<MaSDsubjet1.perp()<<" , subjet2 pt = "<< MaSDsubjet2.perp()<<endl;
		}
*/
	



    //loop over constituents of jet (can be subjets or normal constituents)
  if(debug_==true)		std::cout << "------------------ jetIndex = "<<jetIndex<<endl;
    // std::cout << "N subjets(or constituents): " << constituents.size() << std::endl;  // print out numer of constitunets
//		double sj1pt=0;
	//	double sj2pt=0;
		// double sjzg=0;

    std::vector<fastjet::PseudoJet>::const_iterator itSubJetBegin = constituents.begin(),
      itSubJet = itSubJetBegin, itSubJetEnd = constituents.end();
    for (; itSubJet != itSubJetEnd; ++itSubJet ){

      fastjet::PseudoJet const & subjet = *itSubJet;
      if ( verbosity_ >= 1 ) {
        std::cout << "subjet #" << (itSubJet - itSubJetBegin) << ": Pt = " << subjet.pt() << ", eta = " << subjet.eta() << ", phi = " << subjet.phi() << ", mass = " << subjet.m()
                  << " (#constituents = " << subjet.constituents().size() << ")" << std::endl;
        std::vector<fastjet::PseudoJet> subjet_constituents = subjet.constituents();
        int idx_constituent = 0;
        for ( std::vector<fastjet::PseudoJet>::const_iterator constituent = subjet_constituents.begin();
              constituent != subjet_constituents.end(); ++constituent ) {
          //if ( constituent->pt() < 1.e-3 ) continue; // CV: skip ghosts
          std::cout << "  constituent #" << idx_constituent << ": Pt = " << constituent->pt() << ", eta = " << constituent->eta() << ", phi = " << constituent->phi() << ","
                    << " mass = " << constituent->m() << std::endl;
          ++idx_constituent;
        }
      }

        math::XYZTLorentzVector p4Subjet(subjet.px(), subjet.py(), subjet.pz(), subjet.e() );
        // cout<<"p4sj.X() = "<<p4Subjet.X()<<endl;
//				p4Subjet.SetXYZT(1,1,1,1);
				// cout<<"p4sj.X() = "<<p4Subjet.X()<<endl;

			// cout<<"constituents size = "<<constituents.size()<<endl;
			if(JESpt0_!=0.0 || JESpt1_!=0.0 || JER_!=false){
//				cout<<"save JES SD"<<endl;
			if( constituents.size()==2){
				if(itSubJet==itSubJetBegin){
      	p4Subjet.SetXYZT(subjet.px()*(1+SjJES[jetIndex][0]), subjet.py()*(1+SjJES[jetIndex][0]), subjet.pz(), subjet.e() );
				// sj1pt=subjet.perp()*((1+SjJES[jetIndex][0]));
        if(debug_==true)  cout<<"SjJES[ijet][0] = "<<SjJES[jetIndex][0]<<endl;
        if(debug_==true) cout<<" sj1pt = "<<(subjet.perp()*(1+SjJES[jetIndex][0]))<<endl;
				}else{
        p4Subjet.SetXYZT(subjet.px()*(1+SjJES[jetIndex][1]), subjet.py()*(1+SjJES[jetIndex][1]), subjet.pz(), subjet.e() );
				// sj2pt=subjet.perp()*(1+SjJES[jetIndex][1]);
				// sjzg=sj2pt/(sj2pt+sj1pt);
				// cout<<"sj2 ori pt"<<subjet.perp()<<" SjJES[1] = "<<SjJES[jetIndex][1]<<endl;
				if(debug_==true) cout<<" sj2pt = "<<(subjet.perp()*(1+SjJES[jetIndex][1]))<<endl;
        // cout<<"SjJES[ijet][1] = "<<SjJES[jetIndex][1]<<endl;
				}
			}
			}

			// cout<<"subjet.px = "<<subjet.px()<<" , subjet.py = "<<subjet.py()<<endl;
        // cout<<"p4sj.X() = "<<p4Subjet.X()<<endl;

      reco::Particle::Point point(0,0,0);

      // This will hold ptr's to the subjets/constituents -> MV: not used?
      std::vector<reco::CandidatePtr> subjetConstituents;

      // Get the transient subjet constituents from fastjet
      std::vector<reco::CandidatePtr> constituentsOfSubjet;
      if(subjet.has_constituents()) {
        std::vector<fastjet::PseudoJet> subjetFastjetConstituents = subjet.constituents();
        constituentsOfSubjet = getConstituents(subjetFastjetConstituents );
      }
      indices[jetIndex].push_back( subjetCollection->size() );

      // Add the concrete subjet type to the subjet list to write to event record
      T jet;
      reco::writeSpecific( jet, p4Subjet, point, constituentsOfSubjet, iSetup);
      double subjetArea = 0.0;
      if ( doAreaFastjet_ && itSubJet->has_area() ){
        subjetArea = itSubJet->area();
      }
      jet.setJetArea( subjetArea );
      subjetCollection->push_back( jet );
    }
  }
  // put subjets into event record
  subjetHandleAfterPut = iEvent.put( subjetCollection, jetCollInstanceName_ );
  
  // Now create the hard jets with ptr's to the subjets as constituents
  std::vector<math::XYZTLorentzVector>::const_iterator ip4 = p4_hardJets.begin(),
    ip4Begin = p4_hardJets.begin(),
    ip4End = p4_hardJets.end();

  for ( ; ip4 != ip4End; ++ip4 ) {
    int p4_index = ip4 - ip4Begin;
    std::vector<int> & ind = indices[p4_index];
    std::vector<reco::CandidatePtr> i_hardJetConstituents;
    // Add the subjets to the hard jet
    for( std::vector<int>::const_iterator isub = ind.begin();
         isub != ind.end(); ++isub ) {
      reco::CandidatePtr candPtr( subjetHandleAfterPut, *isub, false );
      i_hardJetConstituents.push_back( candPtr );
    }
    reco::Particle::Point point(0,0,0);
    reco::BasicJet toput( *ip4, point, i_hardJetConstituents);
    toput.setJetArea( area_hardJets[ip4 - ip4Begin] );
    jetCollection->push_back( toput );
  }

  // put hard jets into event record
  edm::OrphanHandle<std::vector<reco::BasicJet> > jetHandleAfterPut = iEvent.put( jetCollection);

  //Fill it into the event
  std::auto_ptr<edm::ValueMap<float> > lSymOut(new edm::ValueMap<float>());
  edm::ValueMap<float>::Filler  lSymFiller(*lSymOut);
  lSymFiller.insert(jetHandleAfterPut,lSym.begin(),lSym.end());
  lSymFiller.fill();
  iEvent.put(lSymOut,"sym");

  std::auto_ptr<edm::ValueMap<int> > lDroppedBranchesOut(new edm::ValueMap<int>());
  edm::ValueMap<int>::Filler  lDroppedBranchesFiller(*lDroppedBranchesOut);
  lDroppedBranchesFiller.insert(jetHandleAfterPut,lDroppedBranches.begin(),lDroppedBranches.end());
  lDroppedBranchesFiller.fill();
  iEvent.put(lDroppedBranchesOut,"droppedBranches");

  //edm::AssociationVector<reco::JetRefBaseProd,std::vector<double>> >
  //edm::Association<std::vector<double>> lDroppedSymOut(new edm::Association<std::vector<double>>());
  //edm::Association<std::vector<double>>::Filler lDroppedSymFiller(*lDroppedSymOut);
  //lDroppedSymFiller.insert(jetHandleAfterPut,lDroppedSym.begin(),lDroppedSym.end());
  //lDroppedSymFiller.fill();
  //iEvent.put(lDroppedSymOut,"droppedSym");


  // std::auto_ptr<edm::ValueMap<std::vector<double>> > lDroppedSymOut(new edm::ValueMap<std::vector<double>>());
  // edm::ValueMap<std::vector<double>>::Filler  lDroppedSymFiller(*lDroppedSymOut);
  // lDroppedSymFiller.insert(jetHandleAfterPut,lDroppedSym.begin(),lDroppedSym.end());
  // lDroppedSymFiller.fill();
  // iEvent.put(lDroppedSymOut,"droppedSym");
  
  
}

////////////////////////////////////////////////////////////////////////////////
// define as cmssw plugin
////////////////////////////////////////////////////////////////////////////////

DEFINE_FWK_MODULE(SoftDropJetProducer);
