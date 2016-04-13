#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch()

def find_range(mass, kappa):
    file_name = "2015_Scalar_2D_v4.root"
    ROOT.gSystem.Load("/afs/cern.ch/user/x/xju/public/src/HggTwoSidedCBPdf_cc.so");
    ROOT.gSystem.Load("/afs/cern.ch/user/x/xju/public/src/HggScalarLineShapePdf_cc.so");
    ROOT.gSystem.Load("/afs/cern.ch/user/x/xju/public/src/HggGravitonLineShapePdf_cc.so");
    ROOT.gSystem.Load("/afs/cern.ch/user/x/xju/public/src/FlexibleInterpVarMkII_cc.so");
    
    f1 = ROOT.TFile.Open(file_name)
    ws = f1.Get("combWS")
    mc = ws.obj("ModelConfig")
    print mass,kappa
    mass_var = ws.var("mX")
    mass_var.setRange(mass-20, mass+20)
    mass_var.setVal(mass)
    width_var = ws.var("wX")
    width_var.setVal(kappa)

    sig_pdf = ws.obj("pdf_signal_inclusive_13TeV")
    observables = mc.GetObservables()
    mc.GetParametersOfInterest().Print('v')
    mc.GetNuisanceParameters().Print('v')

    obs = observables.first()
    step = 10
    obs.setRange("rall", 150, 2000)
    over_all = sig_pdf.createIntegral(observables, "rall").getVal()
    print "total: ", over_all
    for i in range(50):
        low_bound = mass - step*i
        up_bound = mass + step*i
        if low_bound < 150: low_bound = 150
        if up_bound > 2000: up_bound = 2000
        obs.setRange("r"+str(i), low_bound, up_bound)
        int_val = sig_pdf.createIntegral(observables,
                                         ROOT.RooFit.Range("r"+str(i))
                                        ).getVal()
        ratio = int_val/over_all
        #print int_val, ratio
        if ratio > 0.9:
            print ratio
            print mass-step*i,mass+step*i
            break

    canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
    obs.Print()
    frame = obs.frame()
    sig_pdf.plotOn(frame)
    frame.Draw()
    canvas.SaveAs("test_bb.pdf")
    f1.Close()
                

if __name__ == "__main__":
    #find_range(300., 18.)
    #find_range(750, 45)
    find_range(1500., 90.)
