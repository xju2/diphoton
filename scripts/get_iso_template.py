#!/usr/bin/env python
"""
get background template from data
"""

import ROOT
import sys

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
    weight = "HGamEventInfoAuxDyn.weight"
    if "data" not in file_name:
        fin = ROOT.TFile.Open(file_name)
        hist_name = "CutFlow_"+file_name.split('/')[-1].split('.')[0]
        hist_event_info = fin.Get(hist_name)
        total_event = hist_event_info.GetBinContent(1)
        weight = ("HGamEventInfoAuxDyn.crossSectionBRfilterEff*"
                  "HGamEventInfoAuxDyn.vertexWeight*"
                  "1000/"+str(total_event)
                 )
    analysis_cuts = (
        "HGamEventInfoAuxDyn.isPassedPreselection &&"
        "HGamEventInfoAuxDyn.isPassedlPtCutsExotic &&"
        "HGamEventInfoAuxDyn.isPassedPID && "
        "HGamEventInfoAuxDyn.m_yy >= 150E3 && "
        "HGamEventInfoAuxDyn.m_yy < 400E3"
    )
    tree = ROOT.loader(file_name, TREE_NAME)
    leading_jet = ROOT.TH1F("leading_jet", "leading_jet", 80, -10, 30)
    subleading_jet = ROOT.TH1F("subleading_jet", "subleading jet", 80, -10, 30)
    leading_iso = ("(HGamPhotonsAuxDyn.topoetcone40[0]/1E3 -"
                   "0.022*HGamPhotonsAuxDyn.pt[0]/1E3)")
    tree.Draw(leading_iso+">>leading_jet",
              "("+analysis_cuts+"&&"+cut+"[0])*"+weight)

    subleading_iso = ("(HGamPhotonsAuxDyn.topoetcone40[1]/1E3 -"
                      "0.022*HGamPhotonsAuxDyn.pt[1]/1E3)")
    tree.Draw(subleading_iso+">>subleading_jet",
              "("+analysis_cuts+"&&"+cut+"[1])*"+weight)


    # invariant mass
    mass = ROOT.TH1F("mass", "inv mass", 670, 150, 3500)
    tree.Draw("HGamEventInfoAuxDyn.m_yy/1E3 >> mass",
              "("+analysis_cuts+")*"+weight)

    fout = ROOT.TFile.Open(out_name, "recreate")
    leading_jet.Write()
    subleading_jet.Write()
    mass.Write()
    fout.Close()
    print out_name, " is written"


if __name__ == "__main__":
    #get_template("sample_data.txt", "jj_template.root", "!HGamPhotonsAuxDyn.isTight")
    #get_template("sample_gg.txt", "gg_template.root", "HGamPhotonsAuxDyn.isTight")
    if len(sys.argv) < 2:
        print sys.argv[0], " file_name"
        sys.exit(1)
    get_template(sys.argv[1], "output_template.root", "HGamPhotonsAuxDyn.isTight")
