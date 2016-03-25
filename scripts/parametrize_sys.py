#!/usr/bin/env python

import ROOT

import AtlasStyle

ROOT.gROOT.SetBatch()
if not hasattr(ROOT, "myLegend"):
    ROOT.gROOT.LoadMacro("/afs/cern.ch/user/x/xju/tool/loader.c") 


def poly_form(order):
    formular = ""
    if order < 0: 
        print "cannot be negative"
        return ""
    for i in range(order+1):
        if i== 0: formular += "["+str(i)+"]"
        else : 
            formular += " + ["+str(i)+"]"
            for j in range(i):
                formular += "*x"
    return formular

def fit_hist_with_poly(h1, order, tag):
    low = h1.GetBinLowEdge(1)
    nbins = h1.GetNbinsX()
    hi = h1.GetBinLowEdge(nbins+1)
    func = ROOT.TF1('func', poly_form(order), low, hi)
    
    canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
    fit_res = h1.Fit(func, "S")
    func.SetLineColor(2)
    h1.GetXaxis().SetTitle("m_{#gamma#gamma} [GeV]")
    h1.Draw()
    func.Draw("same")
    chi2 = fit_res.Chi2()
    x_off = 0.2
    if h1.GetMaximumBin() < nbins/2:
        x_off = 0.5
    ROOT.myText(x_off, 0.8, 1, tag)
    ROOT.myText(x_off, 0.75, 1, "#chi^{2} = "+str(round(chi2,3)))
    canvas.SaveAs(h1.GetName()+"_"+str(order)+"_order.pdf")

def run():
    file_name = "systematics.root"
    f1 = ROOT.TFile.Open(file_name, "read")
    h1 = f1.Get("bkg_irreducible_syst_gg")
    fit_hist_with_poly(h1, 3, "irreducible uncertainty")
    h2 = f1.Get("bkg_reducible_syst_gg")
    fit_hist_with_poly(h2, 4, "reducible uncertainty")
    f1.Close()

def run_purity():
    file_name = "purity.root"
    f1 = ROOT.TFile.Open(file_name, "read")
    h1 = f1.Get("new_bkg_purity_syst_gg")
    fit_hist_with_poly(h1, 4, "purity uncertainty")
    f1.Close()


if __name__ == "__main__":
    run_purity()
