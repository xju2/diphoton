#!/usr/bin/env python
"""
Read MxAOD from Hyy group and produce histograms
"""
from multiprocessing import Pool
import time
import ROOT
import sys
ROOT.gROOT.SetBatch(True)

__version__ = "$Revision$"

TREE_NAME = "CollectionTree"

if not hasattr(ROOT, "myLegend"):
    ROOT.gROOT.LoadMacro("/afs/cern.ch/user/x/xju/tool/loader.c")

def pass_presel(ph_pt, abs_eta, is_tight):
    res = True
    if ph_pt <= 30:
        res = False
    if abs_eta >= 2.37 or (abs_eta > 1.37 and abs_eta < 1.52):
        res = False
    if not is_tight:
        res = False
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

def read_MxAOD(input_args):
    if len(input_args) < 4:
        print "Inputs are wrong"
        return
    file_name, out_name, istart, iend = input_args
    print "file_name: ", file_name
    print "out_name: ", out_name
    print "start: ", istart
    print "end: ", iend

    ## setup RootCore
    #ROOT.gROOT.Macro("$ROOTCOREDIR/scripts/load_packages.C")
    #if not ROOT.xAOD.Init().isSuccess() :
    #    print "Failed xAOD.Init()"
    fin = ROOT.TFile.Open(file_name)
    hist_name = "CutFlow_"+file_name.split('/')[-1].split('.')[0]
    hist_event_info = fin.Get(hist_name)
    total_event = -1
    is_data = "data" in file_name
    if hist_event_info:
        total_event = hist_event_info.GetBinContent(1)
    else:
        print "cannot find total events: ", hist_name
        if not is_data:
            sys.exit(1)

    tree = ROOT.loader(file_name, TREE_NAME)
    LUMI = 1000.

    nentries = tree.GetEntries()
    print "Number of input events: %s" % nentries

    f_out = ROOT.TFile.Open(out_name, 'recreate')
    ## 2D histogram storing:
    ## BB BE EB EE x EKEI EKHI HKEI HKHI
    num_y_bins = 50
    h_myy_2D = ROOT.TH2F("h_myy_2D", "inv mass", 36, 200, 2000,
                         num_y_bins, -0.5, 0.5+num_y_bins)
    h_myy_all = ROOT.TH1F("h_myy_all", "inv mass", 36, 200, 2000)

    # isolation is defined as: etcone40 - 0.022*ET
    h_leading_etcone40_2D = ROOT.TH2F("h_leading_etcone40_2D",
                                      "etcone40 leading photon",
                                      100, -10, 60,
                                      num_y_bins+1, -0.5, 0.5+num_y_bins)
    h_subleading_etcone40_2D = ROOT.TH2F("h_subleading_etcone40_2D",
                                         "etcone40 subleading photon",
                                         100, -10, 60,
                                         num_y_bins+1, -0.5, .5+num_y_bins)
    # record how long it takes to loop
    start_time = time.time()
    for ientry in xrange(istart, iend):
        if ientry < 0 or ientry > nentries:
            break
        tree.GetEntry(ientry)
        if ientry % 5E5 == 0:
            print "processed, ", ientry - istart, \
                    "with time: ", (time.time()-start_time)/60.

        br_passPreSelection = getattr(tree, "HGamEventInfoAuxDyn.isPassedPreselection")
        br_myy = getattr(tree, "HGamEventInfoAuxDyn.m_yy")
        br_passTight = getattr(tree, "HGamEventInfoAuxDyn.isPassedPID")
        if not br_passPreSelection or br_myy < 150E3 or not br_passTight:
            continue   ## at least two loose photons

        br_passEK = getattr(tree, "HGamEventInfoAuxDyn.isPassedlPtCutsExotic")
        br_passEI = getattr(tree, "HGamEventInfoAuxDyn.isPassedIsolationExotic")
        br_passHK = getattr(tree, "HGamEventInfoAuxDyn.isPassedRelPtCuts")
        br_passHI = getattr(tree, "HGamEventInfoAuxDyn.isPassedIsolation")

        #weights = getattr(tree, "HGamEventInfoAuxDyn.weight") ## vertext * pileup
        vertexWeight = getattr(tree, "HGamEventInfoAuxDyn.vertexWeight")
        conversionType = getattr(tree, "HGamPhotonsAuxDyn.conversionType")
        # not applying pileup weights!
        if not is_data:
            crossSectionBRfilterEff = getattr(tree, "HGamEventInfoAuxDyn.crossSectionBRfilterEff")
            weights = crossSectionBRfilterEff*vertexWeight*LUMI/total_event
        else:
            weights = 1.0


        # photon selections
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

        if y_index < 0:
            continue

        leading_iso = br_etcone40[0]/1E3 - br_pt[0]*0.022/1E3
        subleading_iso = br_etcone40[1]/1E3 - br_pt[1]*0.022/1E3
        if  br_passEK and br_passEI:
            h_myy_2D.Fill(br_myy/1E3, y_index, weights)
            h_myy_all.Fill(br_myy/1E3, weights)
            h_leading_etcone40_2D.Fill(leading_iso, y_index, weights)
            h_subleading_etcone40_2D.Fill(subleading_iso, y_index, weights)

        if  br_passEK and br_passHI:
            h_myy_2D.Fill(br_myy/1E3, y_index+4, weights)
            h_leading_etcone40_2D.Fill(leading_iso, y_index+4, weights)
            h_subleading_etcone40_2D.Fill(subleading_iso, y_index+4, weights)

        if  br_passHK and br_passEI:
            h_myy_2D.Fill(br_myy/1E3, y_index+4*2, weights)
            h_leading_etcone40_2D.Fill(leading_iso, y_index+4*2, weights)
            h_subleading_etcone40_2D.Fill(subleading_iso, y_index+4*2, weights)

        if  br_passHK and br_passHI:
            h_myy_2D.Fill(br_myy/1E3, y_index+4*3, weights)
            h_leading_etcone40_2D.Fill(leading_iso, y_index+4*3, weights)
            h_subleading_etcone40_2D.Fill(subleading_iso, y_index+4*3, weights)

        if  br_passEK:
            h_myy_2D.Fill(br_myy/1E3, y_index+4*4, weights)
            h_leading_etcone40_2D.Fill(leading_iso, y_index+4*4, weights)
            h_subleading_etcone40_2D.Fill(subleading_iso, y_index+4*4, weights)

        if  br_passHK:
            h_myy_2D.Fill(br_myy/1E3, y_index+4*5, weights)
            h_leading_etcone40_2D.Fill(leading_iso, y_index+4*5, weights)
            h_subleading_etcone40_2D.Fill(subleading_iso, y_index+4*5, weights)

    end_time = time.time()
    print "processed time: ", (end_time-start_time)/3600, "H"
    f_out.cd()
    h_myy_2D.Write()
    h_myy_all.Write()
    h_leading_etcone40_2D.Write()
    h_subleading_etcone40_2D.Write()
    f_out.Close()

def process(file_name, njobs):
    args = []
    tree = ROOT.loader(file_name, TREE_NAME)
    total_entries = tree.GetEntries()
    entries_each_job = total_entries/njobs
    print "processing: ", file_name
    print "total entries: ", total_entries
    print "njobs: ", njobs
    print "entries per job: ", entries_each_job
    if njobs > 0:
        for ijob in range(njobs + 1):
            args.append( (file_name, "job_"+str(ijob)+".root",
                        ijob*entries_each_job,
                        (ijob+1)*entries_each_job)
                       )
        p = Pool(njobs)
        p.map(read_MxAOD, args)
    else:
        read_MxAOD( (file_name, "all_jobs.root", 0, total_entries) )

if __name__ == "__main__":
    #TEST_NAME = ("root://eosatlas//eos/atlas/atlascerngroupdisk/phys-higgs/"
    #             "HSG1/MxAOD/h011/mc_25ns/Sherpa_gamgam_2DP20_650-1000.MxAOD._p247.h011.root")
    #GG_SAMPLES = "sample_gg.txt"
    if len(sys.argv) < 2:
        print sys.argv[0]," file_name"
        sys.exit(1)

    process(sys.argv[1], -1)
