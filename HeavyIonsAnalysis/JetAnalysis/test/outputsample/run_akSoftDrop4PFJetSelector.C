// run it with CIN, dont compile 


//#include "akSoftDrop4PFJetSelector.h"
//#include <iostream>
//#include <TChain.h>
//#include <TProof.h>

void run_akSoftDrop4PFJetSelector(int nevt=-1, int firstEntry=0, string outfile = "fnt.root"){


  TProof *plite = TProof::Open("lite://","workers=10");

	TChain *ch_akSD4PF = new TChain("akSoftDrop4PFJetAnalyzer/t","akSD4PFJet");
//	ch_akSD4PF->Add("Test_HiForestAOD_pp_MC_PYTHIA6_bjet30.root");
//	ch_akSD4PF->Add("Test_HiForestAOD_pp_MC_PYTHIA6_bjet120.root");
//  ch_akSD4PF->Add("Test_HiForestAOD_pp_MC_PYTHIA6_Dijet120.root");
//  ch_akSD4PF->Add("Test_HiForestAOD_pp_MC_PYTHIA6_bjet120_n1000.root");
//    ch_akSD4PF->Add("Test_HiForestAOD_pp_MC_PYTHIA6_bjet120_n23000.root");

		ch_akSD4PF->Add("Test_HiForestAOD_pp_MC_PYTHIA6_bjet120_n65000.root");
//		ch_akSD4PF->Add("Test_merge_bracn_pp_p6_b120_n100.root"); 


	ch_akSD4PF->ls();

	// run on Proof
//  ch_akSD4PF->SetProof();


  ch_akSD4PF->Process("akSoftDrop4PFJetSelector.C+");
//	ch_akSD4PF->Process("akSoftDrop4PFJetSelector.C","", nevt, firstEntry);
/*
    string com1 = "mv fnt.root ";
    string command = com1 + outfile;
    gSystem->Exec(command.c_str());
*/


} // end run_akSoftDrop4PFJetSelector
