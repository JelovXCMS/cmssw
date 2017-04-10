// an example of 
// reading vector<vector<float> > 


#include <vector>

#include "TFile.h"
#include "TTree.h"
#include "TCanvas.h"
#include "TFrame.h"
#include "TH1F.h"
#include <iostream>

/*
#ifdef __MAKECINT__
#prama link C++ class vector<float>+;
#endif
*/

static const int MAXJETS=1000;
using namespace std;

void ReadSubJet(){

	TFile *f = TFile::Open("Test_HiForestAOD_pp_MC_PYTHIA6_bjet30.root");
	TTree *t= (TTree*)f->Get("akSoftDrop4PFJetAnalyzer/t");

	TH1F *hall = new TH1F("hall","hall",100,0,100);
	TH1F *hfirst = new TH1F("hfirst","hfirst",100,0,100);
	TH1F *hsecond = new TH1F("hsecond","hsecond",100,0,100);
	TH1F *hratio = new TH1F("hratio","hratio",100,0,2);

  TH1F *hall2 = new TH1F("hall2","hall2",100,0,100);
  TH1F *hfirst2 = new TH1F("hfirst2","hfirst2",100,0,100);
  TH1F *hsecond2 = new TH1F("hsecond2","hsecond2",100,0,100);
  TH1F *hratio2 = new TH1F("hratio2","hratio2",100,0,2);

  TH1F *hall3 = new TH1F("hall3","hall3",100,0,100);
  TH1F *hfirst3 = new TH1F("hfirst3","hfirst3",100,0,100);
  TH1F *hsecond3 = new TH1F("hsecond3","hsecond3",100,0,100);
  TH1F *hratio3 = new TH1F("hratio3","hratio3",100,0,2);




	int nref;
	int evt;
	float jtpt[MAXJETS]; 
	std::vector<std::vector<float>> *subjetPt=0;
	// std::vector<float> *subjetPt=0; class need vector<vector<float>>, 

	TBranch *bsubjetPt=0;
	t->SetBranchAddress("jtSubJetPt",&subjetPt,&bsubjetPt);

	Int_t nevent=t->GetEntries();

	for (Int_t i=0; i<nevent; i++)
	{
		Long64_t tentry = t->LoadTree(i);
		bsubjetPt->GetEntry(tentry);

    //// first method j<V.size()////

		for(UInt_t j=0; j< subjetPt->size(); ++j){
			for(UInt_t k=0; k<subjetPt->at(j).size(); ++k){
				hall->Fill(subjetPt->at(j).at(k));			
			}	// end for k<subjetPt->at(j).size()
			if(subjetPt->at(j).size() >1 ){
				hfirst->Fill(subjetPt->at(j).at(0));
				hsecond->Fill(subjetPt->at(j).at(1));
	      hratio->Fill(subjetPt->at(j).at(1) / subjetPt->at(j).at(0));				
			}
		} // end for j<subjetPt->size()

		//// end of first method ////
		

		//// second method for auto : /////
		for(auto &innerVec : *subjetPt){
			for(float value : innerVec) {
				hall2->Fill(value);
			} // end for inner vector

      cout<<"innerVec size = "<<innerVec.size()<<endl;
			cout<<"subjetPt size = "<<subjetPt->size()<<endl;
			if(subjetPt->size()>0 &&  innerVec.size()>1){
			cout<<"here"<<endl;
      hfirst2->Fill(innerVec.at(0));
      hsecond2->Fill(innerVec.at(1));
      hratio2->Fill(innerVec.at(1) / innerVec.at(0));			
			cout<<"end here"<<endl;
			}

		} // end for subjet vector
    //// end of second method ////


		//// Third method : iterator of vector
		for(auto it=subjetPt->begin(); it !=subjetPt->end(); it++){
			for(auto it2=it->begin(); it2 !=it->end(); it2++){
				hall3->Fill(*it2);
			}// end for it2=it->begin()
			if(it->size()>1){
				hfirst3->Fill(it->at(0));
				hsecond3->Fill(it->at(1));
				hratio3->Fill(it->at(1)/it->at(0));
			}

		}// end for it=subjetPt.begin()




/*
		if(subjetPt->size()>0 && subjetPt->at(0).size() >1 ){
			hfirst2->Fill(subjetPt->at(0).at(0));
			hsecond2->Fill(subjetPt->at(0).at(1));		
			hratio2->Fill(subjetPt->at(0).at(1) / subjetPt->at(0).at(0));
		}
*/
		//// end of second method ////


	} // end for i<nevent

	//	hratio->Divide(hfirst,hsecond,1,1);

	TCanvas *ch = new TCanvas("ch","ch",800,800);
	ch->Divide(2,2);
	ch->cd(1);
	hall->Draw();
	ch->cd(2);
	hfirst->Draw();
	ch->cd(3);
	hsecond->Draw();
	ch->cd(4);
	hratio->Draw();

  TCanvas *ch2 = new TCanvas("ch2","ch2",800,800);
  ch2->Divide(2,2);
  ch2->cd(1);
  hall2->Draw();
  ch2->cd(2);
  hfirst2->Draw();
  ch2->cd(3);
  hsecond2->Draw();
  ch2->cd(4);
  hratio2->Draw();

  TCanvas *ch3 = new TCanvas("ch3","ch3",800,800);
  ch3->Divide(2,2);
  ch3->cd(1);
  hall3->Draw();
  ch3->cd(2);
  hfirst3->Draw();
  ch3->cd(3);
  hsecond3->Draw();
  ch3->cd(4);
  hratio3->Draw();




	t->ResetBranchAddresses();


} // end ReadSubJet
