#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <iomanip> // for setw()
#include <algorithm> 

#include "TROOT.h"
#include "TF1.h"
#include "TMath.h"
#include "TChain.h"
#include "TFile.h"
#include "TTree.h"
#include "TMath.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TCanvas.h"
#include "TDirectory.h"
#include "TBranch.h"
#include "TString.h"
#include "TStyle.h"
#include "TInterpreter.h"
#include "TStyle.h"
#include "TLorentzVector.h"

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>
#include <TTreeReader.h>
#include <TTreeReaderValue.h>
#include <TTreeReaderArray.h>

std::vector<std::string> GetInputFiles(std::string geoConfig)
{
  int numFiles = 20;
  std::string path = "/cms/data/store/user/bcaraway/condor/outputs/";
  std::string startName = "ntuples_digi_pt25_ttbar_";
  std::string midName = "numEvent1000_CMSSW_10_3_0_pre4_";
  std::string endName = "_v01.root";
  std::vector<std::string> inputFiles;
  
  for( int iFile = 0 ; iFile<numFiles ; iFile++ )
    {
      std::ostringstream fileName;
      fileName << path << startName << geoConfig << midName << iFile << endName;
      inputFiles.push_back(fileName.str());
     
    }

  return inputFiles;

}

void WriteToOutput(int n_f,  TH2F* h[n_f], TString outputFile, TString fileOption)
{
  TFile *f = new TFile(outputFile,fileOption); // output file 
  for ( int i = 1; i <= n_f; i++)
    {
      h[i] -> Write();
    }
  f->Close();
}


void ana_main()
{
  
  std::string geoType = "" ; // D30 geo, "" for D28
  std::vector<std::string> inputFiles = GetInputFiles(geoType+"");
  TChain *ch = new TChain("hgcalTupleTree/tree");
  
  for (unsigned int iFile=0; iFile<inputFiles.size(); ++iFile) {
    ch->Add(inputFiles[iFile].c_str());
    std::cout<<inputFiles[iFile]<<std::endl;
  }
  //ch->Print();
  //   printf("%d;\n",ch->GetNtrees());
  printf("%lld;\n",ch->GetEntries());
  
  TTreeReader     fReader(ch);  //!the tree reader
   
  //
  // Set up TTreeReader's
  // -- use MakeSelector of root
  //
  
  // Readers to access the data (delete the ones you do not need).

  //TTreeReaderArray<double> GenParEta = {fReader, "GenParEta"};
  //TTreeReaderArray<double> GenParM = {fReader, "GenParM"};
  //TTreeReaderArray<double> GenParPhi = {fReader, "GenParPhi"};
  //TTreeReaderArray<double> GenParPt = {fReader, "GenParPt"};
  //TTreeReaderArray<double> GeneralTracksD0 = {fReader, "GeneralTracksD0"};
  //TTreeReaderArray<double> GeneralTracksDZ = {fReader, "GeneralTracksDZ"};
  //TTreeReaderArray<double> GeneralTracksEta = {fReader, "GeneralTracksEta"};
  //TTreeReaderArray<double> GeneralTracksPhi = {fReader, "GeneralTracksPhi"};
  //TTreeReaderArray<double> GeneralTracksPt = {fReader, "GeneralTracksPt"};
  //TTreeReaderArray<float> HBHERecHitEnergy = {fReader, "HBHERecHitEnergy"};
  //TTreeReaderArray<float> HBHERecHitEta = {fReader, "HBHERecHitEta"};
  //TTreeReaderArray<float> HBHERecHitPhi = {fReader, "HBHERecHitPhi"};
  //TTreeReaderArray<float> HBHERecHitTime = {fReader, "HBHERecHitTime"};
  //TTreeReaderArray<float> HGCDigiCharge = {fReader, "HGCDigiCharge"};
  TTreeReaderArray<float> HGCDigiEta = {fReader, "HGCDigiEta"};
  TTreeReaderArray<float> HGCDigiPhi = {fReader, "HGCDigiPhi"};
  TTreeReaderArray<float> HGCDigiPosx = {fReader, "HGCDigiPosx"};
  TTreeReaderArray<float> HGCDigiPosy = {fReader, "HGCDigiPosy"};
  TTreeReaderArray<float> HGCDigiPosz = {fReader, "HGCDigiPosz"};
  //TTreeReaderArray<float> HGCRecHitEnergy = {fReader, "HGCRecHitEnergy"};
  //TTreeReaderArray<float> HGCRecHitEta = {fReader, "HGCRecHitEta"};
  //TTreeReaderArray<float> HGCRecHitPhi = {fReader, "HGCRecHitPhi"};
  //TTreeReaderArray<float> HGCRecHitPosx = {fReader, "HGCRecHitPosx"};
  //TTreeReaderArray<float> HGCRecHitPosy = {fReader, "HGCRecHitPosy"};
  //TTreeReaderArray<float> HGCRecHitPosz = {fReader, "HGCRecHitPosz"};
  //TTreeReaderArray<float> HGCSimHitsEnergy = {fReader, "HGCSimHitsEnergy"};
  //TTreeReaderArray<float> HGCSimHitsEta = {fReader, "HGCSimHitsEta"};
  //TTreeReaderArray<float> HGCSimHitsPhi = {fReader, "HGCSimHitsPhi"};
  //TTreeReaderArray<float> HGCSimHitsPosx = {fReader, "HGCSimHitsPosx"};
  //TTreeReaderArray<float> HGCSimHitsPosy = {fReader, "HGCSimHitsPosy"};
  //TTreeReaderArray<float> HGCSimHitsPosz = {fReader, "HGCSimHitsPosz"};
  //TTreeReaderArray<float> HGCSimHitsTime = {fReader, "HGCSimHitsTime"};
  //TTreeReaderArray<float> HGCUncalibratedRecHitAmplitude = {fReader, "HGCUncalibratedRecHitAmplitude"};
  //TTreeReaderArray<float> HGCUncalibratedRecHitEta = {fReader, "HGCUncalibratedRecHitEta"};
  //TTreeReaderArray<float> HGCUncalibratedRecHitPhi = {fReader, "HGCUncalibratedRecHitPhi"};
  //TTreeReaderArray<float> HGCUncalibratedRecHitPosx = {fReader, "HGCUncalibratedRecHitPosx"};
  //TTreeReaderArray<float> HGCUncalibratedRecHitPosy = {fReader, "HGCUncalibratedRecHitPosy"};
  //TTreeReaderArray<float> HGCUncalibratedRecHitPosz = {fReader, "HGCUncalibratedRecHitPosz"};
  //TTreeReaderArray<float> SimTracksEta = {fReader, "SimTracksEta"};
  //TTreeReaderArray<float> SimTracksPhi = {fReader, "SimTracksPhi"};
  //TTreeReaderArray<float> SimTracksPt = {fReader, "SimTracksPt"};
  //TTreeReaderArray<float> SimTracksR = {fReader, "SimTracksR"};
  //TTreeReaderArray<float> SimTracksZ = {fReader, "SimTracksZ"};
  //TTreeReaderArray<int> GenParPdgId = {fReader, "GenParPdgId"};
  //TTreeReaderArray<int> GenParStatus = {fReader, "GenParStatus"};
  //TTreeReaderArray<int> GeneralTracksNValidHits = {fReader, "GeneralTracksNValidHits"};
  //TTreeReaderArray<int> HBHERecHitAux = {fReader, "HBHERecHitAux"};
  //TTreeReaderArray<int> HBHERecHitDepth = {fReader, "HBHERecHitDepth"};
  //TTreeReaderArray<int> HBHERecHitFlags = {fReader, "HBHERecHitFlags"};
  //TTreeReaderArray<int> HBHERecHitHPDid = {fReader, "HBHERecHitHPDid"};
  //TTreeReaderArray<int> HBHERecHitIEta = {fReader, "HBHERecHitIEta"};
  //TTreeReaderArray<int> HBHERecHitIPhi = {fReader, "HBHERecHitIPhi"};
  //TTreeReaderArray<int> HBHERecHitRBXid = {fReader, "HBHERecHitRBXid"};
  TTreeReaderArray<int> HGCDigiCellU = {fReader, "HGCDigiCellU"};
  TTreeReaderArray<int> HGCDigiCellV = {fReader, "HGCDigiCellV"};
  TTreeReaderArray<int> HGCDigiIEta = {fReader, "HGCDigiIEta"};
  TTreeReaderArray<int> HGCDigiIPhi = {fReader, "HGCDigiIPhi"};
  TTreeReaderArray<int> HGCDigiIndex = {fReader, "HGCDigiIndex"};
  TTreeReaderArray<int> HGCDigiLayer = {fReader, "HGCDigiLayer"};
  TTreeReaderArray<int> HGCDigiWaferU = {fReader, "HGCDigiWaferU"};
  TTreeReaderArray<int> HGCDigiWaferV = {fReader, "HGCDigiWaferV"};
  //TTreeReaderArray<int> HGCRecHitIndex = {fReader, "HGCRecHitIndex"};
  //TTreeReaderArray<int> HGCRecHitLayer = {fReader, "HGCRecHitLayer"};
  //TTreeReaderArray<int> HGCSimHitsCellU = {fReader, "HGCSimHitsCellU"};
  //TTreeReaderArray<int> HGCSimHitsCellV = {fReader, "HGCSimHitsCellV"};
  //TTreeReaderArray<int> HGCSimHitsIEta = {fReader, "HGCSimHitsIEta"};
  //TTreeReaderArray<int> HGCSimHitsIPhi = {fReader, "HGCSimHitsIPhi"};
  //TTreeReaderArray<int> HGCSimHitsIndex = {fReader, "HGCSimHitsIndex"};
  //TTreeReaderArray<int> HGCSimHitsLayer = {fReader, "HGCSimHitsLayer"};
  //TTreeReaderArray<int> HGCSimHitsSubdet = {fReader, "HGCSimHitsSubdet"};
  //TTreeReaderArray<int> HGCSimHitsWaferU = {fReader, "HGCSimHitsWaferU"};
  //TTreeReaderArray<int> HGCSimHitsWaferV = {fReader, "HGCSimHitsWaferV"};
  //TTreeReaderArray<int> HGCUncalibratedRecHitIndex = {fReader, "HGCUncalibratedRecHitIndex"};
  //TTreeReaderArray<int> HGCUncalibratedRecHitLayer = {fReader, "HGCUncalibratedRecHitLayer"};
  //TTreeReaderArray<int> SimTracksCharge = {fReader, "SimTracksCharge"};
  //TTreeReaderArray<int> SimTracksPID = {fReader, "SimTracksPID"};
  TTreeReaderValue<UInt_t> bx = {fReader, "bx"};
  TTreeReaderValue<UInt_t> event = {fReader, "event"};
  TTreeReaderValue<UInt_t> ls = {fReader, "ls"};
  TTreeReaderValue<UInt_t> orbit = {fReader, "orbit"};
  TTreeReaderValue<UInt_t> run = {fReader, "run"};
  TTreeReaderArray<unsigned short> HGCDigiADC = {fReader, "HGCDigiADC"};

  // Histos defined here

  TH2F *h_digi_cee_waferuv[28];
  for(int i=1; i<=28; i++) 
    {
      std::ostringstream name;
      name <<"h_digi_cee_waferuv_"<<i;
      h_digi_cee_waferuv[i] = new TH2F(name.str().c_str(),name.str().c_str(),31,-15.5,15.5,31,-15.5,15.5);
    }

  TH2F *h_digi_ceh_waferuv[24];
  for(int i=1; i<=24; i++) 
    {
      std::ostringstream name;
      name <<"h_digi_ceh_waferuv_"<<i;
      h_digi_ceh_waferuv[i] = new TH2F(name.str().c_str(),name.str().c_str(),31,-15.5,15.5,31,-15.5,15.5);
    }

    TH2F *h_digi_cee_celluv[28];
  for(int i=1; i<=28; i++) 
    {
      std::ostringstream name;
      name <<"h_digi_cee_celluv_"<<i;
      h_digi_cee_celluv[i] = new TH2F(name.str().c_str(),name.str().c_str(),36,-5.5,30.5,36,-5.5,30.5);
    }

  TH2F *h_digi_ceh_celluv[24];
  for(int i=1; i<=24; i++) 
    {
      std::ostringstream name;
      name <<"h_digi_ceh_celluv_"<<i;
      h_digi_ceh_celluv[i] = new TH2F(name.str().c_str(),name.str().c_str(),36,-5.5,30.5,36,-5.5,30.5);
    }
  

  // Main Loop Start
  unsigned int nentries = (Int_t)ch->GetEntries();
  int ievent=0; int maxevents = -1; int skipevents = 0;
  while (fReader.Next()) 
    {
  
      // Progress indicator 
      ievent++;
      if(ievent%500==0) cout << "[HGCAL Response analyzer] Processed " << ievent << " out of " << nentries << " events" << endl; 
      if (maxevents>0 && ievent>maxevents) break;
      if (ievent<=skipevents) continue;
      
      //std::cout << "Simhit size: " << HGCSimHitsEnergy.GetSize() << std::endl;
      //std::cout << "Digi size:   " << HGCDigiADC.GetSize() << std::endl;
      //std::cout << "Rechit size: " << HGCRecHitEnergy.GetSize() << std::endl;

      // Analyze over Simhits, Rechits, and Digis here
      // Index definition: 0 -- CEE, 1 -- CEH Si, 2 -- CEH Scint
      // CEE -- 1-28 layers, CEH Si -- 1-24 layers, CEH Scint -- 9-24 layers

      for (int irc = 0, nrc = HGCDigiEta.GetSize(); irc <nrc; ++irc)
	{
	  int l_hit = HGCDigiLayer[irc];
	  int u_wafer = HGCDigiWaferU[irc];
	  int v_wafer = HGCDigiWaferV[irc];
	  int u_cell = HGCDigiCellU[irc];
	  int v_cell = HGCDigiCellV[irc];

	  if (HGCDigiIndex[irc] == 0)
	    {
	      h_digi_cee_waferuv[l_hit]->Fill(u_wafer,v_wafer);
	      h_digi_cee_celluv[l_hit]->Fill(u_cell,v_cell);
	    }
	  if (HGCDigiIndex[irc] == 1)
	    {
	      h_digi_ceh_waferuv[l_hit]->Fill(u_wafer,v_wafer);
	      h_digi_ceh_celluv[l_hit]->Fill(u_cell,v_cell);
	    }
	  
	}

    }
  
  //end of main event loop
  // write histos to output file
  // Note: cee->28, ceh->24
  int cee = 28; int ceh = 24;
  WriteToOutput(cee,h_digi_cee_waferuv,"waferuv.root","RECREATE");
  WriteToOutput(ceh,h_digi_ceh_waferuv,"waferuv.root","UPDATE");
  
  WriteToOutput(cee,h_digi_cee_celluv,"celluv.root","RECREATE");
  WriteToOutput(ceh,h_digi_ceh_celluv,"celluv.root","UPDATE");

  
}



int mian()
{
  ana_main();

  return 0;
}
