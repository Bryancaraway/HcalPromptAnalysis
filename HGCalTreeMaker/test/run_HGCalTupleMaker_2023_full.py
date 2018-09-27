#------------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------------
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
import FWCore.ParameterSet.VarParsing as VarParsing

#------------------------------------------------------------------------------------
# Declare the process and input variables
#------------------------------------------------------------------------------------
#process = cms.Process('NOISE',eras.Run2_50ns)#for 50ns 13 TeV data
#process = cms.Process('NOISE',eras.Run2_25ns)#for 25ns 13 TeV data
options = VarParsing.VarParsing ('analysis')
process = cms.Process("Trees",eras.Phase2)

options.register ('skipEvents', 0, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "no of skipped events")
#
# Dataset
# /RelValSinglePiPt25Eta1p7_2p7/CMSSW_9_3_2-93X_upgrade2023_realistic_v2_2023D17noPU-v1/GEN-SIM-RECO
# /SinglePiPt*Eta1p6_2p8/PhaseIITDRFall17*93X_upgrade2023_realistic_v2*/GEN-SIM-RECO
#
# pt=5 GeV sample
#options.inputFiles = '/store/mc/PhaseIITDRFall17DR/SinglePiPt5Eta1p6_2p8/GEN-SIM-RECO/noPUFEVT_93X_upgrade2023_realistic_v2-v1/00000/18D5CC99-22AA-E711-8020-90B11C08CDC7.root','/store/mc/PhaseIITDRFall17DR/SinglePiPt5Eta1p6_2p8/GEN-SIM-RECO/noPUFEVT_93X_upgrade2023_realistic_v2-v1/00000/B8AEECCD-22AA-E711-82FF-1866DA7F8E98.root'
#options.outputFile = 'ntuples_pt5.root'
#
# pt=10 GeV sample
#options.inputFiles = '/store/mc/PhaseIITDRFall17DR/SinglePiPt10Eta1p6_2p8/GEN-SIM-RECO/noPUFEVT_93X_upgrade2023_realistic_v2-v1/150000/0844EA3B-14A9-E711-9F1D-44A842CFD633.root','/store/mc/PhaseIITDRFall17DR/SinglePiPt10Eta1p6_2p8/GEN-SIM-RECO/noPUFEVT_93X_upgrade2023_realistic_v2-v1/150000/8CF1BCF2-3AA9-E711-B0BE-A4BF0112BD74.root'
#options.outputFile = 'ntuples_pt10.root'
#
# pt=15 GeV sample
#options.inputFiles = '/store/mc/PhaseIITDRFall17DR/SinglePiPt15Eta1p6_2p8/GEN-SIM-RECO/noPUFEVT_93X_upgrade2023_realistic_v2-v1/00000/1E9C9D26-4EA9-E711-B775-6CC2173DA2F0.root','/store/mc/PhaseIITDRFall17DR/SinglePiPt15Eta1p6_2p8/GEN-SIM-RECO/noPUFEVT_93X_upgrade2023_realistic_v2-v1/00000/5C395DE1-ACA9-E711-B391-0CC47A7EEE32.root','/store/mc/PhaseIITDRFall17DR/SinglePiPt15Eta1p6_2p8/GEN-SIM-RECO/noPUFEVT_93X_upgrade2023_realistic_v2-v1/00000/6AD5611D-81A9-E711-92A7-3417EBE7009F.root'
#options.outputFile = 'ntuples_pt15.root'
#
# pt=25 GeV sample *relval*
#options.inputFiles = '/store/relval/CMSSW_9_3_2/RelValSinglePiPt25Eta1p7_2p7/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/2637F672-C7A6-E711-B4EF-0025905A612A.root','/store/relval/CMSSW_9_3_2/RelValSinglePiPt25Eta1p7_2p7/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/3C00B396-CBA6-E711-95E1-0025905A612A.root','/store/relval/CMSSW_9_3_2/RelValSinglePiPt25Eta1p7_2p7/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/60FC86A0-CDA6-E711-960D-0025905B856E.root','/store/relval/CMSSW_9_3_2/RelValSinglePiPt25Eta1p7_2p7/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/E0E29FFF-C6A6-E711-93A0-003048FFCC16.root'
options.inputFiles = '/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_1.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_10.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_100.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_11.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_12.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_13.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_14.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_15.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_16.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_17.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_18.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_19.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_2.root' ,'/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_20.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_21.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_22.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_23.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_24.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_25.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_26.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_27.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_28.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_29.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_3.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_30.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_31.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_32.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_33.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_34.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_35.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_36.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_37.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_38.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_39.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_4.root' ,'/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_40.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_41.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_42.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_43.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_44.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_45.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_46.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_47.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_48.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_49.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_5.root' ,'/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_50.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_51.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_52.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_53.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_54.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_55.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_56.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_57.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_58.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_59.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_6.root ','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_60.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_61.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_62.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_63.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_64.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_65.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_66.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_67.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_68.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_69.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_7.root' ,'/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_70.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_71.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_72.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_73.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_74.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_75.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_76.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_77.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_78.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_79.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_8.root' ,'/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_80.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_81.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_82.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_83.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_84.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_85.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_86.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_87.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_88.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_89.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_9.root' ,'/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_90.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_91.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_92.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_93.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_94.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_95.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_96.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_97.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_98.root','/store/user/bcaraway/crab_outputs/TTbar_14TeV/CMSSW_10_3_0_pre4_Step3_v3/180920_181904/0000/step3_99.root'

options.outputFile = 'ntuples_digi_pt25_ttbar.root'
#
# pt=50 GeV sample
#options.inputFiles = '/store/mc/PhaseIITDRFall17DR/SinglePiPt50Eta1p6_2p8/GEN-SIM-RECO/noPUFEVT_93X_upgrade2023_realistic_v2-v1/00000/B2807A02-50AD-E711-AF78-F01FAFDB45B7.root','/store/mc/PhaseIITDRFall17DR/SinglePiPt50Eta1p6_2p8/GEN-SIM-RECO/noPUFEVT_93X_upgrade2023_realistic_v2-v1/150000/1AB4309F-BAAE-E711-87BC-A0369FC5D904.root','/store/mc/PhaseIITDRFall17DR/SinglePiPt50Eta1p6_2p8/GEN-SIM-RECO/noPUFEVT_93X_upgrade2023_realistic_v2-v1/150000/1AE8206E-E1AD-E711-98C0-FA163E191258.root','/store/mc/PhaseIITDRFall17DR/SinglePiPt50Eta1p6_2p8/GEN-SIM-RECO/noPUFEVT_93X_upgrade2023_realistic_v2-v1/150000/20F00603-FEAD-E711-83F8-0090FAA59EE4.root'
#options.outputFile = 'ntuples_pt50.root'
#
# pt=100 GeV sample
#options.inputFiles = '/store/mc/PhaseIITDRFall17DR/SinglePiPt100Eta1p6_2p8/GEN-SIM-RECO/noPUFEVT_93X_upgrade2023_realistic_v2-v1/150000/BE82B842-31AE-E711-9EA4-0026B94DBDA2.root','/store/mc/PhaseIITDRFall17DR/SinglePiPt100Eta1p6_2p8/GEN-SIM-RECO/noPUFEVT_93X_upgrade2023_realistic_v2-v1/150000/E20ADE15-A5AE-E711-9434-0023AEEEB55F.root','/store/mc/PhaseIITDRFall17DR/SinglePiPt100Eta1p6_2p8/GEN-SIM-RECO/noPUFEVT_93X_upgrade2023_realistic_v2-v1/150000/FC41ACC6-2FAE-E711-B431-F04DA2747854.root'
#options.outputFile = 'ntuples_pt100.root'
#
#'/store/relval/CMSSW_9_3_2/RelValSinglePiPt25Eta1p7_2p7/GEN-SIM-RECO/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/2637F672-C7A6-E711-B4EF-0025905A612A.root'
options.maxEvents = -1 # -1 means all events
#options.skipEvents = 0 # default is 0.

#------------------------------------------------------------------------------------
# Get and parse the command line arguments
#------------------------------------------------------------------------------------
options.parseArguments()
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles),
    secondaryFileNames = cms.untracked.vstring(options.secondaryInputFiles),
    skipEvents = cms.untracked.uint32(options.skipEvents) # default is 0.
)

process.TFileService = cms.Service("TFileService", 
                                   fileName = cms.string(options.outputFile)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
    Rethrow = cms.untracked.vstring("ProductNotFound"), # make this exception fatal
    fileMode  =  cms.untracked.string('NOMERGE') # no ordering needed, but calls endRun/beginRun etc. at file boundaries
)

#------------------------------------------------------------------------------------
# import of standard configurations
#------------------------------------------------------------------------------------
# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D28Reco_cff')  # <=== to be checked
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.PATMC_cff')
process.load('Configuration.StandardSequences.Validation_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

#KH
process.MessageLogger.cerr.FwkReport.reportEvery = 100

#------------------------------------------------------------------------------------
# Set up our analyzer
#------------------------------------------------------------------------------------
process.load("HGCalAnalysis.HGCalTreeMaker.HGCalTupleMaker_Tree_cfi")
process.load("HGCalAnalysis.HGCalTreeMaker.HGCalTupleMaker_Event_cfi")
process.load("HGCalAnalysis.HGCalTreeMaker.HGCalTupleMaker_GenParticles_cfi")
process.load("HGCalAnalysis.HGCalTreeMaker.HGCalTupleMaker_HBHERecHits_cfi")
process.load("HGCalAnalysis.HGCalTreeMaker.HGCalTupleMaker_HGCRecHits_cfi")
process.load("HGCalAnalysis.HGCalTreeMaker.HGCalTupleMaker_HGCUncalibratedRecHits_cfi")
process.load("HGCalAnalysis.HGCalTreeMaker.HGCalTupleMaker_HGCDigis_cfi")
process.load("HGCalAnalysis.HGCalTreeMaker.HGCalTupleMaker_HGCSimHits_cfi")
process.load("HGCalAnalysis.HGCalTreeMaker.HGCalTupleMaker_SimTracks_cfi")
process.load("HGCalAnalysis.HGCalTreeMaker.HGCalTupleMaker_RecoTracks_cfi")

process.load("Validation.HGCalValidation.hgcalHitValidation_cfi")
process.load("Validation.HGCalValidation.digiValidation_cff")

#------------------------------------------------------------------------------------
# Specify Global Tag
#------------------------------------------------------------------------------------
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

#------------------------------------------------------------------------------------
# HGCalTupleMaker sequence definition
#------------------------------------------------------------------------------------
process.tuple_step = cms.Sequence(
    # Make HCAL tuples: Event, run, ls number
    process.hgcalTupleEvent*
    process.hgcalTupleHBHERecHits*
    process.hgcalTupleHGCRecHits*
    process.hgcalTupleHGCDigis*
    process.hgcalTupleHGCUncalibratedRecHits*
    process.hgcalTupleGenParticles*
    process.hgcalTupleHGCSimHits*
    process.hgcalTupleSimTracks*
    process.hgcalTupleGeneralTracks*
    process.hgcalTupleTree
)


#-----------------------------------------------------------------------------------
# Path and EndPath definitions
#-----------------------------------------------------------------------------------
process.preparation = cms.Path(
    process.hgcalHitValidation*
    process.hgcalDigiValidationEE*
    process.hgcalDigiValidationHEF*
    #process.hgcalDigiValidationHEB*
    process.tuple_step
)
