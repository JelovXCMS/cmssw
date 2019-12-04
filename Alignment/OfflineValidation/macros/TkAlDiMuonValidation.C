
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

RooRealVar SMuMu_mass("SMuMu_mass","SMuMu_mass",70,110);
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


FitOut ZMassBinFit(RooDataHist datahist,TString s_cut="",TString s_name="nocut"){

	// cout<<"sumEntries() = "<<datahist.sumEntries()<<endl;
	// RooPlot *frame = SMuMu_mass.frame();
	RooPlot *frame = SMuMu_mass.frame();
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
	RooVoigtian voigt("voigt","voigt",SMuMu_mass,mean,width,sigma);

	RooRealVar lambda("#lambda", "slope", -0.01, -100., 1.);
	RooExponential expo("expo", "expo", SMuMu_mass, lambda);

	RooRealVar b("N_{b}", "Number of background events",0, datahist.sumEntries()/10);
	RooRealVar s("N_{s}", "Number of signal events", 0, datahist.sumEntries());

	RooAddPdf fullModel("fullModel", "Signal + Background Model", RooArgList(voigt, expo), RooArgList(s, b));

	// auto r = fullModel.fitTo(datahist, RooFit::PrintLevel(-1), RooFit::Save(),RooFit::Range(70.,110.));
	auto r = fullModel.fitTo(datahist, RooFit::PrintLevel(-1), RooFit::Save());
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



// int TkAlDiMuonValidation(TString inFname="DiMuon_GT_103X_dataRun2_Prompt_v3.root", TString GTName="103X_dataRun2_Prompt_v3")
int TkAlDiMuonValidation(TString inFname="DiMuon_GT_106X_dataRun2_newTkAl_v18.root", TString GTName="106X_dataRun2_newTkAl_v18.root")
{

	GT=GTName;

	gSystem->Exec(Form("mkdir -p %s",GT.Data()));
	gSystem->Exec(Form("mkdir -p %s/fitResultPlot", GT.Data()));
	
	TFile *fin=TFile::Open(inFname.Data());
	TTree *tMuMu=(TTree*)fin->Get("myanalysis/DiMuTree");
	// TFile *fin=TFile::Open("fnew.root");
	// TTree *tMuMu=(TTree*)fin->Get("DiMuTree");
	tMuMu->Show(1);

	TH1D *h_test=new TH1D("h_test","h_test", 300,60,120); h_test->Sumw2();
	tMuMu->Project("h_test","SMuMu_mass");
	// h_test->Draw();	
	RooDataHist dh("dh","dh",SMuMu_mass,Import(*h_test));
	RooPlot *massframe = SMuMu_mass.frame();
	dh.plotOn(massframe);
	// ZMassBinFit(dh,"test");
	// massframe->Draw();

	// v.s eta
	double eta_bins[]={-4,-3,-2,-1,0,1,2,3,4};
	int n_eta_bins=8;

	TH1D *hInvMassVsEta=new TH1D("hInvMassVsEta","hInvMassVsEta",n_eta_bins,eta_bins);

	for(int i=0; i<n_eta_bins;i++){
		double eta_cutLow=eta_bins[i];
		double eta_cutHigh=eta_bins[i+1];
		tMuMu->Project("h_test","SMuMu_mass",Form("SMuMu_eta>%f && SMuMu_eta<%f", eta_cutLow, eta_cutHigh));
	  RooDataHist dh_temp("dh_temp","dh_temp",SMuMu_mass,Import(*h_test));
	
		TString s_cut=Form("%.1f<#eta<%.1f", eta_cutLow,eta_cutHigh);		
		TString s_name=Form("eta_%.0fto%.0f",eta_cutLow,eta_cutHigh);	
		FitOut fitR=ZMassBinFit(dh_temp,s_cut,s_name);
		hInvMassVsEta->SetBinContent(i+1,fitR.mean);
		hInvMassVsEta->SetBinError(i+1,fitR.mean_err);


	} // end for i<n_eta_bins;

	TCanvas *c_test=new TCanvas("c_test","c_test");
	c_test->cd();
	gStyle->SetOptStat(0);
	hInvMassVsEta->SetMaximum(91.5);
	hInvMassVsEta->SetMinimum(90);
	hInvMassVsEta->GetXaxis()->SetTitle("#eta");	
	hInvMassVsEta->GetYaxis()->SetTitle("Mass mean");	
	hInvMassVsEta->Draw();
	tlxg->DrawLatexNDC(0.2,0.8,Form("%s",GT.Data()));
	c_test->Print(Form("%s/fitResultPlot/VS_eta.pdf",GT.Data()));
	  // hInvMassVsEta->Write();

	// h_test->Draw();


	/*
	// Unbinned fit
	RooDataSet RooDS_All("RooDS_All","RooDS_All",RooArgSet(SMuMu_mass,SMuMu_pt,SMuMu_phi,SMuMu_eta),Import(*tMuMu));
	RooDataSet RooDS_cut=*(RooDataSet *)RooDS_All.reduce(RooArgSet(SMuMu_mass),"");

	// RooDataSet RooDS_Data_cut=*(RooDataSet *)RooDS_DataAll.reduce(RooArgSet(Dmass),DataCuts.Data() ); // Weight is inherited from its mother
	// RooPlot* massframe=new RooPlot("massframe","Dmass",Dmass,DsDataFitRangeLow,DsDataFitRangeHigh,nbin_DmassDraw);
	// RooPlot *massframe=SMuMu_mass.frame()	;
	RooPlot *massframe=new RooPlot("massframe","MuMuMass",SMuMu_mass,60,120,60);
	RooDS_All.plotOn(massframe);
	// RooDS_cut.plotOn(massframe);
	RooDS_All.Print();	
	RooDS_cut.Print();	

	TH1 *htemp=RooDS_cut.createHistogram("htemp",SMuMu_mass,Binning(60));

	cout<<"max = "<<htemp->GetMaximum();
	cout<<"min = "<<htemp->GetMinimum();
	TCanvas *ctest=new TCanvas("ctest","ctest");
	ctest->cd();
	massframe->Draw();
	//	tMuMu->Draw("SMuMu_mass");
	*/

	return 0;
}
