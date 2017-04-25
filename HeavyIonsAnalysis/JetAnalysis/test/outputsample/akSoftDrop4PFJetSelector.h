//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Mon Mar 20 16:02:47 2017 by ROOT version 6.02/13
// from TTree t/akSoftDrop4PFpatJetsWithBtagging Jet Analysis Tree
// found on file: Test_HiForestAOD_pp_MC_PYTHIA6_bjet30.root
//////////////////////////////////////////////////////////

#ifndef akSoftDrop4PFJetSelector_h
#define akSoftDrop4PFJetSelector_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>
#include <TH1D.h>
#include <TCut.h>

// Header file for the classes stored in the TTree if any.
#include "vector"

#include <iostream>

using namespace std;

const int MAX_NJetS = 500;

TCanvas c_test(TH1D*);

float delta_Phi(float phi1, float phi2);
int testfunction(int inputInt=5, int in2=2, int in3=3);
/*int plotCompare_fun(TTree *tjet, int nbin, double binLow, double binHigh,
      TCut CutCommon, TCut Cut1, TCut Cut2, TCut Cut3,
      TString plotVariable, TString plotTitle,TString plotXTitle,
      TString type1Title, TString type2Title, TString type3Title);
*/
int plotCompare_fun(TTree *tjet, int nbin=50, double binLow=0, double binHigh=0.5,
      TCut CutCommon="jtpt>100&&nSubJet>=2", TCut Cut1="abs(refparton_flavorForB)==5&&( refparton_flavorProcess==5 || refparton_flavorProcess==6)", TCut Cut2="abs(refparton_flavorForB)==5&&refparton_flavorProcess==1", TCut Cut3="abs(refparton_flavorForB)!=5",
      TString add_savename="",
			TString plotVariable="jtSubZg", TString plotTitle="Sub-Jet pt2/pt2+pt1",TString plotXTitle="Zg",
      TString type1Title="GSP-B", TString type2Title="FCR-B", TString type3Title="Non B", Int_t DoNormalize=1);



class akSoftDrop4PFJetSelector : public TSelector {
public :

//// for ouput write , must declare here/////

	float nt_array[200];
	
	TTree *t_akSD4PFJet=0;
	TFile *f_out=0;

	TH1D *h_LeadJetSubPt2ov1=0;
	TH1D *h_JetPt=0;	

	Long64_t fProcessed=0;

// write variables
   Float_t         rawpt_;   //[nref]
   Float_t         jtpt_;   //[nref]
   Float_t         jteta_;   //[nref]
   Float_t         jty_;   //[nref]
   Float_t         jtphi_;   //[nref]

	 Float_t         nSubJet_;
	 Float_t         jtSubJetPt1_;
   Float_t         jtSubJetEta1_;
   Float_t         jtSubJetPhi1_;
   Float_t         jtSubJetM1_;
   Float_t         jtSubJetPt2_;
   Float_t         jtSubJetEta2_;
   Float_t         jtSubJetPhi2_;
   Float_t         jtSubJetM2_;

	 Float_t         jtSubJetPt2ov1_;
	 Float_t         jtSubZg_;
	 Float_t         jtSubJetdR12_;

   Float_t         discr_ssvHighEff_;   //[nref]
   Float_t         discr_ssvHighPur_;   //[nref]
   Float_t         discr_csvV1_;   //[nref]
   Float_t         discr_csvV2_;   //[nref]


	// refjet
	 Float_t         nrefSubJet_;
   Float_t         refSubJetPt1_;
   Float_t         refSubJetEta1_;
   Float_t         refSubJetPhi1_;
   Float_t         refSubJetM1_;
   Float_t         refSubJetPt2_;
   Float_t         refSubJetEta2_;
   Float_t         refSubJetPhi2_;
   Float_t         refSubJetM2_;

   Float_t         refSubJetPt2ov1_;
   Float_t         refSubZg_;
   Float_t         refSubJetdR12_;


  //svt
   Float_t         svtxm_;   //[nref]
   Float_t         svtxpt_;   //[nref]
   Float_t         svtxmcorr_;   //[nref]

   Float_t         pthat_;
   Float_t         refpt_;   //[nref]
   Float_t         refeta_;   //[nref]
   Float_t         refy_;   //[nref]
   Float_t         refphi_;   //[nref]
   Int_t           bProdCode_;
   Int_t           cProdCode_;
   Int_t           refparton_flavor_;   //[nref]
   Int_t           refparton_flavorForB_;   //[nref]
   Int_t           refparton_flavorProcess_;   //[nref]

	 Int_t           refFlavorID_jet_hadronID_;
   Int_t           refFlavorID_jet_partonID_;
	 Int_t           refFlavorID_jet_ID_;

   Int_t           refFlavorID_Subjet1_hadronID_;
   Int_t           refFlavorID_Subjet1_partonID_;
   Int_t           refFlavorID_Subjet1_ID_;

   Int_t           refFlavorID_Subjet2_hadronID_;
   Int_t           refFlavorID_Subjet2_partonID_;
   Int_t           refFlavorID_Subjet2_ID_;

	// gsp tag
   Float_t         refGSP_gpt_;   //[nref]
   Float_t         refGSP_geta_;   //[nref]
   Float_t         refGSP_gphi_;   //[nref]
   Float_t         refGSP_gidx_;   //[nref]
   Float_t         refGSP_b1pt_;   //[nref]
   Float_t         refGSP_b1eta_;   //[nref]
   Float_t         refGSP_b1phi_;   //[nref]
   Float_t         refGSP_b2pt_;   //[nref]
   Float_t         refGSP_b2eta_;   //[nref]
   Float_t         refGSP_b2phi_;   //[nref]
   Float_t         refGSP_b1Match_jtdR_;   //[nref]
   Float_t         refGSP_b2Match_jtdR_;   //[nref]
   Float_t         refGSP_bbdR_;   //[nref]
   Float_t         refGSP_bbzg_;   //[nref]
   Int_t           refGSP_SubJtMatched_;   //[nref]

	 // MC b - groomed reco subjet match
	 Float_t	       refGSP_b1Match_SubJt1dR_;
   Float_t         refGSP_b1Match_SubJt2dR_;
   Float_t         refGSP_b2Match_SubJt1dR_;
   Float_t         refGSP_b2Match_SubJt2dR_;
	 Int_t           refGSP_bbSubJt_dRMatchStatus_;          // dR match only 0 for not, 1 for b1-jt1 b2-jt2, 2 for b1-jt2, b2-jt1
	 Int_t   		     refGSP_bbSubJt_dR0p1MatchStatus_;       // 0.1 dR match , must <0.1 for match & >0.1 for another pair.
   Float_t         refGSP_b1Match_SubJt1PtRat_;            // pt ratio
   Float_t         refGSP_b1Match_SubJt2PtRat_;
   Float_t         refGSP_b2Match_SubJt1PtRat_;
   Float_t         refGSP_b2Match_SubJt2PtRat_;

	 Int_t           refGSP_bbSubJt_PtRatMatchStatus_;       // Big small match, 0 for not,1 for b1-jt1, b2-jt2, 2 for reverse. 
	 Int_t           refGSP_bbSubJt_PtRatTightMatchStatus_;  // Tight match
	
	 Int_t           refGSP_bbSubJt_MatchStatus_;            // both pt&dR match ,0 for not, 1 for b1-jt1 b2-jt2, 2 for b1-jt2, b2-jt1
	 Int_t           refGSP_bbSubJt_TightMatchStatus_;       // both pt & dR tight match. 


   // MC b - groomed ref subjet match
   Float_t         refGSP_b1Match_refSubJt1dR_;
   Float_t         refGSP_b1Match_refSubJt2dR_;
   Float_t         refGSP_b2Match_refSubJt1dR_;
   Float_t         refGSP_b2Match_refSubJt2dR_;
   Int_t           refGSP_bbrefSubJt_dRMatchStatus_;  			// dR match only 0 for not, 1 for b1-jt1 b2-jt2, 2 for b1-jt2, b2-jt1
   Int_t       	   refGSP_bbrefSubJt_dR0p1MatchStatus_; 		// 0.1 dR match , must <0.1 for match & >0.1 for another pair.
   Float_t         refGSP_b1Match_refSubJt1PtRat_; 					// pt ratio
   Float_t         refGSP_b1Match_refSubJt2PtRat_;
   Float_t         refGSP_b2Match_refSubJt1PtRat_;
   Float_t         refGSP_b2Match_refSubJt2PtRat_;

   Int_t           refGSP_bbrefSubJt_PtRatMatchStatus_; 			// Big small match, 0 for not,1 for b1-jt1, b2-jt2, 2 for reverse. 
   Int_t           refGSP_bbrefSubJt_PtRatTightMatchStatus_; 	// Tight match

   Int_t           refGSP_bbrefSubJt_MatchStatus_; 						// both pt&dR match ,0 for not, 1 for b1-jt1 b2-jt2, 2 for b1-jt2, b2-jt1
   Int_t           refGSP_bbrefSubJt_TightMatchStatus_;       // both pt & dR tight match. 


	


//// end ouput write ////

///// for read input ///////

   TTree          *fChain;   //!pointer to the analyzed TTree or TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   Int_t           evt;
   Float_t         b;
   Int_t           nref;
   Float_t         rawpt[MAX_NJetS];   //[nref]
   Float_t         jtpt[MAX_NJetS];   //[nref]
   Float_t         jteta[MAX_NJetS];   //[nref]
   Float_t         jty[MAX_NJetS];   //[nref]
   Float_t         jtphi[MAX_NJetS];   //[nref]
   Float_t         jtpu[MAX_NJetS];   //[nref]
   Float_t         jtm[MAX_NJetS];   //[nref]
   Float_t         jtarea[MAX_NJetS];   //[nref]
/*
   Int_t           jtnCands[MAX_NJetS];   //[nref]
   Int_t           jtnChCands[MAX_NJetS];   //[nref]
   Int_t           jtnNeCands[MAX_NJetS];   //[nref]
   Float_t         jtchargedSumConst[MAX_NJetS];   //[nref]
   Int_t           jtchargedNConst[MAX_NJetS];   //[nref]
   Float_t         jteSumConst[MAX_NJetS];   //[nref]
   Int_t           jteNConst[MAX_NJetS];   //[nref]
   Float_t         jtmuSumConst[MAX_NJetS];   //[nref]
   Int_t           jtmuNConst[MAX_NJetS];   //[nref]
   Float_t         jtphotonSumConst[MAX_NJetS];   //[nref]
   Int_t           jtphotonNConst[MAX_NJetS];   //[nref]
   Float_t         jtneutralSumConst[MAX_NJetS];   //[nref]
   Int_t           jtneutralNConst[MAX_NJetS];   //[nref]
   Float_t         jthfhadSumConst[MAX_NJetS];   //[nref]
   Int_t           jthfhadNConst[MAX_NJetS];   //[nref]
   Float_t         jthfemSumConst[MAX_NJetS];   //[nref]
   Int_t           jthfemNConst[MAX_NJetS];   //[nref]
   Float_t         jtMByPt[MAX_NJetS];   //[nref]
   Float_t         jtRMSCand[MAX_NJetS];   //[nref]
   Float_t         jtAxis1[MAX_NJetS];   //[nref]
   Float_t         jtAxis2[MAX_NJetS];   //[nref]
   Float_t         jtSigma[MAX_NJetS];   //[nref]
   Float_t         jtR[MAX_NJetS];   //[nref]
   Float_t         jtpTD[MAX_NJetS];   //[nref]
   Float_t         jtpull[MAX_NJetS];   //[nref]
   Float_t         jtrm0p5[MAX_NJetS];   //[nref]
   Float_t         jtrm1[MAX_NJetS];   //[nref]
   Float_t         jtrm2[MAX_NJetS];   //[nref]
   Float_t         jtrm3[MAX_NJetS];   //[nref]
   Float_t         jtSDm[MAX_NJetS];   //[nref]
   Float_t         jtSDpt[MAX_NJetS];   //[nref]
   Float_t         jtSDeta[MAX_NJetS];   //[nref]
   Float_t         jtSDphi[MAX_NJetS];   //[nref]
   Float_t         jtSDptFrac[MAX_NJetS];   //[nref]
   Float_t         jtSDrm0p5[MAX_NJetS];   //[nref]
   Float_t         jtSDrm1[MAX_NJetS];   //[nref]
   Float_t         jtSDrm2[MAX_NJetS];   //[nref]
   Float_t         jtSDrm3[MAX_NJetS];   //[nref]
   Float_t         jtTbeta20p2[MAX_NJetS];   //[nref]
   Float_t         jtTbeta20p3[MAX_NJetS];   //[nref]
   Float_t         jtTbeta20p4[MAX_NJetS];   //[nref]
   Float_t         jtTbeta20p5[MAX_NJetS];   //[nref]
   Float_t         jtTbeta30p2[MAX_NJetS];   //[nref]
   Float_t         jtTbeta30p3[MAX_NJetS];   //[nref]
   Float_t         jtTbeta30p4[MAX_NJetS];   //[nref]
   Float_t         jtTbeta30p5[MAX_NJetS];   //[nref]
   Float_t         jtCbeta20p2[MAX_NJetS];   //[nref]
   Float_t         jtCbeta20p3[MAX_NJetS];   //[nref]
   Float_t         jtCbeta20p4[MAX_NJetS];   //[nref]
   Float_t         jtCbeta20p5[MAX_NJetS];   //[nref]
   Float_t         jtZ11[MAX_NJetS];   //[nref]
   Float_t         jtZ20[MAX_NJetS];   //[nref]
   Float_t         jtZ22[MAX_NJetS];   //[nref]
   Float_t         jtZ31[MAX_NJetS];   //[nref]
   Float_t         jtZ33[MAX_NJetS];   //[nref]
   Float_t         jtZ40[MAX_NJetS];   //[nref]
   Float_t         jtZ42[MAX_NJetS];   //[nref]
   Float_t         jtZ44[MAX_NJetS];   //[nref]
   Float_t         jtZ51[MAX_NJetS];   //[nref]
   Float_t         jtZ53[MAX_NJetS];   //[nref]
   Float_t         jtZ55[MAX_NJetS];   //[nref]
   Float_t         jtPhi1[MAX_NJetS];   //[nref]
   Float_t         jtPhi2[MAX_NJetS];   //[nref]
   Float_t         jtPhi3[MAX_NJetS];   //[nref]
   Float_t         jtPhi4[MAX_NJetS];   //[nref]
   Float_t         jtPhi5[MAX_NJetS];   //[nref]
   Float_t         jtPhi6[MAX_NJetS];   //[nref]
   Float_t         jtPhi7[MAX_NJetS];   //[nref]
   Float_t         jtSkx[MAX_NJetS];   //[nref]
   Float_t         jtSky[MAX_NJetS];   //[nref]
*/

   Float_t         jtPfCHF[MAX_NJetS];   //[nref]
   Float_t         jtPfNHF[MAX_NJetS];   //[nref]
   Float_t         jtPfCEF[MAX_NJetS];   //[nref]
   Float_t         jtPfNEF[MAX_NJetS];   //[nref]
   Float_t         jtPfMUF[MAX_NJetS];   //[nref]
   Int_t           jtPfCHM[MAX_NJetS];   //[nref]
   Int_t           jtPfNHM[MAX_NJetS];   //[nref]
   Int_t           jtPfCEM[MAX_NJetS];   //[nref]
   Int_t           jtPfNEM[MAX_NJetS];   //[nref]
   Int_t           jtPfMUM[MAX_NJetS];   //[nref]
   Float_t         jttau1[MAX_NJetS];   //[nref]
   Float_t         jttau2[MAX_NJetS];   //[nref]
   Float_t         jttau3[MAX_NJetS];   //[nref]
   vector<vector<float> > *jtSubJetPt;
   vector<vector<float> > *jtSubJetEta;
   vector<vector<float> > *jtSubJetPhi;
   vector<vector<float> > *jtSubJetM;
/*
   vector<vector<int> > *jtConstituentsId;
   vector<vector<float> > *jtConstituentsE;
   vector<vector<float> > *jtConstituentsPt;
   vector<vector<float> > *jtConstituentsEta;
   vector<vector<float> > *jtConstituentsPhi;
   vector<vector<float> > *jtConstituentsM;
   vector<vector<int> > *jtSDConstituentsId;
   vector<vector<float> > *jtSDConstituentsE;
   vector<vector<float> > *jtSDConstituentsPt;
   vector<vector<float> > *jtSDConstituentsEta;
   vector<vector<float> > *jtSDConstituentsPhi;
   vector<vector<float> > *jtSDConstituentsM;
*/
   Float_t         discr_jetID_cuts[MAX_NJetS];   //[nref]
   Float_t         discr_jetID_bdt[MAX_NJetS];   //[nref]
   Float_t         discr_fr01[MAX_NJetS];   //[nref]
   Float_t         trackMax[MAX_NJetS];   //[nref]
   Float_t         trackSum[MAX_NJetS];   //[nref]
   Int_t           trackN[MAX_NJetS];   //[nref]
   Float_t         trackHardSum[MAX_NJetS];   //[nref]
   Int_t           trackHardN[MAX_NJetS];   //[nref]
   Float_t         chargedMax[MAX_NJetS];   //[nref]
   Float_t         chargedSum[MAX_NJetS];   //[nref]
   Int_t           chargedN[MAX_NJetS];   //[nref]
   Float_t         chargedHardSum[MAX_NJetS];   //[nref]
   Int_t           chargedHardN[MAX_NJetS];   //[nref]
   Float_t         photonMax[MAX_NJetS];   //[nref]
   Float_t         photonSum[MAX_NJetS];   //[nref]
   Int_t           photonN[MAX_NJetS];   //[nref]
   Float_t         photonHardSum[MAX_NJetS];   //[nref]
   Int_t           photonHardN[MAX_NJetS];   //[nref]
   Float_t         neutralMax[MAX_NJetS];   //[nref]
   Float_t         neutralSum[MAX_NJetS];   //[nref]
   Int_t           neutralN[MAX_NJetS];   //[nref]
   Float_t         hcalSum[MAX_NJetS];   //[nref]
   Float_t         ecalSum[MAX_NJetS];   //[nref]
   Float_t         eMax[MAX_NJetS];   //[nref]
   Float_t         eSum[MAX_NJetS];   //[nref]
   Int_t           eN[MAX_NJetS];   //[nref]
   Float_t         muMax[MAX_NJetS];   //[nref]
   Float_t         muSum[MAX_NJetS];   //[nref]
   Int_t           muN[MAX_NJetS];   //[nref]
   Float_t         discr_ssvHighEff[MAX_NJetS];   //[nref]
   Float_t         discr_ssvHighPur[MAX_NJetS];   //[nref]
   Float_t         discr_csvV1[MAX_NJetS];   //[nref]
   Float_t         discr_csvV2[MAX_NJetS];   //[nref]
   Float_t         discr_muByIp3[MAX_NJetS];   //[nref]
   Float_t         discr_muByPt[MAX_NJetS];   //[nref]
   Float_t         discr_prob[MAX_NJetS];   //[nref]
   Float_t         discr_probb[MAX_NJetS];   //[nref]
   Float_t         discr_tcHighEff[MAX_NJetS];   //[nref]
   Float_t         discr_tcHighPur[MAX_NJetS];   //[nref]
   Float_t         ndiscr_ssvHighEff[MAX_NJetS];   //[nref]
   Float_t         ndiscr_ssvHighPur[MAX_NJetS];   //[nref]
   Float_t         ndiscr_csvV1[MAX_NJetS];   //[nref]
   Float_t         ndiscr_csvV2[MAX_NJetS];   //[nref]
   Float_t         ndiscr_muByPt[MAX_NJetS];   //[nref]
   Float_t         pdiscr_csvV1[MAX_NJetS];   //[nref]
   Float_t         pdiscr_csvV2[MAX_NJetS];   //[nref]
   Int_t           nsvtx[MAX_NJetS];   //[nref]
   Int_t           svtxntrk[MAX_NJetS];   //[nref]
   Float_t         svtxdl[MAX_NJetS];   //[nref]
   Float_t         svtxdls[MAX_NJetS];   //[nref]
   Float_t         svtxdl2d[MAX_NJetS];   //[nref]
   Float_t         svtxdls2d[MAX_NJetS];   //[nref]
   Float_t         svtxm[MAX_NJetS];   //[nref]
   Float_t         svtxpt[MAX_NJetS];   //[nref]
   Float_t         svtxmcorr[MAX_NJetS];   //[nref]
   Int_t           nIPtrk[MAX_NJetS];   //[nref]
   Int_t           nselIPtrk[MAX_NJetS];   //[nref]
   Float_t         mue[MAX_NJetS];   //[nref]
   Float_t         mupt[MAX_NJetS];   //[nref]
   Float_t         mueta[MAX_NJetS];   //[nref]
   Float_t         muphi[MAX_NJetS];   //[nref]
   Float_t         mudr[MAX_NJetS];   //[nref]
   Float_t         muptrel[MAX_NJetS];   //[nref]
   Int_t           muchg[MAX_NJetS];   //[nref]
   Int_t           beamId1;
   Int_t           beamId2;
   Float_t         pthat;
   Float_t         refpt[MAX_NJetS];   //[nref]
   Float_t         refeta[MAX_NJetS];   //[nref]
   Float_t         refy[MAX_NJetS];   //[nref]
   Float_t         refphi[MAX_NJetS];   //[nref]
   Float_t         refm[MAX_NJetS];   //[nref]
   Float_t         refarea[MAX_NJetS];   //[nref]
   Int_t           bProdCode;
   Int_t           cProdCode;
/*
   Int_t           refnCands[MAX_NJetS];   //[nref]
   Int_t           refnChCands[MAX_NJetS];   //[nref]
   Int_t           refnNeCands[MAX_NJetS];   //[nref]
   Float_t         refchargedSumConst[MAX_NJetS];   //[nref]
   Int_t           refchargedNConst[MAX_NJetS];   //[nref]
   Float_t         refeSumConst[MAX_NJetS];   //[nref]
   Int_t           refeNConst[MAX_NJetS];   //[nref]
   Float_t         refmuSumConst[MAX_NJetS];   //[nref]
   Int_t           refmuNConst[MAX_NJetS];   //[nref]
   Float_t         refphotonSumConst[MAX_NJetS];   //[nref]
   Int_t           refphotonNConst[MAX_NJetS];   //[nref]
   Float_t         refneutralSumConst[MAX_NJetS];   //[nref]
   Int_t           refneutralNConst[MAX_NJetS];   //[nref]
   Float_t         refhfhadSumConst[MAX_NJetS];   //[nref]
   Int_t           refhfhadNConst[MAX_NJetS];   //[nref]
   Float_t         refhfemSumConst[MAX_NJetS];   //[nref]
   Int_t           refhfemNConst[MAX_NJetS];   //[nref]
   Float_t         refMByPt[MAX_NJetS];   //[nref]
   Float_t         refRMSCand[MAX_NJetS];   //[nref]
   Float_t         refAxis1[MAX_NJetS];   //[nref]
   Float_t         refAxis2[MAX_NJetS];   //[nref]
   Float_t         refSigma[MAX_NJetS];   //[nref]
   Float_t         refR[MAX_NJetS];   //[nref]
   Float_t         refpTD[MAX_NJetS];   //[nref]
   Float_t         refpull[MAX_NJetS];   //[nref]
   Float_t         refrm0p5[MAX_NJetS];   //[nref]
   Float_t         refrm1[MAX_NJetS];   //[nref]
   Float_t         refrm2[MAX_NJetS];   //[nref]
   Float_t         refrm3[MAX_NJetS];   //[nref]
   Float_t         refSDm[MAX_NJetS];   //[nref]
   Float_t         refSDpt[MAX_NJetS];   //[nref]
   Float_t         refSDeta[MAX_NJetS];   //[nref]
   Float_t         refSDphi[MAX_NJetS];   //[nref]
   Float_t         refSDptFrac[MAX_NJetS];   //[nref]
   Float_t         refSDrm0p5[MAX_NJetS];   //[nref]
   Float_t         refSDrm1[MAX_NJetS];   //[nref]
   Float_t         refSDrm2[MAX_NJetS];   //[nref]
   Float_t         refSDrm3[MAX_NJetS];   //[nref]
   Float_t         refTbeta20p2[MAX_NJetS];   //[nref]
   Float_t         refTbeta20p3[MAX_NJetS];   //[nref]
   Float_t         refTbeta20p4[MAX_NJetS];   //[nref]
   Float_t         refTbeta20p5[MAX_NJetS];   //[nref]
   Float_t         refTbeta30p2[MAX_NJetS];   //[nref]
   Float_t         refTbeta30p3[MAX_NJetS];   //[nref]
   Float_t         refTbeta30p4[MAX_NJetS];   //[nref]
   Float_t         refTbeta30p5[MAX_NJetS];   //[nref]
   Float_t         refCbeta20p2[MAX_NJetS];   //[nref]
   Float_t         refCbeta20p3[MAX_NJetS];   //[nref]
   Float_t         refCbeta20p4[MAX_NJetS];   //[nref]
   Float_t         refCbeta20p5[MAX_NJetS];   //[nref]
   Float_t         refZ11[MAX_NJetS];   //[nref]
   Float_t         refZ20[MAX_NJetS];   //[nref]
   Float_t         refZ22[MAX_NJetS];   //[nref]
   Float_t         refZ31[MAX_NJetS];   //[nref]
   Float_t         refZ33[MAX_NJetS];   //[nref]
   Float_t         refZ40[MAX_NJetS];   //[nref]
   Float_t         refZ42[MAX_NJetS];   //[nref]
   Float_t         refZ44[MAX_NJetS];   //[nref]
   Float_t         refZ51[MAX_NJetS];   //[nref]
   Float_t         refZ53[MAX_NJetS];   //[nref]
   Float_t         refZ55[MAX_NJetS];   //[nref]
   Float_t         refPhi1[MAX_NJetS];   //[nref]
   Float_t         refPhi2[MAX_NJetS];   //[nref]
   Float_t         refPhi3[MAX_NJetS];   //[nref]
   Float_t         refPhi4[MAX_NJetS];   //[nref]
   Float_t         refPhi5[MAX_NJetS];   //[nref]
   Float_t         refPhi6[MAX_NJetS];   //[nref]
   Float_t         refPhi7[MAX_NJetS];   //[nref]
   Float_t         refSkx[MAX_NJetS];   //[nref]
   Float_t         refSky[MAX_NJetS];   //[nref]
 */

   Float_t         refGSP_gpt[MAX_NJetS];   //[nref]
   Float_t         refGSP_geta[MAX_NJetS];   //[nref]
   Float_t         refGSP_gphi[MAX_NJetS];   //[nref]
   Float_t         refGSP_gidx[MAX_NJetS];   //[nref]
   Float_t         refGSP_b1pt[MAX_NJetS];   //[nref]
   Float_t         refGSP_b1eta[MAX_NJetS];   //[nref]
   Float_t         refGSP_b1phi[MAX_NJetS];   //[nref]
   Float_t         refGSP_b2pt[MAX_NJetS];   //[nref]
   Float_t         refGSP_b2eta[MAX_NJetS];   //[nref]
   Float_t         refGSP_b2phi[MAX_NJetS];   //[nref]
   Float_t         refGSP_b1Match_jtdR[MAX_NJetS];   //[nref]
   Float_t         refGSP_b2Match_jtdR[MAX_NJetS];   //[nref]
   Float_t         refGSP_bbdR[MAX_NJetS];   //[nref]
   Float_t         refGSP_bbzg[MAX_NJetS];   //[nref]
   Int_t           refGSP_SubJtMatched[MAX_NJetS];   //[nref]

   Int_t           refFlavorID_jet_hadronID [MAX_NJetS];   //[nref]
   Float_t         refFlavorID_jet_hadronPT [MAX_NJetS];   //[nref]
   Float_t         refFlavorID_jet_hadronEta[MAX_NJetS];   //[nref]
   Float_t         refFlavorID_jet_hadronPhi[MAX_NJetS];   //[nref]
   Float_t         refFlavorID_jet_hadronDR [MAX_NJetS];   //[nref]
   Int_t           refFlavorID_jet_partonID [MAX_NJetS];   //[nref]
   Float_t         refFlavorID_jet_partonPT [MAX_NJetS];   //[nref]
   Float_t         refFlavorID_jet_partonEta[MAX_NJetS];   //[nref]
   Float_t         refFlavorID_jet_partonPhi[MAX_NJetS];   //[nref]
   Float_t         refFlavorID_jet_partonDR [MAX_NJetS];   //[nref]
   Int_t           refFlavorID_Subjet1_hadronID [MAX_NJetS];   //[nref]
   Float_t         refFlavorID_Subjet1_hadronPT [MAX_NJetS];   //[nref]
   Float_t         refFlavorID_Subjet1_hadronEta[MAX_NJetS];   //[nref]
   Float_t         refFlavorID_Subjet1_hadronPhi[MAX_NJetS];   //[nref]
   Float_t         refFlavorID_Subjet1_hadronDR [MAX_NJetS];   //[nref]
   Int_t           refFlavorID_Subjet1_partonID [MAX_NJetS];   //[nref]
   Float_t         refFlavorID_Subjet1_partonPT [MAX_NJetS];   //[nref]
   Float_t         refFlavorID_Subjet1_partonEta[MAX_NJetS];   //[nref]
   Float_t         refFlavorID_Subjet1_partonPhi[MAX_NJetS];   //[nref]
   Float_t         refFlavorID_Subjet1_partonDR [MAX_NJetS];   //[nref]
   Int_t           refFlavorID_Subjet2_hadronID [MAX_NJetS];   //[nref]
   Float_t         refFlavorID_Subjet2_hadronPT [MAX_NJetS];   //[nref]
   Float_t         refFlavorID_Subjet2_hadronEta[MAX_NJetS];   //[nref]
   Float_t         refFlavorID_Subjet2_hadronPhi[MAX_NJetS];   //[nref]
   Float_t         refFlavorID_Subjet2_hadronDR [MAX_NJetS];   //[nref]
   Int_t           refFlavorID_Subjet2_partonID [MAX_NJetS];   //[nref]
   Float_t         refFlavorID_Subjet2_partonPT [MAX_NJetS];   //[nref]
   Float_t         refFlavorID_Subjet2_partonEta[MAX_NJetS];   //[nref]
   Float_t         refFlavorID_Subjet2_partonPhi[MAX_NJetS];   //[nref]
   Float_t         refFlavorID_Subjet2_partonDR [MAX_NJetS];   //[nref]


   Float_t         reftau1[MAX_NJetS];   //[nref]
   Float_t         reftau2[MAX_NJetS];   //[nref]
   Float_t         reftau3[MAX_NJetS];   //[nref]
   Float_t         refdphijt[MAX_NJetS];   //[nref]
   Float_t         refdrjt[MAX_NJetS];   //[nref]
   Float_t         refparton_pt[MAX_NJetS];   //[nref]
   Int_t           refparton_flavor[MAX_NJetS];   //[nref]
   Int_t           refparton_flavorForB[MAX_NJetS];   //[nref]
   Int_t           refparton_flavorProcess[MAX_NJetS];   //[nref]
   Float_t         refptG[MAX_NJetS];   //[nref]
   Float_t         refetaG[MAX_NJetS];   //[nref]
   Float_t         refphiG[MAX_NJetS];   //[nref]
   Float_t         refmG[MAX_NJetS];   //[nref]
   vector<vector<float> > *refSubJetPt;
   vector<vector<float> > *refSubJetEta;
   vector<vector<float> > *refSubJetPhi;
   vector<vector<float> > *refSubJetM;
 /*
   vector<vector<int> > *refConstituentsId;
   vector<vector<float> > *refConstituentsE;
   vector<vector<float> > *refConstituentsPt;
   vector<vector<float> > *refConstituentsEta;
   vector<vector<float> > *refConstituentsPhi;
   vector<vector<float> > *refConstituentsM;
   vector<vector<int> > *refSDConstituentsId;
   vector<vector<float> > *refSDConstituentsE;
   vector<vector<float> > *refSDConstituentsPt;
   vector<vector<float> > *refSDConstituentsEta;
   vector<vector<float> > *refSDConstituentsPhi;
   vector<vector<float> > *refSDConstituentsM;
*/
   Float_t         genChargedSum[MAX_NJetS];   //[nref]
   Float_t         genHardSum[MAX_NJetS];   //[nref]
   Float_t         signalChargedSum[MAX_NJetS];   //[nref]
   Float_t         signalHardSum[MAX_NJetS];   //[nref]
   Int_t           subid[MAX_NJetS];   //[nref]
   Int_t           ngen;
   Int_t           genmatchindex[MAX_NJetS];   //[ngen]
   Float_t         genpt[MAX_NJetS];   //[ngen]
   Float_t         geneta[MAX_NJetS];   //[ngen]
   Float_t         geny[MAX_NJetS];   //[ngen]
   Float_t         gentau1[MAX_NJetS];   //[ngen]
   Float_t         gentau2[MAX_NJetS];   //[ngen]
   Float_t         gentau3[MAX_NJetS];   //[ngen]
   Float_t         genphi[MAX_NJetS];   //[ngen]
   Float_t         genm[MAX_NJetS];   //[ngen]
   Float_t         gendphijt[MAX_NJetS];   //[ngen]
   Float_t         gendrjt[MAX_NJetS];   //[ngen]
/*
   Int_t           gennCands[MAX_NJetS];   //[ngen]
   Int_t           gennChCands[MAX_NJetS];   //[ngen]
   Int_t           gennNeCands[MAX_NJetS];   //[ngen]
   Int_t           genchargedNConst[MAX_NJetS];   //[ngen]
   Float_t         geneSumConst[MAX_NJetS];   //[ngen]
   Int_t           geneNConst[MAX_NJetS];   //[ngen]
   Float_t         genmuSumConst[MAX_NJetS];   //[ngen]
   Int_t           genmuNConst[MAX_NJetS];   //[ngen]
   Float_t         genphotonSumConst[MAX_NJetS];   //[ngen]
   Int_t           genphotonNConst[MAX_NJetS];   //[ngen]
   Float_t         genneutralSumConst[MAX_NJetS];   //[ngen]
   Int_t           genneutralNConst[MAX_NJetS];   //[ngen]
   Float_t         genhfhadSumConst[MAX_NJetS];   //[ngen]
   Int_t           genhfhadNConst[MAX_NJetS];   //[ngen]
   Float_t         genhfemSumConst[MAX_NJetS];   //[ngen]
   Int_t           genhfemNConst[MAX_NJetS];   //[ngen]
   Float_t         genMByPt[MAX_NJetS];   //[ngen]
   Float_t         genRMSCand[MAX_NJetS];   //[ngen]
   Float_t         genAxis1[MAX_NJetS];   //[ngen]
   Float_t         genAxis2[MAX_NJetS];   //[ngen]
   Float_t         genSigma[MAX_NJetS];   //[ngen]
   Float_t         genR[MAX_NJetS];   //[ngen]
   Float_t         genpTD[MAX_NJetS];   //[ngen]
   Float_t         genpull[MAX_NJetS];   //[ngen]
   Float_t         genrm0p5[MAX_NJetS];   //[ngen]
   Float_t         genrm1[MAX_NJetS];   //[ngen]
   Float_t         genrm2[MAX_NJetS];   //[ngen]
   Float_t         genrm3[MAX_NJetS];   //[ngen]
   Float_t         genSDm[MAX_NJetS];   //[ngen]
   Float_t         genSDpt[MAX_NJetS];   //[ngen]
   Float_t         genSDeta[MAX_NJetS];   //[ngen]
   Float_t         genSDphi[MAX_NJetS];   //[ngen]
   Float_t         genSDptFrac[MAX_NJetS];   //[ngen]
   Float_t         genSDrm0p5[MAX_NJetS];   //[ngen]
   Float_t         genSDrm1[MAX_NJetS];   //[ngen]
   Float_t         genSDrm2[MAX_NJetS];   //[ngen]
   Float_t         genSDrm3[MAX_NJetS];   //[ngen]
   Float_t         genTbeta20p2[MAX_NJetS];   //[ngen]
   Float_t         genTbeta20p3[MAX_NJetS];   //[ngen]
   Float_t         genTbeta20p4[MAX_NJetS];   //[ngen]
   Float_t         genTbeta20p5[MAX_NJetS];   //[ngen]
   Float_t         genTbeta30p2[MAX_NJetS];   //[ngen]
   Float_t         genTbeta30p3[MAX_NJetS];   //[ngen]
   Float_t         genTbeta30p4[MAX_NJetS];   //[ngen]
   Float_t         genTbeta30p5[MAX_NJetS];   //[ngen]
   Float_t         genCbeta20p2[MAX_NJetS];   //[ngen]
   Float_t         genCbeta20p3[MAX_NJetS];   //[ngen]
   Float_t         genCbeta20p4[MAX_NJetS];   //[ngen]
   Float_t         genCbeta20p5[MAX_NJetS];   //[ngen]
   Float_t         genZ11[MAX_NJetS];   //[ngen]
   Float_t         genZ20[MAX_NJetS];   //[ngen]
   Float_t         genZ22[MAX_NJetS];   //[ngen]
   Float_t         genZ31[MAX_NJetS];   //[ngen]
   Float_t         genZ33[MAX_NJetS];   //[ngen]
   Float_t         genZ40[MAX_NJetS];   //[ngen]
   Float_t         genZ42[MAX_NJetS];   //[ngen]
   Float_t         genZ44[MAX_NJetS];   //[ngen]
   Float_t         genZ51[MAX_NJetS];   //[ngen]
   Float_t         genZ53[MAX_NJetS];   //[ngen]
   Float_t         genZ55[MAX_NJetS];   //[ngen]
   Float_t         genPhi1[MAX_NJetS];   //[ngen]
   Float_t         genPhi2[MAX_NJetS];   //[ngen]
   Float_t         genPhi3[MAX_NJetS];   //[ngen]
   Float_t         genPhi4[MAX_NJetS];   //[ngen]
   Float_t         genPhi5[MAX_NJetS];   //[ngen]
   Float_t         genPhi6[MAX_NJetS];   //[ngen]
   Float_t         genPhi7[MAX_NJetS];   //[ngen]
   Float_t         genSkx[MAX_NJetS];   //[ngen]
   Float_t         genSky[MAX_NJetS];   //[ngen]
*/
   Float_t         genptG[MAX_NJetS];   //[ngen]
   Float_t         genetaG[MAX_NJetS];   //[ngen]
   Float_t         genphiG[MAX_NJetS];   //[ngen]
   Float_t         genmG[MAX_NJetS];   //[ngen]
   vector<vector<float> > *genSubJetPt;
   vector<vector<float> > *genSubJetEta;
   vector<vector<float> > *genSubJetPhi;
   vector<vector<float> > *genSubJetM;
/*
   vector<vector<int> > *genConstituentsId;
   vector<vector<float> > *genConstituentsE;
   vector<vector<float> > *genConstituentsPt;
   vector<vector<float> > *genConstituentsEta;
   vector<vector<float> > *genConstituentsPhi;
   vector<vector<float> > *genConstituentsM;
   vector<vector<int> > *genSDConstituentsId;
   vector<vector<float> > *genSDConstituentsE;
   vector<vector<float> > *genSDConstituentsPt;
   vector<vector<float> > *genSDConstituentsEta;
   vector<vector<float> > *genSDConstituentsPhi;
   vector<vector<float> > *genSDConstituentsM;
*/
   Int_t           gensubid[MAX_NJetS];   //[ngen]

   // List of branches
   TBranch        *b_evt;   //!
   TBranch        *b_b;   //!
   TBranch        *b_nref;   //!
   TBranch        *b_rawpt;   //!
   TBranch        *b_jtpt;   //!
   TBranch        *b_jteta;   //!
   TBranch        *b_jty;   //!
   TBranch        *b_jtphi;   //!
   TBranch        *b_jtpu;   //!
   TBranch        *b_jtm;   //!
   TBranch        *b_jtarea;   //!
/*   TBranch        *b_jtnCands;   //!
   TBranch        *b_jtnChCands;   //!
   TBranch        *b_jtnNeCands;   //!
   TBranch        *b_jtchargedSumConst;   //!
   TBranch        *b_jtchargedNConst;   //!
   TBranch        *b_jteSumConst;   //!
   TBranch        *b_jteNConst;   //!
   TBranch        *b_jtmuSumConst;   //!
   TBranch        *b_jtmuNConst;   //!
   TBranch        *b_jtphotonSumConst;   //!
   TBranch        *b_jtphotonNConst;   //!
   TBranch        *b_jtneutralSumConst;   //!
   TBranch        *b_jtneutralNConst;   //!
   TBranch        *b_jthfhadSumConst;   //!
   TBranch        *b_jthfhadNConst;   //!
   TBranch        *b_jthfemSumConst;   //!
   TBranch        *b_jthfemNConst;   //!
   TBranch        *b_jtMByPt;   //!
   TBranch        *b_jtRMSCand;   //!
   TBranch        *b_jtAxis1;   //!
   TBranch        *b_jtAxis2;   //!
   TBranch        *b_jtSigma;   //!
   TBranch        *b_jtR;   //!
   TBranch        *b_jtpTD;   //!
   TBranch        *b_jtpull;   //!
   TBranch        *b_jtrm0p5;   //!
   TBranch        *b_jtrm1;   //!
   TBranch        *b_jtrm2;   //!
   TBranch        *b_jtrm3;   //!
   TBranch        *b_jtSDm;   //!
   TBranch        *b_jtSDpt;   //!
   TBranch        *b_jtSDeta;   //!
   TBranch        *b_jtSDphi;   //!
   TBranch        *b_jtSDptFrac;   //!
   TBranch        *b_jtSDrm0p5;   //!
   TBranch        *b_jtSDrm1;   //!
   TBranch        *b_jtSDrm2;   //!
   TBranch        *b_jtSDrm3;   //!
   TBranch        *b_jtTbeta20p2;   //!
   TBranch        *b_jtTbeta20p3;   //!
   TBranch        *b_jtTbeta20p4;   //!
   TBranch        *b_jtTbeta20p5;   //!
   TBranch        *b_jtTbeta30p2;   //!
   TBranch        *b_jtTbeta30p3;   //!
   TBranch        *b_jtTbeta30p4;   //!
   TBranch        *b_jtTbeta30p5;   //!
   TBranch        *b_jtCbeta20p2;   //!
   TBranch        *b_jtCbeta20p3;   //!
   TBranch        *b_jtCbeta20p4;   //!
   TBranch        *b_jtCbeta20p5;   //!
   TBranch        *b_jtZ11;   //!
   TBranch        *b_jtZ20;   //!
   TBranch        *b_jtZ22;   //!
   TBranch        *b_jtZ31;   //!
   TBranch        *b_jtZ33;   //!
   TBranch        *b_jtZ40;   //!
   TBranch        *b_jtZ42;   //!
   TBranch        *b_jtZ44;   //!
   TBranch        *b_jtZ51;   //!
   TBranch        *b_jtZ53;   //!
   TBranch        *b_jtZ55;   //!
   TBranch        *b_jtPhi1;   //!
   TBranch        *b_jtPhi2;   //!
   TBranch        *b_jtPhi3;   //!
   TBranch        *b_jtPhi4;   //!
   TBranch        *b_jtPhi5;   //!
   TBranch        *b_jtPhi6;   //!
   TBranch        *b_jtPhi7;   //!
   TBranch        *b_jtSkx;   //!
   TBranch        *b_jtSky;  */ //! 
   TBranch        *b_jtPfCHF;   //!
   TBranch        *b_jtPfNHF;   //!
   TBranch        *b_jtPfCEF;   //!
   TBranch        *b_jtPfNEF;   //!
   TBranch        *b_jtPfMUF;   //!
   TBranch        *b_jtPfCHM;   //!
   TBranch        *b_jtPfNHM;   //!
   TBranch        *b_jtPfCEM;   //!
   TBranch        *b_jtPfNEM;   //!
   TBranch        *b_jtPfMUM;   //!
   TBranch        *b_jttau1;   //!
   TBranch        *b_jttau2;   //!
   TBranch        *b_jttau3;   //!
   TBranch        *b_jtSubJetPt;   //!
   TBranch        *b_jtSubJetEta;   //!
   TBranch        *b_jtSubJetPhi;   //!
   TBranch        *b_jtSubJetM;   //!
/*   TBranch        *b_jtConstituentsId;   //!
   TBranch        *b_jtConstituentsE;   //!
   TBranch        *b_jtConstituentsPt;   //!
   TBranch        *b_jtConstituentsEta;   //!
   TBranch        *b_jtConstituentsPhi;   //!
   TBranch        *b_jtConstituentsM;   //!
   TBranch        *b_jtSDConstituentsId;   //!
   TBranch        *b_jtSDConstituentsE;   //!
   TBranch        *b_jtSDConstituentsPt;   //!
   TBranch        *b_jtSDConstituentsEta;   //!
   TBranch        *b_jtSDConstituentsPhi;   //!
   TBranch        *b_jtSDConstituentsM;  */ //!
   TBranch        *b_discr_jetID_cuts;   //!
   TBranch        *b_discr_jetID_bdt;   //!
   TBranch        *b_discr_fr01;   //!
   TBranch        *b_trackMax;   //!
   TBranch        *b_trackSum;   //!
   TBranch        *b_trackN;   //!
   TBranch        *b_trackHardSum;   //!
   TBranch        *b_trackHardN;   //!
   TBranch        *b_chargedMax;   //!
   TBranch        *b_chargedSum;   //!
   TBranch        *b_chargedN;   //!
   TBranch        *b_chargedHardSum;   //!
   TBranch        *b_chargedHardN;   //!
   TBranch        *b_photonMax;   //!
   TBranch        *b_photonSum;   //!
   TBranch        *b_photonN;   //!
   TBranch        *b_photonHardSum;   //!
   TBranch        *b_photonHardN;   //!
   TBranch        *b_neutralMax;   //!
   TBranch        *b_neutralSum;   //!
   TBranch        *b_neutralN;   //!
   TBranch        *b_hcalSum;   //!
   TBranch        *b_ecalSum;   //!
   TBranch        *b_eMax;   //!
   TBranch        *b_eSum;   //!
   TBranch        *b_eN;   //!
   TBranch        *b_muMax;   //!
   TBranch        *b_muSum;   //!
   TBranch        *b_muN;   //!
   TBranch        *b_discr_ssvHighEff;   //!
   TBranch        *b_discr_ssvHighPur;   //!
   TBranch        *b_discr_csvV1;   //!
   TBranch        *b_discr_csvV2;   //!
   TBranch        *b_discr_muByIp3;   //!
   TBranch        *b_discr_muByPt;   //!
   TBranch        *b_discr_prob;   //!
   TBranch        *b_discr_probb;   //!
   TBranch        *b_discr_tcHighEff;   //!
   TBranch        *b_discr_tcHighPur;   //!
   TBranch        *b_ndiscr_ssvHighEff;   //!
   TBranch        *b_ndiscr_ssvHighPur;   //!
   TBranch        *b_ndiscr_csvV1;   //!
   TBranch        *b_ndiscr_csvV2;   //!
   TBranch        *b_ndiscr_muByPt;   //!
   TBranch        *b_pdiscr_csvV1;   //!
   TBranch        *b_pdiscr_csvV2;   //!
   TBranch        *b_nsvtx;   //!
   TBranch        *b_svtxntrk;   //!
   TBranch        *b_svtxdl;   //!
   TBranch        *b_svtxdls;   //!
   TBranch        *b_svtxdl2d;   //!
   TBranch        *b_svtxdls2d;   //!
   TBranch        *b_svtxm;   //!
   TBranch        *b_svtxpt;   //!
   TBranch        *b_svtxmcorr;   //!
   TBranch        *b_nIPtrk;   //!
   TBranch        *b_nselIPtrk;   //!
   TBranch        *b_mue;   //!
   TBranch        *b_mupt;   //!
   TBranch        *b_mueta;   //!
   TBranch        *b_muphi;   //!
   TBranch        *b_mudr;   //!
   TBranch        *b_muptrel;   //!
   TBranch        *b_muchg;   //!
   TBranch        *b_beamId1;   //!
   TBranch        *b_beamId2;   //!
   TBranch        *b_pthat;   //!
   TBranch        *b_refpt;   //!
   TBranch        *b_refeta;   //!
   TBranch        *b_refy;   //!
   TBranch        *b_refphi;   //!
   TBranch        *b_refm;   //!
   TBranch        *b_refarea;   //!
   TBranch        *b_bProdCode;   //!
   TBranch        *b_cProdCode;   //!
/*   TBranch        *b_refnCands;   //!
   TBranch        *b_refnChCands;   //!
   TBranch        *b_refnNeCands;   //!
   TBranch        *b_refchargedSumConst;   //!
   TBranch        *b_refchargedNConst;   //!
   TBranch        *b_refeSumConst;   //!
   TBranch        *b_refeNConst;   //!
   TBranch        *b_refmuSumConst;   //!
   TBranch        *b_refmuNConst;   //!
   TBranch        *b_refphotonSumConst;   //!
   TBranch        *b_refphotonNConst;   //!
   TBranch        *b_refneutralSumConst;   //!
   TBranch        *b_refneutralNConst;   //!
   TBranch        *b_refhfhadSumConst;   //!
   TBranch        *b_refhfhadNConst;   //!
   TBranch        *b_refhfemSumConst;   //!
   TBranch        *b_refhfemNConst;   //!
   TBranch        *b_refMByPt;   //!
   TBranch        *b_refRMSCand;   //!
   TBranch        *b_refAxis1;   //!
   TBranch        *b_refAxis2;   //!
   TBranch        *b_refSigma;   //!
   TBranch        *b_refR;   //!
   TBranch        *b_refpTD;   //!
   TBranch        *b_refpull;   //!
   TBranch        *b_refrm0p5;   //!
   TBranch        *b_refrm1;   //!
   TBranch        *b_refrm2;   //!
   TBranch        *b_refrm3;   //!
   TBranch        *b_refSDm;   //!
   TBranch        *b_refSDpt;   //!
   TBranch        *b_refSDeta;   //!
   TBranch        *b_refSDphi;   //!
   TBranch        *b_refSDptFrac;   //!
   TBranch        *b_refSDrm0p5;   //!
   TBranch        *b_refSDrm1;   //!
   TBranch        *b_refSDrm2;   //!
   TBranch        *b_refSDrm3;   //!
   TBranch        *b_refTbeta20p2;   //!
   TBranch        *b_refTbeta20p3;   //!
   TBranch        *b_refTbeta20p4;   //!
   TBranch        *b_refTbeta20p5;   //!
   TBranch        *b_refTbeta30p2;   //!
   TBranch        *b_refTbeta30p3;   //!
   TBranch        *b_refTbeta30p4;   //!
   TBranch        *b_refTbeta30p5;   //!
   TBranch        *b_refCbeta20p2;   //!
   TBranch        *b_refCbeta20p3;   //!
   TBranch        *b_refCbeta20p4;   //!
   TBranch        *b_refCbeta20p5;   //!
   TBranch        *b_refZ11;   //!
   TBranch        *b_refZ20;   //!
   TBranch        *b_refZ22;   //!
   TBranch        *b_refZ31;   //!
   TBranch        *b_refZ33;   //!
   TBranch        *b_refZ40;   //!
   TBranch        *b_refZ42;   //!
   TBranch        *b_refZ44;   //!
   TBranch        *b_refZ51;   //!
   TBranch        *b_refZ53;   //!
   TBranch        *b_refZ55;   //!
   TBranch        *b_refPhi1;   //!
   TBranch        *b_refPhi2;   //!
   TBranch        *b_refPhi3;   //!
   TBranch        *b_refPhi4;   //!
   TBranch        *b_refPhi5;   //!
   TBranch        *b_refPhi6;   //!
   TBranch        *b_refPhi7;   //!
   TBranch        *b_refSkx;   //!
   TBranch        *b_refSky;  */ //!

   TBranch        *b_refFlavorID_jet_hadronID ;   //!
   TBranch        *b_refFlavorID_jet_hadronPT ;   //!
   TBranch        *b_refFlavorID_jet_hadronEta;   //!
   TBranch        *b_refFlavorID_jet_hadronPhi;   //!
   TBranch        *b_refFlavorID_jet_hadronDR ;   //!
   TBranch        *b_refFlavorID_jet_partonID ;   //!
   TBranch        *b_refFlavorID_jet_partonPT ;   //!
   TBranch        *b_refFlavorID_jet_partonEta;   //!
   TBranch        *b_refFlavorID_jet_partonPhi;   //!
   TBranch        *b_refFlavorID_jet_partonDR ;   //!
   TBranch        *b_refFlavorID_Subjet1_hadronID ;   //!
   TBranch        *b_refFlavorID_Subjet1_hadronPT ;   //!
   TBranch        *b_refFlavorID_Subjet1_hadronEta;   //!
   TBranch        *b_refFlavorID_Subjet1_hadronPhi;   //!
   TBranch        *b_refFlavorID_Subjet1_hadronDR ;   //!
   TBranch        *b_refFlavorID_Subjet1_partonID ;   //!
   TBranch        *b_refFlavorID_Subjet1_partonPT ;   //!
   TBranch        *b_refFlavorID_Subjet1_partonEta;   //!
   TBranch        *b_refFlavorID_Subjet1_partonPhi;   //!
   TBranch        *b_refFlavorID_Subjet1_partonDR ;   //!
   TBranch        *b_refFlavorID_Subjet2_hadronID ;   //!
   TBranch        *b_refFlavorID_Subjet2_hadronPT ;   //!
   TBranch        *b_refFlavorID_Subjet2_hadronEta;   //!
   TBranch        *b_refFlavorID_Subjet2_hadronPhi;   //!
   TBranch        *b_refFlavorID_Subjet2_hadronDR ;   //!
   TBranch        *b_refFlavorID_Subjet2_partonID ;   //!
   TBranch        *b_refFlavorID_Subjet2_partonPT ;   //!
   TBranch        *b_refFlavorID_Subjet2_partonEta;   //!
   TBranch        *b_refFlavorID_Subjet2_partonPhi;   //!
   TBranch        *b_refFlavorID_Subjet2_partonDR ;   //!

   TBranch        *b_reftau1;   //!
   TBranch        *b_reftau2;   //!
   TBranch        *b_reftau3;   //!
   TBranch        *b_refdphijt;   //!
   TBranch        *b_refdrjt;   //!
   TBranch        *b_refparton_pt;   //!
   TBranch        *b_refparton_flavor;   //!
   TBranch        *b_refparton_flavorForB;   //!
   TBranch        *b_refparton_flavorProcess;   //!
   TBranch        *b_refptG;   //!
   TBranch        *b_refetaG;   //!
   TBranch        *b_refphiG;   //!
   TBranch        *b_refmG;   //!
   TBranch        *b_refSubJetPt;   //!
   TBranch        *b_refSubJetEta;   //!
   TBranch        *b_refSubJetPhi;   //!
   TBranch        *b_refSubJetM;   //!

   TBranch        *b_refGSP_gpt;   //!
   TBranch        *b_refGSP_geta;   //!
   TBranch        *b_refGSP_gphi;   //!
   TBranch        *b_refGSP_gidx;   //!
   TBranch        *b_refGSP_b1pt;   //!
   TBranch        *b_refGSP_b1eta;   //!
   TBranch        *b_refGSP_b1phi;   //!
   TBranch        *b_refGSP_b2pt;   //!
   TBranch        *b_refGSP_b2eta;   //!
   TBranch        *b_refGSP_b2phi;   //!
   TBranch        *b_refGSP_b1Match_jtdR;   //!
   TBranch        *b_refGSP_b2Match_jtdR;   //!
   TBranch        *b_refGSP_bbdR;   //!
   TBranch        *b_refGSP_bbzg;   //!
   TBranch        *b_refGSP_SubJtMatched;   //!



/*   TBranch        *b_refConstituentsId;   //!
   TBranch        *b_refConstituentsE;   //!
   TBranch        *b_refConstituentsPt;   //!
   TBranch        *b_refConstituentsEta;   //!
   TBranch        *b_refConstituentsPhi;   //!
   TBranch        *b_refConstituentsM;   //!
   TBranch        *b_refSDConstituentsId;   //!
   TBranch        *b_refSDConstituentsE;   //!
   TBranch        *b_refSDConstituentsPt;   //!
   TBranch        *b_refSDConstituentsEta;   //!
   TBranch        *b_refSDConstituentsPhi;   //!
   TBranch        *b_refSDConstituentsM;  */ //!
   TBranch        *b_genChargedSum;   //!
   TBranch        *b_genHardSum;   //!
   TBranch        *b_signalChargedSum;   //!
   TBranch        *b_signalHardSum;   //!
   TBranch        *b_subid;   //!
   TBranch        *b_ngen;   //!
   TBranch        *b_genmatchindex;   //!
   TBranch        *b_genpt;   //!
   TBranch        *b_geneta;   //!
   TBranch        *b_geny;   //!
   TBranch        *b_gentau1;   //!
   TBranch        *b_gentau2;   //!
   TBranch        *b_gentau3;   //!
   TBranch        *b_genphi;   //!
   TBranch        *b_genm;   //!
   TBranch        *b_gendphijt;   //!
   TBranch        *b_gendrjt;   //!
/*   TBranch        *b_gennCands;   //!
   TBranch        *b_gennChCands;   //!
   TBranch        *b_gennNeCands;   //!
   TBranch        *b_genchargedNConst;   //!
   TBranch        *b_geneSumConst;   //!
   TBranch        *b_geneNConst;   //!
   TBranch        *b_genmuSumConst;   //!
   TBranch        *b_genmuNConst;   //!
   TBranch        *b_genphotonSumConst;   //!
   TBranch        *b_genphotonNConst;   //!
   TBranch        *b_genneutralSumConst;   //!
   TBranch        *b_genneutralNConst;   //!
   TBranch        *b_genhfhadSumConst;   //!
   TBranch        *b_genhfhadNConst;   //!
   TBranch        *b_genhfemSumConst;   //!
   TBranch        *b_genhfemNConst;   //!
   TBranch        *b_genMByPt;   //!
   TBranch        *b_genRMSCand;   //!
   TBranch        *b_genAxis1;   //!
   TBranch        *b_genAxis2;   //!
   TBranch        *b_genSigma;   //!
   TBranch        *b_genR;   //!
   TBranch        *b_genpTD;   //!
   TBranch        *b_genpull;   //!
   TBranch        *b_genrm0p5;   //!
   TBranch        *b_genrm1;   //!
   TBranch        *b_genrm2;   //!
   TBranch        *b_genrm3;   //!
   TBranch        *b_genSDm;   //!
   TBranch        *b_genSDpt;   //!
   TBranch        *b_genSDeta;   //!
   TBranch        *b_genSDphi;   //!
   TBranch        *b_genSDptFrac;   //!
   TBranch        *b_genSDrm0p5;   //!
   TBranch        *b_genSDrm1;   //!
   TBranch        *b_genSDrm2;   //!
   TBranch        *b_genSDrm3;   //!
   TBranch        *b_genTbeta20p2;   //!
   TBranch        *b_genTbeta20p3;   //!
   TBranch        *b_genTbeta20p4;   //!
   TBranch        *b_genTbeta20p5;   //!
   TBranch        *b_genTbeta30p2;   //!
   TBranch        *b_genTbeta30p3;   //!
   TBranch        *b_genTbeta30p4;   //!
   TBranch        *b_genTbeta30p5;   //!
   TBranch        *b_genCbeta20p2;   //!
   TBranch        *b_genCbeta20p3;   //!
   TBranch        *b_genCbeta20p4;   //!
   TBranch        *b_genCbeta20p5;   //!
   TBranch        *b_genZ11;   //!
   TBranch        *b_genZ20;   //!
   TBranch        *b_genZ22;   //!
   TBranch        *b_genZ31;   //!
   TBranch        *b_genZ33;   //!
   TBranch        *b_genZ40;   //!
   TBranch        *b_genZ42;   //!
   TBranch        *b_genZ44;   //!
   TBranch        *b_genZ51;   //!
   TBranch        *b_genZ53;   //!
   TBranch        *b_genZ55;   //!
   TBranch        *b_genPhi1;   //!
   TBranch        *b_genPhi2;   //!
   TBranch        *b_genPhi3;   //!
   TBranch        *b_genPhi4;   //!
   TBranch        *b_genPhi5;   //!
   TBranch        *b_genPhi6;   //!
   TBranch        *b_genPhi7;   //!
   TBranch        *b_genSkx;   //!
   TBranch        *b_genSky;  */ //!
   TBranch        *b_genptG;   //!
   TBranch        *b_genetaG;   //!
   TBranch        *b_genphiG;   //!
   TBranch        *b_genmG;   //!
   TBranch        *b_genSubJetPt;   //!
   TBranch        *b_genSubJetEta;   //!
   TBranch        *b_genSubJetPhi;   //!
   TBranch        *b_genSubJetM;   //!
/*   TBranch        *b_genConstituentsId;   //!
   TBranch        *b_genConstituentsE;   //!
   TBranch        *b_genConstituentsPt;   //!
   TBranch        *b_genConstituentsEta;   //!
   TBranch        *b_genConstituentsPhi;   //!
   TBranch        *b_genConstituentsM;   //!
   TBranch        *b_genSDConstituentsId;   //!
   TBranch        *b_genSDConstituentsE;   //!
   TBranch        *b_genSDConstituentsPt;   //!
   TBranch        *b_genSDConstituentsEta;   //!
   TBranch        *b_genSDConstituentsPhi;   //!
   TBranch        *b_genSDConstituentsM; */  //!
   TBranch        *b_gensubid;   //!

   akSoftDrop4PFJetSelector(TTree * /*tree*/ =0) : fChain(0) { }
   virtual ~akSoftDrop4PFJetSelector() { }
   virtual Int_t   Version() const { return 2; }
   virtual void    Begin(TTree *tree);
   virtual void    SlaveBegin(TTree *tree);
   virtual void    Init(TTree *tree);
   virtual Bool_t  Notify();
   virtual Bool_t  Process(Long64_t entry);
   virtual Int_t   GetEntry(Long64_t entry, Int_t getall = 0) { return fChain ? fChain->GetTree()->GetEntry(entry, getall) : 0; }
   virtual void    SetOption(const char *option) { fOption = option; }
   virtual void    SetObject(TObject *obj) { fObject = obj; }
   virtual void    SetInputList(TList *input) { fInput = input; }
   virtual TList  *GetOutputList() const { return fOutput; }
   virtual void    SlaveTerminate();
   virtual void    Terminate();

   ClassDef(akSoftDrop4PFJetSelector,0);
};

#endif

#ifdef akSoftDrop4PFJetSelector_cxx
void akSoftDrop4PFJetSelector::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   jtSubJetPt = 0;
   jtSubJetEta = 0;
   jtSubJetPhi = 0;
   jtSubJetM = 0;
/*   jtConstituentsId = 0;
   jtConstituentsE = 0;
   jtConstituentsPt = 0;
   jtConstituentsEta = 0;
   jtConstituentsPhi = 0;
   jtConstituentsM = 0;
   jtSDConstituentsId = 0;
   jtSDConstituentsE = 0;
   jtSDConstituentsPt = 0;
   jtSDConstituentsEta = 0;
   jtSDConstituentsPhi = 0;
   jtSDConstituentsM = 0;*/
   refSubJetPt = 0;
   refSubJetEta = 0;
   refSubJetPhi = 0;
   refSubJetM = 0;
/*   refConstituentsId = 0;
   refConstituentsE = 0;
   refConstituentsPt = 0;
   refConstituentsEta = 0;
   refConstituentsPhi = 0;
   refConstituentsM = 0;
   refSDConstituentsId = 0;
   refSDConstituentsE = 0;
   refSDConstituentsPt = 0;
   refSDConstituentsEta = 0;
   refSDConstituentsPhi = 0;
   refSDConstituentsM = 0;*/
   genSubJetPt = 0;
   genSubJetEta = 0;
   genSubJetPhi = 0;
   genSubJetM = 0;
/*   genConstituentsId = 0;
   genConstituentsE = 0;
   genConstituentsPt = 0;
   genConstituentsEta = 0;
   genConstituentsPhi = 0;
   genConstituentsM = 0;
   genSDConstituentsId = 0;
   genSDConstituentsE = 0;
   genSDConstituentsPt = 0;
   genSDConstituentsEta = 0;
   genSDConstituentsPhi = 0;
   genSDConstituentsM = 0;*/
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("evt", &evt, &b_evt);
   fChain->SetBranchAddress("b", &b, &b_b);
   fChain->SetBranchAddress("nref", &nref, &b_nref);
   fChain->SetBranchAddress("rawpt", rawpt, &b_rawpt);
   fChain->SetBranchAddress("jtpt", jtpt, &b_jtpt);
   fChain->SetBranchAddress("jteta", jteta, &b_jteta);
   fChain->SetBranchAddress("jty", jty, &b_jty);
   fChain->SetBranchAddress("jtphi", jtphi, &b_jtphi);
   fChain->SetBranchAddress("jtpu", jtpu, &b_jtpu);
   fChain->SetBranchAddress("jtm", jtm, &b_jtm);
   fChain->SetBranchAddress("jtarea", jtarea, &b_jtarea);
/*   fChain->SetBranchAddress("jtnCands", jtnCands, &b_jtnCands);
   fChain->SetBranchAddress("jtnChCands", jtnChCands, &b_jtnChCands);
   fChain->SetBranchAddress("jtnNeCands", jtnNeCands, &b_jtnNeCands);
   fChain->SetBranchAddress("jtchargedSumConst", jtchargedSumConst, &b_jtchargedSumConst);
   fChain->SetBranchAddress("jtchargedNConst", jtchargedNConst, &b_jtchargedNConst);
   fChain->SetBranchAddress("jteSumConst", jteSumConst, &b_jteSumConst);
   fChain->SetBranchAddress("jteNConst", jteNConst, &b_jteNConst);
   fChain->SetBranchAddress("jtmuSumConst", jtmuSumConst, &b_jtmuSumConst);
   fChain->SetBranchAddress("jtmuNConst", jtmuNConst, &b_jtmuNConst);
   fChain->SetBranchAddress("jtphotonSumConst", jtphotonSumConst, &b_jtphotonSumConst);
   fChain->SetBranchAddress("jtphotonNConst", jtphotonNConst, &b_jtphotonNConst);
   fChain->SetBranchAddress("jtneutralSumConst", jtneutralSumConst, &b_jtneutralSumConst);
   fChain->SetBranchAddress("jtneutralNConst", jtneutralNConst, &b_jtneutralNConst);
   fChain->SetBranchAddress("jthfhadSumConst", jthfhadSumConst, &b_jthfhadSumConst);
   fChain->SetBranchAddress("jthfhadNConst", jthfhadNConst, &b_jthfhadNConst);
   fChain->SetBranchAddress("jthfemSumConst", jthfemSumConst, &b_jthfemSumConst);
   fChain->SetBranchAddress("jthfemNConst", jthfemNConst, &b_jthfemNConst);
   fChain->SetBranchAddress("jtMByPt", jtMByPt, &b_jtMByPt);
   fChain->SetBranchAddress("jtRMSCand", jtRMSCand, &b_jtRMSCand);
   fChain->SetBranchAddress("jtAxis1", jtAxis1, &b_jtAxis1);
   fChain->SetBranchAddress("jtAxis2", jtAxis2, &b_jtAxis2);
   fChain->SetBranchAddress("jtSigma", jtSigma, &b_jtSigma);
   fChain->SetBranchAddress("jtR", jtR, &b_jtR);
   fChain->SetBranchAddress("jtpTD", jtpTD, &b_jtpTD);
   fChain->SetBranchAddress("jtpull", jtpull, &b_jtpull);
   fChain->SetBranchAddress("jtrm0p5", jtrm0p5, &b_jtrm0p5);
   fChain->SetBranchAddress("jtrm1", jtrm1, &b_jtrm1);
   fChain->SetBranchAddress("jtrm2", jtrm2, &b_jtrm2);
   fChain->SetBranchAddress("jtrm3", jtrm3, &b_jtrm3);
   fChain->SetBranchAddress("jtSDm", jtSDm, &b_jtSDm);
   fChain->SetBranchAddress("jtSDpt", jtSDpt, &b_jtSDpt);
   fChain->SetBranchAddress("jtSDeta", jtSDeta, &b_jtSDeta);
   fChain->SetBranchAddress("jtSDphi", jtSDphi, &b_jtSDphi);
   fChain->SetBranchAddress("jtSDptFrac", jtSDptFrac, &b_jtSDptFrac);
   fChain->SetBranchAddress("jtSDrm0p5", jtSDrm0p5, &b_jtSDrm0p5);
   fChain->SetBranchAddress("jtSDrm1", jtSDrm1, &b_jtSDrm1);
   fChain->SetBranchAddress("jtSDrm2", jtSDrm2, &b_jtSDrm2);
   fChain->SetBranchAddress("jtSDrm3", jtSDrm3, &b_jtSDrm3);
   fChain->SetBranchAddress("jtTbeta20p2", jtTbeta20p2, &b_jtTbeta20p2);
   fChain->SetBranchAddress("jtTbeta20p3", jtTbeta20p3, &b_jtTbeta20p3);
   fChain->SetBranchAddress("jtTbeta20p4", jtTbeta20p4, &b_jtTbeta20p4);
   fChain->SetBranchAddress("jtTbeta20p5", jtTbeta20p5, &b_jtTbeta20p5);
   fChain->SetBranchAddress("jtTbeta30p2", jtTbeta30p2, &b_jtTbeta30p2);
   fChain->SetBranchAddress("jtTbeta30p3", jtTbeta30p3, &b_jtTbeta30p3);
   fChain->SetBranchAddress("jtTbeta30p4", jtTbeta30p4, &b_jtTbeta30p4);
   fChain->SetBranchAddress("jtTbeta30p5", jtTbeta30p5, &b_jtTbeta30p5);
   fChain->SetBranchAddress("jtCbeta20p2", jtCbeta20p2, &b_jtCbeta20p2);
   fChain->SetBranchAddress("jtCbeta20p3", jtCbeta20p3, &b_jtCbeta20p3);
   fChain->SetBranchAddress("jtCbeta20p4", jtCbeta20p4, &b_jtCbeta20p4);
   fChain->SetBranchAddress("jtCbeta20p5", jtCbeta20p5, &b_jtCbeta20p5);
   fChain->SetBranchAddress("jtZ11", jtZ11, &b_jtZ11);
   fChain->SetBranchAddress("jtZ20", jtZ20, &b_jtZ20);
   fChain->SetBranchAddress("jtZ22", jtZ22, &b_jtZ22);
   fChain->SetBranchAddress("jtZ31", jtZ31, &b_jtZ31);
   fChain->SetBranchAddress("jtZ33", jtZ33, &b_jtZ33);
   fChain->SetBranchAddress("jtZ40", jtZ40, &b_jtZ40);
   fChain->SetBranchAddress("jtZ42", jtZ42, &b_jtZ42);
   fChain->SetBranchAddress("jtZ44", jtZ44, &b_jtZ44);
   fChain->SetBranchAddress("jtZ51", jtZ51, &b_jtZ51);
   fChain->SetBranchAddress("jtZ53", jtZ53, &b_jtZ53);
   fChain->SetBranchAddress("jtZ55", jtZ55, &b_jtZ55);
   fChain->SetBranchAddress("jtPhi1", jtPhi1, &b_jtPhi1);
   fChain->SetBranchAddress("jtPhi2", jtPhi2, &b_jtPhi2);
   fChain->SetBranchAddress("jtPhi3", jtPhi3, &b_jtPhi3);
   fChain->SetBranchAddress("jtPhi4", jtPhi4, &b_jtPhi4);
   fChain->SetBranchAddress("jtPhi5", jtPhi5, &b_jtPhi5);
   fChain->SetBranchAddress("jtPhi6", jtPhi6, &b_jtPhi6);
   fChain->SetBranchAddress("jtPhi7", jtPhi7, &b_jtPhi7);
   fChain->SetBranchAddress("jtSkx", jtSkx, &b_jtSkx);
   fChain->SetBranchAddress("jtSky", jtSky, &b_jtSky); */
   fChain->SetBranchAddress("jtPfCHF", jtPfCHF, &b_jtPfCHF);
   fChain->SetBranchAddress("jtPfNHF", jtPfNHF, &b_jtPfNHF);
   fChain->SetBranchAddress("jtPfCEF", jtPfCEF, &b_jtPfCEF);
   fChain->SetBranchAddress("jtPfNEF", jtPfNEF, &b_jtPfNEF);
   fChain->SetBranchAddress("jtPfMUF", jtPfMUF, &b_jtPfMUF);
   fChain->SetBranchAddress("jtPfCHM", jtPfCHM, &b_jtPfCHM);
   fChain->SetBranchAddress("jtPfNHM", jtPfNHM, &b_jtPfNHM);
   fChain->SetBranchAddress("jtPfCEM", jtPfCEM, &b_jtPfCEM);
   fChain->SetBranchAddress("jtPfNEM", jtPfNEM, &b_jtPfNEM);
   fChain->SetBranchAddress("jtPfMUM", jtPfMUM, &b_jtPfMUM);
   fChain->SetBranchAddress("jttau1", jttau1, &b_jttau1);
   fChain->SetBranchAddress("jttau2", jttau2, &b_jttau2);
   fChain->SetBranchAddress("jttau3", jttau3, &b_jttau3);
   fChain->SetBranchAddress("jtSubJetPt", &jtSubJetPt, &b_jtSubJetPt);
   fChain->SetBranchAddress("jtSubJetEta", &jtSubJetEta, &b_jtSubJetEta);
   fChain->SetBranchAddress("jtSubJetPhi", &jtSubJetPhi, &b_jtSubJetPhi);
   fChain->SetBranchAddress("jtSubJetM", &jtSubJetM, &b_jtSubJetM);
/*   fChain->SetBranchAddress("jtConstituentsId", &jtConstituentsId, &b_jtConstituentsId);
   fChain->SetBranchAddress("jtConstituentsE", &jtConstituentsE, &b_jtConstituentsE);
   fChain->SetBranchAddress("jtConstituentsPt", &jtConstituentsPt, &b_jtConstituentsPt);
   fChain->SetBranchAddress("jtConstituentsEta", &jtConstituentsEta, &b_jtConstituentsEta);
   fChain->SetBranchAddress("jtConstituentsPhi", &jtConstituentsPhi, &b_jtConstituentsPhi);
   fChain->SetBranchAddress("jtConstituentsM", &jtConstituentsM, &b_jtConstituentsM);
   fChain->SetBranchAddress("jtSDConstituentsId", &jtSDConstituentsId, &b_jtSDConstituentsId);
   fChain->SetBranchAddress("jtSDConstituentsE", &jtSDConstituentsE, &b_jtSDConstituentsE);
   fChain->SetBranchAddress("jtSDConstituentsPt", &jtSDConstituentsPt, &b_jtSDConstituentsPt);
   fChain->SetBranchAddress("jtSDConstituentsEta", &jtSDConstituentsEta, &b_jtSDConstituentsEta);
   fChain->SetBranchAddress("jtSDConstituentsPhi", &jtSDConstituentsPhi, &b_jtSDConstituentsPhi);
   fChain->SetBranchAddress("jtSDConstituentsM", &jtSDConstituentsM, &b_jtSDConstituentsM); */
   fChain->SetBranchAddress("discr_jetID_cuts", discr_jetID_cuts, &b_discr_jetID_cuts);
   fChain->SetBranchAddress("discr_jetID_bdt", discr_jetID_bdt, &b_discr_jetID_bdt);
   fChain->SetBranchAddress("discr_fr01", discr_fr01, &b_discr_fr01);
   fChain->SetBranchAddress("trackMax", trackMax, &b_trackMax);
   fChain->SetBranchAddress("trackSum", trackSum, &b_trackSum);
   fChain->SetBranchAddress("trackN", trackN, &b_trackN);
   fChain->SetBranchAddress("trackHardSum", trackHardSum, &b_trackHardSum);
   fChain->SetBranchAddress("trackHardN", trackHardN, &b_trackHardN);
   fChain->SetBranchAddress("chargedMax", chargedMax, &b_chargedMax);
   fChain->SetBranchAddress("chargedSum", chargedSum, &b_chargedSum);
   fChain->SetBranchAddress("chargedN", chargedN, &b_chargedN);
   fChain->SetBranchAddress("chargedHardSum", chargedHardSum, &b_chargedHardSum);
   fChain->SetBranchAddress("chargedHardN", chargedHardN, &b_chargedHardN);
   fChain->SetBranchAddress("photonMax", photonMax, &b_photonMax);
   fChain->SetBranchAddress("photonSum", photonSum, &b_photonSum);
   fChain->SetBranchAddress("photonN", photonN, &b_photonN);
   fChain->SetBranchAddress("photonHardSum", photonHardSum, &b_photonHardSum);
   fChain->SetBranchAddress("photonHardN", photonHardN, &b_photonHardN);
   fChain->SetBranchAddress("neutralMax", neutralMax, &b_neutralMax);
   fChain->SetBranchAddress("neutralSum", neutralSum, &b_neutralSum);
   fChain->SetBranchAddress("neutralN", neutralN, &b_neutralN);
   fChain->SetBranchAddress("hcalSum", hcalSum, &b_hcalSum);
   fChain->SetBranchAddress("ecalSum", ecalSum, &b_ecalSum);
   fChain->SetBranchAddress("eMax", eMax, &b_eMax);
   fChain->SetBranchAddress("eSum", eSum, &b_eSum);
   fChain->SetBranchAddress("eN", eN, &b_eN);
   fChain->SetBranchAddress("muMax", muMax, &b_muMax);
   fChain->SetBranchAddress("muSum", muSum, &b_muSum);
   fChain->SetBranchAddress("muN", muN, &b_muN);
   fChain->SetBranchAddress("discr_ssvHighEff", discr_ssvHighEff, &b_discr_ssvHighEff);
   fChain->SetBranchAddress("discr_ssvHighPur", discr_ssvHighPur, &b_discr_ssvHighPur);
   fChain->SetBranchAddress("discr_csvV1", discr_csvV1, &b_discr_csvV1);
   fChain->SetBranchAddress("discr_csvV2", discr_csvV2, &b_discr_csvV2);
   fChain->SetBranchAddress("discr_muByIp3", discr_muByIp3, &b_discr_muByIp3);
   fChain->SetBranchAddress("discr_muByPt", discr_muByPt, &b_discr_muByPt);
   fChain->SetBranchAddress("discr_prob", discr_prob, &b_discr_prob);
   fChain->SetBranchAddress("discr_probb", discr_probb, &b_discr_probb);
   fChain->SetBranchAddress("discr_tcHighEff", discr_tcHighEff, &b_discr_tcHighEff);
   fChain->SetBranchAddress("discr_tcHighPur", discr_tcHighPur, &b_discr_tcHighPur);
   fChain->SetBranchAddress("ndiscr_ssvHighEff", ndiscr_ssvHighEff, &b_ndiscr_ssvHighEff);
   fChain->SetBranchAddress("ndiscr_ssvHighPur", ndiscr_ssvHighPur, &b_ndiscr_ssvHighPur);
   fChain->SetBranchAddress("ndiscr_csvV1", ndiscr_csvV1, &b_ndiscr_csvV1);
   fChain->SetBranchAddress("ndiscr_csvV2", ndiscr_csvV2, &b_ndiscr_csvV2);
   fChain->SetBranchAddress("ndiscr_muByPt", ndiscr_muByPt, &b_ndiscr_muByPt);
   fChain->SetBranchAddress("pdiscr_csvV1", pdiscr_csvV1, &b_pdiscr_csvV1);
   fChain->SetBranchAddress("pdiscr_csvV2", pdiscr_csvV2, &b_pdiscr_csvV2);
   fChain->SetBranchAddress("nsvtx", nsvtx, &b_nsvtx);
   fChain->SetBranchAddress("svtxntrk", svtxntrk, &b_svtxntrk);
   fChain->SetBranchAddress("svtxdl", svtxdl, &b_svtxdl);
   fChain->SetBranchAddress("svtxdls", svtxdls, &b_svtxdls);
   fChain->SetBranchAddress("svtxdl2d", svtxdl2d, &b_svtxdl2d);
   fChain->SetBranchAddress("svtxdls2d", svtxdls2d, &b_svtxdls2d);
   fChain->SetBranchAddress("svtxm", svtxm, &b_svtxm);
   fChain->SetBranchAddress("svtxpt", svtxpt, &b_svtxpt);
   fChain->SetBranchAddress("svtxmcorr", svtxmcorr, &b_svtxmcorr);
   fChain->SetBranchAddress("nIPtrk", nIPtrk, &b_nIPtrk);
   fChain->SetBranchAddress("nselIPtrk", nselIPtrk, &b_nselIPtrk);
   fChain->SetBranchAddress("mue", mue, &b_mue);
   fChain->SetBranchAddress("mupt", mupt, &b_mupt);
   fChain->SetBranchAddress("mueta", mueta, &b_mueta);
   fChain->SetBranchAddress("muphi", muphi, &b_muphi);
   fChain->SetBranchAddress("mudr", mudr, &b_mudr);
   fChain->SetBranchAddress("muptrel", muptrel, &b_muptrel);
   fChain->SetBranchAddress("muchg", muchg, &b_muchg);
   fChain->SetBranchAddress("beamId1", &beamId1, &b_beamId1);
   fChain->SetBranchAddress("beamId2", &beamId2, &b_beamId2);
   fChain->SetBranchAddress("pthat", &pthat, &b_pthat);
   fChain->SetBranchAddress("refpt", refpt, &b_refpt);
   fChain->SetBranchAddress("refeta", refeta, &b_refeta);
   fChain->SetBranchAddress("refy", refy, &b_refy);
   fChain->SetBranchAddress("refphi", refphi, &b_refphi);
   fChain->SetBranchAddress("refm", refm, &b_refm);
   fChain->SetBranchAddress("refarea", refarea, &b_refarea);
   fChain->SetBranchAddress("bProdCode", &bProdCode, &b_bProdCode);
   fChain->SetBranchAddress("cProdCode", &cProdCode, &b_cProdCode);
/*   fChain->SetBranchAddress("refnCands", refnCands, &b_refnCands);
   fChain->SetBranchAddress("refnChCands", refnChCands, &b_refnChCands);
   fChain->SetBranchAddress("refnNeCands", refnNeCands, &b_refnNeCands);
   fChain->SetBranchAddress("refchargedSumConst", refchargedSumConst, &b_refchargedSumConst);
   fChain->SetBranchAddress("refchargedNConst", refchargedNConst, &b_refchargedNConst);
   fChain->SetBranchAddress("refeSumConst", refeSumConst, &b_refeSumConst);
   fChain->SetBranchAddress("refeNConst", refeNConst, &b_refeNConst);
   fChain->SetBranchAddress("refmuSumConst", refmuSumConst, &b_refmuSumConst);
   fChain->SetBranchAddress("refmuNConst", refmuNConst, &b_refmuNConst);
   fChain->SetBranchAddress("refphotonSumConst", refphotonSumConst, &b_refphotonSumConst);
   fChain->SetBranchAddress("refphotonNConst", refphotonNConst, &b_refphotonNConst);
   fChain->SetBranchAddress("refneutralSumConst", refneutralSumConst, &b_refneutralSumConst);
   fChain->SetBranchAddress("refneutralNConst", refneutralNConst, &b_refneutralNConst);
   fChain->SetBranchAddress("refhfhadSumConst", refhfhadSumConst, &b_refhfhadSumConst);
   fChain->SetBranchAddress("refhfhadNConst", refhfhadNConst, &b_refhfhadNConst);
   fChain->SetBranchAddress("refhfemSumConst", refhfemSumConst, &b_refhfemSumConst);
   fChain->SetBranchAddress("refhfemNConst", refhfemNConst, &b_refhfemNConst);
   fChain->SetBranchAddress("refMByPt", refMByPt, &b_refMByPt);
   fChain->SetBranchAddress("refRMSCand", refRMSCand, &b_refRMSCand);
   fChain->SetBranchAddress("refAxis1", refAxis1, &b_refAxis1);
   fChain->SetBranchAddress("refAxis2", refAxis2, &b_refAxis2);
   fChain->SetBranchAddress("refSigma", refSigma, &b_refSigma);
   fChain->SetBranchAddress("refR", refR, &b_refR);
   fChain->SetBranchAddress("refpTD", refpTD, &b_refpTD);
   fChain->SetBranchAddress("refpull", refpull, &b_refpull);
   fChain->SetBranchAddress("refrm0p5", refrm0p5, &b_refrm0p5);
   fChain->SetBranchAddress("refrm1", refrm1, &b_refrm1);
   fChain->SetBranchAddress("refrm2", refrm2, &b_refrm2);
   fChain->SetBranchAddress("refrm3", refrm3, &b_refrm3);
   fChain->SetBranchAddress("refSDm", refSDm, &b_refSDm);
   fChain->SetBranchAddress("refSDpt", refSDpt, &b_refSDpt);
   fChain->SetBranchAddress("refSDeta", refSDeta, &b_refSDeta);
   fChain->SetBranchAddress("refSDphi", refSDphi, &b_refSDphi);
   fChain->SetBranchAddress("refSDptFrac", refSDptFrac, &b_refSDptFrac);
   fChain->SetBranchAddress("refSDrm0p5", refSDrm0p5, &b_refSDrm0p5);
   fChain->SetBranchAddress("refSDrm1", refSDrm1, &b_refSDrm1);
   fChain->SetBranchAddress("refSDrm2", refSDrm2, &b_refSDrm2);
   fChain->SetBranchAddress("refSDrm3", refSDrm3, &b_refSDrm3);
   fChain->SetBranchAddress("refTbeta20p2", refTbeta20p2, &b_refTbeta20p2);
   fChain->SetBranchAddress("refTbeta20p3", refTbeta20p3, &b_refTbeta20p3);
   fChain->SetBranchAddress("refTbeta20p4", refTbeta20p4, &b_refTbeta20p4);
   fChain->SetBranchAddress("refTbeta20p5", refTbeta20p5, &b_refTbeta20p5);
   fChain->SetBranchAddress("refTbeta30p2", refTbeta30p2, &b_refTbeta30p2);
   fChain->SetBranchAddress("refTbeta30p3", refTbeta30p3, &b_refTbeta30p3);
   fChain->SetBranchAddress("refTbeta30p4", refTbeta30p4, &b_refTbeta30p4);
   fChain->SetBranchAddress("refTbeta30p5", refTbeta30p5, &b_refTbeta30p5);
   fChain->SetBranchAddress("refCbeta20p2", refCbeta20p2, &b_refCbeta20p2);
   fChain->SetBranchAddress("refCbeta20p3", refCbeta20p3, &b_refCbeta20p3);
   fChain->SetBranchAddress("refCbeta20p4", refCbeta20p4, &b_refCbeta20p4);
   fChain->SetBranchAddress("refCbeta20p5", refCbeta20p5, &b_refCbeta20p5);
   fChain->SetBranchAddress("refZ11", refZ11, &b_refZ11);
   fChain->SetBranchAddress("refZ20", refZ20, &b_refZ20);
   fChain->SetBranchAddress("refZ22", refZ22, &b_refZ22);
   fChain->SetBranchAddress("refZ31", refZ31, &b_refZ31);
   fChain->SetBranchAddress("refZ33", refZ33, &b_refZ33);
   fChain->SetBranchAddress("refZ40", refZ40, &b_refZ40);
   fChain->SetBranchAddress("refZ42", refZ42, &b_refZ42);
   fChain->SetBranchAddress("refZ44", refZ44, &b_refZ44);
   fChain->SetBranchAddress("refZ51", refZ51, &b_refZ51);
   fChain->SetBranchAddress("refZ53", refZ53, &b_refZ53);
   fChain->SetBranchAddress("refZ55", refZ55, &b_refZ55);
   fChain->SetBranchAddress("refPhi1", refPhi1, &b_refPhi1);
   fChain->SetBranchAddress("refPhi2", refPhi2, &b_refPhi2);
   fChain->SetBranchAddress("refPhi3", refPhi3, &b_refPhi3);
   fChain->SetBranchAddress("refPhi4", refPhi4, &b_refPhi4);
   fChain->SetBranchAddress("refPhi5", refPhi5, &b_refPhi5);
   fChain->SetBranchAddress("refPhi6", refPhi6, &b_refPhi6);
   fChain->SetBranchAddress("refPhi7", refPhi7, &b_refPhi7);
   fChain->SetBranchAddress("refSkx", refSkx, &b_refSkx);
   fChain->SetBranchAddress("refSky", refSky, &b_refSky); */

   fChain->SetBranchAddress("refGSP_gpt", refGSP_gpt, &b_refGSP_gpt);
   fChain->SetBranchAddress("refGSP_geta", refGSP_geta, &b_refGSP_geta);
   fChain->SetBranchAddress("refGSP_gphi", refGSP_gphi, &b_refGSP_gphi);
   fChain->SetBranchAddress("refGSP_gidx", refGSP_gidx, &b_refGSP_gidx);
   fChain->SetBranchAddress("refGSP_b1pt", refGSP_b1pt, &b_refGSP_b1pt);
   fChain->SetBranchAddress("refGSP_b1eta", refGSP_b1eta, &b_refGSP_b1eta);
   fChain->SetBranchAddress("refGSP_b1phi", refGSP_b1phi, &b_refGSP_b1phi);
   fChain->SetBranchAddress("refGSP_b2pt", refGSP_b2pt, &b_refGSP_b2pt);
   fChain->SetBranchAddress("refGSP_b2eta", refGSP_b2eta, &b_refGSP_b2eta);
   fChain->SetBranchAddress("refGSP_b2phi", refGSP_b2phi, &b_refGSP_b2phi);
   fChain->SetBranchAddress("refGSP_b1Match_jtdR", refGSP_b1Match_jtdR, &b_refGSP_b1Match_jtdR);
   fChain->SetBranchAddress("refGSP_b2Match_jtdR", refGSP_b2Match_jtdR, &b_refGSP_b2Match_jtdR);
   fChain->SetBranchAddress("refGSP_bbdR", refGSP_bbdR, &b_refGSP_bbdR);
   fChain->SetBranchAddress("refGSP_bbzg", refGSP_bbzg, &b_refGSP_bbzg);
   fChain->SetBranchAddress("refGSP_SubJtMatched", refGSP_SubJtMatched, &b_refGSP_SubJtMatched);

   fChain->SetBranchAddress("refFlavorID_jet_hadronID ", refFlavorID_jet_hadronID , &b_refFlavorID_jet_hadronID );
   fChain->SetBranchAddress("refFlavorID_jet_hadronPT ", refFlavorID_jet_hadronPT , &b_refFlavorID_jet_hadronPT );
   fChain->SetBranchAddress("refFlavorID_jet_hadronEta", refFlavorID_jet_hadronEta, &b_refFlavorID_jet_hadronEta);
   fChain->SetBranchAddress("refFlavorID_jet_hadronPhi", refFlavorID_jet_hadronPhi, &b_refFlavorID_jet_hadronPhi);
   fChain->SetBranchAddress("refFlavorID_jet_hadronDR ", refFlavorID_jet_hadronDR , &b_refFlavorID_jet_hadronDR );
   fChain->SetBranchAddress("refFlavorID_jet_partonID ", refFlavorID_jet_partonID , &b_refFlavorID_jet_partonID );
   fChain->SetBranchAddress("refFlavorID_jet_partonPT ", refFlavorID_jet_partonPT , &b_refFlavorID_jet_partonPT );
   fChain->SetBranchAddress("refFlavorID_jet_partonEta", refFlavorID_jet_partonEta, &b_refFlavorID_jet_partonEta);
   fChain->SetBranchAddress("refFlavorID_jet_partonPhi", refFlavorID_jet_partonPhi, &b_refFlavorID_jet_partonPhi);
   fChain->SetBranchAddress("refFlavorID_jet_partonDR ", refFlavorID_jet_partonDR , &b_refFlavorID_jet_partonDR );
   fChain->SetBranchAddress("refFlavorID_Subjet1_hadronID ", refFlavorID_Subjet1_hadronID , &b_refFlavorID_Subjet1_hadronID );
   fChain->SetBranchAddress("refFlavorID_Subjet1_hadronPT ", refFlavorID_Subjet1_hadronPT , &b_refFlavorID_Subjet1_hadronPT );
   fChain->SetBranchAddress("refFlavorID_Subjet1_hadronEta", refFlavorID_Subjet1_hadronEta, &b_refFlavorID_Subjet1_hadronEta);
   fChain->SetBranchAddress("refFlavorID_Subjet1_hadronPhi", refFlavorID_Subjet1_hadronPhi, &b_refFlavorID_Subjet1_hadronPhi);
   fChain->SetBranchAddress("refFlavorID_Subjet1_hadronDR ", refFlavorID_Subjet1_hadronDR , &b_refFlavorID_Subjet1_hadronDR );
   fChain->SetBranchAddress("refFlavorID_Subjet1_partonID ", refFlavorID_Subjet1_partonID , &b_refFlavorID_Subjet1_partonID );
   fChain->SetBranchAddress("refFlavorID_Subjet1_partonPT ", refFlavorID_Subjet1_partonPT , &b_refFlavorID_Subjet1_partonPT );
   fChain->SetBranchAddress("refFlavorID_Subjet1_partonEta", refFlavorID_Subjet1_partonEta, &b_refFlavorID_Subjet1_partonEta);
   fChain->SetBranchAddress("refFlavorID_Subjet1_partonPhi", refFlavorID_Subjet1_partonPhi, &b_refFlavorID_Subjet1_partonPhi);
   fChain->SetBranchAddress("refFlavorID_Subjet1_partonDR ", refFlavorID_Subjet1_partonDR , &b_refFlavorID_Subjet1_partonDR );
   fChain->SetBranchAddress("refFlavorID_Subjet2_hadronID ", refFlavorID_Subjet2_hadronID , &b_refFlavorID_Subjet2_hadronID );
   fChain->SetBranchAddress("refFlavorID_Subjet2_hadronPT ", refFlavorID_Subjet2_hadronPT , &b_refFlavorID_Subjet2_hadronPT );
   fChain->SetBranchAddress("refFlavorID_Subjet2_hadronEta", refFlavorID_Subjet2_hadronEta, &b_refFlavorID_Subjet2_hadronEta);
   fChain->SetBranchAddress("refFlavorID_Subjet2_hadronPhi", refFlavorID_Subjet2_hadronPhi, &b_refFlavorID_Subjet2_hadronPhi);
   fChain->SetBranchAddress("refFlavorID_Subjet2_hadronDR ", refFlavorID_Subjet2_hadronDR , &b_refFlavorID_Subjet2_hadronDR );
   fChain->SetBranchAddress("refFlavorID_Subjet2_partonID ", refFlavorID_Subjet2_partonID , &b_refFlavorID_Subjet2_partonID );
   fChain->SetBranchAddress("refFlavorID_Subjet2_partonPT ", refFlavorID_Subjet2_partonPT , &b_refFlavorID_Subjet2_partonPT );
   fChain->SetBranchAddress("refFlavorID_Subjet2_partonEta", refFlavorID_Subjet2_partonEta, &b_refFlavorID_Subjet2_partonEta);
   fChain->SetBranchAddress("refFlavorID_Subjet2_partonPhi", refFlavorID_Subjet2_partonPhi, &b_refFlavorID_Subjet2_partonPhi);
   fChain->SetBranchAddress("refFlavorID_Subjet2_partonDR ", refFlavorID_Subjet2_partonDR , &b_refFlavorID_Subjet2_partonDR );




   fChain->SetBranchAddress("reftau1", reftau1, &b_reftau1);
   fChain->SetBranchAddress("reftau2", reftau2, &b_reftau2);
   fChain->SetBranchAddress("reftau3", reftau3, &b_reftau3);
   fChain->SetBranchAddress("refdphijt", refdphijt, &b_refdphijt);
   fChain->SetBranchAddress("refdrjt", refdrjt, &b_refdrjt);
   fChain->SetBranchAddress("refparton_pt", refparton_pt, &b_refparton_pt);
   fChain->SetBranchAddress("refparton_flavor", refparton_flavor, &b_refparton_flavor);
   fChain->SetBranchAddress("refparton_flavorForB", refparton_flavorForB, &b_refparton_flavorForB);
   fChain->SetBranchAddress("refparton_flavorProcess", refparton_flavorProcess, &b_refparton_flavorProcess);
   fChain->SetBranchAddress("refptG", refptG, &b_refptG);
   fChain->SetBranchAddress("refetaG", refetaG, &b_refetaG);
   fChain->SetBranchAddress("refphiG", refphiG, &b_refphiG);
   fChain->SetBranchAddress("refmG", refmG, &b_refmG);
   fChain->SetBranchAddress("refSubJetPt", &refSubJetPt, &b_refSubJetPt);
   fChain->SetBranchAddress("refSubJetEta", &refSubJetEta, &b_refSubJetEta);
   fChain->SetBranchAddress("refSubJetPhi", &refSubJetPhi, &b_refSubJetPhi);
   fChain->SetBranchAddress("refSubJetM", &refSubJetM, &b_refSubJetM);
/*   fChain->SetBranchAddress("refConstituentsId", &refConstituentsId, &b_refConstituentsId);
   fChain->SetBranchAddress("refConstituentsE", &refConstituentsE, &b_refConstituentsE);
   fChain->SetBranchAddress("refConstituentsPt", &refConstituentsPt, &b_refConstituentsPt);
   fChain->SetBranchAddress("refConstituentsEta", &refConstituentsEta, &b_refConstituentsEta);
   fChain->SetBranchAddress("refConstituentsPhi", &refConstituentsPhi, &b_refConstituentsPhi);
   fChain->SetBranchAddress("refConstituentsM", &refConstituentsM, &b_refConstituentsM);
   fChain->SetBranchAddress("refSDConstituentsId", &refSDConstituentsId, &b_refSDConstituentsId);
   fChain->SetBranchAddress("refSDConstituentsE", &refSDConstituentsE, &b_refSDConstituentsE);
   fChain->SetBranchAddress("refSDConstituentsPt", &refSDConstituentsPt, &b_refSDConstituentsPt);
   fChain->SetBranchAddress("refSDConstituentsEta", &refSDConstituentsEta, &b_refSDConstituentsEta);
   fChain->SetBranchAddress("refSDConstituentsPhi", &refSDConstituentsPhi, &b_refSDConstituentsPhi);
   fChain->SetBranchAddress("refSDConstituentsM", &refSDConstituentsM, &b_refSDConstituentsM); */
   fChain->SetBranchAddress("genChargedSum", genChargedSum, &b_genChargedSum);
   fChain->SetBranchAddress("genHardSum", genHardSum, &b_genHardSum);
   fChain->SetBranchAddress("signalChargedSum", signalChargedSum, &b_signalChargedSum);
   fChain->SetBranchAddress("signalHardSum", signalHardSum, &b_signalHardSum);
   fChain->SetBranchAddress("subid", subid, &b_subid);
   fChain->SetBranchAddress("ngen", &ngen, &b_ngen);
   fChain->SetBranchAddress("genmatchindex", genmatchindex, &b_genmatchindex);
   fChain->SetBranchAddress("genpt", genpt, &b_genpt);
   fChain->SetBranchAddress("geneta", geneta, &b_geneta);
   fChain->SetBranchAddress("geny", geny, &b_geny);
   fChain->SetBranchAddress("gentau1", gentau1, &b_gentau1);
   fChain->SetBranchAddress("gentau2", gentau2, &b_gentau2);
   fChain->SetBranchAddress("gentau3", gentau3, &b_gentau3);
   fChain->SetBranchAddress("genphi", genphi, &b_genphi);
   fChain->SetBranchAddress("genm", genm, &b_genm);
   fChain->SetBranchAddress("gendphijt", gendphijt, &b_gendphijt);
   fChain->SetBranchAddress("gendrjt", gendrjt, &b_gendrjt);
/*   fChain->SetBranchAddress("gennCands", gennCands, &b_gennCands);
   fChain->SetBranchAddress("gennChCands", gennChCands, &b_gennChCands);
   fChain->SetBranchAddress("gennNeCands", gennNeCands, &b_gennNeCands);
   fChain->SetBranchAddress("genchargedNConst", genchargedNConst, &b_genchargedNConst);
   fChain->SetBranchAddress("geneSumConst", geneSumConst, &b_geneSumConst);
   fChain->SetBranchAddress("geneNConst", geneNConst, &b_geneNConst);
   fChain->SetBranchAddress("genmuSumConst", genmuSumConst, &b_genmuSumConst);
   fChain->SetBranchAddress("genmuNConst", genmuNConst, &b_genmuNConst);
   fChain->SetBranchAddress("genphotonSumConst", genphotonSumConst, &b_genphotonSumConst);
   fChain->SetBranchAddress("genphotonNConst", genphotonNConst, &b_genphotonNConst);
   fChain->SetBranchAddress("genneutralSumConst", genneutralSumConst, &b_genneutralSumConst);
   fChain->SetBranchAddress("genneutralNConst", genneutralNConst, &b_genneutralNConst);
   fChain->SetBranchAddress("genhfhadSumConst", genhfhadSumConst, &b_genhfhadSumConst);
   fChain->SetBranchAddress("genhfhadNConst", genhfhadNConst, &b_genhfhadNConst);
   fChain->SetBranchAddress("genhfemSumConst", genhfemSumConst, &b_genhfemSumConst);
   fChain->SetBranchAddress("genhfemNConst", genhfemNConst, &b_genhfemNConst);
   fChain->SetBranchAddress("genMByPt", genMByPt, &b_genMByPt);
   fChain->SetBranchAddress("genRMSCand", genRMSCand, &b_genRMSCand);
   fChain->SetBranchAddress("genAxis1", genAxis1, &b_genAxis1);
   fChain->SetBranchAddress("genAxis2", genAxis2, &b_genAxis2);
   fChain->SetBranchAddress("genSigma", genSigma, &b_genSigma);
   fChain->SetBranchAddress("genR", genR, &b_genR);
   fChain->SetBranchAddress("genpTD", genpTD, &b_genpTD);
   fChain->SetBranchAddress("genpull", genpull, &b_genpull);
   fChain->SetBranchAddress("genrm0p5", genrm0p5, &b_genrm0p5);
   fChain->SetBranchAddress("genrm1", genrm1, &b_genrm1);
   fChain->SetBranchAddress("genrm2", genrm2, &b_genrm2);
   fChain->SetBranchAddress("genrm3", genrm3, &b_genrm3);
   fChain->SetBranchAddress("genSDm", genSDm, &b_genSDm);
   fChain->SetBranchAddress("genSDpt", genSDpt, &b_genSDpt);
   fChain->SetBranchAddress("genSDeta", genSDeta, &b_genSDeta);
   fChain->SetBranchAddress("genSDphi", genSDphi, &b_genSDphi);
   fChain->SetBranchAddress("genSDptFrac", genSDptFrac, &b_genSDptFrac);
   fChain->SetBranchAddress("genSDrm0p5", genSDrm0p5, &b_genSDrm0p5);
   fChain->SetBranchAddress("genSDrm1", genSDrm1, &b_genSDrm1);
   fChain->SetBranchAddress("genSDrm2", genSDrm2, &b_genSDrm2);
   fChain->SetBranchAddress("genSDrm3", genSDrm3, &b_genSDrm3);
   fChain->SetBranchAddress("genTbeta20p2", genTbeta20p2, &b_genTbeta20p2);
   fChain->SetBranchAddress("genTbeta20p3", genTbeta20p3, &b_genTbeta20p3);
   fChain->SetBranchAddress("genTbeta20p4", genTbeta20p4, &b_genTbeta20p4);
   fChain->SetBranchAddress("genTbeta20p5", genTbeta20p5, &b_genTbeta20p5);
   fChain->SetBranchAddress("genTbeta30p2", genTbeta30p2, &b_genTbeta30p2);
   fChain->SetBranchAddress("genTbeta30p3", genTbeta30p3, &b_genTbeta30p3);
   fChain->SetBranchAddress("genTbeta30p4", genTbeta30p4, &b_genTbeta30p4);
   fChain->SetBranchAddress("genTbeta30p5", genTbeta30p5, &b_genTbeta30p5);
   fChain->SetBranchAddress("genCbeta20p2", genCbeta20p2, &b_genCbeta20p2);
   fChain->SetBranchAddress("genCbeta20p3", genCbeta20p3, &b_genCbeta20p3);
   fChain->SetBranchAddress("genCbeta20p4", genCbeta20p4, &b_genCbeta20p4);
   fChain->SetBranchAddress("genCbeta20p5", genCbeta20p5, &b_genCbeta20p5);
   fChain->SetBranchAddress("genZ11", genZ11, &b_genZ11);
   fChain->SetBranchAddress("genZ20", genZ20, &b_genZ20);
   fChain->SetBranchAddress("genZ22", genZ22, &b_genZ22);
   fChain->SetBranchAddress("genZ31", genZ31, &b_genZ31);
   fChain->SetBranchAddress("genZ33", genZ33, &b_genZ33);
   fChain->SetBranchAddress("genZ40", genZ40, &b_genZ40);
   fChain->SetBranchAddress("genZ42", genZ42, &b_genZ42);
   fChain->SetBranchAddress("genZ44", genZ44, &b_genZ44);
   fChain->SetBranchAddress("genZ51", genZ51, &b_genZ51);
   fChain->SetBranchAddress("genZ53", genZ53, &b_genZ53);
   fChain->SetBranchAddress("genZ55", genZ55, &b_genZ55);
   fChain->SetBranchAddress("genPhi1", genPhi1, &b_genPhi1);
   fChain->SetBranchAddress("genPhi2", genPhi2, &b_genPhi2);
   fChain->SetBranchAddress("genPhi3", genPhi3, &b_genPhi3);
   fChain->SetBranchAddress("genPhi4", genPhi4, &b_genPhi4);
   fChain->SetBranchAddress("genPhi5", genPhi5, &b_genPhi5);
   fChain->SetBranchAddress("genPhi6", genPhi6, &b_genPhi6);
   fChain->SetBranchAddress("genPhi7", genPhi7, &b_genPhi7);
   fChain->SetBranchAddress("genSkx", genSkx, &b_genSkx);
   fChain->SetBranchAddress("genSky", genSky, &b_genSky); */
   fChain->SetBranchAddress("genptG", genptG, &b_genptG);
   fChain->SetBranchAddress("genetaG", genetaG, &b_genetaG);
   fChain->SetBranchAddress("genphiG", genphiG, &b_genphiG);
   fChain->SetBranchAddress("genmG", genmG, &b_genmG);
   fChain->SetBranchAddress("genSubJetPt", &genSubJetPt, &b_genSubJetPt);
   fChain->SetBranchAddress("genSubJetEta", &genSubJetEta, &b_genSubJetEta);
   fChain->SetBranchAddress("genSubJetPhi", &genSubJetPhi, &b_genSubJetPhi);
   fChain->SetBranchAddress("genSubJetM", &genSubJetM, &b_genSubJetM);
/*   fChain->SetBranchAddress("genConstituentsId", &genConstituentsId, &b_genConstituentsId);
   fChain->SetBranchAddress("genConstituentsE", &genConstituentsE, &b_genConstituentsE);
   fChain->SetBranchAddress("genConstituentsPt", &genConstituentsPt, &b_genConstituentsPt);
   fChain->SetBranchAddress("genConstituentsEta", &genConstituentsEta, &b_genConstituentsEta);
   fChain->SetBranchAddress("genConstituentsPhi", &genConstituentsPhi, &b_genConstituentsPhi);
   fChain->SetBranchAddress("genConstituentsM", &genConstituentsM, &b_genConstituentsM);
   fChain->SetBranchAddress("genSDConstituentsId", &genSDConstituentsId, &b_genSDConstituentsId);
   fChain->SetBranchAddress("genSDConstituentsE", &genSDConstituentsE, &b_genSDConstituentsE);
   fChain->SetBranchAddress("genSDConstituentsPt", &genSDConstituentsPt, &b_genSDConstituentsPt);
   fChain->SetBranchAddress("genSDConstituentsEta", &genSDConstituentsEta, &b_genSDConstituentsEta);
   fChain->SetBranchAddress("genSDConstituentsPhi", &genSDConstituentsPhi, &b_genSDConstituentsPhi);
   fChain->SetBranchAddress("genSDConstituentsM", &genSDConstituentsM, &b_genSDConstituentsM); */
   fChain->SetBranchAddress("gensubid", gensubid, &b_gensubid);
}

Bool_t akSoftDrop4PFJetSelector::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

#endif // #ifdef akSoftDrop4PFJetSelector_cxx
