#!/usr/bin/env python
"""
get background template from data
"""

import ROOT

__version__ = "$Revision$"

TREE_NAME = "CollectionTree"

if not hasattr(ROOT, "myLegend"):
    ROOT.gROOT.LoadMacro("/afs/cern.ch/user/x/xju/tool/loader.c")
ROOT.gROOT.SetBatch(True)

def get_template(file_name, out_name, cut):
    """
    get background template from file_name
    """
    print "processing ", file_name
    analysis_cuts = ("HGamEventInfoAuxDyn.isPassedPreselection &&"
                     "HGamEventInfoAuxDyn.isPassedlPtCutsExotic") # exotic KE cuts
    tree = ROOT.loader(file_name, TREE_NAME)
    leading_jet = ROOT.TH1F("leading_jet", "leading_jet", 100, -10, 60)
    subleading_jet = ROOT.TH1F("subleading_jet", "subleading jet", 100, -10, 60)
    leading_iso = ("(HGamPhotonsAuxDyn.topoetcone40[0]/1E3 -"
                   "0.022*HGamPhotonsAuxDyn.pt[0]/1E3)")
    tree.Draw(leading_iso+">>leading_jet",
              "("+analysis_cuts+"&&"+cut+"[0])*HGamEventInfoAuxDyn.weight")

    subleading_iso = ("(HGamPhotonsAuxDyn.topoetcone40[1]/1E3 -"
                      "0.022*HGamPhotonsAuxDyn.pt[1]/1E3)")
    tree.Draw(subleading_iso+">>subleading_jet",
              "("+analysis_cuts+"&&"+cut+"[1])*HGamEventInfoAuxDyn.weight")
    fout = ROOT.TFile.Open(out_name, "recreate")
    leading_jet.Write()
    subleading_jet.Write()
    fout.Close()
    print out_name, " is written"


if __name__ == "__main__":
    #get_template("sample_data.txt", "jj_template.root", "!HGamPhotonsAuxDyn.isTight")
    #get_template("sample_gg.txt", "gg_template.root", "HGamPhotonsAuxDyn.isTight")
    get_template("sample_data.txt", "data_template.root", "HGamPhotonsAuxDyn.isTight")
