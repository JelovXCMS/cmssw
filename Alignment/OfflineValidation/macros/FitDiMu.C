#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>
#include "TLorentzVector.h"
#include "TFile.h"
#include "TTree.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TCanvas.h"
#include "TBranch.h"
#include <map>

#include <TString.h>
#include "TLegend.h"
#include "TLatex.h"
#include <TCut.h>
#include <TChain.h>
#include "TPad.h"


// RooFit includes
#include "RooPlot.h"
#include "RooRealVar.h"
#include "RooDataHist.h"
#include "RooAddPdf.h"
#include "RooGaussian.h"
#include "RooVoigtian.h"
#include <RooDataSet.h>
#include <RooHistPdf.h>
#include <RooFormulaVar.h>
#include <RooFitResult.h>
#include <RooWorkspace.h>


using namespace std;
using namespace RooFit;


int FitDiMu(TString input="myTkAlDiMeson_output.root", TString alTag="", float etaLow=-5, float etaHigh=5, float phiLow=-3.2, float phiHigh=3.2){

	TString DataCut=Form("MuMu_phi >%f && MuMu_phi < %f && MuMu_eta>%f && MuMu_eta<%f", phiLow,phiHigh, etaLow, etaHigh);
	TFile *f_data=TFile::Open(input.Data());
	TTree *DiMuTree=(TTree*)f_data->Get("myanalysis/DiMuTree");
	// DiMuTree->Draw("MuMu_phi");

	double ZmassFitLow=60;
	double ZmassFitHigh=120;

	RooRealVar MuMu_mass("MuMu_mass","MuMu_mass",ZmassFitLow,ZmassFitHigh);
	RooRealVar MuMu_eta("MuMu_eta","MuMu_eta",0);
	RooRealVar MuMu_phi("MuMu_phi","MuMu_phi",0);

	RooDataSet RooDs_All("RooDs_All","RooDs_All",RooArgSet(MuMu_mass, MuMu_eta, MuMu_phi), Import(*DiMuTree));
	RooDataSet RooDs_Cut=*(RooDataSet *)RooDs_All.reduce(RooArgSet(MuMu_mass),DataCut.Data());

	RooPlot *massframe = MuMu_mass.frame();
	// RooDs_All.plotOn(massframe,LineColor(1));
	RooDs_Cut.plotOn(massframe,LineColor(1));

    RooRealVar mean("mean","mean",95.0, 60.0, 120.0);
    RooRealVar width("width","width",5.0, 0.0, 120.0);
    RooRealVar sigma("sigma","sigma",5.0, 0.0, 120.0);
    //RooBreitWigner gauss("gauss","gauss",x,mean,sigma);
    RooVoigtian voigt("voigt","voigt",MuMu_mass,mean,width,sigma);

    RooFitResult* filters = voigt.fitTo(RooDs_Cut,"qr");

		voigt.plotOn(massframe,LineColor(4));	
		voigt.paramOn(massframe);

	TCanvas *ctest=new TCanvas("ctest","ctest",600,600);
	ctest->cd();
	massframe->Draw();


	return 0;

}
