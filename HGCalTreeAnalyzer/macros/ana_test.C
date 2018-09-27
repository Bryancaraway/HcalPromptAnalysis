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

std::vector<std::string> GetInputFiles()
{
  int numFiles = 20;
  std::string path = "/cms/data/store/user/bcaraway/condor/outputs/";
  std::string startName = "ntuples_digi_pt25_ttbar_numEvent1000_CMSSW_10_3_0_pre4_";
  std::string endName = "_v01.root";
  std::vector<std::string> inputFiles;
  
  for( int iFile = 0 ; iFile<numFiles ; iFile++ )
    {
      std::ostringstream fileName;
      fileName << path << startName << iFile << endName;
      inputFiles.push_back(fileName.str());
     
    }

  return inputFiles;

}


void ana_test()
{
  std::vector<std::string> inputFiles = GetInputFiles();
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
  //TTreeReaderArray<float> HGCDigiEta = {fReader, "HGCDigiEta"};
  //TTreeReaderArray<float> HGCDigiPhi = {fReader, "HGCDigiPhi"};
  //TTreeReaderArray<float> HGCDigiPosx = {fReader, "HGCDigiPosx"};
  //TTreeReaderArray<float> HGCDigiPosy = {fReader, "HGCDigiPosy"};
  //TTreeReaderArray<float> HGCDigiPosz = {fReader, "HGCDigiPosz"};
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
  TTreeReaderArray<int> HGCRecHitIndex = {fReader, "HGCRecHitIndex"};
  TTreeReaderArray<int> HGCRecHitLayer = {fReader, "HGCRecHitLayer"};
  TTreeReaderArray<int> HGCSimHitsCellU = {fReader, "HGCSimHitsCellU"};
  TTreeReaderArray<int> HGCSimHitsCellV = {fReader, "HGCSimHitsCellV"};
  TTreeReaderArray<int> HGCSimHitsIEta = {fReader, "HGCSimHitsIEta"};
  TTreeReaderArray<int> HGCSimHitsIPhi = {fReader, "HGCSimHitsIPhi"};
  TTreeReaderArray<int> HGCSimHitsIndex = {fReader, "HGCSimHitsIndex"};
  TTreeReaderArray<int> HGCSimHitsLayer = {fReader, "HGCSimHitsLayer"};
  TTreeReaderArray<int> HGCSimHitsSubdet = {fReader, "HGCSimHitsSubdet"};
  TTreeReaderArray<int> HGCSimHitsWaferU = {fReader, "HGCSimHitsWaferU"};
  TTreeReaderArray<int> HGCSimHitsWaferV = {fReader, "HGCSimHitsWaferV"};
  TTreeReaderArray<int> HGCUncalibratedRecHitIndex = {fReader, "HGCUncalibratedRecHitIndex"};
  TTreeReaderArray<int> HGCUncalibratedRecHitLayer = {fReader, "HGCUncalibratedRecHitLayer"};
  TTreeReaderArray<int> SimTracksCharge = {fReader, "SimTracksCharge"};
  TTreeReaderArray<int> SimTracksPID = {fReader, "SimTracksPID"};
  TTreeReaderValue<UInt_t> bx = {fReader, "bx"};
  TTreeReaderValue<UInt_t> event = {fReader, "event"};
  TTreeReaderValue<UInt_t> ls = {fReader, "ls"};
  TTreeReaderValue<UInt_t> orbit = {fReader, "orbit"};
  TTreeReaderValue<UInt_t> run = {fReader, "run"};
  TTreeReaderArray<unsigned short> HGCDigiADC = {fReader, "HGCDigiADC"};

  // do stuff here?


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
    }


}

int mian()
{
  ana_test();

  return 0;
}
