#!/usr/bin/env python

import ROOT

def draw_sprious_signal():
    file_name = "inputs/2015_Scalar_2D_v3.root"
    ROOT.gSystem.Load("/afs/cern.ch/user/x/xju/public/src/HggTwoSidedCBPdf_cc.so");
    ROOT.gSystem.Load("/afs/cern.ch/user/x/xju/public/src/HggScalarLineShapePdf_cc.so");
    ROOT.gSystem.Load("/afs/cern.ch/user/x/xju/public/src/HggGravitonLineShapePdf_cc.so");
    ROOT.gSystem.Load("/afs/cern.ch/user/x/xju/public/src/FlexibleInterpVarMkII_cc.so");
    f1 = ROOT.TFile.Open(file_name, "read") 
    ws = f1.Get("combWS")
    poi = ws.Get("xs")
    poi.setVal(0)
    poi.setConstant()
