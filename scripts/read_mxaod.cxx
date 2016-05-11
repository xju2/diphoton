#include <iostream>
#include <stdio.h>
#include <TFile.h>
#include <TTree.h>
#include <TH1F.h>
#include <TH2F.h>

using namespace std;
const int MASSBINS = 5;
const int ETABINS = 4;

int mass_bin(float inv_mass){
    int res = -1;
    if(inv_mass >= 160 && inv_mass < 250){
        res = 0;
    }else if(inv_mass >= 250 && inv_mass < 400) {
        res = 1;
    }else if(inv_mass >= 400 && inv_mass < 650) {
        res = 2;
    }else if(inv_mass >= 650 && inv_mass < 1000) {
        res = 3;
    }else if(inv_mass >= 1000) {
        res = 4;
    }else {
        cout << "possible error in invariant mass" << endl;
    }
    return res;
}

int abseta_bin(float abs_eta){
    int res = -1;
    if(abs_eta > 0 and abs_eta < 0.6) {
        res = 0;
    } else if(abs_eta > 0.6 && abs_eta < 1.37) {
        res = 1;
    } else if(abs_eta > 1.52 && abs_eta < 1.81) {
        res = 2;
    } else if(abs_eta > 1.81 && abs_eta < 2.37) {
        res = 3;
    } else {
    }
    return res;
}

int read_mxaod(
        const string& file_name,
        const string& out_name,
        bool is_bkg, int cut_type = 0
        )
{
    cout << "file name: " << file_name << endl;
    cout << "out name: " << out_name << endl;
    cout << "is bkg: " << is_bkg << endl;

    // 1 ifb
    double lumi = 3.2E3;

    TFile* fin = TFile::Open(file_name.c_str());
    if(!fin) exit(1);
    TTree* tin = (TTree*)fin->Get("CollectionTree");
    if(!tin) exit(2);
    size_t first_ = file_name.rfind('/')+1;
    size_t end_ = file_name.find('.');
    string sub_str = file_name.substr(first_, end_-first_);
    string histname = "CutFlow_"+sub_str;
    cout << "hist name: " << histname << endl;
    long total_events = -1;
    TH1F* cut = (TH1F*)fin->Get(histname.c_str());
    if (cut){
        total_events = cut->GetBinContent(1);
        cout << "total events in generator: " << total_events << endl;
    }
    bool is_data = total_events < 0;

    char isPassedPreselection;
    char isPassedPID;
    char isPassedBasic;
    char isPassedIsolation;
    char isPassedRelPtCuts;
    char isPassedMassCut;
    char isPassedIsolationLowHighMyy;
    char isPassedRelPtCutsLowHighMyy;
    char isPassedLowHighMyy;
    char isPassedIsolationExotic;
    char isPassedlPtCutsExotic;
    char isPassedExotic;
    float vertexWeight;
    float m_yy;
    float crossSectionBRfilterEff;
    float weight;
    unsigned int mcChannelNumber;
    //vector<float>   *mcEventWeights = nullptr;
    vector<float>   *pt = nullptr;
    vector<float>   *eta_s2 = nullptr;
    vector<int>     *conversionType = nullptr;
    vector<float> *etcone40 = nullptr;
    vector<float> *etcone40_DD = nullptr;
    vector<float> *isTight = nullptr;
    vector<float> *ptcone20 = nullptr;

    tin->SetBranchAddress("HGamEventInfoAuxDyn.isPassedPreselection",&isPassedPreselection);
    tin->SetBranchAddress("HGamEventInfoAuxDyn.isPassedPID",&isPassedPID);
    tin->SetBranchAddress("HGamEventInfoAuxDyn.isPassedBasic",&isPassedBasic);
    tin->SetBranchAddress("HGamEventInfoAuxDyn.isPassedIsolation",&isPassedIsolation);
    tin->SetBranchAddress("HGamEventInfoAuxDyn.isPassedRelPtCuts",&isPassedRelPtCuts);
    tin->SetBranchAddress("HGamEventInfoAuxDyn.isPassedMassCut",&isPassedMassCut);
    tin->SetBranchAddress("HGamEventInfoAuxDyn.isPassedIsolationLowHighMyy",&isPassedIsolationLowHighMyy);
    tin->SetBranchAddress("HGamEventInfoAuxDyn.isPassedRelPtCutsLowHighMyy",&isPassedRelPtCutsLowHighMyy);
    tin->SetBranchAddress("HGamEventInfoAuxDyn.isPassedLowHighMyy",&isPassedLowHighMyy);
    tin->SetBranchAddress("HGamEventInfoAuxDyn.isPassedIsolationExotic",&isPassedIsolationExotic);
    tin->SetBranchAddress("HGamEventInfoAuxDyn.isPassedlPtCutsExotic",&isPassedlPtCutsExotic);
    tin->SetBranchAddress("HGamEventInfoAuxDyn.isPassedExotic",&isPassedExotic);
    tin->SetBranchAddress("HGamEventInfoAuxDyn.m_yy",&m_yy);
    if (!is_data){
        tin->SetBranchAddress("HGamEventInfoAuxDyn.crossSectionBRfilterEff",&crossSectionBRfilterEff);
        tin->SetBranchAddress("EventInfoAuxDyn.mcChannelNumber",&mcChannelNumber);
        tin->SetBranchAddress("HGamPhotonsAuxDyn.topoetcone40_DDcorrected",&etcone40_DD);
    }
    tin->SetBranchAddress("HGamEventInfoAuxDyn.weight",&weight);
    tin->SetBranchAddress("HGamEventInfoAuxDyn.vertexWeight",&vertexWeight);
    //tin->SetBranchAddress("EventInfoAuxDyn.mcEventWeights",&mcEventWeights);

    // photon information
    tin->SetBranchAddress("HGamPhotonsAuxDyn.pt",&pt);
    tin->SetBranchAddress("HGamPhotonsAuxDyn.eta_s2",&eta_s2);
    tin->SetBranchAddress("HGamPhotonsAuxDyn.conversionType",&conversionType);
    tin->SetBranchAddress("HGamPhotonsAuxDyn.topoetcone40",&etcone40);
    tin->SetBranchAddress("HGamPhotonsAuxDyn.isTight",&isTight);
    tin->SetBranchAddress("HGamPhotonsAuxDyn.ptcone20",&ptcone20);

    tin->SetBranchStatus("*",0);
    tin->SetBranchStatus("HGamEventInfoAuxDyn.isPassedPreselection",1);
    tin->SetBranchStatus("HGamEventInfoAuxDyn.isPassedPID",1);
    tin->SetBranchStatus("HGamEventInfoAuxDyn.isPassedBasic",1);
    tin->SetBranchStatus("HGamEventInfoAuxDyn.isPassedIsolation",1);
    tin->SetBranchStatus("HGamEventInfoAuxDyn.isPassedRelPtCuts",1);
    tin->SetBranchStatus("HGamEventInfoAuxDyn.isPassedMassCut",1);
    tin->SetBranchStatus("HGamEventInfoAuxDyn.isPassedIsolationLowHighMyy",1);
    tin->SetBranchStatus("HGamEventInfoAuxDyn.isPassedRelPtCutsLowHighMyy",1);
    tin->SetBranchStatus("HGamEventInfoAuxDyn.isPassedLowHighMyy",1);
    tin->SetBranchStatus("HGamEventInfoAuxDyn.isPassedIsolationExotic",1);
    tin->SetBranchStatus("HGamEventInfoAuxDyn.isPassedlPtCutsExotic",1);
    tin->SetBranchStatus("HGamEventInfoAuxDyn.isPassedExotic",1);
    tin->SetBranchStatus("HGamEventInfoAuxDyn.m_yy",1);
    if(!is_data){
        tin->SetBranchStatus("HGamEventInfoAuxDyn.crossSectionBRfilterEff",1);
        tin->SetBranchStatus("EventInfoAuxDyn.mcChannelNumber",1);
        //tin->SetBranchStatus("EventInfoAuxDyn.mcEventWeights",1);
        tin->SetBranchStatus("HGamPhotonsAuxDyn.topoetcone40_DDcorrected",1);
    }
    tin->SetBranchStatus("HGamEventInfoAuxDyn.weight",1);
    tin->SetBranchStatus("HGamEventInfoAuxDyn.vertexWeight",1);
    tin->SetBranchStatus("HGamPhotonsAuxDyn.pt",1);
    tin->SetBranchStatus("HGamPhotonsAuxDyn.eta_s2",1);
    tin->SetBranchStatus("HGamPhotonsAuxDyn.conversionType",1);
    tin->SetBranchStatus("HGamPhotonsAuxDyn.topoetcone40",1);
    tin->SetBranchStatus("HGamPhotonsAuxDyn.isTight",1);
    tin->SetBranchStatus("HGamPhotonsAuxDyn.ptcone20",1);

    TFile* fout = new TFile(out_name.c_str(),"recreate");
    // book histograms for isolation
    int iso_nbins = 80;
    float iso_low_bin = -10., iso_hi_bin = 30.;
    TH2F* h_leading_iso_mass = new TH2F(
            "h_leading_iso_massbin",
            "leading etcone40 in mass bin",
            iso_nbins, iso_low_bin, iso_hi_bin,
            101, -0.5, 100.5);
    TH2F* h_subleading_iso_mass = new TH2F(
            "h_subleading_iso_massbin",
            "subleading etcone40 in mass bin",
            iso_nbins, iso_low_bin, iso_hi_bin,
            101, -0.5, 100.5);
    TH2F* h_leading_isoDD_mass = new TH2F(
            "h_leading_isoDD_massbin",
            "leading etcone40 DD corrected in mass bin",
            iso_nbins, iso_low_bin, iso_hi_bin,
            101, -0.5, 100.5);
    TH2F* h_subleading_isoDD_mass = new TH2F(
            "h_subleading_isoDD_massbin",
            "subleading etcone40 DD corrected in mass bin",
            iso_nbins, iso_low_bin, iso_hi_bin,
            101, -0.5, 100.5
            );

    // mass in different eta bins
    int nbins_mass = 660;
    float mass_low = 200, mass_hi = 3500;
    if(cut_type == 1) { // spin-2 selection
        nbins_mass = 670;
        mass_low = 150;
    }
    TH1F* mass = new TH1F("mass", "inv mass", nbins_mass, mass_low, mass_hi);
    TH2F* mass_etabins = new TH2F("mass_etabins", "mass in eta bins",
            nbins_mass, mass_low, mass_hi,
            101, -0.5, 100.5
            );

    // 2D isolation variable
    int nbins_track_iso = 50;
    float track_iso_low = 0, track_iso_hi = 0.5;
    TH2F* h_leading_iso = new TH2F(
            "h_leading_iso",
            "2D isolation map for leading photon",
            iso_nbins, iso_low_bin, iso_hi_bin, // x-axis calo ISO
            nbins_track_iso, track_iso_low, track_iso_hi// y-axis track ISO
            );
    TH2F* h_subleading_iso = new TH2F(
            "h_subleading_iso",
            "2D isolation map for subleading photon",
            iso_nbins, iso_low_bin, iso_hi_bin, // x-axis calo ISO
            nbins_track_iso, track_iso_low, track_iso_hi// y-axis track ISO
            );
    TH2F* h_leading_isoDD = new TH2F(
            "h_leading_isoDD",
            "2D isolation map for leading photon",
            iso_nbins, iso_low_bin, iso_hi_bin, // x-axis calo ISO
            nbins_track_iso, track_iso_low, track_iso_hi// y-axis track ISO
            );
    TH2F* h_subleading_isoDD = new TH2F(
            "h_subleading_isoDD",
            "2D isolation map for subleading photon",
            iso_nbins, iso_low_bin, iso_hi_bin, // x-axis calo ISO
            nbins_track_iso, track_iso_low, track_iso_hi// y-axis track ISO
            );

    // pT and eta distribution
    TH1F* h_leading_pt = new TH1F(
            "h_leading_pt",
            "leaing photon pT",
            400, 0, 800
            );
    TH1F* h_subleading_pt = new TH1F(
            "h_subleading_pt",
            "leaing photon pT",
            300, 0, 600
            );

    double eta_bins[45] = {
        -2.37, -2.22, -2.12, -2.02, -1.92, -1.82, -1.72, -1.62, -1.52, -1.37,
        -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3,
        -0.2, -0.1, 
        0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,
        1.0, 1.1, 1.2, 1.37, 1.52, 1.62, 1.72, 1.82, 1.92, 2.02,
        2.12, 2.22, 2.37
    };
    TH1F* h_leading_eta = new TH1F(
            "h_leading_eta",
            "leading photon eta",
            44, eta_bins
            );
    TH1F* h_subleading_eta = new TH1F(
            "h_subleading_eta",
            "subleading photon eta",
            44, eta_bins);

    cout<<"There are "<<tin->GetEntries()<<" events in total"<<endl;

    for( int i=0; i<tin->GetEntries(); i++ )
    {
        if( i%500000==0 ) cout<<"processing event "<<i<<endl;
        tin->GetEntry(i);
        // printf("|%i|\n", isPassedPID);
        if( !isPassedPreselection ||
            m_yy < mass_low*1E3
          ) continue;
        bool event_cut = false;
        float leading_iso = etcone40->at(0)/1E3 - pt->at(0)*0.022/1E3;
        float subleading_iso = etcone40->at(1)/1E3 - pt->at(1)*0.022/1E3;
        float leading_track_iso = ptcone20->at(0)/pt->at(0);
        float subleading_track_iso = ptcone20->at(1)/pt->at(1);
        bool pass_iso = leading_iso < 2.45 && subleading_iso < 2.45 && leading_track_iso < 0.05 && subleading_track_iso < 0.05;
        bool pass_spin2_EK = pt->at(0) > 55E3 && pt->at(1) > 55E3;
        bool pass_spin0_EK = pt->at(0)/m_yy > 0.4 && pt->at(1)/m_yy > 0.3;

        if (cut_type == 2) { // spin2 selections
            event_cut = pass_spin2_EK && pass_iso;
        } else if (cut_type == 1) {
            event_cut = pass_spin0_EK && pass_iso;
        } else {
            event_cut = (is_bkg && !isPassedPID && pass_spin2_EK) || (!is_bkg && isPassedPID && pass_spin2_EK);
        }
        if(!event_cut) continue;

        bool fill_leading = true, fill_subleading = true;
        if(is_bkg && isTight->at(0)) fill_leading = false;
        if(is_bkg && isTight->at(1)) fill_subleading = false;
        float weight_ = 1.0;
        if(total_events > 0) {
            float sum_of_weights = total_events/cut->GetBinContent(2)*cut->GetBinContent(3);
            if( mcChannelNumber==303733 ) crossSectionBRfilterEff *= 100;
            weight_ = weight*crossSectionBRfilterEff*lumi/sum_of_weights;
        }
        float leading_isoDD = -1;
        float subleading_isoDD = -1;
        if (!is_data) {
            leading_isoDD = etcone40_DD->at(0)/1E3 - pt->at(0)*0.022/1E3;
            subleading_isoDD = etcone40_DD->at(1)/1E3 - pt->at(1)*0.022/1E3;
        }
        float inv_mass = m_yy/1E3;
        mass->Fill(inv_mass, weight_);

        // fill calo isolation in different mass bin
        int y_bin_val = mass_bin(inv_mass);
        if(fill_leading){
            h_leading_iso_mass->Fill(leading_iso, y_bin_val, weight_);
            h_leading_isoDD_mass->Fill(leading_isoDD, y_bin_val, weight_);
        }
        if(fill_subleading) {
            h_subleading_iso_mass->Fill(subleading_iso, y_bin_val, weight_);
            h_subleading_isoDD_mass->Fill(subleading_isoDD, y_bin_val, weight_);
        }

        // fill isolation for photons with 125 < et < 145 GeV and different eta
        // repeat what we have in paper
        for (int iph = 0; iph < 2; iph++){
            float pt_ = pt->at(iph)/1E3;
            if(pt_ > 125 && pt_ < 145){
                float abs_eta = abs(eta_s2->at(iph));
                int eta_bin = abseta_bin(abs_eta);
                int y_bin = eta_bin + MASSBINS + iph*4;
                if(fill_leading){
                    h_leading_iso_mass->Fill(leading_iso, y_bin, weight_);
                    h_leading_isoDD_mass->Fill(leading_isoDD, y_bin, weight_);
                }
                if(fill_subleading){
                    h_subleading_iso_mass->Fill(subleading_iso, y_bin, weight_);
                    h_subleading_isoDD_mass->Fill(subleading_isoDD, y_bin, weight_);
                }
            }
        }

        // fill track and calo isolation
        h_leading_iso->Fill(leading_iso, leading_track_iso, weight_);
        h_subleading_iso->Fill(subleading_iso, subleading_track_iso, weight_);
        h_leading_isoDD->Fill(leading_isoDD, leading_track_iso, weight_);
        h_subleading_isoDD->Fill(subleading_isoDD, subleading_track_iso, weight_);

        // fill pT and eta
        h_leading_pt->Fill(pt->at(0)/1E3, weight_);
        h_subleading_pt->Fill(pt->at(1)/1E3, weight_);
        h_leading_eta->Fill(eta_s2->at(0), weight_);
        h_subleading_eta->Fill(eta_s2->at(1), weight_);
        // fill mass in different eta bin
        if(abs(eta_s2->at(0)) < 0.75 && abs(eta_s2->at(1)) < 0.75) {
            mass_etabins->Fill(inv_mass, 0., weight_);
        } else {
            mass_etabins->Fill(inv_mass, 1., weight_);
        }
        if(abs(eta_s2->at(0)) < 1.37 && abs(eta_s2->at(1)) < 1.37) {
            mass_etabins->Fill(inv_mass, 2., weight_);
        } else {
            mass_etabins->Fill(inv_mass, 3., weight_);
        }
    }
    fout->cd();
    h_leading_iso_mass->Write();
    h_subleading_iso_mass->Write();
    h_leading_isoDD_mass->Write();
    h_subleading_isoDD_mass->Write();
    mass->Write();
    h_leading_iso->Write();
    h_subleading_iso->Write();
    h_leading_isoDD->Write();
    h_subleading_isoDD->Write();

    h_leading_pt->Write();
    h_subleading_pt->Write();
    h_leading_eta->Write();
    h_subleading_eta->Write();
    mass_etabins->Write();

    fout->Close();
    fin->Close();
    return 0;
}
