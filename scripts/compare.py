#!/usr/bin/env python

import ROOT
import AtlasStyle
import new_sys

ROOT.gROOT.SetBatch()
if not hasattr(ROOT, "myLegend"):
    ROOT.gROOT.LoadMacro("/afs/cern.ch/user/x/xju/tool/loader.c") 

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
    bkg_f2.Rebin(5)

    ws = f1.Get("combined")
    pdf = ws.obj("channel_model")
    obs = ws.var("obs_x_channel")
    obs.setRange(200, 3500)
    nbins = 660
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
    #obs.setRange(200, 3500)
    #nbins = 660
    #bkg_f1 = pdf.createHistogram(hist_name, obs, ROOT.RooFit.Binning(nbins))
    bkg_f1 = pdf.createHistogram(hist_name, obs)
    return bkg_f1

def compare_ws_ws(f1_name, f2_name):
    f1 = ROOT.TFile.Open(f1_name, "read") ## workspace
    f2 = ROOT.TFile.Open(f2_name, "read") ## mine
    if not f1 or not f2: return None

    f3_name = "Bkg_Total_allcat_TOPO_PTDEP_8.0_lead50_sublead50_norm17_62_linear.root"
    f3 = ROOT.TFile.Open(f3_name, "read")
    bkg_f3_org = f3.Get("bkg_total_gg_full")
    bkg_f3 = new_sys.truncate_hist(bkg_f3_org, "bkg_f3")

    ws1 = f1.Get("combined")
    ws2 = f2.Get("combined")

    bkg_f1 = create_hist_from_ws(ws1, "channel", "bkg_f1")
    bkg_f2 = create_hist_from_ws(ws2, "chan_8TeV", "bkg_f2")

    bkg_f1.Scale(bkg_f2.Integral()/bkg_f1.Integral())
    bkg_f3.Scale(bkg_f2.Integral()/bkg_f3.Integral())

    bkg_f1.SetLineColor(2)
    bkg_f2.SetLineColor(4)
    bkg_f1.SetMarkerSize(0)
    bkg_f2.SetMarkerSize(0)
    bkg_f3.SetMarkerSize(0)

    canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
    #canvas.SetLogy()
    h_bkgs = ROOT.TList()
    h_bkgs.Add(bkg_f1)
    h_bkgs.Add(bkg_f2)
    c1 = ROOT.add_ratio_pad(bkg_f3, h_bkgs)
    c1.SetLogy()
    bkg_f1.Draw()
    bkg_f2.Draw("same")
    bkg_f3.Draw("same")


    legend = ROOT.myLegend(0.7, 0.8, 0.9, 0.9)
    legend.AddEntry( bkg_f1, "Rugero", "L")
    legend.AddEntry( bkg_f2, "XY", "L")
    legend.AddEntry( bkg_f3, "input hist", "L")
    legend.Draw()
    canvas.SaveAs(f1_name.replace("root", "pdf"))

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

if __name__ == "__main__":
    #test1()
    compare_ws_ws("bkg_histFitter_ws_8tev.root",
                  "results/test_8TeV_combined_meas_model.root")