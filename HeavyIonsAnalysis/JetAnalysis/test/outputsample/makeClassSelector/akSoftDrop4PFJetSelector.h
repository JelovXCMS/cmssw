//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Fri Mar 17 15:04:44 2017 by ROOT version 6.02/13
// from TTree t/akSoftDrop4PFpatJetsWithBtagging Jet Analysis Tree
// found on file: Test_HiForestAOD_pp_MC_PYTHIA6_bjet30.root
//////////////////////////////////////////////////////////

#ifndef akSoftDrop4PFJetSelector_h
#define akSoftDrop4PFJetSelector_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>

// Header file for the classes stored in the TTree if any.
#include "vector"

class akSoftDrop4PFJetSelector : public TSelector {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   Int_t           evt;
   Float_t         b;
   Int_t           nref;
   Float_t         rawpt[44];   //[nref]
   Float_t         jtpt[44];   //[nref]
   Float_t         jteta[44];   //[nref]
   Float_t         jty[44];   //[nref]
   Float_t         jtphi[44];   //[nref]
   Float_t         jtpu[44];   //[nref]
   Float_t         jtm[44];   //[nref]
   Float_t         jtarea[44];   //[nref]
   Float_t         jtPfCHF[44];   //[nref]
   Float_t         jtPfNHF[44];   //[nref]
   Float_t         jtPfCEF[44];   //[nref]
   Float_t         jtPfNEF[44];   //[nref]
   Float_t         jtPfMUF[44];   //[nref]
   Int_t           jtPfCHM[44];   //[nref]
   Int_t           jtPfNHM[44];   //[nref]
   Int_t           jtPfCEM[44];   //[nref]
   Int_t           jtPfNEM[44];   //[nref]
   Int_t           jtPfMUM[44];   //[nref]
   Float_t         jttau1[44];   //[nref]
   Float_t         jttau2[44];   //[nref]
   Float_t         jttau3[44];   //[nref]
   vector<vector<float> > *jtSubJetPt;
   vector<vector<float> > *jtSubJetEta;
   vector<vector<float> > *jtSubJetPhi;
   vector<vector<float> > *jtSubJetM;
   Float_t         discr_jetID_cuts[44];   //[nref]
   Float_t         discr_jetID_bdt[44];   //[nref]
   Float_t         discr_fr01[44];   //[nref]
   Float_t         trackMax[44];   //[nref]
   Float_t         trackSum[44];   //[nref]
   Int_t           trackN[44];   //[nref]
   Float_t         trackHardSum[44];   //[nref]
   Int_t           trackHardN[44];   //[nref]
   Float_t         chargedMax[44];   //[nref]
   Float_t         chargedSum[44];   //[nref]
   Int_t           chargedN[44];   //[nref]
   Float_t         chargedHardSum[44];   //[nref]
   Int_t           chargedHardN[44];   //[nref]
   Float_t         photonMax[44];   //[nref]
   Float_t         photonSum[44];   //[nref]
   Int_t           photonN[44];   //[nref]
   Float_t         photonHardSum[44];   //[nref]
   Int_t           photonHardN[44];   //[nref]
   Float_t         neutralMax[44];   //[nref]
   Float_t         neutralSum[44];   //[nref]
   Int_t           neutralN[44];   //[nref]
   Float_t         hcalSum[44];   //[nref]
   Float_t         ecalSum[44];   //[nref]
   Float_t         eMax[44];   //[nref]
   Float_t         eSum[44];   //[nref]
   Int_t           eN[44];   //[nref]
   Float_t         muMax[44];   //[nref]
   Float_t         muSum[44];   //[nref]
   Int_t           muN[44];   //[nref]
   Float_t         discr_ssvHighEff[44];   //[nref]
   Float_t         discr_ssvHighPur[44];   //[nref]
   Float_t         discr_csvV1[44];   //[nref]
   Float_t         discr_csvV2[44];   //[nref]
   Float_t         discr_muByIp3[44];   //[nref]
   Float_t         discr_muByPt[44];   //[nref]
   Float_t         discr_prob[44];   //[nref]
   Float_t         discr_probb[44];   //[nref]
   Float_t         discr_tcHighEff[44];   //[nref]
   Float_t         discr_tcHighPur[44];   //[nref]
   Float_t         ndiscr_ssvHighEff[44];   //[nref]
   Float_t         ndiscr_ssvHighPur[44];   //[nref]
   Float_t         ndiscr_csvV1[44];   //[nref]
   Float_t         ndiscr_csvV2[44];   //[nref]
   Float_t         ndiscr_muByPt[44];   //[nref]
   Float_t         pdiscr_csvV1[44];   //[nref]
   Float_t         pdiscr_csvV2[44];   //[nref]
   Int_t           nsvtx[44];   //[nref]
   Int_t           svtxntrk[44];   //[nref]
   Float_t         svtxdl[44];   //[nref]
   Float_t         svtxdls[44];   //[nref]
   Float_t         svtxdl2d[44];   //[nref]
   Float_t         svtxdls2d[44];   //[nref]
   Float_t         svtxm[44];   //[nref]
   Float_t         svtxpt[44];   //[nref]
   Float_t         svtxmcorr[44];   //[nref]
   Int_t           nIPtrk[44];   //[nref]
   Int_t           nselIPtrk[44];   //[nref]
   Float_t         mue[44];   //[nref]
   Float_t         mupt[44];   //[nref]
   Float_t         mueta[44];   //[nref]
   Float_t         muphi[44];   //[nref]
   Float_t         mudr[44];   //[nref]
   Float_t         muptrel[44];   //[nref]
   Int_t           muchg[44];   //[nref]
   Int_t           beamId1;
   Int_t           beamId2;
   Float_t         pthat;
   Float_t         refpt[44];   //[nref]
   Float_t         refeta[44];   //[nref]
   Float_t         refy[44];   //[nref]
   Float_t         refphi[44];   //[nref]
   Float_t         refm[44];   //[nref]
   Float_t         refarea[44];   //[nref]
   Int_t           bProdCode;
   Int_t           cProdCode;
   Float_t         reftau1[44];   //[nref]
   Float_t         reftau2[44];   //[nref]
   Float_t         reftau3[44];   //[nref]
   Float_t         refdphijt[44];   //[nref]
   Float_t         refdrjt[44];   //[nref]
   Float_t         refparton_pt[44];   //[nref]
   Int_t           refparton_flavor[44];   //[nref]
   Int_t           refparton_flavorForB[44];   //[nref]
   Int_t           refparton_flavorProcess[44];   //[nref]
   Float_t         refptG[44];   //[nref]
   Float_t         refetaG[44];   //[nref]
   Float_t         refphiG[44];   //[nref]
   Float_t         refmG[44];   //[nref]
   vector<vector<float> > *refSubJetPt;
   vector<vector<float> > *refSubJetEta;
   vector<vector<float> > *refSubJetPhi;
   vector<vector<float> > *refSubJetM;
   Float_t         genChargedSum[44];   //[nref]
   Float_t         genHardSum[44];   //[nref]
   Float_t         signalChargedSum[44];   //[nref]
   Float_t         signalHardSum[44];   //[nref]
   Int_t           subid[44];   //[nref]
   Int_t           ngen;
   Int_t           genmatchindex[24];   //[ngen]
   Float_t         genpt[24];   //[ngen]
   Float_t         geneta[24];   //[ngen]
   Float_t         geny[24];   //[ngen]
   Float_t         gentau1[24];   //[ngen]
   Float_t         gentau2[24];   //[ngen]
   Float_t         gentau3[24];   //[ngen]
   Float_t         genphi[24];   //[ngen]
   Float_t         genm[24];   //[ngen]
   Float_t         gendphijt[24];   //[ngen]
   Float_t         gendrjt[24];   //[ngen]
   Float_t         genptG[24];   //[ngen]
   Float_t         genetaG[24];   //[ngen]
   Float_t         genphiG[24];   //[ngen]
   Float_t         genmG[24];   //[ngen]
   vector<vector<float> > *genSubJetPt;
   vector<vector<float> > *genSubJetEta;
   vector<vector<float> > *genSubJetPhi;
   vector<vector<float> > *genSubJetM;
   Int_t           gensubid[24];   //[ngen]

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
   TBranch        *b_genptG;   //!
   TBranch        *b_genetaG;   //!
   TBranch        *b_genphiG;   //!
   TBranch        *b_genmG;   //!
   TBranch        *b_genSubJetPt;   //!
   TBranch        *b_genSubJetEta;   //!
   TBranch        *b_genSubJetPhi;   //!
   TBranch        *b_genSubJetM;   //!
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
   refSubJetPt = 0;
   refSubJetEta = 0;
   refSubJetPhi = 0;
   refSubJetM = 0;
   genSubJetPt = 0;
   genSubJetEta = 0;
   genSubJetPhi = 0;
   genSubJetM = 0;
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
   fChain->SetBranchAddress("genptG", genptG, &b_genptG);
   fChain->SetBranchAddress("genetaG", genetaG, &b_genetaG);
   fChain->SetBranchAddress("genphiG", genphiG, &b_genphiG);
   fChain->SetBranchAddress("genmG", genmG, &b_genmG);
   fChain->SetBranchAddress("genSubJetPt", &genSubJetPt, &b_genSubJetPt);
   fChain->SetBranchAddress("genSubJetEta", &genSubJetEta, &b_genSubJetEta);
   fChain->SetBranchAddress("genSubJetPhi", &genSubJetPhi, &b_genSubJetPhi);
   fChain->SetBranchAddress("genSubJetM", &genSubJetM, &b_genSubJetM);
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
