#!/usr/bin/env python

import ROOT
import sys
from ROOT import gROOT, gSystem
gROOT.SetBatch()

def get_hist(file_name, out_name):
    gSystem.Load("/afs/cern.ch/user/x/xju/public/src/HggTwoSidedCBPdf_cc.so");
    gSystem.Load("/afs/cern.ch/user/x/xju/public/src/HggScalarLineShapePdf_cc.so");
    gSystem.Load("/afs/cern.ch/user/x/xju/public/src/HggGravitonLineShapePdf_cc.so");
    gSystem.Load("/afs/cern.ch/user/x/xju/public/src/FlexibleInterpVarMkII_cc.so");
    print file_name, out_name
    f1 = ROOT.TFile.Open(file_name)
    ws = f1.Get("combWS")
    pdf = ws.obj("pdf_background_inclusive_13TeV")
    sys_var_list = [
        "alpha_bkg_isolation_13TeV",
        "alpha_bkg_purity_13TeV",
        "alpha_bkg_reducible_13TeV",
        "alpha_bkg_irreducible_13TeV"
    ]
    mc = ws.obj("ModelConfig")
    observables = mc.GetObservables()
    obs = observables.first()
    obs.Print()
    #obs.setRange(200, 3500)
    #nbins = 660
    #obs.setBins(nbins)

    # load nominal snapshot
    ws.loadSnapshot("nominalNuis")
    # create histograms
    hist_nom = pdf.createHistogram("bkg_total_gg_full", obs)
    hist_nom.SetName("bkg_total_gg_full")
    hist_sys_list = []
    for np_name in sys_var_list:
        sys_var = ws.var(np_name)
        if not sys_var:
            print np_name, " does not exit"
        sys_var.setVal(1)
        sys_name = np_name.split("_")[2]
        print sys_name
        hist_name = "bkg_total_gg_full_sys_"+sys_name
        hist_var = pdf.createHistogram(hist_name, obs)
        hist_var.SetName(hist_name)
        hist_sys_list.append(hist_var)
        sys_var.setVal(0)

    ws.loadSnapshot("ucmles")
    hist_ucmles = pdf.createHistogram("bkg_total_gg_full_ucmle", obs)
    hist_ucmles.SetName("bkg_total_gg_full_ucmle")
    f_out = ROOT.TFile(out_name, "recreate")
    hist_nom.Write()
    hist_ucmles.Write()
    for hist in hist_sys_list:
        hist.Write()
        sys_name = hist.GetName().split('_')[-1]
        hist_ratio = hist.Clone("bkg_"+sys_name+"_syst_gg_full")
        hist_ratio.Add(hist_nom, -1)
        hist_ratio.Divide(hist_nom)
        hist_ratio.Write()
    f_out.Close()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print sys.argv[0]," ws_name out_name"
    get_hist(sys.argv[1], sys.argv[2])
