//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Mon Apr 10 MAX_NJetS:55:52 2017 by ROOT version 6.02/13
// from TTree t/akSoftDrop4PFpatJetsWithBtagging Jet Analysis Tree
// found on file: Test_HiForestAOD_pp_MC_PYTHIA6_Bjet1MAX_NJetS_n1000.root
//////////////////////////////////////////////////////////

#ifndef akSD4Selector_simple_h
#define akSD4Selector_simple_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>

// Header file for the classes stored in the TTree if any.
#include "vector"

class akSD4Selector_simple : public TSelector {
public :
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
   Float_t         reftau1[MAX_NJetS];   //[nref]
   Float_t         reftau2[MAX_NJetS];   //[nref]
   Float_t         reftau3[MAX_NJetS];   //[nref]
   Float_t         refdphijt[MAX_NJetS];   //[nref]
   Float_t         refdrjt[MAX_NJetS];   //[nref]
   Float_t         refparton_pt[MAX_NJetS];   //[nref]
   Int_t           refparton_flavor[MAX_NJetS];   //[nref]
   Int_t           refparton_flavorForB[MAX_NJetS];   //[nref]
   Int_t           refparton_flavorProcess[MAX_NJetS];   //[nref]
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
   Float_t         refptG[MAX_NJetS];   //[nref]
   Float_t         refetaG[MAX_NJetS];   //[nref]
   Float_t         refphiG[MAX_NJetS];   //[nref]
   Float_t         refmG[MAX_NJetS];   //[nref]
   vector<vector<float> > *refSubJetPt;
   vector<vector<float> > *refSubJetEta;
   vector<vector<float> > *refSubJetPhi;
   vector<vector<float> > *refSubJetM;
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
   Float_t         genptG[MAX_NJetS];   //[ngen]
   Float_t         genetaG[MAX_NJetS];   //[ngen]
   Float_t         genphiG[MAX_NJetS];   //[ngen]
   Float_t         genmG[MAX_NJetS];   //[ngen]
   vector<vector<float> > *genSubJetPt;
   vector<vector<float> > *genSubJetEta;
   vector<vector<float> > *genSubJetPhi;
   vector<vector<float> > *genSubJetM;
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

   akSD4Selector_simple(TTree * /*tree*/ =0) : fChain(0) { }
   virtual ~akSD4Selector_simple() { }
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

   ClassDef(akSD4Selector_simple,0);
};

#endif

#ifdef akSD4Selector_simple_cxx
void akSD4Selector_simple::Init(TTree *tree)
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

Bool_t akSD4Selector_simple::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

#endif // #ifdef akSD4Selector_simple_cxx
