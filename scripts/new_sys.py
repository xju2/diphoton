#!/usr/bin/env python

import ROOT

bin_low = 200
bin_hi = 3500
nbins = (bin_hi - bin_low)/5

INFLATE_SYS = False

def create_sys_hist(h_nominal, h_org_sys, hist_name):
    print hist_name, h_nominal.GetNbinsX(), h_org_sys.GetNbinsX()
    h_sys = h_nominal.Clone(hist_name+"_times")
    h_sys.Multiply(h_org_sys)

    h_up = h_nominal.Clone(hist_name+"_up")
    h_up.Add(h_sys, 1)
    h_down = h_nominal.Clone(hist_name+"_down")
    h_down.Add(h_sys, -1)
    return (h_up, h_down)

def truncate_hist(hist, hist_name):
    hout = ROOT.TH1F(hist_name, "hist", nbins, bin_low, bin_hi)
    for ibin in range(nbins):
        iold = hist.FindBin(hout.GetBinCenter(ibin+1))
        hout.SetBinContent(ibin+1, hist.GetBinContent(iold))
        hout.SetBinError(ibin+1, hist.GetBinError(iold))
    return hout

def produce_8TeV_template():
    f1 = ROOT.TFile.Open("new_sys.root", "recreate")
    file_name = "Bkg_Total_allcat_TOPO_PTDEP_8.0_lead50_sublead50_norm17_62_linear.root"
    f2 = ROOT.TFile.Open( file_name, "read")
    h_nom_org = f2.Get("bkg_total_gg_full")
    print "original binning: ", h_nom_org.GetNbinsX()

    f3 = ROOT.TFile.Open("test_smooth.root", "read")
    h_purity_sys = f3.Get("bkg_purity_syst_gg")
    h_reducible_sys = f3.Get("bkg_reducible_syst_gg")
    h_irreducible_sys = f3.Get("bkg_irreducible_syst_gg")
    h_geo_sys = f3.Get("bkg_geo_syst_gg")
    
    #write down sys and nominal
    f1.cd()
    h_nom = truncate_hist(h_nom_org, "bkg_nominal")
    h_nom.Write()
    h_purity_sys.Write()
    h_reducible_sys.Write()
    h_irreducible_sys.Write()
    h_purity_up, h_purity_down = create_sys_hist(h_nom, h_purity_sys, "purity_sys")
    h_purity_up.Write()
    h_purity_down.Write()
    h_red_up, h_red_down = create_sys_hist(h_nom, h_reducible_sys, "reducible_sys")
    h_red_up.Write()
    h_red_down.Write()
    h_irred_up, h_irred_down = create_sys_hist(h_nom, h_irreducible_sys, "irreducible_sys")
    h_irred_up.Write()
    h_irred_down.Write()
    h_geo_up, h_geo_down = create_sys_hist(h_nom, h_geo_sys, "geo_sys")
    h_geo_up.Write()
    h_geo_down.Write()

    f1.Close()

    f2.Close()
    f3.Close()

def produce_13TeV_template(tag_name="HKHI"):
    """
    generate inputs for histofactory.
    It will look for directory: inputs/BkgEstimation_Lin/
    """
    num_rebin = 1
    file_name = "inputs/BkgEstimation_Lin/BkgEstimation_NONE_TOPO_PTDEP_"+tag_name+"_Lin.root"
    print "Input: ", file_name
    fin = ROOT.TFile.Open(file_name, "read")
    h_nom = fin.Get("bkg_total_gg_full").Clone("bkg_nominal_old")
    h_nom.Rebin(num_rebin)
    fout = ROOT.TFile.Open("hists_input_"+tag_name+".root", "recreate")

    h_purity_sys = fin.Get("bkg_purity_syst_gg_full").Clone("bkg_purity_syst_gg")
    h_reducible_sys = fin.Get("bkg_reducible_syst_gg_full").Clone("bkg_reducible_syst_gg")
    h_irreducible_sys = fin.Get("bkg_irreducible_syst_gg_full").Clone("bkg_irreducible_syst_gg")
    h_iso_sys = fin.Get("bkg_iso_syst_gg_full").Clone("bkg_iso_syst_gg")

    #file_iso = "isolation_sys/hist.root"
    #fin2 = ROOT.TFile.Open(file_iso, "read")
    #h_iso_sys = fin2.Get("bkg_isolation_syst_gg")
    ## inflat irreducible uncertainty by factor of 10
    # so that it closes to stats uncertainty in data
    sf = 1
    if INFLATE_SYS:
        sf = 10

    # after rebinning systematic uncertainties, need to scale down,
    # otherwise the uncertainties are inflated.
    h_purity_sys.Rebin(num_rebin).Scale(sf/num_rebin)
    h_irreducible_sys.Rebin(num_rebin).Scale(sf/num_rebin)
    h_reducible_sys.Rebin(num_rebin).Scale(sf/num_rebin)
    h_iso_sys.Rebin(num_rebin).Scale(sf/num_rebin)

    ## truncate the histograms to [200, 2000] GeV
    h_nom_new = truncate_hist(h_nom, "bkg_nominal")
    h_purity_sys_new = truncate_hist(h_purity_sys, "h_purity_sys_new")
    h_irreducible_sys_new = truncate_hist(h_irreducible_sys, "h_irreducible_sys_new")
    h_reducible_sys_new = truncate_hist(h_reducible_sys, "h_reducible_sys_new")
    h_iso_sys_new = truncate_hist(h_iso_sys, "h_iso_sys_new")

    #write down sys and nominal
    fout.cd()
    h_nom_new.Write()
    h_purity_sys_new.Write()
    h_reducible_sys_new.Write()
    h_irreducible_sys_new.Write()
    h_iso_sys_new.Write()

    h_purity_up, h_purity_down = create_sys_hist(h_nom_new, h_purity_sys_new, "purity_sys")
    h_purity_up.Write()
    h_purity_down.Write()

    h_red_up, h_red_down = create_sys_hist(h_nom_new, h_reducible_sys_new, "reducible_sys")
    h_red_up.Write()
    h_red_down.Write()

    h_irred_up, h_irred_down = create_sys_hist(h_nom_new, h_irreducible_sys_new, "irreducible_sys")
    h_irred_up.Write()
    h_irred_down.Write()

    h_iso_up, h_iso_down = create_sys_hist(h_nom_new, h_iso_sys, "isolation_sys")
    h_iso_up.Write()
    h_iso_down.Write()

    fin.Close()
    fout.Close()


if __name__ == "__main__":
    #produce_13TeV_template("EKEI")
    #produce_13TeV_template()
    #produce_13TeV_template("EKHI")
    produce_13TeV_template("HKHI")
