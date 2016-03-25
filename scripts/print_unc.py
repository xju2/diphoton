#!/usr/bin/env python
import ROOT

def read_var(ws, name_list):
    for name in name_list:
        var = ws.var(name)
        if var:
            print name
            var.Print()
            var.Print('v')

def load_additional_class():
    ROOT.gSystem.Load("/afs/cern.ch/user/x/xju/work/lee2d/src/HggTwoSidedCBPdf_cc.so");
    ROOT.gSystem.Load("/afs/cern.ch/user/x/xju/work/lee2d/src/HggScalarLineShapePdf_cc.so");
    ROOT.gSystem.Load("/afs/cern.ch/user/x/xju/work/lee2d/src/HggGravitonLineShapePdf_cc.so");
    ROOT.gSystem.Load("/afs/cern.ch/user/x/xju/work/lee2d/src/FlexibleInterpVarMkII_cc.so");

if __name__ == "__main__":
    load_additional_class()
    np_list = ["uncert_ph_eff_inclusive_13TeV",
               "uncert_ph_iso_inclusive_13TeV",
               "uncertSymm__ATLAS_lumi_2015_signal_inclusive_13TeV",
               "alpha_bkg_isolation"
              ]
    file_name = "2015_Graviton_histfactory_EKHI_v5.root"
    f1 = ROOT.TFile.Open(file_name, "read")
    ws = f1.Get("combWS")
    read_var(ws, np_list)
