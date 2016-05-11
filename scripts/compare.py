#!/usr/bin/env python

import ROOT
import AtlasStyle
import new_sys
import sys

ROOT.gROOT.SetBatch()
if not hasattr(ROOT, "myLegend"):
    ROOT.gROOT.LoadMacro("/afs/cern.ch/user/x/xju/tool/loader.c") 

def extend_hist(h1, h2):
    """
    extend h1 to the range of h2, they has to have the same binning
    """
    h1_clone = h2.Clone(h1.GetName()+"_new")
    for ibin in range(1, h2.GetNbinsX()+1):
        if ibin <= h1.GetNbinsX():
            y_val = h1.GetBinContent(ibin)
        else:
            y_val = 0.0
        h1_clone.SetBinContent(ibin, y_val)
    return h1_clone 

def compare(f1_name, f2_name, f3_name):
    f1 = ROOT.TFile.Open(f1_name, "read")
    f2 = ROOT.TFile.Open(f2_name, "read")
    f3 = ROOT.TFile.Open(f3_name, "read")
    bkg_f1 = f1.Get("hist_bkg_inclusive_13TeV__obs_x_channel")
    bkg_f2 = f2.Get("hist_bkg_inclusive_13TeV__obs_x_channel")
    bkg_f3 = f3.Get("bkg_total_gg_full")
    bkg_f3.Rebin(5)

    canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
    canvas.SetLogy()
    bkg_f1.SetLineColor(2)
    bkg_f2.SetLineColor(8)
    bkg_f3.SetLineColor(4)
    bkg_f1.SetMarkerSize(0)
    bkg_f2.SetMarkerSize(0)
    bkg_f3.SetMarkerSize(0)

    h_bkgs = ROOT.TList()
    h_bkgs.Add(bkg_f1)
    h_bkgs.Add(bkg_f2)
    c1 = ROOT.add_ratio_pad(bkg_f3, bkg_f2)
    c1.SetLogy()
    bkg_f2.Draw("")
    bkg_f3.Draw("same")

    legend = ROOT.myLegend(0.7, 0.8, 0.9, 0.9)
    #legend.AddEntry( bkg_f1, "nominal v4", "L")
    legend.AddEntry( bkg_f2, "nominal v5", "L")
    legend.AddEntry( bkg_f3, "nominal LIN", "L")
    legend.Draw()
    canvas.SaveAs("test.pdf")

def compare_ws_hist(f1_name, f2_name):
    f1 = ROOT.TFile.Open(f1_name, "read") ## workspace
    f2 = ROOT.TFile.Open(f2_name, "read")
    if not f1 or not f2: return None

    bkg_f2 = f2.Get("bkg_total_gg_full")
    #bkg_f2.Rebin(5)

    ws = f1.Get("combined")
    pdf = ws.obj("channel_model")
    obs = ws.var("obs_x_channel")
    obs.setRange(200, 5000)
    nbins = 960
    bkg_f1 = pdf.createHistogram("bkg_f1", obs, ROOT.RooFit.Binning(nbins))
    print bkg_f1.Integral(), bkg_f2.Integral()
    bkg_f1.Scale(bkg_f2.Integral()/bkg_f1.Integral())

    bkg_f1.SetLineColor(2)
    bkg_f2.SetLineColor(4)
    bkg_f1.SetMarkerSize(0)
    bkg_f2.SetMarkerSize(0)

    canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
    #canvas.SetLogy()
    c1 = ROOT.add_ratio_pad(bkg_f2, bkg_f1)
    c1.SetLogy()
    bkg_f1.Draw()
    bkg_f2.Draw("same")

    legend = ROOT.myLegend(0.7, 0.8, 0.9, 0.9)
    legend.AddEntry( bkg_f1, "workspace", "L")
    legend.AddEntry( bkg_f2, "input hist", "L")
    legend.Draw()
    canvas.SaveAs(f1_name.replace("root", "pdf"))

def create_hist_from_ws(ws, tag_name, hist_name):
    pdf = ws.obj(tag_name+"_model")
    pdf.Print()
    obs = ws.var("obs_x_"+tag_name)
    obs.Print()
    #obs.setRange(200, 3500)
    #nbins = 660
    #bkg_f1 = pdf.createHistogram(hist_name, obs, ROOT.RooFit.Binning(nbins))
    bkg_f1 = pdf.createHistogram(hist_name, obs)
    return bkg_f1

def compare_ws_ws(f1_name, f2_name):
    f1 = ROOT.TFile.Open(f1_name, "read") ## workspace
    f2 = ROOT.TFile.Open(f2_name, "read") ## mine
    if not f1 or not f2: return None

    #f3_name = "Bkg_Total_allcat_TOPO_PTDEP_8.0_lead50_sublead50_norm17_62_linear.root"
    f3_name = "BkgEstimation_Lin/BkgEstimation_NONE_TOPO_PTDEP_HKHI_Lin.root"
    f3 = ROOT.TFile.Open(f3_name, "read")
    bkg_f3_org = f3.Get("bkg_total_gg_full").Rebin(5)
    bkg_f3 = new_sys.truncate_hist(bkg_f3_org, "bkg_f3")

    f4_name = "ruggero_template/BkgEstimation_NONE_NONE_TOPO_PTDEP_HKHI_Lin.root"
    f4 = ROOT.TFile.Open(f4_name, "read")
    bkg_f4 = f4.Get("bkg_total_gg_full")

    ws1 = f1.Get("combined")
    ws2 = f2.Get("combined")

    bkg_f1 = create_hist_from_ws(ws1, "channel", "bkg_f1")
    #bkg_f2 = create_hist_from_ws(ws2, "chan_8TeV", "bkg_f2")
    bkg_f2 = create_hist_from_ws(ws2, "chan_HKHI_13TeV", "bkg_f2")

    bkg_f1.Scale(bkg_f2.Integral()/bkg_f1.Integral())
    bkg_f3.Scale(bkg_f2.Integral()/bkg_f3.Integral())
    bkg_f4.Scale(bkg_f2.Integral()/bkg_f4.Integral())

    bkg_f1.SetLineColor(2)
    bkg_f2.SetLineColor(4)
    bkg_f4.SetLineColor(8)

    bkg_f1.SetMarkerSize(0)
    bkg_f2.SetMarkerSize(0)
    bkg_f3.SetMarkerSize(0)
    bkg_f4.SetMarkerSize(0)

    print bkg_f1.GetNbinsX(),bkg_f2.GetNbinsX(),bkg_f3.GetNbinsX(),bkg_f4.GetNbinsX()
    canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
    #canvas.SetLogy()
    h_bkgs = ROOT.TList()
    h_bkgs.Add(bkg_f1)
    h_bkgs.Add(bkg_f2)
    h_bkgs.Add(bkg_f4)
    c1 = ROOT.add_ratio_pad(bkg_f3, h_bkgs)
    c1.SetLogy()
    bkg_f1.Draw()
    bkg_f2.Draw("same")
    bkg_f3.Draw("same")
    bkg_f4.Draw("same")


    legend = ROOT.myLegend(0.7, 0.8, 0.9, 0.9)
    legend.AddEntry( bkg_f1, "Rugero", "L")
    legend.AddEntry( bkg_f2, "XY", "L")
    legend.AddEntry( bkg_f3, "input hist", "L")
    legend.AddEntry( bkg_f4, "new hist", "L")
    legend.Draw()
    canvas.SaveAs(f1_name.replace("root", "pdf"))


def compare_hist_hist(f1_name, f2_name, hist_name):
    f1 = ROOT.TFile.Open(f1_name, "read") # New
    f2 = ROOT.TFile.Open(f2_name, "read") # Old
    h1 = f1.Get(hist_name)
    if "olation" in f2_name:
        h2 = f2.Get("up")
    else:
        h2 = f2.Get(hist_name)
    print "binning: ", h1.GetNbinsX(), h2.GetNbinsX()
    #h2.Rebin(5)
    h2_new = extend_hist(h2, h1)
    h1.SetMarkerSize(0)
    h2_new.SetMarkerSize(0)
    ROOT.compare_two_hists(h1, h2_new, "m_{#gamma#gamma} [GeV]",
                           "New", "Old", True)
    f1.Close()
    f2.Close()

def compare_hists(f1_name, f2_name, hist_name):
    f1 = ROOT.TFile.Open(f1_name, "read") # Data
    f2 = ROOT.TFile.Open(f2_name, "read") # MC 
    h1 = f1.Get(hist_name)
    #if "v7" in f1_name:
        #h2.Rebin(5)
    if "solation" in f2_name:
        if "_extend" in f2_name:
            h2 = f2.Get("h_isoshape")
        else:
            h2 = f2.Get("up")
    elif "irreducible" in hist_name:
        h2 = f2.Get("hreluncert_irreducible")
    else:
        h2 = f2.Get(hist_name)
    print "binning: ", h1.GetNbinsX(), h2.GetNbinsX()
    print h2.GetName()
    sys_name = hist_name.split('_')[1]
    factor = 1.0
    is_log = False
    if "bkg_total_gg_full" in hist_name:
        is_log = True
        factor = h1.Integral()/h2.Integral()
    print "intergral: ", h1.Integral(), h2.Integral(), factor
    h2.Scale(factor)
    h1.SetMarkerSize(0)
    h2.SetMarkerSize(0)
    ROOT.compare_two_hists(h1, h2,
                           #"Isolation [GeV]",
                           "m_{#gamma#gamma} [GeV]",
                           sys_name+" from ws", 
                           sys_name+" from original input",
                           is_log)
    f1.Close()
    f2.Close()

def test1():
    f1 = "out_hist_v4.root"
    #f2 = "out_hist_v5.root"
    #f3 = "BkgEstimation_Lin/BkgEstimation_NONE_TOPO_PTDEP_EKHI_Lin.root"
    #f2 = "out_hist_EKEI_v5.root"
    f2 = "out_hist_EKEI_v5_raw.root"
    f3 = "BkgEstimation_Lin/BkgEstimation_NONE_TOPO_PTDEP_EKEI_Lin.root"
    compare(f1, f2, f3)

def test2():
    patterns = ["EKEI", "HKEI", "HKHI", "EKHICal", "EKHI"]
    for pattern in patterns:
        f1 = "ws13TeV/bkg_histFitter_ws_13TeV_"+pattern+".root"
        f2 = "BkgEstimation_Lin/BkgEstimation_NONE_TOPO_PTDEP_"+pattern+"_Lin.root"
        compare_ws_hist(f1, f2)

def get_mass1D(h1, name, start, end):
    h1_proj = h1.ProjectionX(name, start, end)
    h1_proj.Rebin(2)
    h1_proj.Scale(1./h1_proj.Integral())
    return h1_proj

def test3():
    tag = "spin0"
    f1 = ROOT.TFile.Open(tag+"_data.root")
    f2 = ROOT.TFile.Open(tag+"_sherpa.root")
    f3 = ROOT.TFile.Open(tag+"_pythia.root")
    hist_names = [("mass_etabins","m_{#gamma#gamma} [GeV]", 1),
                  ("h_leading_pt", "p_{0}^{T} [GeV]", 1),
                  ("h_subleading_pt", "p_{1}^{T} [GeV]", 1),
                  ("h_leading_eta", "|#eta_{0}|", 0),
                  ("h_subleading_eta", "|#eta_{1}|", 0),
                 ]
    labels = ROOT.std.vector('string')()
    labels.push_back("Data")
    labels.push_back("Sherpa")
    labels.push_back("Pythia")
    for hist,x_title,is_log in hist_names:
        h1 = f1.Get(hist)
        h2 = f2.Get(hist)
        h3 = f3.Get(hist)
        if "mass_etabins" in hist:
            # CC for 0.75
            h1_all = get_mass1D(h1, tag+"_mass_all", 1, 2)
            h2_all = get_mass1D(h2, tag+"_mass_all_sherpa", 1, 2)
            h3_all = get_mass1D(h3, tag+"_mass_all_pythia", 1, 2)
            list_all = ROOT.TList()
            list_all.Add(h1_all)
            list_all.Add(h2_all)
            list_all.Add(h3_all)
            ROOT.compare_hists(list_all, labels,
                               x_title, is_log)

            # CC for 0.75
            h1_cc1 = get_mass1D(h1, tag+"_mass_cc0p75", 1, 1)
            h2_cc1 = get_mass1D(h2, tag+"_mass_cc0p75_sherpa", 1, 1)
            h3_cc1 = get_mass1D(h3, tag+"_mass_cc0p75_pythia", 1, 1)
            list_cc1 = ROOT.TList()
            list_cc1.Add(h1_cc1)
            list_cc1.Add(h2_cc1)
            list_cc1.Add(h3_cc1)
            ROOT.compare_hists(list_cc1, labels,
                               x_title, is_log)
            # other-than CC
            h1_other1 = get_mass1D(h1, tag+"_mass_other0p75", 2, 2)
            h2_other1 = get_mass1D(h2, tag+"_mass_other0p75_sherpa", 2, 2)
            h3_other1 = get_mass1D(h3, tag+"_mass_other0p75_pythia", 2, 2)
            list_other1 = ROOT.TList()
            list_other1.Add(h1_other1)
            list_other1.Add(h2_other1)
            list_other1.Add(h3_other1)
            ROOT.compare_hists(list_other1, labels,
                               x_title, is_log)

            # CC for 1.37
            h1_cc2 = get_mass1D(h1, tag+"_mass_cc1p37", 3, 3)
            h2_cc2 = get_mass1D(h2, tag+"_mass_cc1p37_sherpa", 3, 3)
            h3_cc2 = get_mass1D(h3, tag+"_mass_cc1p37_pythia", 3, 3)
            list_cc2 = ROOT.TList()
            list_cc2.Add(h1_cc2)
            list_cc2.Add(h2_cc2)
            list_cc2.Add(h3_cc2)
            ROOT.compare_hists(list_cc2, labels,
                               x_title, is_log)
            # other-than CC
            h1_other2 = get_mass1D(h1, tag+"_mass_other1p37", 4, 4)
            h2_other2 = get_mass1D(h2, tag+"_mass_other1p37_sherpa", 4, 4)
            h3_other2 = get_mass1D(h3, tag+"_mass_other1p37_pythia", 4, 4)
            list_other2 = ROOT.TList()
            list_other2.Add(h1_other2)
            list_other2.Add(h2_other2)
            list_other2.Add(h3_other2)
            ROOT.compare_hists(list_other2, labels,
                               x_title, is_log)

        else:
            histList = ROOT.TList()
            h1.SetName(tag+"_"+h1.GetName())
            if not "eta" in h1.GetName():
                h1.Scale(1/h1.Integral())
                h2.Scale(1/h2.Integral())
                h3.Scale(1/h3.Integral())
            else:
                h1.Scale(1/h1.Integral("width"), "width")
                h2.Scale(1/h2.Integral("width"), "width")
                h3.Scale(1/h3.Integral("width"), "width")
            histList.Add(h1)
            histList.Add(h2)
            histList.Add(h3)
            ROOT.compare_hists(histList, labels,
                               x_title, is_log)


if __name__ == "__main__":
    #test1()
    #compare_ws_ws("bkg_histFitter_ws_8tev.root",
    #              "results/test_8TeV_combined_meas_model.root")
    #compare_ws_ws("ruggero_template/bkg_histFitter_ws_13TeV_HKHI.root",
    #              "../bkg_histofactory_13TeV/results/HKHI_13TeV_combined_meas_model_nominal.root")
    #compare_ws_hist("bkg_histFitter_ws_13TeV_HKHI_5TeV_v1.root",
    #                "BkgEstimation_NONE_NONE_TOPO_PTDEP_HKHI_Lin_5000GeV_v2.root")

    #compare_hist_hist(
    #    "BkgEstimation_NONE_NONE_TOPO_PTDEP_EKHI_Lin_5000GeV.root",
    #    "/Users/xju/work/diphoton/check_ws/BkgEstimation_Lin/BkgEstimation_NONE_TOPO_PTDEP_EKHI_Lin.root",
    #    "bkg_total_gg_full"
    #)
    #compare_hist_hist(
    #    "IsolationVariation_extend.root",
    #    "/Users/xju/work/diphoton/bkg_histofactory_13TeV/inputs/BkgEstimation_Lin/isolation_shapevariation.root",
    #    "h_isoshape"
    #)
    #if len(sys.argv) < 3:
        #print sys.argv[0]," f1_name f2_name hist_name"
        #sys.exit(1)
    #compare_hists(sys.argv[1], sys.argv[2], sys.argv[3])

    test3()
