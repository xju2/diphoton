#!/usr/bin/env python
import ROOT
from ROOT import RooArgSet

bin_low = 200
bin_hi = 3000
nbins = (bin_hi - bin_low)/5

def curve_purity(h1):
    if not h1: return None
    hnew = h1.Clone("new_"+h1.GetName())
    bin_1500 = h1.FindBin(1500)
    bin_2000 = h1.FindBin(2000)
    bin_2500 = h1.FindBin(2500)
    nbins_15_25 = bin_2500 - bin_1500
    #mean = h1.Integral(bin_1500, bin_2500)/nbins_15_25
    #mean = h1.Integral(bin_1500, bin_2000)/nbins_15_25
    mean = h1.GetBinContent(bin_1500)
    for i in range(bin_1500, bin_2500, 1):
        hnew.SetBinContent(i, mean)
    return hnew

def purity_func():
    function = ROOT.TF1("func", "[0]+[1]*x+[2]*x*x+[3]*x*x*x", bin_low, bin_hi)
    function.SetParameter(0, -0.0264237)
    function.SetParameter(1, 0.000103069)
    function.SetParameter(2, -7.34631e-08)
    function.SetParameter(3, 1.64727e-11)
    return function

def reducible_func():
    function = ROOT.TF1("func", "[0]+[1]*x+[2]*x*x+[3]*x*x*x+[4]*x*x*x*x", bin_low, bin_hi)
    function.SetParameter(0, 0.00154757)
    function.SetParameter(1, 4.706e-05)
    function.SetParameter(2, -4.66992e-08)
    function.SetParameter(3, 1.77061e-11)
    function.SetParameter(4, -2.32389e-15)
    return function

def irreducible_func():
    function = ROOT.TF1("func", "[0]+[1]*x+[2]*x*x+[3]*x*x*x", bin_low, bin_hi)
    function.SetParameter(0, 0.00214055)
    function.SetParameter(1, -4.66962e-06)
    function.SetParameter(2, 4.61891e-08)
    function.SetParameter(3, -6.63261e-12)
    return function

def geo21_geo20_func():
    function = ROOT.TF1("func", "[0]+[1]*x", bin_low, bin_hi)
    function.SetParameter(0, -1.01251181605 + 1.0)
    function.SetParameter(1, +6.3822E-5)
    return function

def get_fine_hist(hist_name, func):
    hist = ROOT.TH1F(hist_name, "hist", nbins, bin_low, bin_hi)
    for i in range(nbins):
        x_val = hist.GetBinCenter(i+1)
        y_val = func.Eval(x_val)
        hist.SetBinContent(i+1, y_val)
    return hist


def get_fine_binning(hist, func):
    if not hist: return None
    min_x = h1.GetBinLowEdge(1)
    nbins = h1.GetNbinsX()
    max_x = h1.GetBinLowEdge(nbins+1)
    fine_bins = int((max_x - min_x)/5)
    print "fine binning: ", fine_bins
    newhist = ROOT.TH1F("fine_"+hist.GetName(),
                        "fine binning",
                        fine_bins, min_x, max_x)
    for ibin in range(fine_bins):
        x_val = newhist.GetBinCenter(ibin+1)
        oldbin = hist.FindBin(x_val)
        
        y1 = hist.GetBinContent(oldbin)
        x1 = hist.GetBinCenter(oldbin)
        if oldbin == nbins:
            y2 = hist.GetBinConten(oldbin-1)
            x2 = hist.GetBinCenter(oldbin-1)
        else:
            y2 = hist.GetBinContent(oldbin+1)
            x2 = hist.GetBinCenter(oldbin+1)

        value = linear_intpolate(x1, y1, x2, y2, x_val) 
        newhist.SetBinContent(ibin+1, value)
    return newhist
    

def roohistpdf_smooth(h_input):
    """ use RooHistPdf to smooth histogram
        does not work!
    """
    h1 = curve_purity(h_input) 

    min_x = h1.GetBinLowEdge(1)
    nbins = h1.GetNbinsX()
    max_x = h1.GetBinLowEdge(nbins+1)
    fine_bins = int((max_x - min_x)/5)
    print "fine binning: ", fine_bins
    obs = ROOT.RooRealVar("mgg", "mgg", min_x, max_x)
    datahist = ROOT.RooDataHist("datahist",
                                "datahist",
                                ROOT.RooArgList(obs), 
                                h1)
    histpdf = ROOT.RooHistPdf("pdf","pdf", 
                              RooArgSet(obs), datahist, 0)
    hnew = histpdf.createHistogram("smooth_"+h1.GetName(), 
                                   obs,
                                   ROOT.RooFit.Binning(nbins)
                                  )
    return h1,hnew

def test():
    file_name = "systematics.root"
    f1 = ROOT.TFile.Open(file_name, "read")
    h1 = f1.Get("bkg_purity_syst_gg")
    hnew = curve_purity(h1)
    hfine = get_fine_hist("fine", purity_func())
    fout = ROOT.TFile.Open("purity.root", "recreate")
    hnew.Write()
    hfine.Write()
    fout.Close()
    f1.Close()

def process():
    fout_name = "test_smooth.root"
    fout = ROOT.TFile.Open("test_smooth.root", "recreate")
    get_fine_hist("bkg_purity_syst_gg", purity_func()).Write()
    get_fine_hist("bkg_reducible_syst_gg", reducible_func()).Write()
    get_fine_hist("bkg_irreducible_syst_gg", irreducible_func()).Write()
    get_fine_hist("bkg_geo_syst_gg", geo21_geo20_func()).Write()
    print fout_name, " produced"
    fout.Close()

if __name__ == "__main__":
    #test()
    process()
