//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Fri Apr 15 10:48:29 2016 by ROOT version 6.04/12
// from TTree CollectionTree/xAOD event tree
// found on file: root://eosatlas//eos/atlas/atlascerngroupdisk/phys-higgs/HSG1/MxAOD/h011/mc_25ns/Sherpa_gamgam_2DP20_0-55.MxAOD.p2419.h011.root
//////////////////////////////////////////////////////////

#ifndef MxAOD_h
#define MxAOD_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.
#include "AthContainers/DataVector.h"
#include "xAODCore/AuxContainerBase.h"
#include "vector"
#include "vector"
#include "vector"
#include "vector"
#include "AthContainers/DataVector.h"
#include "AthContainers/DataVector.h"
#include "AthContainers/DataVector.h"
#include "xAODMissingET/versions/MissingETContainer_v1.h"
#include "vector"
#include "vector"
#include "vector"
#include "xAODEventInfo/versions/EventInfo_v1.h"
#include "xAODCore/AuxInfoBase.h"
#include "AthContainers/DataVector.h"
#include "AthContainers/DataVector.h"
#include "vector"
#include "vector"

class MxAOD {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.
   const Int_t kMaxHGamPhotonsAux = 1;
   const Int_t kMaxHGamElectronsAux = 1;
   const Int_t kMaxHGamAntiKt4EMTopoJetsAux = 1;
   const Int_t kMaxHGamMuonsAux = 1;
   const Int_t kMaxHGamMET_Reference_AntiKt4EMTopoAux = 1;
   const Int_t kMaxHGamMuonsInJetsAux = 1;
   const Int_t kMaxHGamEventInfoAux = 1;
   const Int_t kMaxHGamTruthPhotonsAux = 1;
   const Int_t kMaxHGamTruthElectronsAux = 1;
   const Int_t kMaxHGamTruthMuonsAux = 1;
   const Int_t kMaxHGamAntiKt4TruthJetsAux = 1;
   const Int_t kMaxHGamMET_TruthAux = 1;
   const Int_t kMaxHGamTruthHiggsBosonsAux = 1;
   const Int_t kMaxHGamTruthEventInfoAux = 1;

   // Declaration of leaf types
   DataVector<xAOD::Photon_v1> *HGamPhotons;
   xAOD::AuxContainerBase *HGamPhotonsAux_;
   vector<float>   *HGamPhotonsAuxDyn_topoetcone20;
   vector<float>   *HGamPhotonsAuxDyn_eta_s2;
   vector<float>   *HGamPhotonsAuxDyn_relEreso;
   vector<float>   *HGamPhotonsAuxDyn_topoetcone40;
   vector<float>   *HGamPhotonsAuxDyn_ptcone20;
   vector<char>    *HGamPhotonsAuxDyn_isTight;
   vector<float>   *HGamPhotonsAuxDyn_ptcone40;
   vector<int>     *HGamPhotonsAuxDyn_conversionType;
   vector<float>   *HGamPhotonsAuxDyn_conversionRadius;
   vector<int>     *HGamPhotonsAuxDyn_truthOrigin;
   vector<float>   *HGamPhotonsAuxDyn_truthConvRadius;
   vector<int>     *HGamPhotonsAuxDyn_truthType;
   vector<char>    *HGamPhotonsAuxDyn_isTight_nofudge;
   vector<unsigned int> *HGamPhotonsAuxDyn_isEMTight_nofudge;
   vector<float>   *HGamPhotonsAuxDyn_topoetcone20_DDcorrected;
   vector<float>   *HGamPhotonsAuxDyn_topoetcone40_DDcorrected;
   vector<float>   *HGamPhotonsAuxDyn_pt;
   vector<float>   *HGamPhotonsAuxDyn_eta;
   vector<float>   *HGamPhotonsAuxDyn_ratioE1E2;
   vector<char>    *HGamPhotonsAuxDyn_isIsoFixedCutLoose;
   vector<float>   *HGamPhotonsAuxDyn_phi;
   vector<char>    *HGamPhotonsAuxDyn_isIsoFixedCutTight;
   vector<float>   *HGamPhotonsAuxDyn_m;
   vector<char>    *HGamPhotonsAuxDyn_isIsoFixedCutTightCaloOnly;
   vector<char>    *HGamPhotonsAuxDyn_isIsoFixedCutLooseCaloOnly;
   vector<float>   *HGamPhotonsAuxDyn_E0_raw;
   vector<float>   *HGamPhotonsAuxDyn_E1_raw;
   vector<float>   *HGamPhotonsAuxDyn_E2_raw;
   vector<float>   *HGamPhotonsAuxDyn_E3_raw;
   vector<unsigned int> *HGamPhotonsAuxDyn_isEMTight;
   vector<float>   *HGamPhotonsAuxDyn_scaleFactor;
   DataVector<xAOD::Electron_v1> *HGamElectrons;
   xAOD::AuxContainerBase *HGamElectronsAux_;
   DataVector<xAOD::Jet_v1> *HGamAntiKt4EMTopoJets;
   xAOD::AuxContainerBase *HGamAntiKt4EMTopoJetsAux_;
   vector<float>   *HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_85;
   vector<float>   *HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_85;
   vector<float>   *HGamAntiKt4EMTopoJetsAuxDyn_Jvt;
   vector<float>   *HGamAntiKt4EMTopoJetsAuxDyn_DetectorEta;
   vector<float>   *HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_60;
   vector<float>   *HGamAntiKt4EMTopoJetsAuxDyn_pt;
   vector<float>   *HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_60;
   vector<float>   *HGamAntiKt4EMTopoJetsAuxDyn_eta;
   vector<float>   *HGamAntiKt4EMTopoJetsAuxDyn_phi;
   vector<float>   *HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_70;
   vector<float>   *HGamAntiKt4EMTopoJetsAuxDyn_m;
   vector<float>   *HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_70;
   vector<float>   *HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_77;
   vector<float>   *HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_77;
   DataVector<xAOD::Muon_v1> *HGamMuons;
   xAOD::AuxContainerBase *HGamMuonsAux_;
   xAOD::MissingETContainer_v1 *HGamMET_Reference_AntiKt4EMTopo;
   xAOD::AuxContainerBase *HGamMET_Reference_AntiKt4EMTopoAux_;
   vector<ULong64_t> *HGamMET_Reference_AntiKt4EMTopoAuxDyn_source;
   vector<double>  *HGamMET_Reference_AntiKt4EMTopoAuxDyn_sumet;
   vector<string>  *HGamMET_Reference_AntiKt4EMTopoAuxDyn_name;
   vector<double>  *HGamMET_Reference_AntiKt4EMTopoAuxDyn_mpx;
   vector<double>  *HGamMET_Reference_AntiKt4EMTopoAuxDyn_mpy;
   DataVector<xAOD::Muon_v1> *HGamMuonsInJets;
   xAOD::AuxContainerBase *HGamMuonsInJetsAux_;
   xAOD::EventInfo_v1 *HGamEventInfo;
   xAOD::AuxInfoBase *HGamEventInfoAux_;
   Float_t         HGamEventInfoAuxDyn_crossSectionBRfilterEff;
   Float_t         HGamEventInfoAuxDyn_yAbs_yy;
   Float_t         HGamEventInfoAuxDyn_pTt_yy;
   Float_t         HGamEventInfoAuxDyn_m_yy;
   Char_t          HGamEventInfoAuxDyn_passMeyCut;
   Float_t         HGamEventInfoAuxDyn_pT_yy;
   Float_t         HGamEventInfoAuxDyn_pT_y1;
   Float_t         HGamEventInfoAuxDyn_pT_y2;
   Float_t         HGamEventInfoAuxDyn_E_y1;
   Float_t         HGamEventInfoAuxDyn_E_y2;
   Float_t         HGamEventInfoAuxDyn_pT_hard;
   Float_t         HGamEventInfoAuxDyn_cosTS_yy;
   Float_t         HGamEventInfoAuxDyn_Dy_y_y;
   Int_t           HGamEventInfoAuxDyn_N_e;
   Int_t           HGamEventInfoAuxDyn_N_mu;
   Int_t           HGamEventInfoAuxDyn_N_j;
   Int_t           HGamEventInfoAuxDyn_N_j_central;
   Int_t           HGamEventInfoAuxDyn_N_j_central30;
   Float_t         HGamEventInfoAuxDyn_pT_j1;
   Float_t         HGamEventInfoAuxDyn_pT_j2;
   Float_t         HGamEventInfoAuxDyn_pT_jj;
   Float_t         HGamEventInfoAuxDyn_m_jj;
   Float_t         HGamEventInfoAuxDyn_Dy_j_j;
   Float_t         HGamEventInfoAuxDyn_Dy_yy_jj;
   Float_t         HGamEventInfoAuxDyn_Dphi_yy_jj;
   Float_t         HGamEventInfoAuxDyn_m_ee;
   Float_t         HGamEventInfoAuxDyn_m_mumu;
   Float_t         HGamEventInfoAuxDyn_DRmin_y_j;
   Float_t         HGamEventInfoAuxDyn_DR_y_y;
   Float_t         HGamEventInfoAuxDyn_Zepp;
   Float_t         HGamEventInfoAuxDyn_cosTS_yyjj;
   Float_t         HGamEventInfoAuxDyn_met_TST;
   Float_t         HGamEventInfoAuxDyn_sumet_TST;
   Float_t         HGamEventInfoAuxDyn_phi_TST;
   Char_t          HGamEventInfoAuxDyn_isPassedBasic;
   Char_t          HGamEventInfoAuxDyn_isPassed;
   Char_t          HGamEventInfoAuxDyn_isPassedJetEventClean;
   Char_t          HGamEventInfoAuxDyn_isDalitz;
   Int_t           HGamEventInfoAuxDyn_cutFlow;
   Float_t         HGamEventInfoAuxDyn_weightInitial;
   Float_t         HGamEventInfoAuxDyn_weight;
   Float_t         HGamEventInfoAuxDyn_vertexWeight;
   Float_t         HGamEventInfoAuxDyn_pileupWeight;
   Float_t         HGamEventInfoAuxDyn_weightCatCoup_dev;
   Int_t           HGamEventInfoAuxDyn_catCoup_dev;
   Float_t         HGamEventInfoAuxDyn_weightCatCoup_Moriond2016;
   Int_t           HGamEventInfoAuxDyn_catCoup_Moriond2016;
   Int_t           HGamEventInfoAuxDyn_numberOfPrimaryVertices;
   Float_t         HGamEventInfoAuxDyn_selectedVertexZ;
   Float_t         HGamEventInfoAuxDyn_hardestVertexZ;
   Float_t         HGamEventInfoAuxDyn_m_yy_resolution;
   Float_t         HGamEventInfoAuxDyn_zCommon;
   Int_t           HGamEventInfoAuxDyn_NLoosePhotons;
   Float_t         HGamEventInfoAuxDyn_truthVertexZ;
   Int_t           HGamEventInfoAuxDyn_N_j_btag;
   Int_t           HGamEventInfoAuxDyn_N_j_btag30;
   Float_t         HGamEventInfoAuxDyn_m_yy_hardestVertex;
   Float_t         HGamEventInfoAuxDyn_eventShapeDensity;
   Float_t         HGamEventInfoAuxDyn_m_yy_truthVertex;
   Float_t         HGamEventInfoAuxDyn_mu;
   Float_t         HGamEventInfoAuxDyn_m_yy_zCommon;
   Char_t          HGamEventInfoAuxDyn_isPassedPreselection;
   Char_t          HGamEventInfoAuxDyn_isPassedPID;
   Char_t          HGamEventInfoAuxDyn_isPassedIsolation;
   Char_t          HGamEventInfoAuxDyn_isPassedRelPtCuts;
   Char_t          HGamEventInfoAuxDyn_isPassedMassCut;
   Char_t          HGamEventInfoAuxDyn_isPassedIsolationLowHighMyy;
   Char_t          HGamEventInfoAuxDyn_isPassedRelPtCutsLowHighMyy;
   Char_t          HGamEventInfoAuxDyn_isPassedLowHighMyy;
   Char_t          HGamEventInfoAuxDyn_isPassedIsolationExotic;
   Char_t          HGamEventInfoAuxDyn_isPassedlPtCutsExotic;
   Char_t          HGamEventInfoAuxDyn_isPassedExotic;
   DataVector<xAOD::TruthParticle_v1> *HGamTruthPhotons;
   xAOD::AuxContainerBase *HGamTruthPhotonsAux_;
   vector<char>    *HGamTruthPhotonsAuxDyn_isIsolated;
   vector<float>   *HGamTruthPhotonsAuxDyn_etcone20;
   vector<float>   *HGamTruthPhotonsAuxDyn_etcone40;
   vector<float>   *HGamTruthPhotonsAuxDyn_px;
   vector<float>   *HGamTruthPhotonsAuxDyn_ptcone20;
   vector<float>   *HGamTruthPhotonsAuxDyn_py;
   vector<float>   *HGamTruthPhotonsAuxDyn_ptcone40;
   vector<float>   *HGamTruthPhotonsAuxDyn_pz;
   vector<float>   *HGamTruthPhotonsAuxDyn_e;
   vector<float>   *HGamTruthPhotonsAuxDyn_pt;
   vector<float>   *HGamTruthPhotonsAuxDyn_eta;
   vector<float>   *HGamTruthPhotonsAuxDyn_m;
   vector<int>     *HGamTruthPhotonsAuxDyn_truthOrigin;
   vector<int>     *HGamTruthPhotonsAuxDyn_truthType;
   DataVector<xAOD::TruthParticle_v1> *HGamTruthElectrons;
   xAOD::AuxContainerBase *HGamTruthElectronsAux_;
   DataVector<xAOD::TruthParticle_v1> *HGamTruthMuons;
   xAOD::AuxContainerBase *HGamTruthMuonsAux_;
   DataVector<xAOD::Jet_v1> *HGamAntiKt4TruthJets;
   xAOD::AuxContainerBase *HGamAntiKt4TruthJetsAux_;
   vector<float>   *HGamAntiKt4TruthJetsAuxDyn_pt;
   vector<float>   *HGamAntiKt4TruthJetsAuxDyn_eta;
   vector<float>   *HGamAntiKt4TruthJetsAuxDyn_phi;
   vector<float>   *HGamAntiKt4TruthJetsAuxDyn_m;
   DataVector<xAOD::MissingET_v1> *HGamMET_Truth;
   xAOD::AuxContainerBase *HGamMET_TruthAux_;
   vector<ULong64_t> *HGamMET_TruthAuxDyn_source;
   vector<double>  *HGamMET_TruthAuxDyn_sumet;
   vector<string>  *HGamMET_TruthAuxDyn_name;
   vector<double>  *HGamMET_TruthAuxDyn_mpx;
   vector<double>  *HGamMET_TruthAuxDyn_mpy;
   DataVector<xAOD::TruthParticle_v1> *HGamTruthHiggsBosons;
   xAOD::AuxContainerBase *HGamTruthHiggsBosonsAux_;
   xAOD::EventInfo_v1 *HGamTruthEventInfo;
   xAOD::AuxInfoBase *HGamTruthEventInfoAux_;
   Float_t         HGamTruthEventInfoAuxDyn_pT_jj;
   Float_t         HGamTruthEventInfoAuxDyn_m_jj;
   Float_t         HGamTruthEventInfoAuxDyn_Dy_j_j;
   Float_t         HGamTruthEventInfoAuxDyn_Dphi_yy_jj;
   Float_t         HGamTruthEventInfoAuxDyn_m_ee;
   Float_t         HGamTruthEventInfoAuxDyn_m_mumu;
   Float_t         HGamTruthEventInfoAuxDyn_DRmin_y_j;
   Float_t         HGamTruthEventInfoAuxDyn_DR_y_y;
   Float_t         HGamTruthEventInfoAuxDyn_Zepp;
   Float_t         HGamTruthEventInfoAuxDyn_cosTS_yyjj;
   Float_t         HGamTruthEventInfoAuxDyn_pT_h1;
   Float_t         HGamTruthEventInfoAuxDyn_pT_h2;
   Float_t         HGamTruthEventInfoAuxDyn_y_h1;
   Float_t         HGamTruthEventInfoAuxDyn_y_h2;
   Char_t          HGamTruthEventInfoAuxDyn_isFiducial;
   Float_t         HGamTruthEventInfoAuxDyn_m_h1;
   Char_t          HGamTruthEventInfoAuxDyn_isFiducialKinOnly;
   Float_t         HGamTruthEventInfoAuxDyn_m_h2;
   Float_t         HGamTruthEventInfoAuxDyn_yAbs_yy;
   Float_t         HGamTruthEventInfoAuxDyn_pTt_yy;
   Float_t         HGamTruthEventInfoAuxDyn_m_yy;
   Char_t          HGamTruthEventInfoAuxDyn_passMeyCut;
   Float_t         HGamTruthEventInfoAuxDyn_pT_yy;
   Float_t         HGamTruthEventInfoAuxDyn_pT_y1;
   Float_t         HGamTruthEventInfoAuxDyn_pT_y2;
   Float_t         HGamTruthEventInfoAuxDyn_E_y1;
   Float_t         HGamTruthEventInfoAuxDyn_E_y2;
   Float_t         HGamTruthEventInfoAuxDyn_pT_hard;
   Float_t         HGamTruthEventInfoAuxDyn_TruthNonInt_met;
   Float_t         HGamTruthEventInfoAuxDyn_cosTS_yy;
   Float_t         HGamTruthEventInfoAuxDyn_TruthInt_sumet;
   Char_t          HGamTruthEventInfoAuxDyn_isFiducialLowHighMyy;
   Char_t          HGamTruthEventInfoAuxDyn_isFiducialExotic;
   Float_t         HGamTruthEventInfoAuxDyn_Dy_y_y;
   Int_t           HGamTruthEventInfoAuxDyn_N_e;
   Int_t           HGamTruthEventInfoAuxDyn_N_mu;
   Int_t           HGamTruthEventInfoAuxDyn_N_j;
   Int_t           HGamTruthEventInfoAuxDyn_N_j_central;
   Int_t           HGamTruthEventInfoAuxDyn_N_j_central30;
   Float_t         HGamTruthEventInfoAuxDyn_pT_j1;
   Float_t         HGamTruthEventInfoAuxDyn_pT_j2;
   xAOD::EventInfo_v1 *EventInfo;
   UInt_t          EventInfoAuxDyn_runNumber;
   UInt_t          EventInfoAuxDyn_eventTypeBitmask;
   ULong64_t       EventInfoAuxDyn_eventNumber;
   UInt_t          EventInfoAuxDyn_RandomRunNumber;
   UInt_t          EventInfoAuxDyn_lumiBlock;
   UInt_t          EventInfoAuxDyn_coreFlags;
   UInt_t          EventInfoAuxDyn_mcChannelNumber;
   Float_t         EventInfoAuxDyn_averageInteractionsPerCrossing;
   Char_t          EventInfoAuxDyn_passTrig_HLT_g35_loose_g25_loose;
   vector<float>   *EventInfoAuxDyn_mcEventWeights;
   Char_t          EventInfoAuxDyn_passTrig_HLT_2g50_loose;
   vector<ElementLink<DataVector<xAOD::IParticle> > > *HGamPhotonsAuxDyn_truthLink;
   vector<int>     *HGamPhotonsAuxDyn_parentPdgId;
   vector<int>     *HGamPhotonsAuxDyn_pdgId;
   vector<ElementLink<DataVector<xAOD::IParticle> > > *HGamTruthPhotonsAuxDyn_recoLink;
   vector<float>   *HGamMuonsInJetsAuxDyn_ptvarcone20;
   vector<char>    *HGamMuonsInJetsAuxDyn_passIPCut;
   vector<unsigned short> *HGamMuonsInJetsAuxDyn_muonType;
   vector<float>   *HGamMuonsInJetsAuxDyn_pt;
   vector<float>   *HGamMuonsInJetsAuxDyn_topoetcone20;
   vector<float>   *HGamMuonsInJetsAuxDyn_eta;
   vector<float>   *HGamMuonsInJetsAuxDyn_scaleFactor;
   vector<float>   *HGamMuonsInJetsAuxDyn_phi;
   vector<float>   *HGamMuonsInJetsAuxDyn_charge;
   vector<float>   *HGamTruthElectronsAuxDyn_px;
   vector<float>   *HGamTruthElectronsAuxDyn_py;
   vector<float>   *HGamTruthElectronsAuxDyn_pz;
   vector<float>   *HGamTruthElectronsAuxDyn_pt;
   vector<float>   *HGamTruthElectronsAuxDyn_eta;
   vector<float>   *HGamTruthElectronsAuxDyn_e;
   vector<float>   *HGamTruthElectronsAuxDyn_m;
   vector<ElementLink<DataVector<xAOD::IParticle> > > *HGamTruthElectronsAuxDyn_recoLink;
   vector<float>   *HGamTruthMuonsAuxDyn_px;
   vector<float>   *HGamTruthMuonsAuxDyn_py;
   vector<float>   *HGamTruthMuonsAuxDyn_pz;
   vector<float>   *HGamTruthMuonsAuxDyn_pt;
   vector<float>   *HGamTruthMuonsAuxDyn_eta;
   vector<float>   *HGamTruthMuonsAuxDyn_e;
   vector<float>   *HGamTruthMuonsAuxDyn_m;
   vector<float>   *HGamMuonsAuxDyn_ptvarcone20;
   vector<char>    *HGamMuonsAuxDyn_passIPCut;
   vector<unsigned short> *HGamMuonsAuxDyn_muonType;
   vector<float>   *HGamMuonsAuxDyn_pt;
   vector<float>   *HGamMuonsAuxDyn_topoetcone20;
   vector<float>   *HGamMuonsAuxDyn_eta;
   vector<float>   *HGamMuonsAuxDyn_scaleFactor;
   vector<float>   *HGamMuonsAuxDyn_phi;
   vector<float>   *HGamMuonsAuxDyn_charge;
   vector<float>   *HGamElectronsAuxDyn_eta_s2;
   vector<float>   *HGamElectronsAuxDyn_ptvarcone20;
   vector<float>   *HGamElectronsAuxDyn_pt;
   vector<float>   *HGamElectronsAuxDyn_topoetcone20;
   vector<char>    *HGamElectronsAuxDyn_isTight;
   vector<float>   *HGamElectronsAuxDyn_eta;
   vector<float>   *HGamElectronsAuxDyn_scaleFactor;
   vector<float>   *HGamElectronsAuxDyn_phi;
   vector<float>   *HGamElectronsAuxDyn_charge;
   vector<float>   *HGamElectronsAuxDyn_m;
   vector<ElementLink<DataVector<xAOD::IParticle> > > *HGamElectronsAuxDyn_truthLink;

   // List of branches
   TBranch        *b_HGamPhotons;   //!
   TBranch        *b_HGamPhotonsAux_;   //!
   TBranch        *b_HGamPhotonsAuxDyn_topoetcone20;   //!
   TBranch        *b_HGamPhotonsAuxDyn_eta_s2;   //!
   TBranch        *b_HGamPhotonsAuxDyn_relEreso;   //!
   TBranch        *b_HGamPhotonsAuxDyn_topoetcone40;   //!
   TBranch        *b_HGamPhotonsAuxDyn_ptcone20;   //!
   TBranch        *b_HGamPhotonsAuxDyn_isTight;   //!
   TBranch        *b_HGamPhotonsAuxDyn_ptcone40;   //!
   TBranch        *b_HGamPhotonsAuxDyn_conversionType;   //!
   TBranch        *b_HGamPhotonsAuxDyn_conversionRadius;   //!
   TBranch        *b_HGamPhotonsAuxDyn_truthOrigin;   //!
   TBranch        *b_HGamPhotonsAuxDyn_truthConvRadius;   //!
   TBranch        *b_HGamPhotonsAuxDyn_truthType;   //!
   TBranch        *b_HGamPhotonsAuxDyn_isTight_nofudge;   //!
   TBranch        *b_HGamPhotonsAuxDyn_isEMTight_nofudge;   //!
   TBranch        *b_HGamPhotonsAuxDyn_topoetcone20_DDcorrected;   //!
   TBranch        *b_HGamPhotonsAuxDyn_topoetcone40_DDcorrected;   //!
   TBranch        *b_HGamPhotonsAuxDyn_pt;   //!
   TBranch        *b_HGamPhotonsAuxDyn_eta;   //!
   TBranch        *b_HGamPhotonsAuxDyn_ratioE1E2;   //!
   TBranch        *b_HGamPhotonsAuxDyn_isIsoFixedCutLoose;   //!
   TBranch        *b_HGamPhotonsAuxDyn_phi;   //!
   TBranch        *b_HGamPhotonsAuxDyn_isIsoFixedCutTight;   //!
   TBranch        *b_HGamPhotonsAuxDyn_m;   //!
   TBranch        *b_HGamPhotonsAuxDyn_isIsoFixedCutTightCaloOnly;   //!
   TBranch        *b_HGamPhotonsAuxDyn_isIsoFixedCutLooseCaloOnly;   //!
   TBranch        *b_HGamPhotonsAuxDyn_E0_raw;   //!
   TBranch        *b_HGamPhotonsAuxDyn_E1_raw;   //!
   TBranch        *b_HGamPhotonsAuxDyn_E2_raw;   //!
   TBranch        *b_HGamPhotonsAuxDyn_E3_raw;   //!
   TBranch        *b_HGamPhotonsAuxDyn_isEMTight;   //!
   TBranch        *b_HGamPhotonsAuxDyn_scaleFactor;   //!
   TBranch        *b_HGamElectrons;   //!
   TBranch        *b_HGamElectronsAux_;   //!
   TBranch        *b_HGamAntiKt4EMTopoJets;   //!
   TBranch        *b_HGamAntiKt4EMTopoJetsAux_;   //!
   TBranch        *b_HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_85;   //!
   TBranch        *b_HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_85;   //!
   TBranch        *b_HGamAntiKt4EMTopoJetsAuxDyn_Jvt;   //!
   TBranch        *b_HGamAntiKt4EMTopoJetsAuxDyn_DetectorEta;   //!
   TBranch        *b_HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_60;   //!
   TBranch        *b_HGamAntiKt4EMTopoJetsAuxDyn_pt;   //!
   TBranch        *b_HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_60;   //!
   TBranch        *b_HGamAntiKt4EMTopoJetsAuxDyn_eta;   //!
   TBranch        *b_HGamAntiKt4EMTopoJetsAuxDyn_phi;   //!
   TBranch        *b_HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_70;   //!
   TBranch        *b_HGamAntiKt4EMTopoJetsAuxDyn_m;   //!
   TBranch        *b_HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_70;   //!
   TBranch        *b_HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_77;   //!
   TBranch        *b_HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_77;   //!
   TBranch        *b_HGamMuons;   //!
   TBranch        *b_HGamMuonsAux_;   //!
   TBranch        *b_HGamMET_Reference_AntiKt4EMTopo;   //!
   TBranch        *b_HGamMET_Reference_AntiKt4EMTopoAux_;   //!
   TBranch        *b_HGamMET_Reference_AntiKt4EMTopoAuxDyn_source;   //!
   TBranch        *b_HGamMET_Reference_AntiKt4EMTopoAuxDyn_sumet;   //!
   TBranch        *b_HGamMET_Reference_AntiKt4EMTopoAuxDyn_name;   //!
   TBranch        *b_HGamMET_Reference_AntiKt4EMTopoAuxDyn_mpx;   //!
   TBranch        *b_HGamMET_Reference_AntiKt4EMTopoAuxDyn_mpy;   //!
   TBranch        *b_HGamMuonsInJets;   //!
   TBranch        *b_HGamMuonsInJetsAux_;   //!
   TBranch        *b_HGamEventInfo;   //!
   TBranch        *b_HGamEventInfoAux_;   //!
   TBranch        *b_HGamEventInfoAuxDyn_crossSectionBRfilterEff;   //!
   TBranch        *b_HGamEventInfoAuxDyn_yAbs_yy;   //!
   TBranch        *b_HGamEventInfoAuxDyn_pTt_yy;   //!
   TBranch        *b_HGamEventInfoAuxDyn_m_yy;   //!
   TBranch        *b_HGamEventInfoAuxDyn_passMeyCut;   //!
   TBranch        *b_HGamEventInfoAuxDyn_pT_yy;   //!
   TBranch        *b_HGamEventInfoAuxDyn_pT_y1;   //!
   TBranch        *b_HGamEventInfoAuxDyn_pT_y2;   //!
   TBranch        *b_HGamEventInfoAuxDyn_E_y1;   //!
   TBranch        *b_HGamEventInfoAuxDyn_E_y2;   //!
   TBranch        *b_HGamEventInfoAuxDyn_pT_hard;   //!
   TBranch        *b_HGamEventInfoAuxDyn_cosTS_yy;   //!
   TBranch        *b_HGamEventInfoAuxDyn_Dy_y_y;   //!
   TBranch        *b_HGamEventInfoAuxDyn_N_e;   //!
   TBranch        *b_HGamEventInfoAuxDyn_N_mu;   //!
   TBranch        *b_HGamEventInfoAuxDyn_N_j;   //!
   TBranch        *b_HGamEventInfoAuxDyn_N_j_central;   //!
   TBranch        *b_HGamEventInfoAuxDyn_N_j_central30;   //!
   TBranch        *b_HGamEventInfoAuxDyn_pT_j1;   //!
   TBranch        *b_HGamEventInfoAuxDyn_pT_j2;   //!
   TBranch        *b_HGamEventInfoAuxDyn_pT_jj;   //!
   TBranch        *b_HGamEventInfoAuxDyn_m_jj;   //!
   TBranch        *b_HGamEventInfoAuxDyn_Dy_j_j;   //!
   TBranch        *b_HGamEventInfoAuxDyn_Dy_yy_jj;   //!
   TBranch        *b_HGamEventInfoAuxDyn_Dphi_yy_jj;   //!
   TBranch        *b_HGamEventInfoAuxDyn_m_ee;   //!
   TBranch        *b_HGamEventInfoAuxDyn_m_mumu;   //!
   TBranch        *b_HGamEventInfoAuxDyn_DRmin_y_j;   //!
   TBranch        *b_HGamEventInfoAuxDyn_DR_y_y;   //!
   TBranch        *b_HGamEventInfoAuxDyn_Zepp;   //!
   TBranch        *b_HGamEventInfoAuxDyn_cosTS_yyjj;   //!
   TBranch        *b_HGamEventInfoAuxDyn_met_TST;   //!
   TBranch        *b_HGamEventInfoAuxDyn_sumet_TST;   //!
   TBranch        *b_HGamEventInfoAuxDyn_phi_TST;   //!
   TBranch        *b_HGamEventInfoAuxDyn_isPassedBasic;   //!
   TBranch        *b_HGamEventInfoAuxDyn_isPassed;   //!
   TBranch        *b_HGamEventInfoAuxDyn_isPassedJetEventClean;   //!
   TBranch        *b_HGamEventInfoAuxDyn_isDalitz;   //!
   TBranch        *b_HGamEventInfoAuxDyn_cutFlow;   //!
   TBranch        *b_HGamEventInfoAuxDyn_weightInitial;   //!
   TBranch        *b_HGamEventInfoAuxDyn_weight;   //!
   TBranch        *b_HGamEventInfoAuxDyn_vertexWeight;   //!
   TBranch        *b_HGamEventInfoAuxDyn_pileupWeight;   //!
   TBranch        *b_HGamEventInfoAuxDyn_weightCatCoup_dev;   //!
   TBranch        *b_HGamEventInfoAuxDyn_catCoup_dev;   //!
   TBranch        *b_HGamEventInfoAuxDyn_weightCatCoup_Moriond2016;   //!
   TBranch        *b_HGamEventInfoAuxDyn_catCoup_Moriond2016;   //!
   TBranch        *b_HGamEventInfoAuxDyn_numberOfPrimaryVertices;   //!
   TBranch        *b_HGamEventInfoAuxDyn_selectedVertexZ;   //!
   TBranch        *b_HGamEventInfoAuxDyn_hardestVertexZ;   //!
   TBranch        *b_HGamEventInfoAuxDyn_m_yy_resolution;   //!
   TBranch        *b_HGamEventInfoAuxDyn_zCommon;   //!
   TBranch        *b_HGamEventInfoAuxDyn_NLoosePhotons;   //!
   TBranch        *b_HGamEventInfoAuxDyn_truthVertexZ;   //!
   TBranch        *b_HGamEventInfoAuxDyn_N_j_btag;   //!
   TBranch        *b_HGamEventInfoAuxDyn_N_j_btag30;   //!
   TBranch        *b_HGamEventInfoAuxDyn_m_yy_hardestVertex;   //!
   TBranch        *b_HGamEventInfoAuxDyn_eventShapeDensity;   //!
   TBranch        *b_HGamEventInfoAuxDyn_m_yy_truthVertex;   //!
   TBranch        *b_HGamEventInfoAuxDyn_mu;   //!
   TBranch        *b_HGamEventInfoAuxDyn_m_yy_zCommon;   //!
   TBranch        *b_HGamEventInfoAuxDyn_isPassedPreselection;   //!
   TBranch        *b_HGamEventInfoAuxDyn_isPassedPID;   //!
   TBranch        *b_HGamEventInfoAuxDyn_isPassedIsolation;   //!
   TBranch        *b_HGamEventInfoAuxDyn_isPassedRelPtCuts;   //!
   TBranch        *b_HGamEventInfoAuxDyn_isPassedMassCut;   //!
   TBranch        *b_HGamEventInfoAuxDyn_isPassedIsolationLowHighMyy;   //!
   TBranch        *b_HGamEventInfoAuxDyn_isPassedRelPtCutsLowHighMyy;   //!
   TBranch        *b_HGamEventInfoAuxDyn_isPassedLowHighMyy;   //!
   TBranch        *b_HGamEventInfoAuxDyn_isPassedIsolationExotic;   //!
   TBranch        *b_HGamEventInfoAuxDyn_isPassedlPtCutsExotic;   //!
   TBranch        *b_HGamEventInfoAuxDyn_isPassedExotic;   //!
   TBranch        *b_HGamTruthPhotons;   //!
   TBranch        *b_HGamTruthPhotonsAux_;   //!
   TBranch        *b_HGamTruthPhotonsAuxDyn_isIsolated;   //!
   TBranch        *b_HGamTruthPhotonsAuxDyn_etcone20;   //!
   TBranch        *b_HGamTruthPhotonsAuxDyn_etcone40;   //!
   TBranch        *b_HGamTruthPhotonsAuxDyn_px;   //!
   TBranch        *b_HGamTruthPhotonsAuxDyn_ptcone20;   //!
   TBranch        *b_HGamTruthPhotonsAuxDyn_py;   //!
   TBranch        *b_HGamTruthPhotonsAuxDyn_ptcone40;   //!
   TBranch        *b_HGamTruthPhotonsAuxDyn_pz;   //!
   TBranch        *b_HGamTruthPhotonsAuxDyn_e;   //!
   TBranch        *b_HGamTruthPhotonsAuxDyn_pt;   //!
   TBranch        *b_HGamTruthPhotonsAuxDyn_eta;   //!
   TBranch        *b_HGamTruthPhotonsAuxDyn_m;   //!
   TBranch        *b_HGamTruthPhotonsAuxDyn_truthOrigin;   //!
   TBranch        *b_HGamTruthPhotonsAuxDyn_truthType;   //!
   TBranch        *b_HGamTruthElectrons;   //!
   TBranch        *b_HGamTruthElectronsAux_;   //!
   TBranch        *b_HGamTruthMuons;   //!
   TBranch        *b_HGamTruthMuonsAux_;   //!
   TBranch        *b_HGamAntiKt4TruthJets;   //!
   TBranch        *b_HGamAntiKt4TruthJetsAux_;   //!
   TBranch        *b_HGamAntiKt4TruthJetsAuxDyn_pt;   //!
   TBranch        *b_HGamAntiKt4TruthJetsAuxDyn_eta;   //!
   TBranch        *b_HGamAntiKt4TruthJetsAuxDyn_phi;   //!
   TBranch        *b_HGamAntiKt4TruthJetsAuxDyn_m;   //!
   TBranch        *b_HGamMET_Truth;   //!
   TBranch        *b_HGamMET_TruthAux_;   //!
   TBranch        *b_HGamMET_TruthAuxDyn_source;   //!
   TBranch        *b_HGamMET_TruthAuxDyn_sumet;   //!
   TBranch        *b_HGamMET_TruthAuxDyn_name;   //!
   TBranch        *b_HGamMET_TruthAuxDyn_mpx;   //!
   TBranch        *b_HGamMET_TruthAuxDyn_mpy;   //!
   TBranch        *b_HGamTruthHiggsBosons;   //!
   TBranch        *b_HGamTruthHiggsBosonsAux_;   //!
   TBranch        *b_HGamTruthEventInfo;   //!
   TBranch        *b_HGamTruthEventInfoAux_;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_pT_jj;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_m_jj;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_Dy_j_j;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_Dphi_yy_jj;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_m_ee;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_m_mumu;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_DRmin_y_j;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_DR_y_y;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_Zepp;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_cosTS_yyjj;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_pT_h1;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_pT_h2;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_y_h1;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_y_h2;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_isFiducial;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_m_h1;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_isFiducialKinOnly;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_m_h2;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_yAbs_yy;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_pTt_yy;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_m_yy;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_passMeyCut;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_pT_yy;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_pT_y1;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_pT_y2;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_E_y1;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_E_y2;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_pT_hard;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_TruthNonInt_met;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_cosTS_yy;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_TruthInt_sumet;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_isFiducialLowHighMyy;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_isFiducialExotic;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_Dy_y_y;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_N_e;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_N_mu;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_N_j;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_N_j_central;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_N_j_central30;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_pT_j1;   //!
   TBranch        *b_HGamTruthEventInfoAuxDyn_pT_j2;   //!
   TBranch        *b_EventInfo;   //!
   TBranch        *b_EventInfoAuxDyn_runNumber;   //!
   TBranch        *b_EventInfoAuxDyn_eventTypeBitmask;   //!
   TBranch        *b_EventInfoAuxDyn_eventNumber;   //!
   TBranch        *b_EventInfoAuxDyn_RandomRunNumber;   //!
   TBranch        *b_EventInfoAuxDyn_lumiBlock;   //!
   TBranch        *b_EventInfoAuxDyn_coreFlags;   //!
   TBranch        *b_EventInfoAuxDyn_mcChannelNumber;   //!
   TBranch        *b_EventInfoAuxDyn_averageInteractionsPerCrossing;   //!
   TBranch        *b_EventInfoAuxDyn_passTrig_HLT_g35_loose_g25_loose;   //!
   TBranch        *b_EventInfoAuxDyn_mcEventWeights;   //!
   TBranch        *b_EventInfoAuxDyn_passTrig_HLT_2g50_loose;   //!
   TBranch        *b_HGamPhotonsAuxDyn_truthLink;   //!
   TBranch        *b_HGamPhotonsAuxDyn_parentPdgId;   //!
   TBranch        *b_HGamPhotonsAuxDyn_pdgId;   //!
   TBranch        *b_HGamTruthPhotonsAuxDyn_recoLink;   //!
   TBranch        *b_HGamMuonsInJetsAuxDyn_ptvarcone20;   //!
   TBranch        *b_HGamMuonsInJetsAuxDyn_passIPCut;   //!
   TBranch        *b_HGamMuonsInJetsAuxDyn_muonType;   //!
   TBranch        *b_HGamMuonsInJetsAuxDyn_pt;   //!
   TBranch        *b_HGamMuonsInJetsAuxDyn_topoetcone20;   //!
   TBranch        *b_HGamMuonsInJetsAuxDyn_eta;   //!
   TBranch        *b_HGamMuonsInJetsAuxDyn_scaleFactor;   //!
   TBranch        *b_HGamMuonsInJetsAuxDyn_phi;   //!
   TBranch        *b_HGamMuonsInJetsAuxDyn_charge;   //!
   TBranch        *b_HGamTruthElectronsAuxDyn_px;   //!
   TBranch        *b_HGamTruthElectronsAuxDyn_py;   //!
   TBranch        *b_HGamTruthElectronsAuxDyn_pz;   //!
   TBranch        *b_HGamTruthElectronsAuxDyn_pt;   //!
   TBranch        *b_HGamTruthElectronsAuxDyn_eta;   //!
   TBranch        *b_HGamTruthElectronsAuxDyn_e;   //!
   TBranch        *b_HGamTruthElectronsAuxDyn_m;   //!
   TBranch        *b_HGamTruthElectronsAuxDyn_recoLink;   //!
   TBranch        *b_HGamTruthMuonsAuxDyn_px;   //!
   TBranch        *b_HGamTruthMuonsAuxDyn_py;   //!
   TBranch        *b_HGamTruthMuonsAuxDyn_pz;   //!
   TBranch        *b_HGamTruthMuonsAuxDyn_pt;   //!
   TBranch        *b_HGamTruthMuonsAuxDyn_eta;   //!
   TBranch        *b_HGamTruthMuonsAuxDyn_e;   //!
   TBranch        *b_HGamTruthMuonsAuxDyn_m;   //!
   TBranch        *b_HGamMuonsAuxDyn_ptvarcone20;   //!
   TBranch        *b_HGamMuonsAuxDyn_passIPCut;   //!
   TBranch        *b_HGamMuonsAuxDyn_muonType;   //!
   TBranch        *b_HGamMuonsAuxDyn_pt;   //!
   TBranch        *b_HGamMuonsAuxDyn_topoetcone20;   //!
   TBranch        *b_HGamMuonsAuxDyn_eta;   //!
   TBranch        *b_HGamMuonsAuxDyn_scaleFactor;   //!
   TBranch        *b_HGamMuonsAuxDyn_phi;   //!
   TBranch        *b_HGamMuonsAuxDyn_charge;   //!
   TBranch        *b_HGamElectronsAuxDyn_eta_s2;   //!
   TBranch        *b_HGamElectronsAuxDyn_ptvarcone20;   //!
   TBranch        *b_HGamElectronsAuxDyn_pt;   //!
   TBranch        *b_HGamElectronsAuxDyn_topoetcone20;   //!
   TBranch        *b_HGamElectronsAuxDyn_isTight;   //!
   TBranch        *b_HGamElectronsAuxDyn_eta;   //!
   TBranch        *b_HGamElectronsAuxDyn_scaleFactor;   //!
   TBranch        *b_HGamElectronsAuxDyn_phi;   //!
   TBranch        *b_HGamElectronsAuxDyn_charge;   //!
   TBranch        *b_HGamElectronsAuxDyn_m;   //!
   TBranch        *b_HGamElectronsAuxDyn_truthLink;   //!

   MxAOD(TTree *tree=0);
   virtual ~MxAOD();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef MxAOD_cxx
MxAOD::MxAOD(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("root://eosatlas//eos/atlas/atlascerngroupdisk/phys-higgs/HSG1/MxAOD/h011/mc_25ns/Sherpa_gamgam_2DP20_0-55.MxAOD.p2419.h011.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("root://eosatlas//eos/atlas/atlascerngroupdisk/phys-higgs/HSG1/MxAOD/h011/mc_25ns/Sherpa_gamgam_2DP20_0-55.MxAOD.p2419.h011.root");
      }
      f->GetObject("CollectionTree",tree);

   }
   Init(tree);
}

MxAOD::~MxAOD()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t MxAOD::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t MxAOD::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void MxAOD::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   HGamPhotons = 0;
   HGamPhotonsAux_ = 0;
   HGamPhotonsAuxDyn_topoetcone20 = 0;
   HGamPhotonsAuxDyn_eta_s2 = 0;
   HGamPhotonsAuxDyn_relEreso = 0;
   HGamPhotonsAuxDyn_topoetcone40 = 0;
   HGamPhotonsAuxDyn_ptcone20 = 0;
   HGamPhotonsAuxDyn_isTight = 0;
   HGamPhotonsAuxDyn_ptcone40 = 0;
   HGamPhotonsAuxDyn_conversionType = 0;
   HGamPhotonsAuxDyn_conversionRadius = 0;
   HGamPhotonsAuxDyn_truthOrigin = 0;
   HGamPhotonsAuxDyn_truthConvRadius = 0;
   HGamPhotonsAuxDyn_truthType = 0;
   HGamPhotonsAuxDyn_isTight_nofudge = 0;
   HGamPhotonsAuxDyn_isEMTight_nofudge = 0;
   HGamPhotonsAuxDyn_topoetcone20_DDcorrected = 0;
   HGamPhotonsAuxDyn_topoetcone40_DDcorrected = 0;
   HGamPhotonsAuxDyn_pt = 0;
   HGamPhotonsAuxDyn_eta = 0;
   HGamPhotonsAuxDyn_ratioE1E2 = 0;
   HGamPhotonsAuxDyn_isIsoFixedCutLoose = 0;
   HGamPhotonsAuxDyn_phi = 0;
   HGamPhotonsAuxDyn_isIsoFixedCutTight = 0;
   HGamPhotonsAuxDyn_m = 0;
   HGamPhotonsAuxDyn_isIsoFixedCutTightCaloOnly = 0;
   HGamPhotonsAuxDyn_isIsoFixedCutLooseCaloOnly = 0;
   HGamPhotonsAuxDyn_E0_raw = 0;
   HGamPhotonsAuxDyn_E1_raw = 0;
   HGamPhotonsAuxDyn_E2_raw = 0;
   HGamPhotonsAuxDyn_E3_raw = 0;
   HGamPhotonsAuxDyn_isEMTight = 0;
   HGamPhotonsAuxDyn_scaleFactor = 0;
   HGamElectrons = 0;
   HGamElectronsAux_ = 0;
   HGamAntiKt4EMTopoJets = 0;
   HGamAntiKt4EMTopoJetsAux_ = 0;
   HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_85 = 0;
   HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_85 = 0;
   HGamAntiKt4EMTopoJetsAuxDyn_Jvt = 0;
   HGamAntiKt4EMTopoJetsAuxDyn_DetectorEta = 0;
   HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_60 = 0;
   HGamAntiKt4EMTopoJetsAuxDyn_pt = 0;
   HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_60 = 0;
   HGamAntiKt4EMTopoJetsAuxDyn_eta = 0;
   HGamAntiKt4EMTopoJetsAuxDyn_phi = 0;
   HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_70 = 0;
   HGamAntiKt4EMTopoJetsAuxDyn_m = 0;
   HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_70 = 0;
   HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_77 = 0;
   HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_77 = 0;
   HGamMuons = 0;
   HGamMuonsAux_ = 0;
   HGamMET_Reference_AntiKt4EMTopo = 0;
   HGamMET_Reference_AntiKt4EMTopoAux_ = 0;
   HGamMET_Reference_AntiKt4EMTopoAuxDyn_source = 0;
   HGamMET_Reference_AntiKt4EMTopoAuxDyn_sumet = 0;
   HGamMET_Reference_AntiKt4EMTopoAuxDyn_name = 0;
   HGamMET_Reference_AntiKt4EMTopoAuxDyn_mpx = 0;
   HGamMET_Reference_AntiKt4EMTopoAuxDyn_mpy = 0;
   HGamMuonsInJets = 0;
   HGamMuonsInJetsAux_ = 0;
   HGamEventInfo = 0;
   HGamEventInfoAux_ = 0;
   HGamTruthPhotons = 0;
   HGamTruthPhotonsAux_ = 0;
   HGamTruthPhotonsAuxDyn_isIsolated = 0;
   HGamTruthPhotonsAuxDyn_etcone20 = 0;
   HGamTruthPhotonsAuxDyn_etcone40 = 0;
   HGamTruthPhotonsAuxDyn_px = 0;
   HGamTruthPhotonsAuxDyn_ptcone20 = 0;
   HGamTruthPhotonsAuxDyn_py = 0;
   HGamTruthPhotonsAuxDyn_ptcone40 = 0;
   HGamTruthPhotonsAuxDyn_pz = 0;
   HGamTruthPhotonsAuxDyn_e = 0;
   HGamTruthPhotonsAuxDyn_pt = 0;
   HGamTruthPhotonsAuxDyn_eta = 0;
   HGamTruthPhotonsAuxDyn_m = 0;
   HGamTruthPhotonsAuxDyn_truthOrigin = 0;
   HGamTruthPhotonsAuxDyn_truthType = 0;
   HGamTruthElectrons = 0;
   HGamTruthElectronsAux_ = 0;
   HGamTruthMuons = 0;
   HGamTruthMuonsAux_ = 0;
   HGamAntiKt4TruthJets = 0;
   HGamAntiKt4TruthJetsAux_ = 0;
   HGamAntiKt4TruthJetsAuxDyn_pt = 0;
   HGamAntiKt4TruthJetsAuxDyn_eta = 0;
   HGamAntiKt4TruthJetsAuxDyn_phi = 0;
   HGamAntiKt4TruthJetsAuxDyn_m = 0;
   HGamMET_Truth = 0;
   HGamMET_TruthAux_ = 0;
   HGamMET_TruthAuxDyn_source = 0;
   HGamMET_TruthAuxDyn_sumet = 0;
   HGamMET_TruthAuxDyn_name = 0;
   HGamMET_TruthAuxDyn_mpx = 0;
   HGamMET_TruthAuxDyn_mpy = 0;
   HGamTruthHiggsBosons = 0;
   HGamTruthHiggsBosonsAux_ = 0;
   HGamTruthEventInfo = 0;
   HGamTruthEventInfoAux_ = 0;
   EventInfo = 0;
   EventInfoAuxDyn_mcEventWeights = 0;
   HGamPhotonsAuxDyn_truthLink = 0;
   HGamPhotonsAuxDyn_parentPdgId = 0;
   HGamPhotonsAuxDyn_pdgId = 0;
   HGamTruthPhotonsAuxDyn_recoLink = 0;
   HGamMuonsInJetsAuxDyn_ptvarcone20 = 0;
   HGamMuonsInJetsAuxDyn_passIPCut = 0;
   HGamMuonsInJetsAuxDyn_muonType = 0;
   HGamMuonsInJetsAuxDyn_pt = 0;
   HGamMuonsInJetsAuxDyn_topoetcone20 = 0;
   HGamMuonsInJetsAuxDyn_eta = 0;
   HGamMuonsInJetsAuxDyn_scaleFactor = 0;
   HGamMuonsInJetsAuxDyn_phi = 0;
   HGamMuonsInJetsAuxDyn_charge = 0;
   HGamTruthElectronsAuxDyn_px = 0;
   HGamTruthElectronsAuxDyn_py = 0;
   HGamTruthElectronsAuxDyn_pz = 0;
   HGamTruthElectronsAuxDyn_pt = 0;
   HGamTruthElectronsAuxDyn_eta = 0;
   HGamTruthElectronsAuxDyn_e = 0;
   HGamTruthElectronsAuxDyn_m = 0;
   HGamTruthElectronsAuxDyn_recoLink = 0;
   HGamTruthMuonsAuxDyn_px = 0;
   HGamTruthMuonsAuxDyn_py = 0;
   HGamTruthMuonsAuxDyn_pz = 0;
   HGamTruthMuonsAuxDyn_pt = 0;
   HGamTruthMuonsAuxDyn_eta = 0;
   HGamTruthMuonsAuxDyn_e = 0;
   HGamTruthMuonsAuxDyn_m = 0;
   HGamMuonsAuxDyn_ptvarcone20 = 0;
   HGamMuonsAuxDyn_passIPCut = 0;
   HGamMuonsAuxDyn_muonType = 0;
   HGamMuonsAuxDyn_pt = 0;
   HGamMuonsAuxDyn_topoetcone20 = 0;
   HGamMuonsAuxDyn_eta = 0;
   HGamMuonsAuxDyn_scaleFactor = 0;
   HGamMuonsAuxDyn_phi = 0;
   HGamMuonsAuxDyn_charge = 0;
   HGamElectronsAuxDyn_eta_s2 = 0;
   HGamElectronsAuxDyn_ptvarcone20 = 0;
   HGamElectronsAuxDyn_pt = 0;
   HGamElectronsAuxDyn_topoetcone20 = 0;
   HGamElectronsAuxDyn_isTight = 0;
   HGamElectronsAuxDyn_eta = 0;
   HGamElectronsAuxDyn_scaleFactor = 0;
   HGamElectronsAuxDyn_phi = 0;
   HGamElectronsAuxDyn_charge = 0;
   HGamElectronsAuxDyn_m = 0;
   HGamElectronsAuxDyn_truthLink = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("HGamPhotons", &HGamPhotons, &b_HGamPhotons);
   fChain->SetBranchAddress("HGamPhotonsAux.", &HGamPhotonsAux_, &b_HGamPhotonsAux_);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.topoetcone20", &HGamPhotonsAuxDyn_topoetcone20, &b_HGamPhotonsAuxDyn_topoetcone20);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.eta_s2", &HGamPhotonsAuxDyn_eta_s2, &b_HGamPhotonsAuxDyn_eta_s2);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.relEreso", &HGamPhotonsAuxDyn_relEreso, &b_HGamPhotonsAuxDyn_relEreso);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.topoetcone40", &HGamPhotonsAuxDyn_topoetcone40, &b_HGamPhotonsAuxDyn_topoetcone40);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.ptcone20", &HGamPhotonsAuxDyn_ptcone20, &b_HGamPhotonsAuxDyn_ptcone20);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.isTight", &HGamPhotonsAuxDyn_isTight, &b_HGamPhotonsAuxDyn_isTight);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.ptcone40", &HGamPhotonsAuxDyn_ptcone40, &b_HGamPhotonsAuxDyn_ptcone40);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.conversionType", &HGamPhotonsAuxDyn_conversionType, &b_HGamPhotonsAuxDyn_conversionType);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.conversionRadius", &HGamPhotonsAuxDyn_conversionRadius, &b_HGamPhotonsAuxDyn_conversionRadius);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.truthOrigin", &HGamPhotonsAuxDyn_truthOrigin, &b_HGamPhotonsAuxDyn_truthOrigin);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.truthConvRadius", &HGamPhotonsAuxDyn_truthConvRadius, &b_HGamPhotonsAuxDyn_truthConvRadius);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.truthType", &HGamPhotonsAuxDyn_truthType, &b_HGamPhotonsAuxDyn_truthType);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.isTight_nofudge", &HGamPhotonsAuxDyn_isTight_nofudge, &b_HGamPhotonsAuxDyn_isTight_nofudge);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.isEMTight_nofudge", &HGamPhotonsAuxDyn_isEMTight_nofudge, &b_HGamPhotonsAuxDyn_isEMTight_nofudge);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.topoetcone20_DDcorrected", &HGamPhotonsAuxDyn_topoetcone20_DDcorrected, &b_HGamPhotonsAuxDyn_topoetcone20_DDcorrected);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.topoetcone40_DDcorrected", &HGamPhotonsAuxDyn_topoetcone40_DDcorrected, &b_HGamPhotonsAuxDyn_topoetcone40_DDcorrected);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.pt", &HGamPhotonsAuxDyn_pt, &b_HGamPhotonsAuxDyn_pt);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.eta", &HGamPhotonsAuxDyn_eta, &b_HGamPhotonsAuxDyn_eta);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.ratioE1E2", &HGamPhotonsAuxDyn_ratioE1E2, &b_HGamPhotonsAuxDyn_ratioE1E2);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.isIsoFixedCutLoose", &HGamPhotonsAuxDyn_isIsoFixedCutLoose, &b_HGamPhotonsAuxDyn_isIsoFixedCutLoose);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.phi", &HGamPhotonsAuxDyn_phi, &b_HGamPhotonsAuxDyn_phi);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.isIsoFixedCutTight", &HGamPhotonsAuxDyn_isIsoFixedCutTight, &b_HGamPhotonsAuxDyn_isIsoFixedCutTight);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.m", &HGamPhotonsAuxDyn_m, &b_HGamPhotonsAuxDyn_m);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.isIsoFixedCutTightCaloOnly", &HGamPhotonsAuxDyn_isIsoFixedCutTightCaloOnly, &b_HGamPhotonsAuxDyn_isIsoFixedCutTightCaloOnly);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.isIsoFixedCutLooseCaloOnly", &HGamPhotonsAuxDyn_isIsoFixedCutLooseCaloOnly, &b_HGamPhotonsAuxDyn_isIsoFixedCutLooseCaloOnly);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.E0_raw", &HGamPhotonsAuxDyn_E0_raw, &b_HGamPhotonsAuxDyn_E0_raw);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.E1_raw", &HGamPhotonsAuxDyn_E1_raw, &b_HGamPhotonsAuxDyn_E1_raw);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.E2_raw", &HGamPhotonsAuxDyn_E2_raw, &b_HGamPhotonsAuxDyn_E2_raw);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.E3_raw", &HGamPhotonsAuxDyn_E3_raw, &b_HGamPhotonsAuxDyn_E3_raw);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.isEMTight", &HGamPhotonsAuxDyn_isEMTight, &b_HGamPhotonsAuxDyn_isEMTight);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.scaleFactor", &HGamPhotonsAuxDyn_scaleFactor, &b_HGamPhotonsAuxDyn_scaleFactor);
   fChain->SetBranchAddress("HGamElectrons", &HGamElectrons, &b_HGamElectrons);
   fChain->SetBranchAddress("HGamElectronsAux.", &HGamElectronsAux_, &b_HGamElectronsAux_);
   fChain->SetBranchAddress("HGamAntiKt4EMTopoJets", &HGamAntiKt4EMTopoJets, &b_HGamAntiKt4EMTopoJets);
   fChain->SetBranchAddress("HGamAntiKt4EMTopoJetsAux.", &HGamAntiKt4EMTopoJetsAux_, &b_HGamAntiKt4EMTopoJetsAux_);
   fChain->SetBranchAddress("HGamAntiKt4EMTopoJetsAuxDyn.Eff_MV2c20_FixedCutBEff_85", &HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_85, &b_HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_85);
   fChain->SetBranchAddress("HGamAntiKt4EMTopoJetsAuxDyn.SF_MV2c20_FixedCutBEff_85", &HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_85, &b_HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_85);
   fChain->SetBranchAddress("HGamAntiKt4EMTopoJetsAuxDyn.Jvt", &HGamAntiKt4EMTopoJetsAuxDyn_Jvt, &b_HGamAntiKt4EMTopoJetsAuxDyn_Jvt);
   fChain->SetBranchAddress("HGamAntiKt4EMTopoJetsAuxDyn.DetectorEta", &HGamAntiKt4EMTopoJetsAuxDyn_DetectorEta, &b_HGamAntiKt4EMTopoJetsAuxDyn_DetectorEta);
   fChain->SetBranchAddress("HGamAntiKt4EMTopoJetsAuxDyn.Eff_MV2c20_FixedCutBEff_60", &HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_60, &b_HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_60);
   fChain->SetBranchAddress("HGamAntiKt4EMTopoJetsAuxDyn.pt", &HGamAntiKt4EMTopoJetsAuxDyn_pt, &b_HGamAntiKt4EMTopoJetsAuxDyn_pt);
   fChain->SetBranchAddress("HGamAntiKt4EMTopoJetsAuxDyn.SF_MV2c20_FixedCutBEff_60", &HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_60, &b_HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_60);
   fChain->SetBranchAddress("HGamAntiKt4EMTopoJetsAuxDyn.eta", &HGamAntiKt4EMTopoJetsAuxDyn_eta, &b_HGamAntiKt4EMTopoJetsAuxDyn_eta);
   fChain->SetBranchAddress("HGamAntiKt4EMTopoJetsAuxDyn.phi", &HGamAntiKt4EMTopoJetsAuxDyn_phi, &b_HGamAntiKt4EMTopoJetsAuxDyn_phi);
   fChain->SetBranchAddress("HGamAntiKt4EMTopoJetsAuxDyn.Eff_MV2c20_FixedCutBEff_70", &HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_70, &b_HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_70);
   fChain->SetBranchAddress("HGamAntiKt4EMTopoJetsAuxDyn.m", &HGamAntiKt4EMTopoJetsAuxDyn_m, &b_HGamAntiKt4EMTopoJetsAuxDyn_m);
   fChain->SetBranchAddress("HGamAntiKt4EMTopoJetsAuxDyn.SF_MV2c20_FixedCutBEff_70", &HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_70, &b_HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_70);
   fChain->SetBranchAddress("HGamAntiKt4EMTopoJetsAuxDyn.Eff_MV2c20_FixedCutBEff_77", &HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_77, &b_HGamAntiKt4EMTopoJetsAuxDyn_Eff_MV2c20_FixedCutBEff_77);
   fChain->SetBranchAddress("HGamAntiKt4EMTopoJetsAuxDyn.SF_MV2c20_FixedCutBEff_77", &HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_77, &b_HGamAntiKt4EMTopoJetsAuxDyn_SF_MV2c20_FixedCutBEff_77);
   fChain->SetBranchAddress("HGamMuons", &HGamMuons, &b_HGamMuons);
   fChain->SetBranchAddress("HGamMuonsAux.", &HGamMuonsAux_, &b_HGamMuonsAux_);
   fChain->SetBranchAddress("HGamMET_Reference_AntiKt4EMTopo", &HGamMET_Reference_AntiKt4EMTopo, &b_HGamMET_Reference_AntiKt4EMTopo);
   fChain->SetBranchAddress("HGamMET_Reference_AntiKt4EMTopoAux.", &HGamMET_Reference_AntiKt4EMTopoAux_, &b_HGamMET_Reference_AntiKt4EMTopoAux_);
   fChain->SetBranchAddress("HGamMET_Reference_AntiKt4EMTopoAuxDyn.source", &HGamMET_Reference_AntiKt4EMTopoAuxDyn_source, &b_HGamMET_Reference_AntiKt4EMTopoAuxDyn_source);
   fChain->SetBranchAddress("HGamMET_Reference_AntiKt4EMTopoAuxDyn.sumet", &HGamMET_Reference_AntiKt4EMTopoAuxDyn_sumet, &b_HGamMET_Reference_AntiKt4EMTopoAuxDyn_sumet);
   fChain->SetBranchAddress("HGamMET_Reference_AntiKt4EMTopoAuxDyn.name", &HGamMET_Reference_AntiKt4EMTopoAuxDyn_name, &b_HGamMET_Reference_AntiKt4EMTopoAuxDyn_name);
   fChain->SetBranchAddress("HGamMET_Reference_AntiKt4EMTopoAuxDyn.mpx", &HGamMET_Reference_AntiKt4EMTopoAuxDyn_mpx, &b_HGamMET_Reference_AntiKt4EMTopoAuxDyn_mpx);
   fChain->SetBranchAddress("HGamMET_Reference_AntiKt4EMTopoAuxDyn.mpy", &HGamMET_Reference_AntiKt4EMTopoAuxDyn_mpy, &b_HGamMET_Reference_AntiKt4EMTopoAuxDyn_mpy);
   fChain->SetBranchAddress("HGamMuonsInJets", &HGamMuonsInJets, &b_HGamMuonsInJets);
   fChain->SetBranchAddress("HGamMuonsInJetsAux.", &HGamMuonsInJetsAux_, &b_HGamMuonsInJetsAux_);
   fChain->SetBranchAddress("HGamEventInfo", &HGamEventInfo, &b_HGamEventInfo);
   fChain->SetBranchAddress("HGamEventInfoAux.", &HGamEventInfoAux_, &b_HGamEventInfoAux_);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.crossSectionBRfilterEff", &HGamEventInfoAuxDyn_crossSectionBRfilterEff, &b_HGamEventInfoAuxDyn_crossSectionBRfilterEff);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.yAbs_yy", &HGamEventInfoAuxDyn_yAbs_yy, &b_HGamEventInfoAuxDyn_yAbs_yy);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.pTt_yy", &HGamEventInfoAuxDyn_pTt_yy, &b_HGamEventInfoAuxDyn_pTt_yy);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.m_yy", &HGamEventInfoAuxDyn_m_yy, &b_HGamEventInfoAuxDyn_m_yy);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.passMeyCut", &HGamEventInfoAuxDyn_passMeyCut, &b_HGamEventInfoAuxDyn_passMeyCut);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.pT_yy", &HGamEventInfoAuxDyn_pT_yy, &b_HGamEventInfoAuxDyn_pT_yy);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.pT_y1", &HGamEventInfoAuxDyn_pT_y1, &b_HGamEventInfoAuxDyn_pT_y1);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.pT_y2", &HGamEventInfoAuxDyn_pT_y2, &b_HGamEventInfoAuxDyn_pT_y2);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.E_y1", &HGamEventInfoAuxDyn_E_y1, &b_HGamEventInfoAuxDyn_E_y1);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.E_y2", &HGamEventInfoAuxDyn_E_y2, &b_HGamEventInfoAuxDyn_E_y2);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.pT_hard", &HGamEventInfoAuxDyn_pT_hard, &b_HGamEventInfoAuxDyn_pT_hard);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.cosTS_yy", &HGamEventInfoAuxDyn_cosTS_yy, &b_HGamEventInfoAuxDyn_cosTS_yy);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.Dy_y_y", &HGamEventInfoAuxDyn_Dy_y_y, &b_HGamEventInfoAuxDyn_Dy_y_y);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.N_e", &HGamEventInfoAuxDyn_N_e, &b_HGamEventInfoAuxDyn_N_e);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.N_mu", &HGamEventInfoAuxDyn_N_mu, &b_HGamEventInfoAuxDyn_N_mu);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.N_j", &HGamEventInfoAuxDyn_N_j, &b_HGamEventInfoAuxDyn_N_j);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.N_j_central", &HGamEventInfoAuxDyn_N_j_central, &b_HGamEventInfoAuxDyn_N_j_central);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.N_j_central30", &HGamEventInfoAuxDyn_N_j_central30, &b_HGamEventInfoAuxDyn_N_j_central30);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.pT_j1", &HGamEventInfoAuxDyn_pT_j1, &b_HGamEventInfoAuxDyn_pT_j1);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.pT_j2", &HGamEventInfoAuxDyn_pT_j2, &b_HGamEventInfoAuxDyn_pT_j2);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.pT_jj", &HGamEventInfoAuxDyn_pT_jj, &b_HGamEventInfoAuxDyn_pT_jj);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.m_jj", &HGamEventInfoAuxDyn_m_jj, &b_HGamEventInfoAuxDyn_m_jj);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.Dy_j_j", &HGamEventInfoAuxDyn_Dy_j_j, &b_HGamEventInfoAuxDyn_Dy_j_j);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.Dy_yy_jj", &HGamEventInfoAuxDyn_Dy_yy_jj, &b_HGamEventInfoAuxDyn_Dy_yy_jj);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.Dphi_yy_jj", &HGamEventInfoAuxDyn_Dphi_yy_jj, &b_HGamEventInfoAuxDyn_Dphi_yy_jj);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.m_ee", &HGamEventInfoAuxDyn_m_ee, &b_HGamEventInfoAuxDyn_m_ee);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.m_mumu", &HGamEventInfoAuxDyn_m_mumu, &b_HGamEventInfoAuxDyn_m_mumu);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.DRmin_y_j", &HGamEventInfoAuxDyn_DRmin_y_j, &b_HGamEventInfoAuxDyn_DRmin_y_j);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.DR_y_y", &HGamEventInfoAuxDyn_DR_y_y, &b_HGamEventInfoAuxDyn_DR_y_y);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.Zepp", &HGamEventInfoAuxDyn_Zepp, &b_HGamEventInfoAuxDyn_Zepp);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.cosTS_yyjj", &HGamEventInfoAuxDyn_cosTS_yyjj, &b_HGamEventInfoAuxDyn_cosTS_yyjj);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.met_TST", &HGamEventInfoAuxDyn_met_TST, &b_HGamEventInfoAuxDyn_met_TST);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.sumet_TST", &HGamEventInfoAuxDyn_sumet_TST, &b_HGamEventInfoAuxDyn_sumet_TST);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.phi_TST", &HGamEventInfoAuxDyn_phi_TST, &b_HGamEventInfoAuxDyn_phi_TST);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.isPassedBasic", &HGamEventInfoAuxDyn_isPassedBasic, &b_HGamEventInfoAuxDyn_isPassedBasic);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.isPassed", &HGamEventInfoAuxDyn_isPassed, &b_HGamEventInfoAuxDyn_isPassed);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.isPassedJetEventClean", &HGamEventInfoAuxDyn_isPassedJetEventClean, &b_HGamEventInfoAuxDyn_isPassedJetEventClean);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.isDalitz", &HGamEventInfoAuxDyn_isDalitz, &b_HGamEventInfoAuxDyn_isDalitz);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.cutFlow", &HGamEventInfoAuxDyn_cutFlow, &b_HGamEventInfoAuxDyn_cutFlow);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.weightInitial", &HGamEventInfoAuxDyn_weightInitial, &b_HGamEventInfoAuxDyn_weightInitial);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.weight", &HGamEventInfoAuxDyn_weight, &b_HGamEventInfoAuxDyn_weight);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.vertexWeight", &HGamEventInfoAuxDyn_vertexWeight, &b_HGamEventInfoAuxDyn_vertexWeight);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.pileupWeight", &HGamEventInfoAuxDyn_pileupWeight, &b_HGamEventInfoAuxDyn_pileupWeight);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.weightCatCoup_dev", &HGamEventInfoAuxDyn_weightCatCoup_dev, &b_HGamEventInfoAuxDyn_weightCatCoup_dev);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.catCoup_dev", &HGamEventInfoAuxDyn_catCoup_dev, &b_HGamEventInfoAuxDyn_catCoup_dev);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.weightCatCoup_Moriond2016", &HGamEventInfoAuxDyn_weightCatCoup_Moriond2016, &b_HGamEventInfoAuxDyn_weightCatCoup_Moriond2016);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.catCoup_Moriond2016", &HGamEventInfoAuxDyn_catCoup_Moriond2016, &b_HGamEventInfoAuxDyn_catCoup_Moriond2016);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.numberOfPrimaryVertices", &HGamEventInfoAuxDyn_numberOfPrimaryVertices, &b_HGamEventInfoAuxDyn_numberOfPrimaryVertices);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.selectedVertexZ", &HGamEventInfoAuxDyn_selectedVertexZ, &b_HGamEventInfoAuxDyn_selectedVertexZ);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.hardestVertexZ", &HGamEventInfoAuxDyn_hardestVertexZ, &b_HGamEventInfoAuxDyn_hardestVertexZ);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.m_yy_resolution", &HGamEventInfoAuxDyn_m_yy_resolution, &b_HGamEventInfoAuxDyn_m_yy_resolution);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.zCommon", &HGamEventInfoAuxDyn_zCommon, &b_HGamEventInfoAuxDyn_zCommon);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.NLoosePhotons", &HGamEventInfoAuxDyn_NLoosePhotons, &b_HGamEventInfoAuxDyn_NLoosePhotons);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.truthVertexZ", &HGamEventInfoAuxDyn_truthVertexZ, &b_HGamEventInfoAuxDyn_truthVertexZ);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.N_j_btag", &HGamEventInfoAuxDyn_N_j_btag, &b_HGamEventInfoAuxDyn_N_j_btag);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.N_j_btag30", &HGamEventInfoAuxDyn_N_j_btag30, &b_HGamEventInfoAuxDyn_N_j_btag30);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.m_yy_hardestVertex", &HGamEventInfoAuxDyn_m_yy_hardestVertex, &b_HGamEventInfoAuxDyn_m_yy_hardestVertex);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.eventShapeDensity", &HGamEventInfoAuxDyn_eventShapeDensity, &b_HGamEventInfoAuxDyn_eventShapeDensity);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.m_yy_truthVertex", &HGamEventInfoAuxDyn_m_yy_truthVertex, &b_HGamEventInfoAuxDyn_m_yy_truthVertex);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.mu", &HGamEventInfoAuxDyn_mu, &b_HGamEventInfoAuxDyn_mu);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.m_yy_zCommon", &HGamEventInfoAuxDyn_m_yy_zCommon, &b_HGamEventInfoAuxDyn_m_yy_zCommon);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.isPassedPreselection", &HGamEventInfoAuxDyn_isPassedPreselection, &b_HGamEventInfoAuxDyn_isPassedPreselection);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.isPassedPID", &HGamEventInfoAuxDyn_isPassedPID, &b_HGamEventInfoAuxDyn_isPassedPID);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.isPassedIsolation", &HGamEventInfoAuxDyn_isPassedIsolation, &b_HGamEventInfoAuxDyn_isPassedIsolation);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.isPassedRelPtCuts", &HGamEventInfoAuxDyn_isPassedRelPtCuts, &b_HGamEventInfoAuxDyn_isPassedRelPtCuts);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.isPassedMassCut", &HGamEventInfoAuxDyn_isPassedMassCut, &b_HGamEventInfoAuxDyn_isPassedMassCut);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.isPassedIsolationLowHighMyy", &HGamEventInfoAuxDyn_isPassedIsolationLowHighMyy, &b_HGamEventInfoAuxDyn_isPassedIsolationLowHighMyy);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.isPassedRelPtCutsLowHighMyy", &HGamEventInfoAuxDyn_isPassedRelPtCutsLowHighMyy, &b_HGamEventInfoAuxDyn_isPassedRelPtCutsLowHighMyy);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.isPassedLowHighMyy", &HGamEventInfoAuxDyn_isPassedLowHighMyy, &b_HGamEventInfoAuxDyn_isPassedLowHighMyy);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.isPassedIsolationExotic", &HGamEventInfoAuxDyn_isPassedIsolationExotic, &b_HGamEventInfoAuxDyn_isPassedIsolationExotic);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.isPassedlPtCutsExotic", &HGamEventInfoAuxDyn_isPassedlPtCutsExotic, &b_HGamEventInfoAuxDyn_isPassedlPtCutsExotic);
   fChain->SetBranchAddress("HGamEventInfoAuxDyn.isPassedExotic", &HGamEventInfoAuxDyn_isPassedExotic, &b_HGamEventInfoAuxDyn_isPassedExotic);
   fChain->SetBranchAddress("HGamTruthPhotons", &HGamTruthPhotons, &b_HGamTruthPhotons);
   fChain->SetBranchAddress("HGamTruthPhotonsAux.", &HGamTruthPhotonsAux_, &b_HGamTruthPhotonsAux_);
   fChain->SetBranchAddress("HGamTruthPhotonsAuxDyn.isIsolated", &HGamTruthPhotonsAuxDyn_isIsolated, &b_HGamTruthPhotonsAuxDyn_isIsolated);
   fChain->SetBranchAddress("HGamTruthPhotonsAuxDyn.etcone20", &HGamTruthPhotonsAuxDyn_etcone20, &b_HGamTruthPhotonsAuxDyn_etcone20);
   fChain->SetBranchAddress("HGamTruthPhotonsAuxDyn.etcone40", &HGamTruthPhotonsAuxDyn_etcone40, &b_HGamTruthPhotonsAuxDyn_etcone40);
   fChain->SetBranchAddress("HGamTruthPhotonsAuxDyn.px", &HGamTruthPhotonsAuxDyn_px, &b_HGamTruthPhotonsAuxDyn_px);
   fChain->SetBranchAddress("HGamTruthPhotonsAuxDyn.ptcone20", &HGamTruthPhotonsAuxDyn_ptcone20, &b_HGamTruthPhotonsAuxDyn_ptcone20);
   fChain->SetBranchAddress("HGamTruthPhotonsAuxDyn.py", &HGamTruthPhotonsAuxDyn_py, &b_HGamTruthPhotonsAuxDyn_py);
   fChain->SetBranchAddress("HGamTruthPhotonsAuxDyn.ptcone40", &HGamTruthPhotonsAuxDyn_ptcone40, &b_HGamTruthPhotonsAuxDyn_ptcone40);
   fChain->SetBranchAddress("HGamTruthPhotonsAuxDyn.pz", &HGamTruthPhotonsAuxDyn_pz, &b_HGamTruthPhotonsAuxDyn_pz);
   fChain->SetBranchAddress("HGamTruthPhotonsAuxDyn.e", &HGamTruthPhotonsAuxDyn_e, &b_HGamTruthPhotonsAuxDyn_e);
   fChain->SetBranchAddress("HGamTruthPhotonsAuxDyn.pt", &HGamTruthPhotonsAuxDyn_pt, &b_HGamTruthPhotonsAuxDyn_pt);
   fChain->SetBranchAddress("HGamTruthPhotonsAuxDyn.eta", &HGamTruthPhotonsAuxDyn_eta, &b_HGamTruthPhotonsAuxDyn_eta);
   fChain->SetBranchAddress("HGamTruthPhotonsAuxDyn.m", &HGamTruthPhotonsAuxDyn_m, &b_HGamTruthPhotonsAuxDyn_m);
   fChain->SetBranchAddress("HGamTruthPhotonsAuxDyn.truthOrigin", &HGamTruthPhotonsAuxDyn_truthOrigin, &b_HGamTruthPhotonsAuxDyn_truthOrigin);
   fChain->SetBranchAddress("HGamTruthPhotonsAuxDyn.truthType", &HGamTruthPhotonsAuxDyn_truthType, &b_HGamTruthPhotonsAuxDyn_truthType);
   fChain->SetBranchAddress("HGamTruthElectrons", &HGamTruthElectrons, &b_HGamTruthElectrons);
   fChain->SetBranchAddress("HGamTruthElectronsAux.", &HGamTruthElectronsAux_, &b_HGamTruthElectronsAux_);
   fChain->SetBranchAddress("HGamTruthMuons", &HGamTruthMuons, &b_HGamTruthMuons);
   fChain->SetBranchAddress("HGamTruthMuonsAux.", &HGamTruthMuonsAux_, &b_HGamTruthMuonsAux_);
   fChain->SetBranchAddress("HGamAntiKt4TruthJets", &HGamAntiKt4TruthJets, &b_HGamAntiKt4TruthJets);
   fChain->SetBranchAddress("HGamAntiKt4TruthJetsAux.", &HGamAntiKt4TruthJetsAux_, &b_HGamAntiKt4TruthJetsAux_);
   fChain->SetBranchAddress("HGamAntiKt4TruthJetsAuxDyn.pt", &HGamAntiKt4TruthJetsAuxDyn_pt, &b_HGamAntiKt4TruthJetsAuxDyn_pt);
   fChain->SetBranchAddress("HGamAntiKt4TruthJetsAuxDyn.eta", &HGamAntiKt4TruthJetsAuxDyn_eta, &b_HGamAntiKt4TruthJetsAuxDyn_eta);
   fChain->SetBranchAddress("HGamAntiKt4TruthJetsAuxDyn.phi", &HGamAntiKt4TruthJetsAuxDyn_phi, &b_HGamAntiKt4TruthJetsAuxDyn_phi);
   fChain->SetBranchAddress("HGamAntiKt4TruthJetsAuxDyn.m", &HGamAntiKt4TruthJetsAuxDyn_m, &b_HGamAntiKt4TruthJetsAuxDyn_m);
   fChain->SetBranchAddress("HGamMET_Truth", &HGamMET_Truth, &b_HGamMET_Truth);
   fChain->SetBranchAddress("HGamMET_TruthAux.", &HGamMET_TruthAux_, &b_HGamMET_TruthAux_);
   fChain->SetBranchAddress("HGamMET_TruthAuxDyn.source", &HGamMET_TruthAuxDyn_source, &b_HGamMET_TruthAuxDyn_source);
   fChain->SetBranchAddress("HGamMET_TruthAuxDyn.sumet", &HGamMET_TruthAuxDyn_sumet, &b_HGamMET_TruthAuxDyn_sumet);
   fChain->SetBranchAddress("HGamMET_TruthAuxDyn.name", &HGamMET_TruthAuxDyn_name, &b_HGamMET_TruthAuxDyn_name);
   fChain->SetBranchAddress("HGamMET_TruthAuxDyn.mpx", &HGamMET_TruthAuxDyn_mpx, &b_HGamMET_TruthAuxDyn_mpx);
   fChain->SetBranchAddress("HGamMET_TruthAuxDyn.mpy", &HGamMET_TruthAuxDyn_mpy, &b_HGamMET_TruthAuxDyn_mpy);
   fChain->SetBranchAddress("HGamTruthHiggsBosons", &HGamTruthHiggsBosons, &b_HGamTruthHiggsBosons);
   fChain->SetBranchAddress("HGamTruthHiggsBosonsAux.", &HGamTruthHiggsBosonsAux_, &b_HGamTruthHiggsBosonsAux_);
   fChain->SetBranchAddress("HGamTruthEventInfo", &HGamTruthEventInfo, &b_HGamTruthEventInfo);
   fChain->SetBranchAddress("HGamTruthEventInfoAux.", &HGamTruthEventInfoAux_, &b_HGamTruthEventInfoAux_);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.pT_jj", &HGamTruthEventInfoAuxDyn_pT_jj, &b_HGamTruthEventInfoAuxDyn_pT_jj);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.m_jj", &HGamTruthEventInfoAuxDyn_m_jj, &b_HGamTruthEventInfoAuxDyn_m_jj);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.Dy_j_j", &HGamTruthEventInfoAuxDyn_Dy_j_j, &b_HGamTruthEventInfoAuxDyn_Dy_j_j);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.Dphi_yy_jj", &HGamTruthEventInfoAuxDyn_Dphi_yy_jj, &b_HGamTruthEventInfoAuxDyn_Dphi_yy_jj);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.m_ee", &HGamTruthEventInfoAuxDyn_m_ee, &b_HGamTruthEventInfoAuxDyn_m_ee);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.m_mumu", &HGamTruthEventInfoAuxDyn_m_mumu, &b_HGamTruthEventInfoAuxDyn_m_mumu);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.DRmin_y_j", &HGamTruthEventInfoAuxDyn_DRmin_y_j, &b_HGamTruthEventInfoAuxDyn_DRmin_y_j);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.DR_y_y", &HGamTruthEventInfoAuxDyn_DR_y_y, &b_HGamTruthEventInfoAuxDyn_DR_y_y);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.Zepp", &HGamTruthEventInfoAuxDyn_Zepp, &b_HGamTruthEventInfoAuxDyn_Zepp);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.cosTS_yyjj", &HGamTruthEventInfoAuxDyn_cosTS_yyjj, &b_HGamTruthEventInfoAuxDyn_cosTS_yyjj);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.pT_h1", &HGamTruthEventInfoAuxDyn_pT_h1, &b_HGamTruthEventInfoAuxDyn_pT_h1);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.pT_h2", &HGamTruthEventInfoAuxDyn_pT_h2, &b_HGamTruthEventInfoAuxDyn_pT_h2);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.y_h1", &HGamTruthEventInfoAuxDyn_y_h1, &b_HGamTruthEventInfoAuxDyn_y_h1);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.y_h2", &HGamTruthEventInfoAuxDyn_y_h2, &b_HGamTruthEventInfoAuxDyn_y_h2);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.isFiducial", &HGamTruthEventInfoAuxDyn_isFiducial, &b_HGamTruthEventInfoAuxDyn_isFiducial);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.m_h1", &HGamTruthEventInfoAuxDyn_m_h1, &b_HGamTruthEventInfoAuxDyn_m_h1);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.isFiducialKinOnly", &HGamTruthEventInfoAuxDyn_isFiducialKinOnly, &b_HGamTruthEventInfoAuxDyn_isFiducialKinOnly);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.m_h2", &HGamTruthEventInfoAuxDyn_m_h2, &b_HGamTruthEventInfoAuxDyn_m_h2);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.yAbs_yy", &HGamTruthEventInfoAuxDyn_yAbs_yy, &b_HGamTruthEventInfoAuxDyn_yAbs_yy);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.pTt_yy", &HGamTruthEventInfoAuxDyn_pTt_yy, &b_HGamTruthEventInfoAuxDyn_pTt_yy);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.m_yy", &HGamTruthEventInfoAuxDyn_m_yy, &b_HGamTruthEventInfoAuxDyn_m_yy);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.passMeyCut", &HGamTruthEventInfoAuxDyn_passMeyCut, &b_HGamTruthEventInfoAuxDyn_passMeyCut);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.pT_yy", &HGamTruthEventInfoAuxDyn_pT_yy, &b_HGamTruthEventInfoAuxDyn_pT_yy);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.pT_y1", &HGamTruthEventInfoAuxDyn_pT_y1, &b_HGamTruthEventInfoAuxDyn_pT_y1);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.pT_y2", &HGamTruthEventInfoAuxDyn_pT_y2, &b_HGamTruthEventInfoAuxDyn_pT_y2);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.E_y1", &HGamTruthEventInfoAuxDyn_E_y1, &b_HGamTruthEventInfoAuxDyn_E_y1);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.E_y2", &HGamTruthEventInfoAuxDyn_E_y2, &b_HGamTruthEventInfoAuxDyn_E_y2);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.pT_hard", &HGamTruthEventInfoAuxDyn_pT_hard, &b_HGamTruthEventInfoAuxDyn_pT_hard);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.TruthNonInt_met", &HGamTruthEventInfoAuxDyn_TruthNonInt_met, &b_HGamTruthEventInfoAuxDyn_TruthNonInt_met);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.cosTS_yy", &HGamTruthEventInfoAuxDyn_cosTS_yy, &b_HGamTruthEventInfoAuxDyn_cosTS_yy);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.TruthInt_sumet", &HGamTruthEventInfoAuxDyn_TruthInt_sumet, &b_HGamTruthEventInfoAuxDyn_TruthInt_sumet);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.isFiducialLowHighMyy", &HGamTruthEventInfoAuxDyn_isFiducialLowHighMyy, &b_HGamTruthEventInfoAuxDyn_isFiducialLowHighMyy);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.isFiducialExotic", &HGamTruthEventInfoAuxDyn_isFiducialExotic, &b_HGamTruthEventInfoAuxDyn_isFiducialExotic);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.Dy_y_y", &HGamTruthEventInfoAuxDyn_Dy_y_y, &b_HGamTruthEventInfoAuxDyn_Dy_y_y);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.N_e", &HGamTruthEventInfoAuxDyn_N_e, &b_HGamTruthEventInfoAuxDyn_N_e);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.N_mu", &HGamTruthEventInfoAuxDyn_N_mu, &b_HGamTruthEventInfoAuxDyn_N_mu);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.N_j", &HGamTruthEventInfoAuxDyn_N_j, &b_HGamTruthEventInfoAuxDyn_N_j);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.N_j_central", &HGamTruthEventInfoAuxDyn_N_j_central, &b_HGamTruthEventInfoAuxDyn_N_j_central);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.N_j_central30", &HGamTruthEventInfoAuxDyn_N_j_central30, &b_HGamTruthEventInfoAuxDyn_N_j_central30);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.pT_j1", &HGamTruthEventInfoAuxDyn_pT_j1, &b_HGamTruthEventInfoAuxDyn_pT_j1);
   fChain->SetBranchAddress("HGamTruthEventInfoAuxDyn.pT_j2", &HGamTruthEventInfoAuxDyn_pT_j2, &b_HGamTruthEventInfoAuxDyn_pT_j2);
   fChain->SetBranchAddress("EventInfo", &EventInfo, &b_EventInfo);
   fChain->SetBranchAddress("EventInfoAuxDyn.runNumber", &EventInfoAuxDyn_runNumber, &b_EventInfoAuxDyn_runNumber);
   fChain->SetBranchAddress("EventInfoAuxDyn.eventTypeBitmask", &EventInfoAuxDyn_eventTypeBitmask, &b_EventInfoAuxDyn_eventTypeBitmask);
   fChain->SetBranchAddress("EventInfoAuxDyn.eventNumber", &EventInfoAuxDyn_eventNumber, &b_EventInfoAuxDyn_eventNumber);
   fChain->SetBranchAddress("EventInfoAuxDyn.RandomRunNumber", &EventInfoAuxDyn_RandomRunNumber, &b_EventInfoAuxDyn_RandomRunNumber);
   fChain->SetBranchAddress("EventInfoAuxDyn.lumiBlock", &EventInfoAuxDyn_lumiBlock, &b_EventInfoAuxDyn_lumiBlock);
   fChain->SetBranchAddress("EventInfoAuxDyn.coreFlags", &EventInfoAuxDyn_coreFlags, &b_EventInfoAuxDyn_coreFlags);
   fChain->SetBranchAddress("EventInfoAuxDyn.mcChannelNumber", &EventInfoAuxDyn_mcChannelNumber, &b_EventInfoAuxDyn_mcChannelNumber);
   fChain->SetBranchAddress("EventInfoAuxDyn.averageInteractionsPerCrossing", &EventInfoAuxDyn_averageInteractionsPerCrossing, &b_EventInfoAuxDyn_averageInteractionsPerCrossing);
   fChain->SetBranchAddress("EventInfoAuxDyn.passTrig_HLT_g35_loose_g25_loose", &EventInfoAuxDyn_passTrig_HLT_g35_loose_g25_loose, &b_EventInfoAuxDyn_passTrig_HLT_g35_loose_g25_loose);
   fChain->SetBranchAddress("EventInfoAuxDyn.mcEventWeights", &EventInfoAuxDyn_mcEventWeights, &b_EventInfoAuxDyn_mcEventWeights);
   fChain->SetBranchAddress("EventInfoAuxDyn.passTrig_HLT_2g50_loose", &EventInfoAuxDyn_passTrig_HLT_2g50_loose, &b_EventInfoAuxDyn_passTrig_HLT_2g50_loose);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.truthLink", &HGamPhotonsAuxDyn_truthLink, &b_HGamPhotonsAuxDyn_truthLink);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.parentPdgId", &HGamPhotonsAuxDyn_parentPdgId, &b_HGamPhotonsAuxDyn_parentPdgId);
   fChain->SetBranchAddress("HGamPhotonsAuxDyn.pdgId", &HGamPhotonsAuxDyn_pdgId, &b_HGamPhotonsAuxDyn_pdgId);
   fChain->SetBranchAddress("HGamTruthPhotonsAuxDyn.recoLink", &HGamTruthPhotonsAuxDyn_recoLink, &b_HGamTruthPhotonsAuxDyn_recoLink);
   fChain->SetBranchAddress("HGamMuonsInJetsAuxDyn.ptvarcone20", &HGamMuonsInJetsAuxDyn_ptvarcone20, &b_HGamMuonsInJetsAuxDyn_ptvarcone20);
   fChain->SetBranchAddress("HGamMuonsInJetsAuxDyn.passIPCut", &HGamMuonsInJetsAuxDyn_passIPCut, &b_HGamMuonsInJetsAuxDyn_passIPCut);
   fChain->SetBranchAddress("HGamMuonsInJetsAuxDyn.muonType", &HGamMuonsInJetsAuxDyn_muonType, &b_HGamMuonsInJetsAuxDyn_muonType);
   fChain->SetBranchAddress("HGamMuonsInJetsAuxDyn.pt", &HGamMuonsInJetsAuxDyn_pt, &b_HGamMuonsInJetsAuxDyn_pt);
   fChain->SetBranchAddress("HGamMuonsInJetsAuxDyn.topoetcone20", &HGamMuonsInJetsAuxDyn_topoetcone20, &b_HGamMuonsInJetsAuxDyn_topoetcone20);
   fChain->SetBranchAddress("HGamMuonsInJetsAuxDyn.eta", &HGamMuonsInJetsAuxDyn_eta, &b_HGamMuonsInJetsAuxDyn_eta);
   fChain->SetBranchAddress("HGamMuonsInJetsAuxDyn.scaleFactor", &HGamMuonsInJetsAuxDyn_scaleFactor, &b_HGamMuonsInJetsAuxDyn_scaleFactor);
   fChain->SetBranchAddress("HGamMuonsInJetsAuxDyn.phi", &HGamMuonsInJetsAuxDyn_phi, &b_HGamMuonsInJetsAuxDyn_phi);
   fChain->SetBranchAddress("HGamMuonsInJetsAuxDyn.charge", &HGamMuonsInJetsAuxDyn_charge, &b_HGamMuonsInJetsAuxDyn_charge);
   fChain->SetBranchAddress("HGamTruthElectronsAuxDyn.px", &HGamTruthElectronsAuxDyn_px, &b_HGamTruthElectronsAuxDyn_px);
   fChain->SetBranchAddress("HGamTruthElectronsAuxDyn.py", &HGamTruthElectronsAuxDyn_py, &b_HGamTruthElectronsAuxDyn_py);
   fChain->SetBranchAddress("HGamTruthElectronsAuxDyn.pz", &HGamTruthElectronsAuxDyn_pz, &b_HGamTruthElectronsAuxDyn_pz);
   fChain->SetBranchAddress("HGamTruthElectronsAuxDyn.pt", &HGamTruthElectronsAuxDyn_pt, &b_HGamTruthElectronsAuxDyn_pt);
   fChain->SetBranchAddress("HGamTruthElectronsAuxDyn.eta", &HGamTruthElectronsAuxDyn_eta, &b_HGamTruthElectronsAuxDyn_eta);
   fChain->SetBranchAddress("HGamTruthElectronsAuxDyn.e", &HGamTruthElectronsAuxDyn_e, &b_HGamTruthElectronsAuxDyn_e);
   fChain->SetBranchAddress("HGamTruthElectronsAuxDyn.m", &HGamTruthElectronsAuxDyn_m, &b_HGamTruthElectronsAuxDyn_m);
   fChain->SetBranchAddress("HGamTruthElectronsAuxDyn.recoLink", &HGamTruthElectronsAuxDyn_recoLink, &b_HGamTruthElectronsAuxDyn_recoLink);
   fChain->SetBranchAddress("HGamTruthMuonsAuxDyn.px", &HGamTruthMuonsAuxDyn_px, &b_HGamTruthMuonsAuxDyn_px);
   fChain->SetBranchAddress("HGamTruthMuonsAuxDyn.py", &HGamTruthMuonsAuxDyn_py, &b_HGamTruthMuonsAuxDyn_py);
   fChain->SetBranchAddress("HGamTruthMuonsAuxDyn.pz", &HGamTruthMuonsAuxDyn_pz, &b_HGamTruthMuonsAuxDyn_pz);
   fChain->SetBranchAddress("HGamTruthMuonsAuxDyn.pt", &HGamTruthMuonsAuxDyn_pt, &b_HGamTruthMuonsAuxDyn_pt);
   fChain->SetBranchAddress("HGamTruthMuonsAuxDyn.eta", &HGamTruthMuonsAuxDyn_eta, &b_HGamTruthMuonsAuxDyn_eta);
   fChain->SetBranchAddress("HGamTruthMuonsAuxDyn.e", &HGamTruthMuonsAuxDyn_e, &b_HGamTruthMuonsAuxDyn_e);
   fChain->SetBranchAddress("HGamTruthMuonsAuxDyn.m", &HGamTruthMuonsAuxDyn_m, &b_HGamTruthMuonsAuxDyn_m);
   fChain->SetBranchAddress("HGamMuonsAuxDyn.ptvarcone20", &HGamMuonsAuxDyn_ptvarcone20, &b_HGamMuonsAuxDyn_ptvarcone20);
   fChain->SetBranchAddress("HGamMuonsAuxDyn.passIPCut", &HGamMuonsAuxDyn_passIPCut, &b_HGamMuonsAuxDyn_passIPCut);
   fChain->SetBranchAddress("HGamMuonsAuxDyn.muonType", &HGamMuonsAuxDyn_muonType, &b_HGamMuonsAuxDyn_muonType);
   fChain->SetBranchAddress("HGamMuonsAuxDyn.pt", &HGamMuonsAuxDyn_pt, &b_HGamMuonsAuxDyn_pt);
   fChain->SetBranchAddress("HGamMuonsAuxDyn.topoetcone20", &HGamMuonsAuxDyn_topoetcone20, &b_HGamMuonsAuxDyn_topoetcone20);
   fChain->SetBranchAddress("HGamMuonsAuxDyn.eta", &HGamMuonsAuxDyn_eta, &b_HGamMuonsAuxDyn_eta);
   fChain->SetBranchAddress("HGamMuonsAuxDyn.scaleFactor", &HGamMuonsAuxDyn_scaleFactor, &b_HGamMuonsAuxDyn_scaleFactor);
   fChain->SetBranchAddress("HGamMuonsAuxDyn.phi", &HGamMuonsAuxDyn_phi, &b_HGamMuonsAuxDyn_phi);
   fChain->SetBranchAddress("HGamMuonsAuxDyn.charge", &HGamMuonsAuxDyn_charge, &b_HGamMuonsAuxDyn_charge);
   fChain->SetBranchAddress("HGamElectronsAuxDyn.eta_s2", &HGamElectronsAuxDyn_eta_s2, &b_HGamElectronsAuxDyn_eta_s2);
   fChain->SetBranchAddress("HGamElectronsAuxDyn.ptvarcone20", &HGamElectronsAuxDyn_ptvarcone20, &b_HGamElectronsAuxDyn_ptvarcone20);
   fChain->SetBranchAddress("HGamElectronsAuxDyn.pt", &HGamElectronsAuxDyn_pt, &b_HGamElectronsAuxDyn_pt);
   fChain->SetBranchAddress("HGamElectronsAuxDyn.topoetcone20", &HGamElectronsAuxDyn_topoetcone20, &b_HGamElectronsAuxDyn_topoetcone20);
   fChain->SetBranchAddress("HGamElectronsAuxDyn.isTight", &HGamElectronsAuxDyn_isTight, &b_HGamElectronsAuxDyn_isTight);
   fChain->SetBranchAddress("HGamElectronsAuxDyn.eta", &HGamElectronsAuxDyn_eta, &b_HGamElectronsAuxDyn_eta);
   fChain->SetBranchAddress("HGamElectronsAuxDyn.scaleFactor", &HGamElectronsAuxDyn_scaleFactor, &b_HGamElectronsAuxDyn_scaleFactor);
   fChain->SetBranchAddress("HGamElectronsAuxDyn.phi", &HGamElectronsAuxDyn_phi, &b_HGamElectronsAuxDyn_phi);
   fChain->SetBranchAddress("HGamElectronsAuxDyn.charge", &HGamElectronsAuxDyn_charge, &b_HGamElectronsAuxDyn_charge);
   fChain->SetBranchAddress("HGamElectronsAuxDyn.m", &HGamElectronsAuxDyn_m, &b_HGamElectronsAuxDyn_m);
   fChain->SetBranchAddress("HGamElectronsAuxDyn.truthLink", &HGamElectronsAuxDyn_truthLink, &b_HGamElectronsAuxDyn_truthLink);
   Notify();
}

Bool_t MxAOD::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void MxAOD::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t MxAOD::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef MxAOD_cxx
