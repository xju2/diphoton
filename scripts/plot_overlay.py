#!/bin/env python

import ROOT
import AtlasStyle
import math
from new_sys import create_sys_hist
from new_sys import truncate_hist

ROOT.gROOT.SetBatch()
if not hasattr(ROOT, "myLegend"):
    ROOT.gROOT.LoadMacro("/afs/cern.ch/user/x/xju/tool/loader.c") 

def plot_frame(f1_name, f2_name):
    f1 = ROOT.TFile.Open(f1_name, "read")
    f2 = ROOT.TFile.Open(f2_name, "read")
    frame1 = f1.Get("frame_obs_x_channel_4597820")
    frame2 = f2.Get("frame_atlas_invMass_44e4a50")
    canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
    canvas.SetLogy();
    frame2.Draw()
    frame1.Draw("same")
    canvas.SaveAs("over_lay.pdf")
    f1.Close()
    f2.Close()


def overlay( f_func = "out_function.root", 
           f_template = "out_template.root",
           tag = "EKEI",
           frame_name = "frame_atlas_invMass_165fca0",
           is_splusb = False):
    f_sys = "inputs/BkgEstimation_Lin/BkgEstimation_NONE_TOPO_PTDEP_"+tag+"_Lin.root"
    f1 = ROOT.TFile.Open(f_func, "read")
    f2 = ROOT.TFile.Open(f_template, "read")
    f3 = ROOT.TFile.Open(f_sys, "read")

    if "HKHI" in tag: 
        h_bkg_fitted_template = f2.Get("hist_bkg_inclusive_13TeV__obs_x_chan_HKHI_13TeV").Rebin(4)
    else:
        h_bkg_fitted_template = f2.Get("hist_bkg_inclusive_13TeV__obs_x_channel").Rebin(4)
    h_bkg_fitted_template.SetLineColor(2)
    h_bkg_fitted_template.GetXaxis().SetTitle("m_{#gamma#gamma} [GeV]")
    h_template_error_band = f2.Get(frame_name)
    h_frame = f1.Get(frame_name)

    h_func_norm = f1.Get("nominal")
    h_func_err_band = f1.Get("error_band")
    #ROOT.print_graph(h_func_norm)
    #ROOT.print_graph(h_func_err_band)
    n_points = h_func_norm.GetN()
    integral_norm = h_func_norm.Integral(1, n_points-2)
    integral_err =  h_func_err_band.Integral(1, n_points-2)
    print "nominal: ", integral_norm, ROOT.sum_graph_entries(h_func_norm, 200,
                                                             2000, 90)
    print "error: ", integral_err, ROOT.sum_graph_entries(h_func_err_band, 200,
                                                          2000, 90)
    
    step = 20
    h_data = truncate_hist(f3.Get("mgg_data").Rebin(step), "data")
    h_nom = truncate_hist(f3.Get("bkg_total_gg_full").Rebin(step), 
                          "bkg_total_gg")
    h_purity = truncate_hist(f3.Get("bkg_purity_syst_gg_full").Rebin(step),
                             "bkg_purity_syst_gg")
    h_red = truncate_hist(f3.Get("bkg_reducible_syst_gg_full").Rebin(step),
                          "bkg_reducible_syst_gg")
    h_irred = truncate_hist(f3.Get("bkg_irreducible_syst_gg_full").Rebin(step),
                            "bkg_irreducible_syst_gg")
    ## the uncertainties need to be scaled down
    h_purity.Scale(1./step)
    h_red.Scale(1./step)
    h_irred.Scale(1./step)

    print h_nom.GetNbinsX(), h_bkg_fitted_template.GetNbinsX()

    h_total_uncer = h_nom.Clone("total_uncertainty")
    for ibin in range(1, h_nom.GetNbinsX()+1):
        mass = h_nom.GetBinCenter(ibin)
        stats = h_nom.GetBinError(ibin)
        purity = h_purity.GetBinContent(ibin)
        red = h_red.GetBinContent(ibin)
        irred = h_irred.GetBinContent(ibin)
        val = h_nom.GetBinContent(ibin)
        total = math.sqrt(stats**2+(purity*val)**2+(red*val)**2+(irred*val)**2)
        if False: print "{:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f}".format(mass,stats,
                                                                 purity, red,
                                                                 irred,
                                                                 total/val)
        h_total_uncer.SetBinContent(ibin, val)
        h_total_uncer.SetBinError(ibin, total)
    h_total_uncer.SetLineColor(4)
    h_total_uncer.SetMarkerSize(0)
    h_total_uncer.SetFillColor(33)
    


    h_func_ratio = h_bkg_fitted_template.Clone("h_func_ratio")
    nbins = h_func_ratio.GetNbinsX()
    for ibin in range(1, nbins+1):
        x_val = h_func_ratio.GetBinCenter(ibin)
        x_low = h_func_ratio.GetBinLowEdge(ibin)
        x_hi = x_low + h_func_ratio.GetBinWidth(ibin)
        func_nom = h_func_norm.average(x_low, x_hi)
        func_error = abs(h_func_err_band.average(x_low, x_hi)-func_nom)
        temp_nom = h_total_uncer.GetBinContent(ibin)
        temp_err = h_total_uncer.GetBinError(ibin)
        ratio = func_nom/temp_nom
        error = ratio*math.sqrt((func_error/func_nom)**2 + (temp_err/temp_nom)**2)
        if False:
            print "{:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f} ".format(x_val, 
                            func_nom, func_error, temp_nom, temp_err,
                            ratio, error)
        h_func_ratio.SetBinContent(ibin, ratio)
        h_func_ratio.SetBinError(ibin, error)

    h_func_ratio.SetLineColor(ROOT.kOrange+1)
    h_func_ratio.SetFillColor(ROOT.kGreen)
    h_func_ratio.SetFillStyle(3144)
    h_func_ratio.SetMarkerSize(0)


    canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
    pad1 = ROOT.TPad("pad1", "pad1", 0, 0.15, 1.0, 1.0)
    pad1.SetBottomMargin(0.161)
    pad2 = ROOT.TPad("pad2", "pad2", 0, 0.01, 1.0, 0.286)
    pad2.SetBottomMargin(0.28)
    pad1.Draw()
    pad2.Draw()

    pad2.cd()
    h_bkg_temp_ratio = h_bkg_fitted_template.Clone("bkg_temp_ratio")
    ROOT.SetAtlasHist(h_bkg_temp_ratio)
    h_bkg_temp_ratio.GetYaxis().SetTitleSize(0.10);
    h_bkg_temp_ratio.GetYaxis().SetTitle("ratio w.r.t pre-fit MC")
    max_y = 1.8
    if is_splusb: 
        if "EKHI" in tag or "EKEI" in tag: max_y = 2.5 
        else: max_y = 3.5
    h_bkg_temp_ratio.GetYaxis().SetRangeUser(0.45, max_y)
    h_bkg_temp_ratio.Divide(h_total_uncer)
    h_bkg_temp_ratio.Draw("HIST")

    #gr_ratio = ROOT.TH1TOTGraph(h_func_ratio)
    #gr_ratio.Draw("3")
    h_func_ratio.Draw("SAME E3")
    h_func_ratio_cp = h_func_ratio.Clone("h_func_ratio_cp")
    h_func_ratio_cp.SetFillColor(0)

    h_total_uncer_cp_err = h_total_uncer.Clone("signal_error")
    h_total_uncer_cp_err.Divide(h_total_uncer)
    h_total_uncer_cp_err.SetFillColor(h_total_uncer.GetFillColor())
    h_total_uncer_cp_err.Draw("SAME E3")
    h_total_uncer_cp_err_cp = h_total_uncer_cp_err.Clone("signal_error_cp")
    h_total_uncer_cp_err_cp.SetFillColor(0)
    h_total_uncer_cp_err_cp.Draw("SAME HIST")
    h_bkg_temp_ratio.Draw("HIST SAME")
    h_func_ratio_cp.Draw("SAME HIST")
    

    pad1.cd()
    pad1.SetLogy()
    h_data.GetYaxis().SetTitle("Events / 20 GeV")
    h_data.GetYaxis().SetRangeUser(5E-2, 5E4)
    h_data.SetMarkerSize(0.8)
    h_data.Draw()
    h_frame.Draw("same")
    h_total_uncer.Draw("same E3")
    h_total_copy = h_total_uncer.Clone("total_copy")
    h_total_copy.SetFillColor(0)
    h_total_copy.Draw("same HIST")
    h_data.Draw("same")
    h_func_norm.Draw("same")
    h_func_norm.SetLineColor(ROOT.kOrange+1)

    if h_template_error_band:
        h_template_error_band.Draw("same")
    h_bkg_fitted_template.Draw("same")
    h_data.Draw("same")


    #add legend
    x_off = 0.4
    leg = ROOT.myLegend(x_off-0.010, 0.59, 0.85, 0.79)
    leg.AddEntry(h_data, "data", "PL")
    leg.AddEntry(h_total_uncer, "pre-fit, MC template", "LF")
    leg.AddEntry(h_func_ratio, "post-fit, floating bkg", "LF")
    leg.AddEntry(h_bkg_fitted_template, "post-fit, MC template", "L")
    leg.Draw()

    ROOT.ATLAS(x_off, 0.89)
    ROOT.DATA(x_off, 0.84, 13, 3.2)
    fit_des = "B-only Fit"
    fit_tag = "bonly"
    if is_splusb: 
        fit_des = "S+B Fit"
        fit_tag = "splusb"
    if "EKHI" in tag:
        des =  "Graviton tight selection, " + fit_des
    elif "EKEI" in tag:
        des = "Graviton loose selection, " + fit_des
    else:
        des = "Scalar selection, " + fit_des
    ROOT.myText(x_off, 0.80, 1, des)
    
    canvas.SaveAs("results/overlay_13TeV_"+tag+"_"+fit_tag+".pdf")

    f1.Close()
    f2.Close()
    f3.Close()


if __name__ == "__main__":
    #plot_frame("out_template.root", "out_function.root")
    paras = [
        #("EKEI", "frame_atlas_invMass_2d61800"), 
        #("EKHI", "frame_atlas_invMass_26b1d70"), 
        #("HKHI", "frame_obs")

        #("EKEI", "frame_obs"), 
        ("EKHI", "frame_obs"), 
        ("HKHI", "frame_obs")
    ]
    is_splusb = True
    for par in paras:
        tag, frame_name = par
        overlay("out_function_"+tag+".root",
                "out_template_"+tag+".root",
                tag, 
                frame_name, 
                is_splusb
            )
