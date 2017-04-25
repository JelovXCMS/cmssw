#define akSoftDrop4PFJetSelector_cxx
// The class definition in akSoftDrop4PFJetSelector.h has been generated automatically
// by the ROOT utility TTree::MakeSelector(). This class is derived
// from the ROOT class TSelector. For more information on the TSelector
// framework see $ROOTSYS/README/README.SELECTOR or the ROOT User Manual.

// The following methods are defined in this file:
//    Begin():        called every time a loop on the tree starts,
//                    a convenient place to create your histograms.
//    SlaveBegin():   called after Begin(), when on PROOF called only on the
//                    slave servers.
//    Process():      called for each event, in this function you decide what
//                    to read and fill your histograms.
//    SlaveTerminate: called at the end of the loop on the tree, when on PROOF
//                    called only on the slave servers.
//    Terminate():    called at the end of the loop on the tree,
//                    a convenient place to draw/fit your histograms.
//
// To use this file, try the following session on your Tree T:
//
// root> T->Process("akSoftDrop4PFJetSelector.C")
// root> T->Process("akSoftDrop4PFJetSelector.C","some options")
// root> T->Process("akSoftDrop4PFJetSelector.C+")
//

#include "akSoftDrop4PFJetSelector.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TH1F.h>
#include <TLegend.h>
#include <TMath.h>

void akSoftDrop4PFJetSelector::Begin(TTree * /*tree*/)
{
	// The Begin() function is called at the start of the query.
	// When running with PROOF Begin() is only called on the client.
	// The tree argument is deprecated (on PROOF 0 is passed).

	TString option = GetOption();

	f_out = new TFile("fout.root","RECREATE");

	// initialize object (tree, histograms varaible) to empty. needed??
	//	 t_akSD4PFJet = 0;

	//	 h_JetPt = 0;
	//	 h_LeadJetSubPt2ov1 = 0 ;
	//	 fProcessed =0 ;


}

void akSoftDrop4PFJetSelector::SlaveBegin(TTree * /*tree*/)
{
	// The SlaveBegin() function is called after the Begin() function.
	// When running with PROOF SlaveBegin() is called on each slave server.
	// The tree argument is deprecated (on PROOF 0 is passed).

	TString option = GetOption();

	// Init(tree); // no need , Init automatically load after Slave Begin.

	/// book histogram & tree here , object has create before here, not here, ex TH1D *h = new TH1D(..) here will send error.

	h_JetPt = new TH1D("h_JetPt","h_JetPt",100,0,400);

	cout<<"slaveBegin"<<endl;

	h_LeadJetSubPt2ov1= new TH1D("h_LeadJetSubPt2ov1","h_LeadJetSubPt2ov1",100,0,2);	

	cout<<"slaveBegin before branch"<<endl;

	t_akSD4PFJet= new TTree("t_akSD4PFJet","t_akSD4PFJet");

	t_akSD4PFJet->Branch("rawpt", &rawpt_);
	cout<<"slaveBegin first branch"<<endl;

	t_akSD4PFJet->Branch("jtpt", &jtpt_);
	t_akSD4PFJet->Branch("jteta", &jteta_);
	t_akSD4PFJet->Branch("jty", &jty_);
	t_akSD4PFJet->Branch("jtphi", &jtphi_);

	cout<<"slaveBegin jt branch"<<endl;


	t_akSD4PFJet->Branch("nSubJet", &nSubJet_);
	t_akSD4PFJet->Branch("jtSubJetPt1", &jtSubJetPt1_);
	t_akSD4PFJet->Branch("jtSubJetEta1", &jtSubJetEta1_);
	t_akSD4PFJet->Branch("jtSubJetPhi1", &jtSubJetPhi1_);
	t_akSD4PFJet->Branch("jtSubJetM1", &jtSubJetM1_);
	t_akSD4PFJet->Branch("jtSubJetPt2", &jtSubJetPt2_);
	t_akSD4PFJet->Branch("jtSubJetEta2", &jtSubJetEta2_);
	t_akSD4PFJet->Branch("jtSubJetPhi2", &jtSubJetPhi2_);
	t_akSD4PFJet->Branch("jtSubJetM2", &jtSubJetM2_);

	t_akSD4PFJet->Branch("jtSubJetPt2ov1", &jtSubJetPt2ov1_);
	t_akSD4PFJet->Branch("jtSubZg", &jtSubZg_);
	t_akSD4PFJet->Branch("jtSubJetdR12", &jtSubJetdR12_);

	cout<<"slaveBegin jtsub branch"<<endl;

	t_akSD4PFJet->Branch("discr_ssvHighEff", &discr_ssvHighEff_);
	t_akSD4PFJet->Branch("discr_ssvHighPur", &discr_ssvHighPur_);
	t_akSD4PFJet->Branch("discr_csvV1", &discr_csvV1_);
	t_akSD4PFJet->Branch("discr_csvV2", &discr_csvV2_);
	t_akSD4PFJet->Branch("svtxm", &svtxm_);
	t_akSD4PFJet->Branch("svtxpt", &svtxpt_);
	t_akSD4PFJet->Branch("svtxmcorr", &svtxmcorr_);

	cout<<"slaveBegin dis,svt branch"<<endl;


	t_akSD4PFJet->Branch("pthat", &pthat_);
	t_akSD4PFJet->Branch("refpt", &refpt_);
	t_akSD4PFJet->Branch("refeta", &refeta_);
	t_akSD4PFJet->Branch("refy", &refy_);
	t_akSD4PFJet->Branch("refphi", &refphi_);
	cout<<"slaveBegin ref branch"<<endl;

	t_akSD4PFJet->Branch("bProdCode", &bProdCode_);
	t_akSD4PFJet->Branch("cProdCode", &cProdCode_);
	t_akSD4PFJet->Branch("refparton_flavor", &refparton_flavor_);
	t_akSD4PFJet->Branch("refparton_flavorForB", &refparton_flavorForB_);
	t_akSD4PFJet->Branch("refparton_flavorProcess", &refparton_flavorProcess_);
	cout<<"slaveBegin refflavor branch"<<endl;

	// refjet part
	t_akSD4PFJet->Branch("nrefSubJet", &nrefSubJet_);
	t_akSD4PFJet->Branch("refSubJetPt1", &refSubJetPt1_);
	t_akSD4PFJet->Branch("refSubJetEta1", &refSubJetEta1_);
	t_akSD4PFJet->Branch("refSubJetPhi1", &refSubJetPhi1_);
	t_akSD4PFJet->Branch("refSubJetM1", &refSubJetM1_);
	t_akSD4PFJet->Branch("refSubJetPt2", &refSubJetPt2_);
	t_akSD4PFJet->Branch("refSubJetEta2", &refSubJetEta2_);
	t_akSD4PFJet->Branch("refSubJetPhi2", &refSubJetPhi2_);
	t_akSD4PFJet->Branch("refSubJetM2", &refSubJetM2_);

	t_akSD4PFJet->Branch("refSubJetPt2ov1", &refSubJetPt2ov1_);
	t_akSD4PFJet->Branch("refSubZg", &refSubZg_);
	t_akSD4PFJet->Branch("refSubJetdR12", &refSubJetdR12_);



	/* not use now, 
		 t_akSD4PFJet->Branch("refSubJetPt", &refSubJetPt_);
		 t_akSD4PFJet->Branch("refSubJetEta", &refSubJetEta_);
		 t_akSD4PFJet->Branch("refSubJetPhi", &refSubJetPhi_);
		 t_akSD4PFJet->Branch("refSubJetM", &refSubJetM_);

		 t_akSD4PFJet->Branch("genpt", &genpt_);
		 t_akSD4PFJet->Branch("geneta", &geneta_);
		 t_akSD4PFJet->Branch("geny", &geny_);
		 t_akSD4PFJet->Branch("genphi", &genphi_);
		 t_akSD4PFJet->Branch("genSubJetPt", &genSubJetPt_);
		 t_akSD4PFJet->Branch("genSubJetEta", &genSubJetEta_);
		 t_akSD4PFJet->Branch("genSubJetPhi", &genSubJetPhi_);
		 t_akSD4PFJet->Branch("genSubJetM", &genSubJetM_);
		 */

	t_akSD4PFJet->Branch("refGSP_gpt",                    &refGSP_gpt_);                 
	t_akSD4PFJet->Branch("refGSP_geta",                   &refGSP_geta_);  
	t_akSD4PFJet->Branch("refGSP_gphi",                   &refGSP_gphi_);  
	t_akSD4PFJet->Branch("refGSP_gidx",                   &refGSP_gidx_);  
	t_akSD4PFJet->Branch("refGSP_b1pt",                   &refGSP_b1pt_);  
	t_akSD4PFJet->Branch("refGSP_b1eta",                  &refGSP_b1eta_); 
	t_akSD4PFJet->Branch("refGSP_b1phi",                  &refGSP_b1phi_); 
	t_akSD4PFJet->Branch("refGSP_b2pt",                   &refGSP_b2pt_);  
	t_akSD4PFJet->Branch("refGSP_b2eta",                  &refGSP_b2eta_); 
	t_akSD4PFJet->Branch("refGSP_b2phi",                  &refGSP_b2phi_); 
	t_akSD4PFJet->Branch("refGSP_b1Match_jtdR",           &refGSP_b1Match_jtdR_);   
	t_akSD4PFJet->Branch("refGSP_b2Match_jtdR",           &refGSP_b2Match_jtdR_);   
	t_akSD4PFJet->Branch("refGSP_bbdR",                   &refGSP_bbdR_);   
	t_akSD4PFJet->Branch("refGSP_bbzg",                   &refGSP_bbzg_);   
	t_akSD4PFJet->Branch("refGSP_SubJtMatched",           &refGSP_SubJtMatched_);   
	//
	t_akSD4PFJet->Branch("refGSP_b1Match_SubJt1dR",       &refGSP_b1Match_SubJt1dR_); 
	t_akSD4PFJet->Branch("refGSP_b1Match_SubJt2dR",       &refGSP_b1Match_SubJt2dR_); 
	t_akSD4PFJet->Branch("refGSP_b2Match_SubJt1dR",       &refGSP_b2Match_SubJt1dR_); 
	t_akSD4PFJet->Branch("refGSP_b2Match_SubJt2dR",       &refGSP_b2Match_SubJt2dR_); 
	t_akSD4PFJet->Branch("refGSP_bbSubJt_dRMatchStatus",                  &refGSP_bbSubJt_dRMatchStatus_);                            
	t_akSD4PFJet->Branch("refGSP_bbSubJt_dR0p1MatchStatus",               &refGSP_bbSubJt_dR0p1MatchStatus_);     
	t_akSD4PFJet->Branch("refGSP_b1Match_SubJt1PtRat",                    &refGSP_b1Match_SubJt1PtRat_);          
	t_akSD4PFJet->Branch("refGSP_b1Match_SubJt2PtRat",                    &refGSP_b1Match_SubJt2PtRat_);
	t_akSD4PFJet->Branch("refGSP_b2Match_SubJt1PtRat",                    &refGSP_b2Match_SubJt1PtRat_);
	t_akSD4PFJet->Branch("refGSP_b2Match_SubJt2PtRat",                    &refGSP_b2Match_SubJt2PtRat_);               
	t_akSD4PFJet->Branch("refGSP_bbSubJt_PtRatMatchStatus",               &refGSP_bbSubJt_PtRatMatchStatus_);     
	t_akSD4PFJet->Branch("refGSP_bbSubJt_PtRatTightMatchStatus",          &refGSP_bbSubJt_PtRatTightMatchStatus_);     
	t_akSD4PFJet->Branch("refGSP_bbSubJt_MatchStatus",                    &refGSP_bbSubJt_MatchStatus_);          
	// 
	t_akSD4PFJet->Branch("refGSP_b1Match_refSubJt1dR",                    &refGSP_b1Match_refSubJt1dR_);
	t_akSD4PFJet->Branch("refGSP_b1Match_refSubJt2dR",                    &refGSP_b1Match_refSubJt2dR_);
	t_akSD4PFJet->Branch("refGSP_b2Match_refSubJt1dR",                    &refGSP_b2Match_refSubJt1dR_);
	t_akSD4PFJet->Branch("refGSP_b2Match_refSubJt2dR",                    &refGSP_b2Match_refSubJt2dR_);
	t_akSD4PFJet->Branch("refGSP_bbrefSubJt_dRMatchStatus",  			        &refGSP_bbrefSubJt_dRMatchStatus_);  			
	t_akSD4PFJet->Branch("refGSP_bbrefSubJt_dR0p1MatchStatus", 		        &refGSP_bbrefSubJt_dR0p1MatchStatus_); 		
	t_akSD4PFJet->Branch("refGSP_b1Match_refSubJt1PtRat", 					      &refGSP_b1Match_refSubJt1PtRat_); 					
	t_akSD4PFJet->Branch("refGSP_b1Match_refSubJt2PtRat",                 &refGSP_b1Match_refSubJt2PtRat_);
	t_akSD4PFJet->Branch("refGSP_b2Match_refSubJt1PtRat",                 &refGSP_b2Match_refSubJt1PtRat_);
	t_akSD4PFJet->Branch("refGSP_b2Match_refSubJt2PtRat",                 &refGSP_b2Match_refSubJt2PtRat_);            
	t_akSD4PFJet->Branch("refGSP_bbrefSubJt_PtRatMatchStatus", 		        &refGSP_bbrefSubJt_PtRatMatchStatus_); 		
	t_akSD4PFJet->Branch("refGSP_bbrefSubJt_PtRatTightMatchStatus",       &refGSP_bbrefSubJt_PtRatTightMatchStatus_);  
	t_akSD4PFJet->Branch("refGSP_bbrefSubJt_MatchStatus", 					      &refGSP_bbrefSubJt_MatchStatus_); 					

	cout<<"slaveBegin refFlavorID "<<endl;

	t_akSD4PFJet->Branch("refFlavorID_jet_hadronID", &refFlavorID_jet_hadronID_);
  t_akSD4PFJet->Branch("refFlavorID_jet_partonID", &refFlavorID_jet_partonID_);
  t_akSD4PFJet->Branch("refFlavorID_jet_ID", &refFlavorID_jet_ID_);

  t_akSD4PFJet->Branch("refFlavorID_Subjet1_hadronID", &refFlavorID_Subjet1_hadronID_);
  t_akSD4PFJet->Branch("refFlavorID_Subjet1_partonID", &refFlavorID_Subjet1_partonID_);
  t_akSD4PFJet->Branch("refFlavorID_Subjet1_ID", &refFlavorID_Subjet1_ID_);

  t_akSD4PFJet->Branch("refFlavorID_Subjet2_hadronID", &refFlavorID_Subjet2_hadronID_);
  t_akSD4PFJet->Branch("refFlavorID_Subjet2_partonID", &refFlavorID_Subjet2_partonID_);
  t_akSD4PFJet->Branch("refFlavorID_Subjet2_ID", &refFlavorID_Subjet2_ID_);



	fOutput->Add(h_JetPt);
	fOutput->Add(h_LeadJetSubPt2ov1);
	fOutput->Add(t_akSD4PFJet);


	/*
		 TTree *recoTree = new TTree("recoTree","recoTree");
		 recoTree->Branch("Dsize",&Dsize);
		 recoTree->Branch("Dpt",Dpt,"Dpt[Dsize]/F");
		 recoTree->Branch("Dmass",Dmass,"Dmass[Dsize]/F");
		 recoTree->Branch("NewLeaf",&NewLeaf);	
		 */

	cout<<"slaveBegin end"<<endl;



}

Bool_t akSoftDrop4PFJetSelector::Process(Long64_t entry)
{
	// The Process() function is called for each entry in the tree (or possibly
	// keyed object in the case of PROOF) to be processed. The entry argument
	// specifies which entry in the currently loaded tree is to be processed.
	// It can be passed to either akSoftDrop4PFJetSelector::GetEntry() or TBranch::GetEntry()
	// to read either all or the required parts of the data. When processing
	// keyed objects with PROOF, the object is already loaded and is available
	// via the fObject pointer.
	//
	// This function should contain the "body" of the analysis. It can contain
	// simple or elaborate selection criteria, run algorithms on the data
	// of the event and typically fill histograms.
	//
	// The processing can be stopped by calling Abort().
	//
	// Use fStatus to set the return value of TTree::Process().
	//
	// The return value is currently not used.



	fChain->GetTree()->GetEntry(entry);  // must GetTree first in many Tree in a TChain case.

	fProcessed++;

	for(int iJets = 0 ; iJets<nref; iJets++){
		h_JetPt->Fill(jtpt[iJets]);			
	} // end for iJets<nref;


	// using Iterator to retrieve vector<vector<float> > like "jtSubJetPt",
	for(auto itNref=jtSubJetPt->begin(); itNref !=jtSubJetPt->end(); itNref ++){
		for(auto itNsubJet= itNref->begin(); itNsubJet != itNref->end(); itNsubJet++){
			// hall->Fill(*itNsubJet);
		} // end for itNsubJet != itNref->end();
		if (itNref->size()>=2) // only consider the case a jet has at least two sub-jets
		{ 
			h_LeadJetSubPt2ov1->Fill( itNref->at(1) / itNref->at(0) );

		} // end if itNref->size()>1


	} // end for itNref !=jtSubJetPt->end()


	// writng tree for leading jet only
	rawpt_=								rawpt[0];
	jtpt_= 								jtpt[0];
	jteta_=								jteta[0];
	jty_=									jty[0];
	jtphi_=								jtphi[0];

	discr_ssvHighEff_=		discr_ssvHighEff[0];
	discr_ssvHighPur_=		discr_ssvHighPur[0];
	discr_csvV1_=					discr_csvV1[0];
	discr_csvV2_=					discr_csvV2[0];

	svtxm_= 							svtxm[0];
	svtxpt_=              svtxpt[0];
	svtxmcorr_=           svtxmcorr[0];

	pthat_ = 							pthat;
	refpt_=								refpt[0];  
	refeta_= 							refeta[0];
	refy_=								refy[0]; 
	refphi_=  						refphi[0];   
	bProdCode_=						bProdCode;
	cProdCode_=						cProdCode;
	refparton_flavor_=            refparton_flavor[0];         
	refparton_flavorForB_=        refparton_flavorForB[0];   
	refparton_flavorProcess_=     refparton_flavorProcess[0];  

	
	refFlavorID_jet_hadronID_ =refFlavorID_jet_hadronID[0];
  refFlavorID_jet_partonID_ =refFlavorID_jet_partonID[0];
	refFlavorID_jet_ID_= refFlavorID_jet_hadronID_;
	if(refFlavorID_jet_ID_==0){refFlavorID_jet_ID_=refFlavorID_jet_partonID_ ; }
  refFlavorID_Subjet1_hadronID_ =refFlavorID_Subjet1_hadronID[0];
  refFlavorID_Subjet1_partonID_ =refFlavorID_Subjet1_partonID[0];
  refFlavorID_Subjet1_ID_= refFlavorID_Subjet1_hadronID_;
  if(refFlavorID_Subjet1_ID_==0){refFlavorID_Subjet1_ID_=refFlavorID_Subjet1_partonID_ ; }
  refFlavorID_Subjet2_hadronID_ =refFlavorID_Subjet2_hadronID[0];
  refFlavorID_Subjet2_partonID_ =refFlavorID_Subjet2_partonID[0];
  refFlavorID_Subjet2_ID_= refFlavorID_Subjet2_hadronID_;
  if(refFlavorID_Subjet2_ID_==0){refFlavorID_Subjet2_ID_=refFlavorID_Subjet2_partonID_ ; }


	// jtSubJet part
	nSubJet_=-1;
	nSubJet_= jtSubJetPt->at(0).size(); // sub-jet of leading jet
	jtSubJetPt1_   =-999;			 
	jtSubJetEta1_  =-999;        
	jtSubJetPhi1_  =-999;          
	jtSubJetM1_    =-999;            
	jtSubJetPt2_   =-999;            
	jtSubJetEta2_  =-999;          
	jtSubJetPhi2_  =-999;          
	jtSubJetM2_    =-999;      
	jtSubJetPt2ov1_=-999;           
	jtSubJetdR12_ =-999;
	if(nSubJet_>=2){
		jtSubJetPt1_   = jtSubJetPt->at(0).at(0);
		jtSubJetEta1_  = jtSubJetEta->at(0).at(0);
		jtSubJetPhi1_  = jtSubJetPhi->at(0).at(0);
		jtSubJetM1_    = jtSubJetM->at(0).at(0);
		jtSubJetPt2_   = jtSubJetPt->at(0).at(1);
		jtSubJetEta2_  = jtSubJetEta->at(0).at(1);
		jtSubJetPhi2_  = jtSubJetPhi->at(0).at(1);
		jtSubJetM2_    = jtSubJetM->at(0).at(1);
		jtSubJetPt2ov1_= jtSubJetPt->at(0).at(1)/jtSubJetPt->at(0).at(0);
		jtSubZg_       = jtSubJetPt2_/( jtSubJetPt1_ + jtSubJetPt2_);

		//		cout<<"jtSubJetPhi1_ = "<<jtSubJetPhi1_<<endl; //" , *3.14/180 = "<<jtSubJetPhi1_*3.14/180<<endl;
		//		cout<<"jtSubJetPhi2_ = "<<jtSubJetPhi2_<<endl; //" , *3.14/180 = "<<jtSubJetPhi2_*3.14/180<<endl;

		Float_t deltaPhi = (jtSubJetPhi1_- jtSubJetPhi2_); //*(Float_t)TMath::Pi()/(Float_t)180.0;
		//		cout<<"original deltaPhi = "<<deltaPhi<<endl;
		if (deltaPhi < -(Float_t)TMath::Pi()) deltaPhi+=2*(Float_t)TMath::Pi();
		if (deltaPhi >  (Float_t)TMath::Pi()) deltaPhi-=2*(Float_t)TMath::Pi();	
		//	cout<<"(flaot)TMath pi = "<<(Float_t)TMath::Pi()<<" , TMath::Pi() = "<<TMath::Pi()<<endl;
		//		cout<<"deltaPhi = "<<deltaPhi<<endl;
		//		cout<<"deltaEta = "<<jtSubJetEta1_-jtSubJetEta2_<<endl;
		jtSubJetdR12_  = sqrt(pow(jtSubJetEta1_-jtSubJetEta2_,2)+ pow(deltaPhi,2));
		//		cout<<"dR = "<<jtSubJetdR12_<<endl;

	} // end if nSubJet_>=2;

	// refSubJet part
	nrefSubJet_=-1;
	nrefSubJet_= refSubJetPt->at(0).size(); // sub-jet of leading jet
	refSubJetPt1_   =-999;
	refSubJetEta1_  =-999;
	refSubJetPhi1_  =-999;
	refSubJetM1_    =-999;
	refSubJetPt2_   =-999;
	refSubJetEta2_  =-999;
	refSubJetPhi2_  =-999;
	refSubJetM2_    =-999;
	refSubJetPt2ov1_=-999;
	refSubJetdR12_ =-999;
	if(nrefSubJet_>=2){
		refSubJetPt1_   = refSubJetPt->at(0).at(0);
		refSubJetEta1_  = refSubJetEta->at(0).at(0);
		refSubJetPhi1_  = refSubJetPhi->at(0).at(0);
		refSubJetM1_    = refSubJetM->at(0).at(0);
		refSubJetPt2_   = refSubJetPt->at(0).at(1);
		refSubJetEta2_  = refSubJetEta->at(0).at(1);
		refSubJetPhi2_  = refSubJetPhi->at(0).at(1);
		refSubJetM2_    = refSubJetM->at(0).at(1);
		refSubJetPt2ov1_= refSubJetPt->at(0).at(1)/refSubJetPt->at(0).at(0);
		refSubZg_       = refSubJetPt2_/( refSubJetPt1_ + refSubJetPt2_);

		// cout<<"refSubJetPhi1_ = "<<refSubJetPhi1_<<endl; //" , *3.14/180 = "<<refSubJetPhi1_*3.14/180<<endl;
		// cout<<"refSubJetPhi2_ = "<<refSubJetPhi2_<<endl; //" , *3.14/180 = "<<refSubJetPhi2_*3.14/180<<endl;

		Float_t deltaPhi = (refSubJetPhi1_- refSubJetPhi2_); //*(Float_t)TMath::Pi()/(Float_t)180.0;
		// cout<<"original deltaPhi = "<<deltaPhi<<endl;
		if (deltaPhi < -(Float_t)TMath::Pi()) deltaPhi+=2*(Float_t)TMath::Pi();
		if (deltaPhi >  (Float_t)TMath::Pi()) deltaPhi-=2*(Float_t)TMath::Pi();
		//  cout<<"(flaot)TMath pi = "<<(Float_t)TMath::Pi()<<" , TMath::Pi() = "<<TMath::Pi()<<endl;
		// cout<<"deltaPhi = "<<deltaPhi<<endl;
		// cout<<"deltaEta = "<<refSubJetEta1_-refSubJetEta2_<<endl;
		refSubJetdR12_  = sqrt(pow(refSubJetEta1_-refSubJetEta2_,2)+ pow(deltaPhi,2));
		// cout<<"dR = "<<refSubJetdR12_<<endl;

	} // end if nrefSubJet_>=2;

	// refGSP part
	refGSP_gpt_             =refGSP_gpt[0];              
	refGSP_geta_            =refGSP_geta[0];  
	refGSP_gphi_            =refGSP_gphi[0];  
	refGSP_gidx_            =refGSP_gidx[0];  
	refGSP_b1pt_            =refGSP_b1pt[0];  
	refGSP_b1eta_           =refGSP_b1eta[0]; 
	refGSP_b1phi_           =refGSP_b1phi[0]; 
	refGSP_b2pt_            =refGSP_b2pt[0];  
	refGSP_b2eta_           =refGSP_b2eta[0]; 
	refGSP_b2phi_           =refGSP_b2phi[0]; 
	refGSP_b1Match_jtdR_    =refGSP_b1Match_jtdR[0];   
	refGSP_b2Match_jtdR_    =refGSP_b2Match_jtdR[0];   
	refGSP_bbdR_            =refGSP_bbdR[0];  
	refGSP_bbzg_            =refGSP_bbzg[0];  
	refGSP_SubJtMatched_    =refGSP_SubJtMatched[0];   

	refGSP_b1Match_SubJt1dR_ = -1;
	refGSP_b1Match_SubJt2dR_ = -1;
	refGSP_b2Match_SubJt1dR_ = -1;
	refGSP_b2Match_SubJt2dR_ = -1;
	refGSP_bbSubJt_dRMatchStatus_ = -1;        
	refGSP_bbSubJt_dR0p1MatchStatus_ = -1;     
	refGSP_b1Match_SubJt1PtRat_ = -1;          
	refGSP_b1Match_SubJt2PtRat_ = -1;
	refGSP_b2Match_SubJt1PtRat_ = -1;
	refGSP_b2Match_SubJt2PtRat_ = -1;                                      
	refGSP_bbSubJt_PtRatMatchStatus_ = -1;     
	refGSP_bbSubJt_PtRatTightMatchStatus_ = -1;                                      
	refGSP_bbSubJt_MatchStatus_ = -1;          

	refGSP_b1Match_refSubJt1dR_ = -1;
	refGSP_b1Match_refSubJt2dR_ = -1;
	refGSP_b2Match_refSubJt1dR_ = -1;
	refGSP_b2Match_refSubJt2dR_ = -1;
	refGSP_bbrefSubJt_dRMatchStatus_ = -1;  			
	refGSP_bbrefSubJt_dR0p1MatchStatus_ = -1; 		
	refGSP_b1Match_refSubJt1PtRat_ = -1; 					
	refGSP_b1Match_refSubJt2PtRat_ = -1;
	refGSP_b2Match_refSubJt1PtRat_ = -1;
	refGSP_b2Match_refSubJt2PtRat_ = -1;                                         
	refGSP_bbrefSubJt_PtRatMatchStatus_ = -1; 		
	refGSP_bbrefSubJt_PtRatTightMatchStatus_ = -1;                                         
	refGSP_bbrefSubJt_MatchStatus_ = -1; 					



	// modify refGSP_SubJtMatched_ dr value
	//		if(refGSP_SubJtMatched_==1) refGSP_SubJtMatched_=0;
	//	  if(refGSP_b1Match_jtdR_ <0.3 && refGSP_b2Match_jtdR_ <0.3) refGSP_SubJtMatched_=1;


	if (refGSP_SubJtMatched_==1 && refGSP_b2pt_>refGSP_b1pt_){
		cout<<"hello in one reco jet 2pt > 1pt"<<endl;  // why this appear  // the findParton ask exact flavor, not abs(flavor)
	}

	if (refGSP_SubJtMatched_==1 && nSubJet_>=2){
    // dR Match
		refGSP_b1Match_SubJt1dR_ =pow( pow(refGSP_b1eta_- jtSubJetEta1_,2)+pow(delta_Phi(refGSP_b1phi_,jtSubJetPhi1_),2) , 0.5);
		refGSP_b1Match_SubJt2dR_ =pow( pow(refGSP_b1eta_- jtSubJetEta2_,2)+pow(delta_Phi(refGSP_b1phi_,jtSubJetPhi2_),2) , 0.5);
		refGSP_b2Match_SubJt1dR_ =pow( pow(refGSP_b2eta_- jtSubJetEta1_,2)+pow(delta_Phi(refGSP_b2phi_,jtSubJetPhi1_),2) , 0.5);
		refGSP_b2Match_SubJt2dR_ =pow( pow(refGSP_b2eta_- jtSubJetEta2_,2)+pow(delta_Phi(refGSP_b2phi_,jtSubJetPhi2_),2) , 0.5);

		refGSP_bbSubJt_dRMatchStatus_=0;
		if (refGSP_b1Match_SubJt1dR_ < refGSP_b1Match_SubJt2dR_ && refGSP_b2Match_SubJt1dR_ > refGSP_b2Match_SubJt2dR_) { refGSP_bbSubJt_dRMatchStatus_=1; }
		if (refGSP_b1Match_SubJt1dR_ > refGSP_b1Match_SubJt2dR_ && refGSP_b2Match_SubJt1dR_ < refGSP_b2Match_SubJt2dR_) { refGSP_bbSubJt_dRMatchStatus_=2; }

		refGSP_bbSubJt_dR0p1MatchStatus_=0;
		if(refGSP_bbSubJt_dRMatchStatus_==1 && refGSP_b1Match_SubJt1dR_ <0.1 && refGSP_b1Match_SubJt2dR_ >0.1 && refGSP_b2Match_SubJt2dR_<0.1 && refGSP_b2Match_SubJt1dR_ >0.1) {refGSP_bbSubJt_dR0p1MatchStatus_=1;}
    if(refGSP_bbSubJt_dRMatchStatus_==2 && refGSP_b1Match_SubJt1dR_ >0.1 && refGSP_b1Match_SubJt2dR_ <0.1 && refGSP_b2Match_SubJt2dR_>0.1 && refGSP_b2Match_SubJt1dR_ <0.1) {refGSP_bbSubJt_dR0p1MatchStatus_=2;}

		// pt Match
		if (jtSubJetPt1_ >0){ refGSP_b1Match_SubJt1PtRat_=refGSP_b1pt_ / jtSubJetPt1_ ; }
    if (jtSubJetPt2_ >0){ refGSP_b1Match_SubJt2PtRat_=refGSP_b1pt_ / jtSubJetPt2_ ; }
    if (jtSubJetPt1_ >0){ refGSP_b2Match_SubJt1PtRat_=refGSP_b2pt_ / jtSubJetPt1_ ; }
    if (jtSubJetPt2_ >0){ refGSP_b2Match_SubJt2PtRat_=refGSP_b2pt_ / jtSubJetPt2_ ; }

		refGSP_bbSubJt_PtRatMatchStatus_=0;
		if(abs(refGSP_b1Match_SubJt1PtRat_-1) < abs(refGSP_b1Match_SubJt2PtRat_-1) && abs(refGSP_b2Match_SubJt1PtRat_ -1) > abs(refGSP_b2Match_SubJt2PtRat_-1))
		{ refGSP_bbSubJt_PtRatMatchStatus_=1 ; }
    if(abs(refGSP_b1Match_SubJt1PtRat_-1) > abs(refGSP_b1Match_SubJt2PtRat_-1) && abs(refGSP_b2Match_SubJt1PtRat_ -1) < abs(refGSP_b2Match_SubJt2PtRat_-1))
    { refGSP_bbSubJt_PtRatMatchStatus_=2 ; }

		refGSP_bbSubJt_PtRatTightMatchStatus_=0;
	  float dPtRcut=0.3;
		if( refGSP_bbSubJt_PtRatMatchStatus_==1 && abs(refGSP_b1Match_SubJt1PtRat_-1) < dPtRcut &&  abs(refGSP_b2Match_SubJt2PtRat_-1)<dPtRcut)
		{refGSP_bbSubJt_PtRatTightMatchStatus_=1;}
    if( refGSP_bbSubJt_PtRatMatchStatus_==2 && abs(refGSP_b1Match_SubJt2PtRat_-1) < dPtRcut &&  abs(refGSP_b2Match_SubJt1PtRat_-1)<dPtRcut)
    {refGSP_bbSubJt_PtRatTightMatchStatus_=2;}

		// pt & dR match
		refGSP_bbSubJt_MatchStatus_=0;
		if(refGSP_bbSubJt_dRMatchStatus_==1 && refGSP_bbSubJt_PtRatMatchStatus_==1) { refGSP_bbSubJt_MatchStatus_=1;}
    if(refGSP_bbSubJt_dRMatchStatus_==2 && refGSP_bbSubJt_PtRatMatchStatus_==2) { refGSP_bbSubJt_MatchStatus_=2;}

		refGSP_bbSubJt_TightMatchStatus_=0;
		if(refGSP_bbSubJt_dR0p1MatchStatus_==1 && refGSP_bbSubJt_PtRatTightMatchStatus_ ==1) {refGSP_bbSubJt_TightMatchStatus_=1;}
    if(refGSP_bbSubJt_dR0p1MatchStatus_==2 && refGSP_bbSubJt_PtRatTightMatchStatus_ ==2) {refGSP_bbSubJt_TightMatchStatus_=2;}

	} // end if (refGSP_SubJtMatched_==1 && nSubJet_>=2)


	if (refGSP_SubJtMatched_==1 && nrefSubJet_>=2){
    // dR Match
		refGSP_b1Match_refSubJt1dR_ =pow( pow(refGSP_b1eta_- refSubJetEta1_,2)+pow(delta_Phi(refGSP_b1phi_,refSubJetPhi1_),2) , 0.5);
		refGSP_b1Match_refSubJt2dR_ =pow( pow(refGSP_b1eta_- refSubJetEta2_,2)+pow(delta_Phi(refGSP_b1phi_,refSubJetPhi2_),2) , 0.5);
		refGSP_b2Match_refSubJt1dR_ =pow( pow(refGSP_b2eta_- refSubJetEta1_,2)+pow(delta_Phi(refGSP_b2phi_,refSubJetPhi1_),2) , 0.5);
		refGSP_b2Match_refSubJt2dR_ =pow( pow(refGSP_b2eta_- refSubJetEta2_,2)+pow(delta_Phi(refGSP_b2phi_,refSubJetPhi2_),2) , 0.5);

		refGSP_bbrefSubJt_dRMatchStatus_=0;
		if (refGSP_b1Match_refSubJt1dR_ < refGSP_b1Match_refSubJt2dR_ && refGSP_b2Match_refSubJt1dR_ > refGSP_b2Match_refSubJt2dR_) { refGSP_bbrefSubJt_dRMatchStatus_=1; }
		if (refGSP_b1Match_refSubJt1dR_ > refGSP_b1Match_refSubJt2dR_ && refGSP_b2Match_refSubJt1dR_ < refGSP_b2Match_refSubJt2dR_) { refGSP_bbrefSubJt_dRMatchStatus_=2; }

		refGSP_bbrefSubJt_dR0p1MatchStatus_=0;
		if(refGSP_bbrefSubJt_dRMatchStatus_==1 && refGSP_b1Match_refSubJt1dR_ <0.1 && refGSP_b1Match_refSubJt2dR_ >0.1 && refGSP_b2Match_refSubJt2dR_<0.1 && refGSP_b2Match_refSubJt1dR_ >0.1) {refGSP_bbrefSubJt_dR0p1MatchStatus_=1;}
    if(refGSP_bbrefSubJt_dRMatchStatus_==2 && refGSP_b1Match_refSubJt1dR_ >0.1 && refGSP_b1Match_refSubJt2dR_ <0.1 && refGSP_b2Match_refSubJt2dR_>0.1 && refGSP_b2Match_refSubJt1dR_ <0.1) {refGSP_bbrefSubJt_dR0p1MatchStatus_=2;}

		// pt Match
		if (refSubJetPt1_ >0){ refGSP_b1Match_refSubJt1PtRat_=refGSP_b1pt_ / refSubJetPt1_ ; }
    if (refSubJetPt2_ >0){ refGSP_b1Match_refSubJt2PtRat_=refGSP_b1pt_ / refSubJetPt2_ ; }
    if (refSubJetPt1_ >0){ refGSP_b2Match_refSubJt1PtRat_=refGSP_b2pt_ / refSubJetPt1_ ; }
    if (refSubJetPt2_ >0){ refGSP_b2Match_refSubJt2PtRat_=refGSP_b2pt_ / refSubJetPt2_ ; }

		refGSP_bbrefSubJt_PtRatMatchStatus_=0;
		if(abs(refGSP_b1Match_refSubJt1PtRat_-1) < abs(refGSP_b1Match_refSubJt2PtRat_-1) && abs(refGSP_b2Match_refSubJt1PtRat_ -1) > abs(refGSP_b2Match_refSubJt2PtRat_-1))
		{ refGSP_bbrefSubJt_PtRatMatchStatus_=1 ; }
    if(abs(refGSP_b1Match_refSubJt1PtRat_-1) > abs(refGSP_b1Match_refSubJt2PtRat_-1) && abs(refGSP_b2Match_refSubJt1PtRat_ -1) < abs(refGSP_b2Match_refSubJt2PtRat_-1))
    { refGSP_bbrefSubJt_PtRatMatchStatus_=2 ; }

		refGSP_bbrefSubJt_PtRatTightMatchStatus_=0;
	  float dPtRcut=0.3;
		if( refGSP_bbrefSubJt_PtRatMatchStatus_==1 && abs(refGSP_b1Match_refSubJt1PtRat_-1) < dPtRcut &&  abs(refGSP_b2Match_refSubJt2PtRat_-1)<dPtRcut)
		{refGSP_bbrefSubJt_PtRatTightMatchStatus_=1;}
    if( refGSP_bbrefSubJt_PtRatMatchStatus_==2 && abs(refGSP_b1Match_refSubJt2PtRat_-1) < dPtRcut &&  abs(refGSP_b2Match_refSubJt1PtRat_-1)<dPtRcut)
    {refGSP_bbrefSubJt_PtRatTightMatchStatus_=2;}

		// pt & dR match
		refGSP_bbrefSubJt_MatchStatus_=0;
		if(refGSP_bbrefSubJt_dRMatchStatus_==1 && refGSP_bbrefSubJt_PtRatMatchStatus_==1) { refGSP_bbrefSubJt_MatchStatus_=1;}
    if(refGSP_bbrefSubJt_dRMatchStatus_==2 && refGSP_bbrefSubJt_PtRatMatchStatus_==2) { refGSP_bbrefSubJt_MatchStatus_=2;}

		refGSP_bbrefSubJt_TightMatchStatus_=0;
		if(refGSP_bbrefSubJt_dR0p1MatchStatus_==1 && refGSP_bbrefSubJt_PtRatTightMatchStatus_ ==1) {refGSP_bbrefSubJt_TightMatchStatus_=1;}
    if(refGSP_bbrefSubJt_dR0p1MatchStatus_==2 && refGSP_bbrefSubJt_PtRatTightMatchStatus_ ==2) {refGSP_bbrefSubJt_TightMatchStatus_=2;}

	} // end if (refGSP_SubJtMatched_==1 && nrefSubJet_>=2)




	// end of value assign, fill tree
	t_akSD4PFJet->Fill();

	return kTRUE;
}

void akSoftDrop4PFJetSelector::SlaveTerminate()
{
	// The SlaveTerminate() function is called after all entries or objects
	// have been processed. When running with PROOF SlaveTerminate() is called
	// on each slave server.

}

void akSoftDrop4PFJetSelector::Terminate()
{
	// The Terminate() function is the last function to be called during
	// a query. It always runs on the client, it can be used to present
	// the results graphically or save the results to file.

	//// save file
	f_out->cd();

	h_LeadJetSubPt2ov1 = dynamic_cast<TH1D*>(fOutput->FindObject("h_LeadJetSubPt2ov1"));
	h_JetPt = dynamic_cast<TH1D*>(fOutput->FindObject("h_JetPt"));
	t_akSD4PFJet = dynamic_cast<TTree*>(fOutput->FindObject("t_akSD4PFJet"));

	if (h_LeadJetSubPt2ov1) h_LeadJetSubPt2ov1->Write("",TObject::kOverwrite);
	if (h_JetPt) h_JetPt->Write("",TObject::kOverwrite);
	if (t_akSD4PFJet) t_akSD4PFJet->Write("",TObject::kOverwrite);
	//	 f_out->Close();

	cout<<"number of entries process is : "<<fProcessed<<endl;



	//// create TCanvas , plot
	/*
		 TCanvas *c_test = new TCanvas("c_test","c_test",800,800);
		 c_test->Divide(2,2);
		 c_test->cd(1);
		 h_LeadJetSubPt2ov1->Draw();
		 c_test->cd(2);
		 h_JetPt->Draw();
		 */
	int nbin=50;
	double binLow=0;
	double binHigh=1;
/*
	TH1D *h_jtSubJetPt2ov1_nonB = new TH1D("h_jtSubJetPt2ov1_nonB","h_jtSubJetPt2ov1_nonB",nbin,binLow,binHigh);
	TH1D *h_jtSubJetPt2ov1_FCRB = new TH1D("h_jtSubJetPt2ov1_FCRB","h_jtSubJetPt2ov1_FCRB",nbin,binLow,binHigh);
	TH1D *h_jtSubJetPt2ov1_GSPB = new TH1D("h_jtSubJetPt2ov1_GSPB","h_jtSubJetPt2ov1_GSPB",nbin,binLow,binHigh);

	t_akSD4PFJet->Draw("jtSubJetPt2ov1>>h_jtSubJetPt2ov1_GSPB","nSubJet>=2&&abs(refparton_flavorForB)==5&&refparton_flavorProcess==6");
	t_akSD4PFJet->Draw("jtSubJetPt2ov1>>h_jtSubJetPt2ov1_FCRB","nSubJet>=2&&abs(refparton_flavorForB)==5&&refparton_flavorProcess==1");
	t_akSD4PFJet->Draw("jtSubJetPt2ov1>>h_jtSubJetPt2ov1_nonB","nSubJet>=2&&abs(refparton_flavorForB)!=5");

	h_jtSubJetPt2ov1_nonB->Scale(1/h_jtSubJetPt2ov1_nonB->Integral());
	h_jtSubJetPt2ov1_FCRB->Scale(1/h_jtSubJetPt2ov1_FCRB->Integral());
	h_jtSubJetPt2ov1_GSPB->Scale(1/h_jtSubJetPt2ov1_GSPB->Integral());

	gStyle->SetOptStat(0);
	TCanvas *c_jtSubJetPt2ov1 = new TCanvas("c_jtSubJetPt2ov1","c_jtSubJetPt2ov1",800,800);
	c_jtSubJetPt2ov1->cd();
	h_jtSubJetPt2ov1_nonB->SetTitle("");
	h_jtSubJetPt2ov1_nonB->Draw();
	h_jtSubJetPt2ov1_FCRB->SetLineColor(2);
	h_jtSubJetPt2ov1_FCRB->Draw("SAME");
	h_jtSubJetPt2ov1_GSPB->SetLineColor(4);
	h_jtSubJetPt2ov1_GSPB->Draw("SAME");

	TLegend *le_jtSubJetPt2ov1 = new TLegend(0.65,0.60,0.88,0.88,NULL,"brNDC");
	le_jtSubJetPt2ov1->SetBorderSize(0);
	le_jtSubJetPt2ov1->AddEntry((TObject*)0,"Sub-Jet pt2/pt1","");
	le_jtSubJetPt2ov1->AddEntry(h_jtSubJetPt2ov1_nonB,"nonB","l");
	le_jtSubJetPt2ov1->AddEntry(h_jtSubJetPt2ov1_FCRB,"FCR-B","l");
	le_jtSubJetPt2ov1->AddEntry(h_jtSubJetPt2ov1_GSPB,"GSP-B","l");
	le_jtSubJetPt2ov1->Draw("SAME");

	c_jtSubJetPt2ov1->SaveAs("plots/jtSubJetPt2ov1.pdf");
*/
/*
	TH1D *h_jtSubZg_nonB = new TH1D("h_jtSubZg_nonB","h_jtSubZg_nonB",nbin,binLow,binHigh/2); h_jtSubZg_nonB->Sumw2();
	TH1D *h_jtSubZg_FCRB = new TH1D("h_jtSubZg_FCRB","h_jtSubZg_FCRB",nbin,binLow,binHigh/2); h_jtSubZg_FCRB->Sumw2();
	TH1D *h_jtSubZg_GSPB = new TH1D("h_jtSubZg_GSPB","h_jtSubZg_GSPB",nbin,binLow,binHigh/2); h_jtSubZg_GSPB->Sumw2();

	t_akSD4PFJet->Draw("jtSubZg>>h_jtSubZg_GSPB","jtpt>100 && abs(jteta)<2&&nSubJet>=2&&abs(refparton_flavorForB)==5&&( refparton_flavorProcess==5 || refparton_flavorProcess==6)");
	t_akSD4PFJet->Draw("jtSubZg>>h_jtSubZg_FCRB","jtpt>100 && abs(jteta)<2&&nSubJet>=2&&abs(refparton_flavorForB)==5&&refparton_flavorProcess==1");
	t_akSD4PFJet->Draw("jtSubZg>>h_jtSubZg_nonB","jtpt>100 && abs(jteta)<2&&nSubJet>=2&&abs(refparton_flavorForB)!=5");

	h_jtSubZg_nonB->Scale(1/h_jtSubZg_nonB->Integral());
	h_jtSubZg_FCRB->Scale(1/h_jtSubZg_FCRB->Integral());
	h_jtSubZg_GSPB->Scale(1/h_jtSubZg_GSPB->Integral());

	gStyle->SetOptStat(0);
	TCanvas *c_jtSubZg = new TCanvas("c_jtSubZg","c_jtSubZg",800,800);
	c_jtSubZg->cd();
	h_jtSubZg_nonB->GetXaxis()->SetTitle("Zg"); 
	h_jtSubZg_nonB->GetYaxis()->SetTitle("1/N");
	h_jtSubZg_nonB->SetLineColor(1);
	h_jtSubZg_nonB->SetTitle("");
	h_jtSubZg_nonB->Draw();
	h_jtSubZg_FCRB->SetLineColor(2);
	h_jtSubZg_FCRB->Draw("SAME");
	h_jtSubZg_GSPB->SetLineColor(4);
	h_jtSubZg_GSPB->Draw("SAME");

	TLegend *le_jtSubZg = new TLegend(0.65,0.60,0.88,0.88,NULL,"brNDC");
	le_jtSubZg->SetBorderSize(0);
	le_jtSubZg->AddEntry((TObject*)0,"Sub-Jet pt2/pt2+pt1","");
	le_jtSubZg->AddEntry(h_jtSubZg_nonB,"nonB","l");
	le_jtSubZg->AddEntry(h_jtSubZg_FCRB,"FCR-B","l");
	le_jtSubZg->AddEntry(h_jtSubZg_GSPB,"GSP-B","l");
	le_jtSubZg->Draw("SAME");

	c_jtSubZg->SaveAs("plots/jtSubZg.pdf");
*/

	TH1D *h_jtSubZg_dR0p1_nonB = new TH1D("h_jtSubZg_dR0p1_nonB","h_jtSubZg_dR0p1_nonB",nbin,binLow,binHigh/2); h_jtSubZg_dR0p1_nonB->Sumw2();
	TH1D *h_jtSubZg_dR0p1_FCRB = new TH1D("h_jtSubZg_dR0p1_FCRB","h_jtSubZg_dR0p1_FCRB",nbin,binLow,binHigh/2); h_jtSubZg_dR0p1_FCRB->Sumw2();
	TH1D *h_jtSubZg_dR0p1_GSPB = new TH1D("h_jtSubZg_dR0p1_GSPB","h_jtSubZg_dR0p1_GSPB",nbin,binLow,binHigh/2); h_jtSubZg_dR0p1_GSPB->Sumw2();

	t_akSD4PFJet->Draw("jtSubZg>>h_jtSubZg_dR0p1_GSPB","jtSubJetdR12>0.1 && jtpt>100 && abs(jteta)<2&&nSubJet>=2&&abs(refparton_flavorForB)==5&&( refparton_flavorProcess==5 || refparton_flavorProcess==6)");
	t_akSD4PFJet->Draw("jtSubZg>>h_jtSubZg_dR0p1_FCRB","jtSubJetdR12>0.1 && jtpt>100 && abs(jteta)<2&&nSubJet>=2&&abs(refparton_flavorForB)==5&&refparton_flavorProcess==1");
	t_akSD4PFJet->Draw("jtSubZg>>h_jtSubZg_dR0p1_nonB","jtSubJetdR12>0.1 && jtpt>100 && abs(jteta)<2&&nSubJet>=2&&abs(refparton_flavorForB)!=5");

	h_jtSubZg_dR0p1_nonB->Scale(1/h_jtSubZg_dR0p1_nonB->Integral());
	h_jtSubZg_dR0p1_FCRB->Scale(1/h_jtSubZg_dR0p1_FCRB->Integral());
	h_jtSubZg_dR0p1_GSPB->Scale(1/h_jtSubZg_dR0p1_GSPB->Integral());

	gStyle->SetOptStat(0);
	TCanvas *c_jtSubZg_dR0p1 = new TCanvas("c_jtSubZg_dR0p1","c_jtSubZg_dR0p1",800,800);
	c_jtSubZg_dR0p1->cd();
	h_jtSubZg_dR0p1_nonB->GetXaxis()->SetTitle("Zg");
	h_jtSubZg_dR0p1_nonB->GetYaxis()->SetTitle("1/N");
	h_jtSubZg_dR0p1_nonB->SetLineColor(1);
	h_jtSubZg_dR0p1_nonB->SetTitle("");
	h_jtSubZg_dR0p1_nonB->Draw();
	h_jtSubZg_dR0p1_FCRB->SetLineColor(2);
	h_jtSubZg_dR0p1_FCRB->Draw("SAME");
	h_jtSubZg_dR0p1_GSPB->SetLineColor(4);
	h_jtSubZg_dR0p1_GSPB->Draw("SAME");

	TLegend *le_jtSubZg_dR0p1 = new TLegend(0.65,0.60,0.88,0.88,NULL,"brNDC");
	le_jtSubZg_dR0p1->SetBorderSize(0);
	le_jtSubZg_dR0p1->AddEntry((TObject*)0,"Zg, dR>0.1","");
	le_jtSubZg_dR0p1->AddEntry(h_jtSubZg_dR0p1_nonB,"nonB","l");
	le_jtSubZg_dR0p1->AddEntry(h_jtSubZg_dR0p1_FCRB,"FCR-B","l");
	le_jtSubZg_dR0p1->AddEntry(h_jtSubZg_dR0p1_GSPB,"GSP-B","l");
	le_jtSubZg_dR0p1->Draw("SAME");

	c_jtSubZg_dR0p1->SaveAs("plots/jtSubZg_dR0p1.pdf");


	binLow=0;
	binHigh=1;

	TH1D *h_jtSubJetdR12_nonB = new TH1D("h_jtSubJetdR12_nonB","h_jtSubJetdR12_nonB",nbin,binLow,binHigh/2); h_jtSubJetdR12_nonB->Sumw2();
	TH1D *h_jtSubJetdR12_FCRB = new TH1D("h_jtSubJetdR12_FCRB","h_jtSubJetdR12_FCRB",nbin,binLow,binHigh/2); h_jtSubJetdR12_FCRB->Sumw2();
	TH1D *h_jtSubJetdR12_GSPB = new TH1D("h_jtSubJetdR12_GSPB","h_jtSubJetdR12_GSPB",nbin,binLow,binHigh/2); h_jtSubJetdR12_GSPB->Sumw2();

	t_akSD4PFJet->Draw("jtSubJetdR12>>h_jtSubJetdR12_GSPB","jtpt>100 && abs(jteta)<2&&nSubJet>=2&&abs(refparton_flavorForB)==5&&( refparton_flavorProcess==5 || refparton_flavorProcess==6)");
	t_akSD4PFJet->Draw("jtSubJetdR12>>h_jtSubJetdR12_FCRB","jtpt>100 && abs(jteta)<2&&nSubJet>=2&&abs(refparton_flavorForB)==5&&refparton_flavorProcess==1");
	t_akSD4PFJet->Draw("jtSubJetdR12>>h_jtSubJetdR12_nonB","jtpt>100 && abs(jteta)<2&&nSubJet>=2&&abs(refparton_flavorForB)!=5");

	h_jtSubJetdR12_nonB->Scale(1/h_jtSubJetdR12_nonB->Integral());
	h_jtSubJetdR12_FCRB->Scale(1/h_jtSubJetdR12_FCRB->Integral());
	h_jtSubJetdR12_GSPB->Scale(1/h_jtSubJetdR12_GSPB->Integral());

	gStyle->SetOptStat(0);
	TCanvas *c_jtSubJetdR12 = new TCanvas("c_jtSubJetdR12","c_jtSubJetdR12",800,800);
	c_jtSubJetdR12->cd();
	h_jtSubJetdR12_nonB->SetLineColor(1);
	h_jtSubJetdR12_FCRB->SetTitle("");
	h_jtSubJetdR12_FCRB->GetXaxis()->SetTitle("dR"); 
	h_jtSubJetdR12_FCRB->GetYaxis()->SetTitle("1/N");
	h_jtSubJetdR12_FCRB->SetLineColor(2);
	h_jtSubJetdR12_FCRB->Draw("SAME");
	h_jtSubJetdR12_nonB->SetTitle("");
	h_jtSubJetdR12_nonB->Draw("SAME");
	h_jtSubJetdR12_GSPB->SetLineColor(4);
	h_jtSubJetdR12_GSPB->Draw("SAME");

	TLegend *le_jtSubJetdR12 = new TLegend(0.65,0.60,0.88,0.88,NULL,"brNDC");
	le_jtSubJetdR12->SetBorderSize(0);
	le_jtSubJetdR12->AddEntry((TObject*)0,"Sub-Jet dR","");
	le_jtSubJetdR12->AddEntry(h_jtSubJetdR12_nonB,"nonB","l");
	le_jtSubJetdR12->AddEntry(h_jtSubJetdR12_FCRB,"FCR-B","l");
	le_jtSubJetdR12->AddEntry(h_jtSubJetdR12_GSPB,"GSP-B","l");
	le_jtSubJetdR12->Draw("SAME");

	c_jtSubJetdR12->SaveAs("plots/jtSubJetdR12.pdf");



	TCanvas *c_bbpt= new TCanvas("c_bbpt","c_bbpt");
	c_bbpt->Divide(2,2);
	c_bbpt->cd(1);
	t_akSD4PFJet->Draw("refGSP_b1pt","jtpt>100 && abs(jteta)<2&& refparton_flavorProcess==6 && refGSP_SubJtMatched==1");
  c_bbpt->cd(2);
  t_akSD4PFJet->Draw("refGSP_b2pt","jtpt>100 && abs(jteta)<2&& refparton_flavorProcess==6 && refGSP_SubJtMatched==1");
  c_bbpt->cd(3);
  t_akSD4PFJet->Draw("refGSP_b1pt","jtpt>100 && abs(jteta)<2&& refparton_flavorProcess==6 && refGSP_SubJtMatched==-1");
  c_bbpt->cd(4);
  t_akSD4PFJet->Draw("refGSP_b2pt","jtpt>100 && abs(jteta)<2&& refparton_flavorProcess==6 && refGSP_SubJtMatched==-1");
	c_bbpt->SaveAs("plots/bbpt_vs_JtMatched.pdf");
	



	TCanvas *c_LeadJtPt= new TCanvas("c_LeadJtPt","c_LeadJtPt",800,800);
	c_LeadJtPt->cd();
	t_akSD4PFJet->Draw("jtpt");
	c_LeadJtPt->SaveAs("plots/lead_jtpt.pdf");

	TCanvas *c_FlavorforB = new TCanvas("c_FlavorforB","c_FlavorforB",800,800);
	c_FlavorforB->cd();
	t_akSD4PFJet->Draw("refparton_flavorForB","jtpt>100 && abs(jteta)<2");
	c_FlavorforB->SaveAs("plots/refparton_flavorForB.pdf");

	TCanvas *c_FlavorProcess = new TCanvas("c_FlavorProcess","c_FlavorProcess",800,800);
	c_FlavorProcess->cd();
	t_akSD4PFJet->Draw("refparton_flavorProcess","jtpt>100 && abs(jteta)<2");
	c_FlavorProcess->SaveAs("plots/refparton_flavorProcess.pdf");

	TCanvas *c_refGSP_bbJtMatched = new TCanvas("c_refGSP_bbJtMatched","c_refGSP_bbJtMatched",800,800);
	c_refGSP_bbJtMatched->cd();
	t_akSD4PFJet->Draw("refGSP_SubJtMatched","jtpt>100 && abs(jteta)<2 && refparton_flavorProcess==6");
	c_refGSP_bbJtMatched->SaveAs("plots/refGSP_bbJtMatched.pdf");

	TCanvas *c_refGSP_bbSubJt_Match = new TCanvas("c_refGSP_bbSubJt_Match","c_refGSP_bbSubJt_Match",800,800);
	c_refGSP_bbSubJt_Match->cd();
	t_akSD4PFJet->Draw("refGSP_bbSubJt_MatchStatus","jtpt>100 && abs(jteta)<2 && refparton_flavorProcess==6 && refGSP_SubJtMatched==1");
	c_refGSP_bbSubJt_Match->SaveAs("plots/refGSP_bbSubJt_Match.pdf");

  TCanvas *c_refGSP_bbSubJt_dRMatch = new TCanvas("c_refGSP_bbSubJt_dRMatch","c_refGSP_bbSubJt_dRMatch",800,800);
  c_refGSP_bbSubJt_dRMatch->cd();
  t_akSD4PFJet->Draw("refGSP_bbSubJt_dRMatchStatus","jtpt>100 && abs(jteta)<2 && refparton_flavorProcess==6 && refGSP_SubJtMatched==1");
  c_refGSP_bbSubJt_dRMatch->SaveAs("plots/refGSP_bbSubJt_dRMatch.pdf");


	TCanvas *c_nSubJet = new TCanvas("c_nSubJet","c_nSubJet",800,800);
	c_nSubJet->cd();
	t_akSD4PFJet->Draw("nSubJet","jtpt>100 && abs(jteta)<2&&abs(refparton_flavorForB)==5");
	c_nSubJet->SaveAs("plots/nSubJet.pdf");

/*
	TCanvas *c_bbdR = new TCanvas("c_bbdR","c_bbdR",800,800);
	c_bbdR->Divide(2,2);
	c_bbdR->cd(1);
	t_akSD4PFJet->Draw("refGSP_bbdR","jtpt>100 && abs(jteta)<2 && refGSP_SubJtMatched!=-2 && refparton_flavorProcess==6");
	c_bbdR->cd(2);
	t_akSD4PFJet->Draw("refGSP_bbdR","jtpt>100 && abs(jteta)<2 && refGSP_SubJtMatched==-1 && refparton_flavorProcess==6");
	c_bbdR->cd(3);
	t_akSD4PFJet->Draw("refGSP_bbdR","jtpt>100 && abs(jteta)<2 && refGSP_SubJtMatched==1 && refparton_flavorProcess==6");
	c_bbdR->SaveAs("plots/refGSP_bbdR.pdf");
*/

	TCanvas *c_bbzg = new TCanvas("c_bbzg","c_bbzg",800,800);
	c_bbzg->Divide(2,2);
	c_bbzg->cd(1);
	t_akSD4PFJet->Draw("refGSP_bbzg","jtpt>100 && abs(jteta)<2 && refGSP_SubJtMatched!=-2 && refparton_flavorProcess==6");
	c_bbzg->cd(2);
	t_akSD4PFJet->Draw("refGSP_bbzg","jtpt>100 && abs(jteta)<2 && refGSP_SubJtMatched!=-2 && refparton_flavorProcess==6 && refGSP_bbSubJt_dRMatchStatus==1");
	c_bbzg->cd(3);
	t_akSD4PFJet->Draw("refGSP_bbzg","jtpt>100 && abs(jteta)<2 && refGSP_SubJtMatched!=-2 && refparton_flavorProcess==6 && refGSP_bbSubJt_dRMatchStatus==2");
	c_bbzg->SaveAs("plots/refGSP_bbzg.pdf");

	TCanvas *c_SubJtMatched_dR = new TCanvas("c_SubJtMatched_dR","c_SubJtMatched_dR",800,800);
	c_SubJtMatched_dR->Divide(2,2);
	c_SubJtMatched_dR->cd(1);
	t_akSD4PFJet->Draw("refGSP_b1Match_SubJt1dR","refparton_flavorProcess==6 && refGSP_bbSubJt_dRMatchStatus==1");
	c_SubJtMatched_dR->cd(2);
	t_akSD4PFJet->Draw("refGSP_b2Match_SubJt2dR","refparton_flavorProcess==6 && refGSP_bbSubJt_dRMatchStatus==1");
	c_SubJtMatched_dR->cd(3);
	t_akSD4PFJet->Draw("refGSP_b1Match_SubJt2dR","refparton_flavorProcess==6 && refGSP_bbSubJt_dRMatchStatus==2");
	c_SubJtMatched_dR->cd(4);
	t_akSD4PFJet->Draw("refGSP_b2Match_SubJt1dR","refparton_flavorProcess==6 && refGSP_bbSubJt_dRMatchStatus==2");
	c_SubJtMatched_dR->SaveAs("plots/refGSP_b12Match_SubJtdR.pdf");

	TCanvas *c_SubJtMatched_SubJtPtRat = new TCanvas("c_SubJtMatched_SubJtPtRat","c_SubJtMatched_SubJtPtRat",800,800);
  c_SubJtMatched_SubJtPtRat->Divide(2,2);
  c_SubJtMatched_SubJtPtRat->cd(1);
  t_akSD4PFJet->Draw("refGSP_b1Match_SubJt1PtRat","refparton_flavorProcess==6 && refGSP_bbSubJt_dRMatchStatus==1");
  c_SubJtMatched_SubJtPtRat->cd(2);
  t_akSD4PFJet->Draw("refGSP_b2Match_SubJt2PtRat","refparton_flavorProcess==6 && refGSP_bbSubJt_dRMatchStatus==1");
  c_SubJtMatched_SubJtPtRat->cd(3);
  t_akSD4PFJet->Draw("refGSP_b1Match_SubJt2PtRat","refparton_flavorProcess==6 && refGSP_bbSubJt_dRMatchStatus==2");
  c_SubJtMatched_SubJtPtRat->cd(4);
  t_akSD4PFJet->Draw("refGSP_b2Match_SubJt1PtRat","refparton_flavorProcess==6 && refGSP_bbSubJt_dRMatchStatus==2");
  c_SubJtMatched_SubJtPtRat->SaveAs("plots/refGSP_b12Match_SubJtPtRat.pdf");

  TCanvas *c_SubJtMatched_SubJtPtRat_dR0p1Cut = new TCanvas("c_SubJtMatched_SubJtPtRat_dR0p1Cut","c_SubJtMatched_SubJtPtRat_dR0p1Cut",800,800);
  c_SubJtMatched_SubJtPtRat_dR0p1Cut->Divide(2,2);
  c_SubJtMatched_SubJtPtRat_dR0p1Cut->cd(1);
  t_akSD4PFJet->Draw("refGSP_b1Match_SubJt1PtRat","refparton_flavorProcess==6 && refGSP_bbSubJt_dR0p1MatchStatus==1");
  c_SubJtMatched_SubJtPtRat_dR0p1Cut->cd(2);
  t_akSD4PFJet->Draw("refGSP_b2Match_SubJt2PtRat","refparton_flavorProcess==6 && refGSP_bbSubJt_dR0p1MatchStatus==1");
  c_SubJtMatched_SubJtPtRat_dR0p1Cut->cd(3);
  t_akSD4PFJet->Draw("refGSP_b1Match_SubJt2PtRat","refparton_flavorProcess==6 && refGSP_bbSubJt_dR0p1MatchStatus==2");
  c_SubJtMatched_SubJtPtRat_dR0p1Cut->cd(4);
  t_akSD4PFJet->Draw("refGSP_b2Match_SubJt1PtRat","refparton_flavorProcess==6 && refGSP_bbSubJt_dR0p1MatchStatus==2");
  c_SubJtMatched_SubJtPtRat_dR0p1Cut->SaveAs("plots/refGSP_b12Match_SubJtPtRat_dR0p1Cut.pdf");

  TCanvas *c_refSubJtMatched_SubJtPtRat = new TCanvas("c_refSubJtMatched_SubJtPtRat","c_refSubJtMatched_SubJtPtRat",800,800);
  c_refSubJtMatched_SubJtPtRat->Divide(2,2);
  c_refSubJtMatched_SubJtPtRat->cd(1);
  t_akSD4PFJet->Draw("refGSP_b1Match_refSubJt1PtRat","refparton_flavorProcess==6 && refGSP_bbrefSubJt_dRMatchStatus==1");
  c_refSubJtMatched_SubJtPtRat->cd(2);
  t_akSD4PFJet->Draw("refGSP_b2Match_refSubJt2PtRat","refparton_flavorProcess==6 && refGSP_bbrefSubJt_dRMatchStatus==1");
  c_refSubJtMatched_SubJtPtRat->cd(3);
  t_akSD4PFJet->Draw("refGSP_b1Match_refSubJt2PtRat","refparton_flavorProcess==6 && refGSP_bbrefSubJt_dRMatchStatus==2");
  c_refSubJtMatched_SubJtPtRat->cd(4);
  t_akSD4PFJet->Draw("refGSP_b2Match_refSubJt1PtRat","refparton_flavorProcess==6 && refGSP_bbrefSubJt_dRMatchStatus==2");
  c_refSubJtMatched_SubJtPtRat->SaveAs("plots/refGSP_b12Match_refSubJtPtRat.pdf");


//	plotCompare_fun(t_akSD4PFJet);


	// plot GSP-B, FCR-B Non B , jtSubZg
	nbin=50; binLow=0; binHigh=0.5;
	TCut CutCommon="jtpt>100 && abs(jteta)<2&&nSubJet>=2"; TCut Cut1="abs(refparton_flavorForB)==5&&( refparton_flavorProcess==5 || refparton_flavorProcess==6)"; 
	TCut Cut2="abs(refparton_flavorForB)==5&&refparton_flavorProcess==1"; TCut Cut3="abs(refparton_flavorForB)!=5";
	TString add_savename="";
	TString plotVariable="jtSubZg"; TString plotTitle="Sub-Jet pt2/pt2+pt1";TString plotXTitle="Zg";
	TString type1Title="GSP-B"; TString type2Title="FCR-B"; TString type3Title="Non B";
  Int_t DoNorm=1;
  plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);


	//  plot GSP-B, FCR-B Non B , jtSubZg with SubJt dR12>0.1
  nbin=50; binLow=0; binHigh=0.5;
  CutCommon="jtpt>100 && abs(jteta)<2&&nSubJet>=2&&jtSubJetdR12>0.1"; Cut1="abs(refparton_flavorForB)==5&&( refparton_flavorProcess==5 || refparton_flavorProcess==6)";
  Cut2="abs(refparton_flavorForB)==5&&refparton_flavorProcess==1"; Cut3="abs(refparton_flavorForB)!=5";
  add_savename="SubJt12dR0p1cut";
  plotVariable="jtSubZg"; plotTitle="Sub-Jet pt2/pt2+pt1";plotXTitle="Zg";
  type1Title="GSP-B"; type2Title="FCR-B"; type3Title="Non B";

  plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);

  // refSubjtdR
  nbin=50; binLow=0; binHigh=0.6;
  CutCommon="jtpt>100 && abs(jteta)<2&&nSubJet>=2";
  Cut1="abs(refparton_flavorForB)==5&&( refparton_flavorProcess==5 || refparton_flavorProcess==6)";
  Cut2="abs(refparton_flavorForB)==5&&( refparton_flavorProcess==1 )";
  Cut3="abs(refparton_flavorForB)!=5";
  add_savename="";
  plotVariable="jtSubJetdR12";
  plotTitle="Subj-Jet dR";
  plotXTitle="dR12";
  type1Title="GSP-B"; type2Title="FCR-B";type3Title="Non B";
  plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);

	// plot GSP-ghost bb match, GSP-bbdr match, nonGSP-ghost bb match; Zg
  nbin=25; binLow=0; binHigh=0.5;
  CutCommon="jtpt>100 && abs(jteta)<2&&nSubJet>=2";
  Cut1="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && ( abs(refFlavorID_Subjet1_ID)==5 &&  abs(refFlavorID_Subjet2_ID)==5 ) ";
  Cut2="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && (refGSP_bbSubJt_dRMatchStatus==1 || refGSP_bbSubJt_dRMatchStatus==2 ) ";
  Cut3="abs(refparton_flavorForB)==5 && refparton_flavorProcess!=6 && ( abs(refFlavorID_Subjet1_ID)==5 &&  abs(refFlavorID_Subjet2_ID)==5 )";
  add_savename="GSP_bbdr_ghostMatch";
  plotVariable="jtSubZg"; plotTitle="Sub-Jet Zg"; plotXTitle="Zg";
  type1Title="GSP ghost bb match ";type2Title="GSP SubJt bb dR match"; type3Title="NonGSP ghost bb match";
  plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);
	
  // plot GSP-ghost bb match, GSP-bbdr match, nonGSP-ghost bb match; dR
  nbin=25; binLow=0; binHigh=0.5;
  CutCommon="jtpt>100 && abs(jteta)<2&&nSubJet>=2";
  Cut1="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && ( abs(refFlavorID_Subjet1_ID)==5 &&  abs(refFlavorID_Subjet2_ID)==5 ) ";
  Cut2="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && (refGSP_bbSubJt_dRMatchStatus==1 || refGSP_bbSubJt_dRMatchStatus==2 ) ";
  Cut3="abs(refparton_flavorForB)==5 && refparton_flavorProcess!=6 && ( abs(refFlavorID_Subjet1_ID)==5 &&  abs(refFlavorID_Subjet2_ID)==5 )";
  add_savename="GSP_bbdr_ghostMatch";
  plotVariable="jtSubJetdR12"; plotTitle="Sub-Jet dR"; plotXTitle="dR";
  type1Title="GSP ghost bb match ";type2Title="GSP SubJt bb dR match"; type3Title="NonGSP ghost bb match";
  plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);


  // plot GSP-ghost bb match, GSP one ghost b match, FCR ghost one b match; Zg
  nbin=25; binLow=0; binHigh=0.5;
  CutCommon="jtpt>100 && abs(jteta)<2&&nSubJet>=2";
  Cut1="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && ( abs(refFlavorID_Subjet1_ID)==5 &&  abs(refFlavorID_Subjet2_ID)==5 ) ";
  Cut2="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && ( (abs(refFlavorID_Subjet1_ID)==5 &&  abs(refFlavorID_Subjet2_ID)!=5) || (abs(refFlavorID_Subjet1_ID)!=5 &&  abs(refFlavorID_Subjet2_ID)==5)) ";
  Cut3="abs(refparton_flavorForB)==5 && refparton_flavorProcess!=6 && ( (abs(refFlavorID_Subjet1_ID)==5 &&  abs(refFlavorID_Subjet2_ID)!=5) || (abs(refFlavorID_Subjet1_ID)!=5 &&  abs(refFlavorID_Subjet2_ID)==5)) ";
  add_savename="GSP_ghostMatch";
  plotVariable="jtSubZg"; plotTitle="Sub-Jet Zg"; plotXTitle="Zg";
  type1Title="GSP ghost bb match ";type2Title="GSP ghost one b match"; type3Title="FCR ghost one match";
  plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);

  // plot GSP-ghost bb match, GSP one ghost b match, FCR ghost one b match; dR
  nbin=25; binLow=0; binHigh=0.5;
  CutCommon="jtpt>100 && abs(jteta)<2&&nSubJet>=2";
  Cut1="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && ( abs(refFlavorID_Subjet1_ID)==5 &&  abs(refFlavorID_Subjet2_ID)==5 ) ";
  Cut2="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && ( (abs(refFlavorID_Subjet1_ID)==5 &&  abs(refFlavorID_Subjet2_ID)!=5) || (abs(refFlavorID_Subjet1_ID)!=5 &&  abs(refFlavorID_Subjet2_ID)==5)) ";
  Cut3="abs(refparton_flavorForB)==5 && refparton_flavorProcess!=6 && ( (abs(refFlavorID_Subjet1_ID)==5 &&  abs(refFlavorID_Subjet2_ID)!=5) || (abs(refFlavorID_Subjet1_ID)!=5 &&  abs(refFlavorID_Subjet2_ID)==5)) ";
  add_savename="GSP_ghostMatch";
  plotVariable="jtSubJetdR12"; plotTitle="Sub-Jet dR"; plotXTitle="dR";
  type1Title="GSP ghost bb match ";type2Title="GSP ghost one b match"; type3Title="FCR ghost one match";
  plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);



	

	// plot GSP-bb match, GSP-B single, FCR ; Zg
	nbin=25; binLow=0; binHigh=0.5;
	CutCommon="jtpt>100 && abs(jteta)<2&&nSubJet>=2";
	Cut1="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && (refGSP_bbSubJt_dRMatchStatus==1 || refGSP_bbSubJt_dRMatchStatus==2) ";
	Cut2="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && refGSP_SubJtMatched==-1";
	Cut3="abs(refparton_flavorForB)==5 && refparton_flavorProcess==1";
	add_savename="GSP_bbMatch";
	plotVariable="jtSubZg"; plotTitle="Sub-Jet Zg"; plotXTitle="Zg";
	type1Title="GSP-B SubJt bb match"; type2Title="GSP-B one b jet"; type3Title="FCR-B";
	plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);

  // plot GSP-bb match, not match, GSP-B single ; Zg
  nbin=25; binLow=0; binHigh=0.5;
  CutCommon="jtpt>100 && abs(jteta)<2&&nSubJet>=2";
  Cut1="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && (refGSP_bbSubJt_dRMatchStatus==1 || refGSP_bbSubJt_dRMatchStatus==2) ";
  Cut2="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && refGSP_bbSubJt_dRMatchStatus==0";
  Cut3="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && refGSP_SubJtMatched==-1";
  add_savename="GSP_bbMatch2";
  plotVariable="jtSubZg"; plotTitle="Sub-Jet Zg"; plotXTitle="Zg";
  type1Title="GSP-B SubJt bb match"; type2Title="GSP-B bb not Match"; type3Title="GSP-B one b jet";
  plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);


  // plot GSP-bb tight match, loose match, GSP-B single ; Zg
  nbin=25; binLow=0; binHigh=0.5;
  CutCommon="jtpt>100 && abs(jteta)<2&&nSubJet>=2";
  Cut1="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && (refGSP_bbSubJt_dR0p1MatchStatus==1 || refGSP_bbSubJt_dR0p1MatchStatus==2) ";
  Cut2="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && (refGSP_bbSubJt_dRMatchStatus==1 || refGSP_bbSubJt_dRMatchStatus==2)";
  Cut3="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && refGSP_SubJtMatched==-1";
  add_savename="GSP_bbMatchTight";
  plotVariable="jtSubZg"; plotTitle="Sub-Jet Zg"; plotXTitle="Zg";
  type1Title="GSP-B bb dR0.1 Match"; type2Title="GSP-B bb Match"; type3Title="GSP-B one b jet";
  plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);


	// plot GSP-bb match, GSP one b, FCR ; dR
	nbin=25; binLow=0; binHigh=0.5;
	CutCommon="jtpt>100 && abs(jteta)<2&&nSubJet>=2";
	Cut1="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && (refGSP_bbSubJt_dRMatchStatus==1 || refGSP_bbSubJt_dRMatchStatus==2) ";
	Cut2="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && refGSP_SubJtMatched==-1";
	Cut3="abs(refparton_flavorForB)==5 && refparton_flavorProcess==1";
	add_savename="GSP_bbMatch";
	plotVariable="jtSubJetdR12"; plotTitle="Sub-Jet dR"; plotXTitle="dR";
	type1Title="GSP-B SubJt bb match"; type2Title="GSP-B one b jet"; type3Title="FCR-B";
	plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);

 // plot GSP-bb match, not match, GSP-B single; dR
  nbin=25; binLow=0; binHigh=0.5;
  CutCommon="jtpt>100 && abs(jteta)<2&&nSubJet>=2";
  Cut1="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && (refGSP_bbSubJt_dRMatchStatus==1 || refGSP_bbSubJt_dRMatchStatus==2) ";
  Cut2="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && refGSP_bbSubJt_dRMatchStatus==0";
  Cut3="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && refGSP_SubJtMatched==-1";
  add_savename="GSP_bbMatch2";
  plotVariable="jtSubJetdR12"; plotTitle="Sub-Jet dR"; plotXTitle="dR";
  type1Title="GSP-B SubJt bb match"; type2Title="GSP-B bb not Match"; type3Title="GSP-B one b jet";
  plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);


 // plot GSP-bb tight match, loose match, GSP-B single; dR
  nbin=25; binLow=0; binHigh=0.5;
  CutCommon="jtpt>100 && abs(jteta)<2&&nSubJet>=2";
  Cut1="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && (refGSP_bbSubJt_dR0p1MatchStatus==1 || refGSP_bbSubJt_dR0p1MatchStatus==2) ";
  Cut2="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && (refGSP_bbSubJt_dRMatchStatus==1 || refGSP_bbSubJt_dRMatchStatus==2)";
  Cut3="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && refGSP_SubJtMatched==-1";
  add_savename="GSP_bbMatchTight";
  plotVariable="jtSubJetdR12"; plotTitle="Sub-Jet dR"; plotXTitle="dR";
  type1Title="GSP-B SubJt bb match"; type2Title="GSP-B bb loose Match"; type3Title="GSP-B one b jet";
  plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);



	// plot Gluon-spliiting B , differenet dR
	nbin=50; binLow=0; binHigh=0.5;
	CutCommon="jtpt>100 && abs(jteta)<2&&nSubJet>=2"; 
	Cut1="abs(refparton_flavorForB)==5&&( refparton_flavorProcess==5 || refparton_flavorProcess==6)&&jtSubJetdR12>0.23";	
	Cut2="abs(refparton_flavorForB)==5&&( refparton_flavorProcess==5 || refparton_flavorProcess==6)&&jtSubJetdR12<0.12";
	Cut3="abs(refparton_flavorForB)==5&&refparton_flavorProcess==1";
	add_savename="ZgWithdRcut";
	plotVariable="jtSubZg"; plotTitle="Sub-Jet Zg"; plotXTitle="Zg";
	type1Title="GSP-B dR>0.23"; type2Title="GSP-B dR<0.12"; type3Title="FCR-B";
	plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);


	// refSubZg, GSP-B FCR-B Non B
	nbin=50; binLow=0; binHigh=0.5;
	CutCommon="jtpt>100 && abs(jteta)<2&&nrefSubJet>=2";	
	Cut1="abs(refparton_flavorForB)==5&&( refparton_flavorProcess==5 || refparton_flavorProcess==6)";
	Cut2="abs(refparton_flavorForB)==5&&( refparton_flavorProcess==1 )";
	Cut3="abs(refparton_flavorForB)!=5";	
	add_savename="";
	plotVariable="refSubZg";	
	plotTitle="ref Sub-Jet Zg"; plotXTitle="Zg";
	type1Title="GSP-B"; type2Title="FCR-B";type3Title="Non B";
	plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);


	// refSubjtdR
	nbin=50; binLow=0; binHigh=0.5;
	CutCommon="jtpt>100 && abs(jteta)<2&&nrefSubJet>=2";
	Cut1="abs(refparton_flavorForB)==5&&( refparton_flavorProcess==5 || refparton_flavorProcess==6)";
	Cut2="abs(refparton_flavorForB)==5&&( refparton_flavorProcess==1 )";
	Cut3="abs(refparton_flavorForB)!=5";
	add_savename="";
	plotVariable="refSubJetdR12";
	plotTitle="ref Subj-Jet dR";
	plotXTitle="dR12";
	type1Title="GSP-B"; type2Title="FCR-B";type3Title="Non B";
	plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);


  // plot refJt GSP-bb match, not match, GSP-B single ; Zg
  nbin=25; binLow=0; binHigh=0.5;
  CutCommon="jtpt>100 && abs(jteta)<2&&nrefSubJet>=2";
  Cut1="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && (refGSP_bbrefSubJt_dRMatchStatus==1 || refGSP_bbrefSubJt_dRMatchStatus==2) ";
  Cut2="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && refGSP_bbrefSubJt_dRMatchStatus==0";
  Cut3="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && refGSP_SubJtMatched==-1";
  add_savename="GSP_bbMatch2";
  plotVariable="refSubZg"; plotTitle="ref Sub-Jet Zg"; plotXTitle="Zg";
  type1Title="GSP-B SubJt bb match"; type2Title="GSP-B bb not Match"; type3Title="GSP-B one b jet";
  plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);

  // plot refJt GSP-bb match, not match, GSP-B single ; dR
  nbin=25; binLow=0; binHigh=0.5;
  CutCommon="jtpt>100 && abs(jteta)<2&&nrefSubJet>=2";
  Cut1="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && (refGSP_bbrefSubJt_dRMatchStatus==1 || refGSP_bbrefSubJt_dRMatchStatus==2) ";
  Cut2="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && refGSP_bbrefSubJt_dRMatchStatus==0";
  Cut3="abs(refparton_flavorForB)==5 && refparton_flavorProcess==6 && refGSP_SubJtMatched==-1";
  add_savename="GSP_bbMatch2";
  plotVariable="refSubJetdR12"; plotTitle="ref Subj-Jet dR"; plotXTitle="dR12";
  type1Title="GSP-B SubJt bb match"; type2Title="GSP-B bb not Match"; type3Title="GSP-B one b jet";
  plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);




	// bbdR vs GSP-B one-jet & GSP seperate jets
	nbin=45; binLow=0; binHigh=4.5;
	CutCommon="jtpt>100 && abs(jteta)<2 && refparton_flavorProcess==6";
	Cut1="refGSP_SubJtMatched==1";
	Cut2="refGSP_SubJtMatched==-1";
	Cut3="refGSP_SubJtMatched!=-2";
	add_savename="vs_SubJtMatched";
	plotVariable="refGSP_bbdR";
	plotTitle="MC bb dR";
	plotXTitle="dR12";
	type1Title="GSP-B one-jet"; type2Title="GSP seperate jets";type3Title="All GSP-B";
	DoNorm=0;
	plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title,DoNorm);
	DoNorm=1;

  // bbdR vs GSP-BB matched & GSP BB not & all GSP BB
  nbin=25; binLow=0; binHigh=0.5;
  CutCommon="jtpt>100 && abs(jteta)<2 && refparton_flavorProcess==6 && refGSP_SubJtMatched!=-2";
  Cut1="refGSP_bbSubJt_dRMatchStatus==1 || refGSP_bbSubJt_dRMatchStatus==2";
  Cut2="refGSP_bbSubJt_dRMatchStatus==0";
  Cut3="refGSP_bbSubJt_dRMatchStatus!=-1";
  add_savename="vs_bbSubJtMatched";
  plotVariable="refGSP_bbdR";
  plotTitle="MC bb dR";
  plotXTitle="dR12";
  type1Title="GSP-BB matched"; type2Title="GSP-BB not Matched";type3Title="All GSP-BB";
  DoNorm=0;
  plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title,DoNorm);
  DoNorm=1;





	// bbzg
	nbin=25; binLow=0; binHigh=0.5;
	CutCommon="jtpt>100 && abs(jteta)<2 && refparton_flavorProcess==6 && refGSP_SubJtMatched!=-2";
	Cut1="refGSP_bbSubJt_dRMatchStatus==1";
	Cut2="refGSP_bbSubJt_dRMatchStatus==2";
	Cut3="refGSP_bbSubJt_dRMatchStatus==0";
	add_savename="vs_bbSubJtMatch";
	plotVariable="refGSP_bbzg";
	plotTitle="MC bb zg";
	plotXTitle="zg";
	type1Title="GSP-B pair1"; type2Title="GSP-B pair2";type3Title="GSP-B notMatch";
	plotCompare_fun(t_akSD4PFJet,nbin,binLow,binHigh,CutCommon,Cut1,Cut2,Cut3,add_savename,plotVariable,plotTitle,plotXTitle,type1Title,type2Title,type3Title);



	//	testfunction(1,3,2);


	f_out->Write();
	f_out->Close();  // need to close file here?

} // end of Selector:Terminate

int plotCompare_fun(TTree *tjet, int nbin, double binLow, double binHigh,
		TCut CutCommon, TCut Cut1, TCut Cut2, TCut Cut3,
		TString add_savename,
		TString plotVariable, TString plotTitle,TString plotXTitle,
		TString type1Title, TString type2Title, TString type3Title, 
		Int_t DoNormalize)
{

	//	if (tjet) // check tjet

	TH1D *h_type1 = new TH1D("h_type1","h_type1",nbin,binLow,binHigh); h_type1->Sumw2();
	TH1D *h_type2 = new TH1D("h_type2","h_type2",nbin,binLow,binHigh); h_type2->Sumw2();
	TH1D *h_type3 = new TH1D("h_type3","h_type3",nbin,binLow,binHigh); h_type3->Sumw2();

	tjet->Draw(Form("%s>>h_type1",plotVariable.Data()),CutCommon&&Cut1);
	tjet->Draw(Form("%s>>h_type2",plotVariable.Data()),CutCommon&&Cut2);
	tjet->Draw(Form("%s>>h_type3",plotVariable.Data()),CutCommon&&Cut3);

	if(DoNormalize==1){
	h_type3->Scale(1/h_type3->Integral());
	h_type2->Scale(1/h_type2->Integral());
	h_type1->Scale(1/h_type1->Integral());
	}

	// set plot maximum & minimum
	double his_max=0;
	double his_min=h_type3->GetMinimum();
	his_max=h_type3->GetMaximum();
	if (h_type2->GetMaximum() > his_max) his_max=h_type2->GetMaximum();
	if (h_type1->GetMaximum() > his_max) his_max=h_type1->GetMaximum();
  if (h_type2->GetMinimum() > his_max) his_max=h_type2->GetMinimum();
  if (h_type1->GetMinimum() > his_max) his_max=h_type1->GetMinimum();
	double hisTall=his_max-his_min;
	his_max=his_max+hisTall*0.1;
	his_min=his_min-hisTall*0.05;
  h_type3->SetMaximum(his_max);	
  h_type3->SetMinimum(his_min);
	


	gStyle->SetOptStat(0);
	TCanvas *c_Compare = new TCanvas(Form("c_%s",plotVariable.Data()),Form("c_%s",plotVariable.Data()),800,800);
	c_Compare->cd();
	h_type3->GetXaxis()->SetTitle(Form("%s",plotXTitle.Data()));
	h_type3->GetYaxis()->SetTitle("1/N");
	h_type3->SetLineColor(1);
	h_type3->SetTitle("");
	h_type3->Draw();
	h_type2->SetLineColor(2);
	h_type2->Draw("SAME");
	h_type1->SetLineColor(4);
	h_type1->Draw("SAME");

	TLegend *le_Compare = new TLegend(0.65,0.60,0.88,0.88,NULL,"brNDC");
	le_Compare->SetBorderSize(0);
	le_Compare->AddEntry((TObject*)0,Form("%s",plotTitle.Data()),"");
	le_Compare->AddEntry(h_type3,Form("%s",type3Title.Data()),"l");
	le_Compare->AddEntry(h_type2,Form("%s",type2Title.Data()),"l");
	le_Compare->AddEntry(h_type1,Form("%s",type1Title.Data()),"l");
	le_Compare->Draw("SAME");

	c_Compare->SaveAs(Form("plots/%s_%s_byFun.pdf",plotVariable.Data(),add_savename.Data()));

	delete c_Compare;
	delete le_Compare;
	delete h_type1; delete h_type2; delete h_type3;


	return 0;
}

float delta_Phi(float phi1, float phi2){
	float dphi= phi1-phi2;
	if (dphi < -(Float_t)TMath::Pi()) dphi+=2*(Float_t)TMath::Pi();
	if (dphi >  (Float_t)TMath::Pi()) dphi-=2*(Float_t)TMath::Pi();
	return dphi;
}


int testfunction(int inputInt, int in2, int in3){

	cout<<"hello in test function"<<endl;
	cout<<inputInt<<endl;
	cout<<in2<<endl;
	cout<<in3<<endl;

	return 1;
} 

