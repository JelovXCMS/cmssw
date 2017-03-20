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
	 h_LeadJetSubPt2ov1= new TH1D("h_LeadJetSubPt2ov1","h_LeadJetSubPt2ov1",100,0,2);	

	 fOutput->Add(h_JetPt);
   fOutput->Add(h_LeadJetSubPt2ov1);



/*
   TTree *recoTree = new TTree("recoTree","recoTree");
   recoTree->Branch("Dsize",&Dsize);
   recoTree->Branch("Dpt",Dpt,"Dpt[Dsize]/F");
   recoTree->Branch("Dmass",Dmass,"Dmass[Dsize]/F");
   recoTree->Branch("NewLeaf",&NewLeaf);	
*/



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

	 if (h_LeadJetSubPt2ov1) h_LeadJetSubPt2ov1->Write("",TObject::kOverwrite);
	 if (h_JetPt) h_JetPt->Write("",TObject::kOverwrite);
//	 f_out->Close();

	 cout<<"number of entries process is : "<<fProcessed<<endl;
	 


   //// create TCanvas , plot

	 TCanvas *c_test = new TCanvas("c_test","c_test",800,800);
	 c_test->Divide(2,2);
	 c_test->cd(1);
	 h_LeadJetSubPt2ov1->Draw();
	 c_test->cd(2);
	 h_JetPt->Draw();

	
	f_out->Close();  // need to close file here?

}
