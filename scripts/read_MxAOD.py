#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch()
if not hasattr(ROOT, "myLegend"):
    ROOT.gROOT.LoadMacro("/afs/cern.ch/user/x/xju/tool/loader.c") 

def pass_presel(ph_pt, abs_eta, is_tight):
    res = True 
    if ph_pt <= 30: res = False
    if abs_eta >= 2.37 or (abs_eta > 1.37 and abs_eta < 1.52): res = False
    if not is_tight: False 
    return res

def plot_hist(file_name = "test.root"):
    f1 = ROOT.TFile.Open(file_name, "read")
    hist_2D = f1.Get("h_myy_2D")
    
    cut_index = 4*0;
    h_all = hist_2D.ProjectionX("all_"+str(cut_index), cut_index+1, cut_index+4)
    h_BB = hist_2D.ProjectionX("BB_"+str(cut_index), cut_index+1, cut_index+1)
    h_BE = hist_2D.ProjectionX("BE_"+str(cut_index), cut_index+2, cut_index+2)
    h_EB = hist_2D.ProjectionX("EB_"+str(cut_index), cut_index+3, cut_index+3)
    h_EE = hist_2D.ProjectionX("EE_"+str(cut_index), cut_index+4, cut_index+4)

    canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
    canvas.SetLogy()
    h_all.Draw()

    h_BB.SetLineColor(2)
    h_BE.SetLineColor(4)
    h_EB.SetLineColor(ROOT.kOrange)
    h_EE.SetLineColor(8)

    h_BB.Draw("same")
    h_BE.Draw("same")
    h_EB.Draw("same")
    h_EE.Draw("same")
    canvas.SaveAs("comp_EKEI.pdf")
    f1.Close()

    

def read_MxAOD():
    file_name = "root://eosatlas//eos/atlas/atlascerngroupdisk/phys-higgs/HSG1/MxAOD/h011/data_25ns/data15_13TeV.periodAll25ns.physics_Main.MxAOD.p2425.h011.root"

    ## setup RootCore
    ROOT.gROOT.Macro("$ROOTCOREDIR/scripts/load_packages.C")
    if not ROOT.xAOD.Init().isSuccess() :
        print "Failed xAOD.Init()"

    tree_name = "CollectionTree"
    f_in = ROOT.TFile.Open(file_name)
    #tree = ROOT.xAOD.MakeTransientTree(f_in, tree_name) ## not needed
    tree = f_in.Get(tree_name) 

    nentries = tree.GetEntries()
    print "Number of input events: %s" % nentries
    
    ## print attributes
    #attrs = vars(tree)
    #print ', '.join("%s: %s" % item for item in attrs.items())
    #tree.Print()
    
    f_out = ROOT.TFile.Open("test.root", 'recreate')
    ## 2D histogram storing: 
    ## BB BE EB EE x EKEI EKHI HKEI HKHI
    h_myy_2D = ROOT.TH2F("h_myy_2D", "inv mass", 36, 200, 2000, 
                           17, -0.5, 16.5)
    h_myy_all = ROOT.TH1F("h_myy_all", "inv mass", 36, 200, 2000)

    for ientry in xrange(nentries):
        tree.GetEntry(ientry)
       
        weights = getattr(tree, "HGamEventInfoAuxDyn.weight")
        br_passPreSelection = getattr(tree, "HGamEventInfoAuxDyn.isPassedPreselection")
        if not br_passPreSelection: continue   ## at least two loose photons

        br_passTight = getattr(tree, "HGamEventInfoAuxDyn.isPassedPID")
        br_passEK = getattr(tree, "HGamEventInfoAuxDyn.isPassedlPtCutsExotic")
        br_passEI = getattr(tree, "HGamEventInfoAuxDyn.isPassedIsolationExotic")
        br_passHK = getattr(tree, "HGamEventInfoAuxDyn.isPassedRelPtCuts")
        br_passHI = getattr(tree, "HGamEventInfoAuxDyn.isPassedIsolation")
        br_myy = getattr(tree, "HGamEventInfoAuxDyn.m_yy")


        ## photon selections
        br_isTight = getattr(tree, "HGamPhotonsAuxDyn.isTight")
        br_pt = getattr(tree, "HGamPhotonsAuxDyn.pt")
        br_etcone40 = getattr(tree, "HGamPhotonsAuxDyn.topoetcone40")
        br_ptcone20 = getattr(tree, "HGamPhotonsAuxDyn.ptcone20")
        br_isEMTight = getattr(tree, "HGamPhotonsAuxDyn.isEMTight")
        br_eta_s2 = getattr(tree, "HGamPhotonsAuxDyn.eta_s2")
        
        y_index = -1
        if abs(br_eta_s2[0]) <= 1.37 and abs(br_eta_s2[1]) <= 1.37:
            y_index = 0
        elif abs(br_eta_s2[0]) <= 1.37 and abs(br_eta_s2[1]) >= 1.52:
            y_index = 1
        elif abs(br_eta_s2[0]) >= 1.52 and abs(br_eta_s2[1]) <= 1.37:
            y_index = 2
        elif abs(br_eta_s2[0]) >= 1.52 and abs(br_eta_s2[1]) >= 1.52:
            y_index = 3
        else:
            y_index = -1

        if y_index < 0: continue
        
        if br_passTight and br_passEK and br_passEI:
            h_myy_2D.Fill(br_myy/1E3, y_index, weights)
            h_myy_all.Fill(br_myy/1E3, weights)
        elif br_passTight and br_passEK and br_passHI:
            h_myy_2D.Fill(br_myy/1E3, y_index+4, weights)
        elif br_passTight and br_passHK and br_passEI:
            h_myy_2D.Fill(br_myy/1E3, y_index+4*2, weights)
        elif br_passTight and br_passHK and br_passHI:
            h_myy_2D.Fill(br_myy/1E3, y_index+4*3, weights)
        else:
            pass

    f_out.cd()
    h_myy_2D.Write()
    h_myy_all.Write()
    f_out.Close()

    f_in.Close()

if __name__ == "__main__":
    read_MxAOD()
