
#include <iostream>
#include <TString.h>
#include <TCanvas.h>
#include "TBranch.h"
#include "TTree.h"
#include "TSystem.h"
#include "TH1F.h"
#include "TH1D.h"
#include "TF1.h"
#include "TMath.h"
#include "TLegend.h"
#include "TLatex.h"
#include <TH2F.h>
#include <TCut.h>
#include <TStyle.h>

#include <math.h>
#include <string>
#include <TChain.h>
#include <TFile.h>

#include "TH1.h"
#include "TROOT.h"
#include "TPad.h"
#include "TRandom.h"
#include "THStack.h"
#include "TH2.h"
#include "TLatex.h"
#include "TPaveText.h"
#include "TFrame.h"
#include "TAxis.h"
#include <iostream>
#include <fstream>
#include <iomanip>
#include <TCut.h>

#include <RooFit.h>
#include <RooRealVar.h>
#include <RooDataHist.h>
#include <RooDataSet.h>
#include <RooHistPdf.h>
#include <RooPlot.h>
#include <RooAddPdf.h>
#include <RooGlobalFunc.h>
#include <RooGaussian.h>
#include <RooPolynomial.h>
#include <RooGenericPdf.h>
#include <RooFormulaVar.h>
#include <RooChebychev.h>
#include <RooExponential.h>
#include <RooFitResult.h>
#include <RooWorkspace.h>
#include <RooMCStudy.h>
#include "RooHist.h"
#include "RooConstVar.h"
#include "RooMsgService.h"
#include "RooVoigtian.h"

using namespace RooFit;
using namespace std;

RooRealVar MuMu_mass("MuMu_mass","MuMu_mass",70,110);
RooRealVar SMuMu_pt("SMuMu_pt","SMuMu_pt",0);
RooRealVar SMuMu_phi("SMuMu_phi","SMuMu_phi",0);
RooRealVar SMuMu_eta("SMuMu_eta","SMuMu_eta",0);

static TString GT="";

TLatex *tlxg=new TLatex();

class FitOut{
	public:
	double mean;
	double mean_err;
	double sigma;
	double sigma_err;

	FitOut(double a, double b, double c, double d): mean(a), mean_err(b), sigma(c),sigma_err(d){}

};

/*--------------------------------------------------------------------*/
void makeNicePlotStyle(RooPlot* plot)
/*--------------------------------------------------------------------*/
{ 
  plot->GetXaxis()->CenterTitle(true);
  plot->GetYaxis()->CenterTitle(true);
  plot->GetXaxis()->SetTitleFont(42); 
  plot->GetYaxis()->SetTitleFont(42);  
  plot->GetXaxis()->SetTitleSize(0.05);
  plot->GetYaxis()->SetTitleSize(0.05);
  plot->GetXaxis()->SetTitleOffset(0.9);
  plot->GetYaxis()->SetTitleOffset(1.3);
  plot->GetXaxis()->SetLabelFont(42);
  plot->GetYaxis()->SetLabelFont(42);
  plot->GetYaxis()->SetLabelSize(.05);
  plot->GetXaxis()->SetLabelSize(.05);
}



// FitOut ZMassUnBinFit(){
//}


FitOut ZMassBinFit(RooDataHist datahist,TString s_cut="",TString s_name="nocut")
// FitOut ZMassUnBinFit(RooDataSet datahist,TString s_cut="",TString s_name="nocut")
{

	// cout<<"sumEntries() = "<<datahist.sumEntries()<<endl;
	// RooPlot *frame = SMuMu_mass.frame();
	RooPlot *frame = MuMu_mass.frame();
	datahist.plotOn(frame);
	// RooPlot* massframe=new RooPlot("massframe","Dmass",Dmass,DsDataFitRangeLow,DsDataFitRangeHigh,nbin_DmassDraw);
	//RDH.plotOn(frame);
	//frame->Draw();

	RooMsgService::instance().setGlobalKillBelow(RooFit::FATAL);
	TCanvas *c1 = new TCanvas();
	c1->Clear();

	c1->SetLeftMargin(0.15);
	c1->SetRightMargin(0.10);

	RooRealVar mean("#mu","mean",90.0, 60.0, 120.0);
	RooRealVar width("width","width",5.0, 0.0, 120.0);
	RooRealVar sigma("#sigma","sigma",5.0, 0.0, 120.0);
	//RooBreitWigner gauss("gauss","gauss",x,mean,sigma);
	RooVoigtian voigt("voigt","voigt",MuMu_mass,mean,width,sigma);

	RooRealVar lambda("#lambda", "slope", -0.01, -100., 1.);
	RooExponential expo("expo", "expo", MuMu_mass, lambda);

	RooRealVar b("N_{b}", "Number of background events",0, datahist.sumEntries()/10);
	RooRealVar s("N_{s}", "Number of signal events", 0, datahist.sumEntries());

	RooAddPdf fullModel("fullModel", "Signal + Background Model", RooArgList(voigt, expo), RooArgList(s, b));

	// auto r = fullModel.fitTo(datahist, RooFit::PrintLevel(-1), RooFit::Save(),RooFit::Range(70.,110.));
	auto r = fullModel.fitTo(datahist, RooFit::PrintLevel(-1), RooFit::Save(), NumCPU(20));
	// r = fullModel.fitTo(datahist, RooFit::PrintLevel(-1), RooFit::Save());
	// r = fullModel.fitTo(datahist, RooFit::PrintLevel(-1), RooFit::Save());

	fullModel.plotOn(frame,RooFit::LineColor(kRed));
	fullModel.plotOn(frame,RooFit::Components(expo),RooFit::LineStyle(kDashed)) ; //Other option
	fullModel.paramOn(frame,RooFit::Layout(0.65,0.90,0.90));
	frame->getAttText()->SetTextSize(0.03);

	makeNicePlotStyle(frame);

	// Redraw data on top and print / store everything
	datahist.plotOn(frame);
	frame->GetYaxis()->SetTitle("n. of events");
	frame->GetXaxis()->SetTitle("M_{#mu#mu}");
	frame->SetTitle(GT.Data());
	// TString histName = hist->GetName();
	// frame->SetName("frame"+histName);
	// frame->SetTitle(hist->GetTitle());
	frame->Draw();


	TLatex *tlx=new TLatex();
	// tlx->DrawLatexNDC(0.2,0.8,GT.Data());
	tlx->DrawLatexNDC(0.2,0.8,s_cut.Data());

	gSystem->Exec(Form("mkdir -p %s/fitplot", GT.Data()));
	c1->Print(Form("%s/fitplot/%s.pdf",GT.Data(),s_name.Data()));
	// double mean_1=1;
	// double error_1=2;

	FitOut fitRes(mean.getValV(), mean.getError(), sigma.getValV(), sigma.getError());
	return fitRes;

}



int TkAlDiMuonValidation(TString inFname="DiMuon_GT_103X_dataRun2_Prompt_v3.root", TString GTName="103X_dataRun2_Prompt_v3")
// int TkAlDiMuonValidation(TString inFname="DiMuon_GT_106X_dataRun2_newTkAl_v18.root", TString GTName="106X_dataRun2_newTkAl_v18")
{

	GT=GTName;

	gSystem->Exec(Form("mkdir -p %s",GT.Data()));
	gSystem->Exec(Form("mkdir -p %s/fitResultPlot", GT.Data()));
	
	TFile *fin=TFile::Open(inFname.Data());
	TTree *tMuMu=(TTree*)fin->Get("myanalysis/DiMuTree");
	TFile *fout=TFile::Open(Form("%s/output.root",GT.Data()),"recreate");
	// TFile *fin=TFile::Open("fnew.root");
	// TTree *tMuMu=(TTree*)fin->Get("DiMuTree");
	tMuMu->Show(1);

	TH1D *h_test=new TH1D("h_test","h_test", 300,60,120); h_test->Sumw2();
	tMuMu->Project("h_test","SMuMu_mass");
	// h_test->Draw();	
	RooDataHist dh("dh","dh",MuMu_mass,Import(*h_test));
	RooPlot *massframe = MuMu_mass.frame();
	// dh.plotOn(massframe);
	// ZMassBinFit(dh,"test");
	// massframe->Draw();


	TCanvas *c_test=new TCanvas("c_test","c_test");

	// v.s eta
	double eta_bins[]={-4,-3,-2,-1,0,1,2,3,4};
	int n_eta_bins=8;

	fout->cd();
	TH1D *hInvMassVsEta=new TH1D("hInvMassVsEta","hInvMassVsEta",n_eta_bins,eta_bins);

	for(int i=0; i<n_eta_bins;i++){
		double eta_cutLow=eta_bins[i];
		double eta_cutHigh=eta_bins[i+1];
		tMuMu->Project("h_test","SMuMu_mass",Form("SMuMu_eta>%f && SMuMu_eta<%f", eta_cutLow, eta_cutHigh));
	  RooDataHist dh_temp("dh_temp","dh_temp",MuMu_mass,Import(*h_test));
	
		TString s_cut=Form("%.1f<#eta<%.1f", eta_cutLow,eta_cutHigh);		
		TString s_name=Form("eta_%.0fto%.0f",eta_cutLow,eta_cutHigh);	
		FitOut fitR=ZMassBinFit(dh_temp,s_cut,s_name);
		hInvMassVsEta->SetBinContent(i+1,fitR.mean);
		hInvMassVsEta->SetBinError(i+1,fitR.mean_err);


	} // end for i<n_eta_bins;

	c_test->cd();
	gStyle->SetOptStat(0);
	hInvMassVsEta->SetMaximum(91.5);
	hInvMassVsEta->SetMinimum(90);
	hInvMassVsEta->GetXaxis()->SetTitle("#eta");	
	hInvMassVsEta->GetYaxis()->SetTitle("Mass mean");	
	hInvMassVsEta->Draw();
	tlxg->DrawLatexNDC(0.2,0.8,Form("%s",GT.Data()));
	c_test->Print(Form("%s/fitResultPlot/VS_eta.pdf",GT.Data()));
	hInvMassVsEta->Write();

	// h_test->Draw();



	// v.s phi
	double phi_bins[]={-3.15,-2,-1,0,1,2,3.15};
	int n_phi_bins=sizeof(phi_bins)/sizeof(phi_bins[0])-1;

	fout->cd();
	TH1D *hInvMassVsPhi=new TH1D("hInvMassVsPhi","hInvMassVsPhi",n_phi_bins,phi_bins);

	for(int i=0; i<n_phi_bins;i++){
		double phi_cutLow=phi_bins[i];
		double phi_cutHigh=phi_bins[i+1];
		tMuMu->Project("h_test","SMuMu_mass",Form("SMuMu_phi>%f && SMuMu_phi<%f", phi_cutLow, phi_cutHigh));
	  RooDataHist dh_temp("dh_temp","dh_temp",MuMu_mass,Import(*h_test));
	
		TString s_cut=Form("%.1f<#phi<%.1f", phi_cutLow,phi_cutHigh);		
		TString s_name=Form("phi_%.0fto%.0f",phi_cutLow,phi_cutHigh);	
		FitOut fitR=ZMassBinFit(dh_temp,s_cut,s_name);
		hInvMassVsPhi->SetBinContent(i+1,fitR.mean);
		hInvMassVsPhi->SetBinError(i+1,fitR.mean_err);


	} // end for i<n_phi_bins;

	// TCanvas *c_test=new TCanvas("c_test","c_test");
	c_test->cd();
	gStyle->SetOptStat(0);
	hInvMassVsPhi->SetMaximum(91.5);
	hInvMassVsPhi->SetMinimum(90);
	hInvMassVsPhi->GetXaxis()->SetTitle("#phi");	
	hInvMassVsPhi->GetYaxis()->SetTitle("Mass mean");	
	hInvMassVsPhi->Draw();
	tlxg->DrawLatexNDC(0.2,0.8,Form("%s",GT.Data()));
	c_test->Print(Form("%s/fitResultPlot/VS_phi.pdf",GT.Data()));
	hInvMassVsPhi->Write();

	// v.s pt
	double pt_bins[]={0,5,10,15,20,30,40,60,100};
	int n_pt_bins=sizeof(pt_bins)/sizeof(pt_bins[0])-1;

	fout->cd();
	TH1D *hInvMassVsPt=new TH1D("hInvMassVsPt","hInvMassVsPt",n_pt_bins,pt_bins);

	for(int i=0; i<n_pt_bins;i++){
		double pt_cutLow=pt_bins[i];
		double pt_cutHigh=pt_bins[i+1];
		tMuMu->Project("h_test","SMuMu_mass",Form("SMuMu_pt>%f && SMuMu_pt<%f", pt_cutLow, pt_cutHigh));
	  RooDataHist dh_temp("dh_temp","dh_temp",MuMu_mass,Import(*h_test));
	
		TString s_cut=Form("%.1f<#pt<%.1f", pt_cutLow,pt_cutHigh);		
		TString s_name=Form("pt_%.0fto%.0f",pt_cutLow,pt_cutHigh);	
		FitOut fitR=ZMassBinFit(dh_temp,s_cut,s_name);
		hInvMassVsPt->SetBinContent(i+1,fitR.mean);
		hInvMassVsPt->SetBinError(i+1,fitR.mean_err);


	} // end for i<n_pt_bins;

	// TCanvas *c_test=new TCanvas("c_test","c_test");
	c_test->cd();
	gStyle->SetOptStat(0);
	hInvMassVsPt->SetMaximum(91.5);
	hInvMassVsPt->SetMinimum(90);
	hInvMassVsPt->GetXaxis()->SetTitle("p_T");	
	hInvMassVsPt->GetYaxis()->SetTitle("Mass mean");	
	hInvMassVsPt->Draw();
	tlxg->DrawLatexNDC(0.2,0.8,Form("%s",GT.Data()));
	c_test->Print(Form("%s/fitResultPlot/VS_pt.pdf",GT.Data()));
	hInvMassVsPt->Write();


	// v.s delta_eta
	double deta_bins[]={0,0.25,0.5,0.75,1,1.5,2,2.5,4};
	int n_deta_bins=sizeof(deta_bins)/sizeof(deta_bins[0])-1;

	fout->cd();
	TH1D *hInvMassVsdEta=new TH1D("hInvMassVsdEta","hInvMassVsdEta",n_deta_bins,deta_bins);

	for(int i=0; i<n_deta_bins;i++){
		double deta_cutLow=deta_bins[i];
		double deta_cutHigh=deta_bins[i+1];
		tMuMu->Project("h_test","SMuMu_mass",Form("Sdelta_eta>%f && Sdelta_eta<%f", deta_cutLow, deta_cutHigh));
	  RooDataHist dh_temp("dh_temp","dh_temp",MuMu_mass,Import(*h_test));
	
		TString s_cut=Form("%.1f<#Delta#eta<%.1f", deta_cutLow,deta_cutHigh);		
		TString s_name=Form("deta_%.0fto%.0f",deta_cutLow,deta_cutHigh);	
		FitOut fitR=ZMassBinFit(dh_temp,s_cut,s_name);
		hInvMassVsdEta->SetBinContent(i+1,fitR.mean);
		hInvMassVsdEta->SetBinError(i+1,fitR.mean_err);


	} // end for i<n_deta_bins;

	// TCanvas *c_test=new TCanvas("c_test","c_test");
	c_test->cd();
	gStyle->SetOptStat(0);
	hInvMassVsdEta->SetMaximum(91.5);
	hInvMassVsdEta->SetMinimum(90);
	hInvMassVsdEta->GetXaxis()->SetTitle("#Delta#eta");	
	hInvMassVsdEta->GetYaxis()->SetTitle("Mass mean");	
	hInvMassVsdEta->Draw();
	tlxg->DrawLatexNDC(0.2,0.8,Form("%s",GT.Data()));
	c_test->Print(Form("%s/fitResultPlot/VS_deta.pdf",GT.Data()));
	hInvMassVsdEta->Write();



	// v.s costhetaCS
	double costhetaCS_bins[]={-1,-0.75,-0.5,-0.25,0.0,0.25,0.5,0.75,1};
	int n_costhetaCS_bins=sizeof(costhetaCS_bins)/sizeof(costhetaCS_bins[0])-1;

	fout->cd();
	TH1D *hInvMassVsCosthetaCS=new TH1D("hInvMassVsCosthetaCS","hInvMassVsCosthetaCS",n_costhetaCS_bins,costhetaCS_bins);

	for(int i=0; i<n_costhetaCS_bins;i++){
		double costhetaCS_cutLow=costhetaCS_bins[i];
		double costhetaCS_cutHigh=costhetaCS_bins[i+1];
		tMuMu->Project("h_test","SMuMu_mass",Form("ScosthetaCS>%f && ScosthetaCS<%f", costhetaCS_cutLow, costhetaCS_cutHigh));
	  RooDataHist dh_temp("dh_temp","dh_temp",MuMu_mass,Import(*h_test));
	
		TString s_cut=Form("%.1f<cos(#theta_CS)<%.1f", costhetaCS_cutLow,costhetaCS_cutHigh);		
		TString s_name=Form("costhetaCS_%.0fto%.0f",costhetaCS_cutLow,costhetaCS_cutHigh);	
		FitOut fitR=ZMassBinFit(dh_temp,s_cut,s_name);
		hInvMassVsCosthetaCS->SetBinContent(i+1,fitR.mean);
		hInvMassVsCosthetaCS->SetBinError(i+1,fitR.mean_err);


	} // end for i<n_costhetaCS_bins;

	// TCanvas *c_test=new TCanvas("c_test","c_test");
	c_test->cd();
	gStyle->SetOptStat(0);
	hInvMassVsCosthetaCS->SetMaximum(91.5);
	hInvMassVsCosthetaCS->SetMinimum(90);
	hInvMassVsCosthetaCS->GetXaxis()->SetTitle("cos(#theta_CS)");	
	hInvMassVsCosthetaCS->GetYaxis()->SetTitle("Mass mean");	
	hInvMassVsCosthetaCS->Draw();
	tlxg->DrawLatexNDC(0.2,0.8,Form("%s",GT.Data()));
	c_test->Print(Form("%s/fitResultPlot/VS_costhetaCS.pdf",GT.Data()));
	hInvMassVsCosthetaCS->Write();


	// v.s phiCS
	double phiCS_bins[]={-1,-0.75,-0.5,-0.25,0.0,0.25,0.5,0.75,1};
	int n_phiCS_bins=sizeof(phiCS_bins)/sizeof(phiCS_bins[0])-1;

	fout->cd();
	TH1D *hInvMassVsPhiCS=new TH1D("hInvMassVsPhiCS","hInvMassVsPhiCS",n_phiCS_bins,phiCS_bins);

	for(int i=0; i<n_phiCS_bins;i++){
		double phiCS_cutLow=phiCS_bins[i];
		double phiCS_cutHigh=phiCS_bins[i+1];
		tMuMu->Project("h_test","SMuMu_mass",Form("SphiCS>%f && SphiCS<%f", phiCS_cutLow, phiCS_cutHigh));
	  RooDataHist dh_temp("dh_temp","dh_temp",MuMu_mass,Import(*h_test));
	
		TString s_cut=Form("%.1f<#phi_CS<%.1f", phiCS_cutLow,phiCS_cutHigh);		
		TString s_name=Form("phiCS_%.0fto%.0f",phiCS_cutLow,phiCS_cutHigh);	
		FitOut fitR=ZMassBinFit(dh_temp,s_cut,s_name);
		hInvMassVsPhiCS->SetBinContent(i+1,fitR.mean);
		hInvMassVsPhiCS->SetBinError(i+1,fitR.mean_err);


	} // end for i<n_phiCS_bins;

	// TCanvas *c_test=new TCanvas("c_test","c_test");
	c_test->cd();
	gStyle->SetOptStat(0);
	hInvMassVsPhiCS->SetMaximum(91.5);
	hInvMassVsPhiCS->SetMinimum(90);
	hInvMassVsPhiCS->GetXaxis()->SetTitle("#phi_CS");	
	hInvMassVsPhiCS->GetYaxis()->SetTitle("Mass mean");	
	hInvMassVsPhiCS->Draw();
	tlxg->DrawLatexNDC(0.2,0.8,Form("%s",GT.Data()));
	c_test->Print(Form("%s/fitResultPlot/VS_phiCS.pdf",GT.Data()));
	hInvMassVsPhiCS->Write();








/*
	// Unbinned fit
	RooDataSet RooDS_All("RooDS_All","RooDS_All",RooArgSet(MuMu_mass,SMuMu_pt,SMuMu_phi,SMuMu_eta),Import(*tMuMu));
	RooDataSet RooDS_cut=*(RooDataSet *)RooDS_All.reduce(RooArgSet(MuMu_mass),"");

	// RooDataSet RooDS_Data_cut=*(RooDataSet *)RooDS_DataAll.reduce(RooArgSet(Dmass),DataCuts.Data() ); // Weight is inherited from its mother
	// RooPlot* massframe=new RooPlot("massframe","Dmass",Dmass,DsDataFitRangeLow,DsDataFitRangeHigh,nbin_DmassDraw);
	// RooPlot *massframe=MuMu_mass.frame()	;
	// RooPlot *massframe=new RooPlot("massframe","MuMuMass",MuMu_mass,60,120,60);
	RooDS_All.plotOn(massframe);
	// RooDS_cut.plotOn(massframe);
	RooDS_All.Print();	
	RooDS_cut.Print();	

	TH1 *htemp=RooDS_cut.createHistogram("htemp",MuMu_mass,Binning(60));

	cout<<"max = "<<htemp->GetMaximum();
	cout<<"min = "<<htemp->GetMinimum();
	TCanvas *ctest=new TCanvas("ctest","ctest");
	ctest->cd();
	massframe->Draw();
	//	tMuMu->Draw("SMuMu_mass");

	
		// TString s_cut=Form("%.1f<#eta<%.1f", eta_cutLow,eta_cutHigh);		
		// TString s_name=Form("eta_%.0fto%.0f",eta_cutLow,eta_cutHigh);	
		FitOut fitR=ZMassUnBinFit(RooDS_cut,"","");
*/

	return 0;
}
