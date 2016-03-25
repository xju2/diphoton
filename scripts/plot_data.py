#!/usr/bin/env python

import ROOT
import AtlasStyle

ROOT.gROOT.SetBatch()
if not hasattr(ROOT, "myLegend"):
    ROOT.gROOT.LoadMacro("/afs/cern.ch/user/x/xju/tool/loader.c") 

def plot():
    file_name = "Bkg_Total_allcat_TOPO_PTDEP_8.0_lead50_sublead50_norm17_62_linear.root"
    f1 = ROOT.TFile.Open(file_name, "read")
    h1 = f1.Get("mgg_data")
    h2 = f1.Get("bkg_total_gg_full")
    h1.Rebin(10)
    h2.Rebin(10)

    canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
    h1.SetMarkerSize(0.5)
    h2.SetLineColor(4) 
    h2.SetMarkerSize(0)
    h2.GetXaxis().SetTitle("m_{#gamma#gamma} [GeV]")
    
    c1 = ROOT.add_ratio_pad(h1, h2)
    c1.SetLogy()
    h1.Draw("EP")
    h2.Draw("same HIST")

    leg = ROOT.myLegend(0.6, 0.8, 0.9, 0.9)
    leg.AddEntry(h1, "data", "LP")
    leg.AddEntry(h2, "MC", "L")
    leg.Draw()
    canvas.SaveAs("data.pdf")


if __name__ == "__main__":
    plot()
