#!/usr/bin/env python

import ROOT
import AtlasStyle
import math
import sys

ROOT.gROOT.SetBatch()
if not hasattr(ROOT, "myLegend"):
    ROOT.gROOT.LoadMacro("/afs/cern.ch/user/x/xju/tool/loader.c") 

def plot_sys(file_name="hists_input_HKHI.root", is_8TeV=False, new_sample=True):
    f2 = ROOT.TFile.Open(file_name, "read")

    h_nom = f2.Get("bkg_nominal")
    #new_sample = True
    if new_sample:
        SUFFIX = "_sys_new" # syst_gg
        prefix = "h_" #bkg_
        h_iso = f2.Get(prefix+"iso"+SUFFIX)
    else:
        SUFFIX = "_syst_gg" # syst_gg
        prefix = "bkg_" #bkg_
        f1 = ROOT.TFile.Open("isolation_sys/hist.root", "read")
        h_iso = f1.Get("bkg_isolation_syst_gg")
    h_purity = f2.Get(prefix+"purity"+SUFFIX)
    h_red = f2.Get(prefix+"reducible"+SUFFIX)
    h_irred = f2.Get(prefix+"irreducible"+SUFFIX)
    h_geo = f2.Get(prefix+"geo"+SUFFIX)


    h_stats = h_nom.Clone("h_stats")
    h_total = h_nom.Clone("h_total")
    print "nbins of nominal shape: ", h_nom.GetNbinsX()
    for ibin in range(h_nom.GetNbinsX()):
        bin_val = h_nom.GetBinContent(ibin+1)
        error = h_nom.GetBinError(ibin+1) / bin_val
        h_stats.SetBinContent(ibin+1, error)
        h_stats.SetBinError(ibin+1, 0)

        purity = h_purity.GetBinContent(ibin+1)
        red = h_red.GetBinContent(ibin+1)
        irred = h_irred.GetBinContent(ibin+1)
        iso = h_iso.GetBinContent(ibin+1)
        if h_geo: geo = h_geo.GetBinContent(ibin+1)
        else: geo = 0
        total = math.sqrt(purity**2+red**2+irred**2+geo**2+iso**2)
        h_total.SetBinContent(ibin+1, total)
        h_total.SetBinError(ibin+1, 0)


    canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
    max_y = h_total.GetMaximum()
    #h_total.GetYaxis().SetRangeUser(-0.010, max_y*1.1)
    h_total.GetYaxis().SetRangeUser(-0.20, 0.8)

    h_total.SetMarkerSize(0.)
    h_purity.SetMarkerSize(0.)
    h_red.SetMarkerSize(0.)
    h_irred.SetMarkerSize(0.)

    h_stats.SetLineColor(ROOT.kOrange)
    h_purity.SetLineColor(8)
    h_red.SetLineColor(4)
    h_irred.SetLineColor(2)
    h_iso.SetLineColor(6)
    h_total.SetFillColor(33)
    h_total.SetLineColor(33)
    h_total.GetXaxis().SetTitle("m_{#gamma#gamma} [GeV]")

    h_total.Draw()
    h_stats.Draw("same HIST")
    h_purity.Draw("same HIST")
    h_red.Draw("same HIST")
    h_irred.Draw("same HIST")
    h_iso.Draw("same HIST")
    if h_geo:
        h_geo.SetLineColor(ROOT.kViolet)
        h_geo.Draw("same HIST")

    leg = ROOT.myLegend(0.2, 0.5, 0.45, 0.80)
    leg.AddEntry(h_total, "total sys", "F")
    leg.AddEntry(h_red, "reducible", "L")
    leg.AddEntry(h_irred, "irreducible", "L")
    leg.AddEntry(h_purity, "purity", "L")
    leg.AddEntry(h_iso, "isolation", "L")
    if h_geo:
        leg.AddEntry(h_geo, "Geo21/Geo20", "L")
    leg.AddEntry(h_stats, "stats", "l")
    leg.Draw()
    ROOT.ATLAS(0.2, 0.9)
    if is_8TeV: ROOT.DATA(0.2, 0.85, 8, 20.3)
    else: ROOT.DATA(0.2, 0.85, 13, 3.2)

    canvas.SaveAs("sys_"+file_name.replace("root", "pdf"))

    f2.Close()

def raw_smooth_cmp():
    # because of different binning, cannot compare
    f1 = ROOT.TFile.Open("systematics.root")
    f2 = ROOT.TFile.Open("test_smooth.root")
    
    sys_list = ["bkg_purity_syst_gg", "bkg_reducible_syst_gg",
                "bkg_irreducible_syst_gg"]
    sys_name = ["purity", "reducible", "irreducible"]
    for sys,name in zip(sys_list, sys_name):
        h1 = f1.Get(sys)
        h2 = f2.Get(sys)

        canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
        h2.Scale(h1.Integral()/h2.Integral())
        print h1.Integral(), h2.Integral()
        h1.SetLineColor(2)
        h2.SetLineColor(4)
        h1.Draw()
        h2.Draw("same")
        leg = ROOT.myLegend(0.7, 0.8, 0.9, 0.9)
        leg.AddEntry(h1, "raw", "L")
        leg.AddEntry(h2, "smooth", "L")
        leg.Draw()
        canvas.SaveAs(h1.GetName()+".pdf")
    
    f1.Close()
    f2.Close()

def plot_overall(file_name = "hists_input_HKHI.root", is_8TeV = False):
    ##have not finished,, plot the m_gg with sys
    f1 = ROOT.TFile.Open(file_name, "read")
    h_nom = f1.Get("bkg_nominal")
    h_nom.SetMarkerSize(0)
    h_purity_up = f1.Get("purity_sys_up")
    h_purity_down = f1.Get("purity_sys_down")
    h_purity_up.SetLineColor(8)
    h_purity_down.SetLineColor(8)
    h_purity_up.SetMarkerSize(0)
    h_purity_down.SetMarkerSize(0)

    h_red_up = f1.Get("reducible_sys_up")
    h_red_down = f1.Get("reducible_sys_down")
    h_red_up.SetLineColor(4)
    h_red_down.SetLineColor(4)
    h_red_up.SetMarkerSize(0)
    h_red_down.SetMarkerSize(0)

    h_irred_up = f1.Get("irreducible_sys_up")
    h_irred_down = f1.Get("irreducible_sys_down")
    h_irred_up.SetLineColor(2)
    h_irred_down.SetLineColor(2)
    h_irred_up.SetMarkerSize(0)
    h_irred_down.SetMarkerSize(0)

    h_geo_up = f1.Get("geo_sys_up")
    h_geo_down = f1.Get("geo_sys_down")
    #h_geo_up.SetLineColor(ROOT.kViolet)
    #h_geo_down.SetLineColor(ROOT.kViolet)
    if h_geo_up:
        h_geo_up.SetLineColor(33)
        h_geo_down.SetLineColor(33)
        h_geo_up.SetMarkerSize(0)
        h_geo_down.SetMarkerSize(0)

    canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
    canvas.SetLogy()
    h_nom.GetXaxis().SetTitle("m_{#gamma#gamma} [GeV]")
    h_purity_up.GetXaxis().SetTitle("m_{#gamma#gamma} [GeV]")

    h_bkgs = ROOT.TList()
    h_bkgs.Add(h_purity_up)
    h_bkgs.Add(h_purity_down)
    h_bkgs.Add(h_red_up)
    h_bkgs.Add(h_red_down)
    h_bkgs.Add(h_irred_up)
    h_bkgs.Add(h_irred_down)
    if h_geo_up:
        h_bkgs.Add(h_geo_up)
        h_bkgs.Add(h_geo_down)

    c1 = ROOT.add_ratio_pad(h_nom, h_bkgs)
    c1.SetLogy()
    
    h_nom.Draw();
    if h_geo_up:
        h_geo_up.Draw("same")
        h_geo_down.Draw("same")
    h_irred_up.Draw("same")
    h_irred_down.Draw("same")
    h_purity_up.Draw("same")
    h_purity_down.Draw("same")
    h_red_up.Draw("same")
    h_red_down.Draw("same")
    h_nom.Draw("same")


    leg = ROOT.myLegend(0.6, 0.6, 0.9, 0.9)
    leg.AddEntry(h_nom, "nominal", "F")
    leg.AddEntry(h_red_up, "reducible", "L")
    leg.AddEntry(h_irred_up, "irreducible", "L")
    leg.AddEntry(h_purity_up, "purity", "L")
    if h_geo_up:
        leg.AddEntry(h_geo_up, "Geo21/Geo20", "L")
    leg.Draw()

    ROOT.ATLAS(0.3, 0.85)
    if is_8TeV: ROOT.DATA(0.3, 0.80, 8, 20.3)
    else: ROOT.DATA(0.3, 0.80, 13, 3.2)
    
    canvas.SaveAs("mgg_sys_"+file_name.replace("root","pdf"))


if __name__ == "__main__":
    if len(sys.argv) < 3: 
        print sys.argv[0]," hist_input is_8TeV newsample"
        sys.exit(1)

    input_name = sys.argv[1]
    is_8TeV = bool(int(sys.argv[2]))
    new_sample = bool(int(sys.argv[3]))

    print input_name, is_8TeV, new_sample
    plot_sys(input_name, is_8TeV, new_sample)
    #plot_overall(input_name, is_8TeV)
