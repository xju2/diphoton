#!/usr/bin/env python

import ROOT
def read_MxAOD():
    file_name = "root://eosatlas//eos/atlas/atlascerngroupdisk/phys-higgs/HSG1/MxAOD/h011/data_25ns/data15_13TeV.periodAll25ns.physics_Main.MxAOD.p2425.h011.root"

    ## setup RootCore
    ROOT.gROOT.Macro("$ROOTCOREDIR/scripts/load_packages.C")
    if not ROOT.xAOD.Init().isSuccess() :
        print "Failed xAOD.Init()"

    tree_name = "CollectionTree"
    f_in = ROOT.TFile.Open(file_name)
    tree = ROOT.xAOD.MakeTransientTree(f_in, tree_name)
    nentries = tree.GetEntries()
    print "Number of input events: %s" % nentries
    for entry in xrange(0,10):
        tree.GetEntry(entry)

        if not tree.EventInfo.passTrig_HLT_g35_loose_g25_loose:
            continue

        ## photon selections
        for ph_id in range(tree.HGamPhotons.size()):
            ph = tree.HGamPhotons.at(ph_id)
            is_tight = tree.HGamPhotons.isTight


if __name__ == "__main__":
    read_MxAOD()
