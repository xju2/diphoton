#!/usr/bin/env python

import ROOT
import AtlasStyle
from ROOT import RooArgSet, RooArgList, RooFit

if not hasattr(ROOT, "myLegend"):
    ROOT.gROOT.LoadMacro("/Users/xju/Documents/Programs/hzzws/scripts/loader.c")

class HistHandler:
    def __init__(self):
        print "HistHandler create"
        self.OBS_NAME = "obs"
        self.ws = ROOT.RooWorkspace("combined", "combined")
        self.analysis = "EKHI"
        self.OUTPUT_NAME = "ws_"+self.analysis+".root"
        self.out_file = ROOT.TFile.Open(self.OUTPUT_NAME, "recreate")

    def make_dataset(self, hist):
        if not hist:
            return None
        nbins = hist.GetNbinsX()
        obs = self.ws.var(self.OBS_NAME)
        dataset = ROOT.RooDataSet("dataset_"+hist.GetName(), "data",
                                  RooArgSet(obs), "weight")
        for ibin in range(1, nbins+1):
            x_val = hist.GetBinCenter(ibin)
            y_val = hist.GetBinContent(ibin)
            obs.setVal(x_val)
            dataset.add(RooArgSet(obs), y_val)
        return dataset

    def get_datahist():
        datahist = ROOT.RooDataHist("data", "data",
                                    RooArgList(obs),
                                    RooFit.Index(categories),
                                    RooFit.Import("leading", data_leading),
                                    RooFit.Import("subleading", data_subleading)
                                   )
        datahist.Print('v')
        getattr(self.ws, 'import')(datahist, RooFit.RecycleConflictNodes())

    def make_histpdf(self, hist):
        if not hist:
            print "hist does not exist!"
            return
        obs = self.ws.var(self.OBS_NAME)
        if not obs:
            nbins = hist.GetNbinsX()
            low = hist.GetBinLowEdge(1)
            high = hist.GetBinLowEdge(nbins+1)
            obs = ROOT.RooRealVar(self.OBS_NAME, self.OBS_NAME, low, high)
            getattr(self.ws, 'import')(obs, RooFit.RecycleConflictNodes())

        obs_list = ROOT.RooArgList(obs)
        histdata = ROOT.RooDataHist("histdata_"+hist.GetName(),
                                    "data_hist",
                                    obs_list, hist)
        INTERPOLATE_ORDER = 2
        pdf_name = "histpdf_"+hist.GetName()
        histpdf = ROOT.RooHistPdf(pdf_name, pdf_name,
                                  ROOT.RooArgSet(obs),
                                  histdata,
                                  INTERPOLATE_ORDER)
        getattr(self.ws, 'import')(histpdf, RooFit.RecycleConflictNodes())
        return self.ws.obj(pdf_name)

    def get_combined_ws(self,
                        leading_gamma, subleading_gamma,
                        leading_jet, subleading_jet,
                        data_leading, data_subleading):
        """
        using input histograms, build the combined workspace, 
        which contains models and data
        """
        leading_gamma_pdf = self.make_histpdf(leading_gamma)
        leading_jet_pdf = self.make_histpdf(leading_jet)
        subleading_gamma_pdf = self.make_histpdf(subleading_gamma)
        subleading_jet_pdf = self.make_histpdf(subleading_jet)

        gg_events = ROOT.RooRealVar("gg_events", "gg", 0, 1E4)
        gj_events = ROOT.RooRealVar("gj_events", "gj", 0, 1E4)
        jg_events = ROOT.RooRealVar("jg_events", "jg", 0, 1E4)
        jj_events = ROOT.RooRealVar("jj_events", "jj", 0, 1E4)
        LEADING_PDF_NAME = "combined_leading"
        combined_leading_pdf = ROOT.RooAddPdf(LEADING_PDF_NAME,
                                              LEADING_PDF_NAME,
                                              RooArgList(leading_gamma_pdf,
                                                         leading_gamma_pdf,
                                                         leading_jet_pdf,
                                                         leading_jet_pdf),
                                              RooArgList(gg_events,
                                                         gj_events,
                                                         jg_events,
                                                         jj_events)
                                             )
        SUBLEADING_PDF_NAME = "combined_subleading"
        combined_subleading_pdf = ROOT.RooAddPdf(SUBLEADING_PDF_NAME,
                                                 SUBLEADING_PDF_NAME,
                                                 RooArgList(subleading_gamma_pdf,
                                                            subleading_jet_pdf,
                                                            subleading_gamma_pdf,
                                                            subleading_jet_pdf),
                                                 RooArgList(gg_events,
                                                            gj_events,
                                                            jg_events,
                                                            jj_events)
                                                )
        categories = ROOT.RooCategory("channelCat", "channelCat")
        categories.defineType("leading", 0)
        categories.defineType("subleading", 1)
        COMBINE_PDF_NAME = "combined"
        combined_pdf = ROOT.RooSimultaneous(COMBINE_PDF_NAME, COMBINE_PDF_NAME, categories)
        combined_pdf.addPdf(combined_leading_pdf, "leading")
        combined_pdf.addPdf(combined_subleading_pdf, "subleading")
        getattr(self.ws, 'import')(combined_pdf, RooFit.RecycleConflictNodes())

        # build RooDataSet
        obs = self.ws.var(self.OBS_NAME)
        dataset_leading = self.make_dataset(data_leading)
        dataset_subleading = self.make_dataset(data_subleading)
        dataset = ROOT.RooDataSet("data", "data",
                                  RooArgSet(obs),
                                  RooFit.Index(categories),
                                  RooFit.Import("leading", dataset_leading),
                                  RooFit.Import("subleading", dataset_subleading)
                                 )
        getattr(self.ws, 'import')(dataset, RooFit.RecycleConflictNodes())

        self.ws.writeToFile(self.OUTPUT_NAME)

    def get_1D_hists(self, hist_2d):
        """
        get projection for EKEI (1-4), EKHI (5-8)
        HKEI (9-12), HKHI (13-16)
        """
        if self.analysis == "EKEI":
            Y_START = 1
            Y_END = 4
        elif self.analysis == "EKHI":
            Y_START = 5
            Y_END = 8
        elif self.analysis == "HKEI":
            Y_START = 9
            Y_END = 12
        elif self.analysis == "HKHI":
            Y_START = 13
            Y_END = 16
        else:
            Y_START = 1
            Y_END = 16

        h1 = hist_2d.ProjectionX(hist_2d.GetName()+"_px", Y_START, Y_END)
        return h1

    def get_hists(self, file_name):
        """ """
        fin = ROOT.TFile.Open(file_name, "read")
        LEADING_2D_HIST_NAME = "h_leading_etcone40_2D"
        SUBLEADING_2D_HIST_NAME = "h_subleading_etcone40_2D"
        h2d_leading = fin.Get(LEADING_2D_HIST_NAME)
        h2d_subleading = fin.Get(SUBLEADING_2D_HIST_NAME)
        if not h2d_leading or not h2d_subleading:
            print "cannot find hist in", file_name
        h1d_leading = self.get_1D_hists(h2d_leading)
        h1d_subleading = self.get_1D_hists(h2d_subleading)
        if not h1d_leading or not h1d_subleading:
            print "cannot find projection"
            return None
        h1d_leading.SetDirectory(0)
        h1d_subleading.SetDirectory(0)
        fin.Close()
        return (h1d_leading, h1d_subleading)

    def process(self, fgg_name, fjj_name, fdata_name):
        """
            main function to process the three files
        """
        gg_leading, gg_subleading = self.get_hists(fgg_name)
        jj_leading, jj_subleading = self.get_hists(fjj_name)
        data_leading, data_subleading = self.get_hists(fdata_name)

        # check the distributions
        self.compare_hists(gg_leading, jj_leading, data_leading, "leading")
        self.compare_hists(gg_subleading, jj_subleading,
                           data_subleading, "subleading")

        self.get_combined_ws(gg_leading, gg_subleading,
                             jj_leading, jj_subleading,
                             data_leading, data_subleading)

    def compare_hists(self, h_gg, h_jj, h_data, out_name):
        """
        compare the two templates with the data
        They are scaled to unit
        """
        canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
        # rebin histograms for comparison only!
        num_rebin = 2
        h_data.Rebin(num_rebin)
        h_gg.Rebin(num_rebin)
        h_jj.Rebin(num_rebin)

        # scale all histograms to unit
        h_gg.Scale(1./h_gg.Integral())
        h_jj.Scale(1./h_jj.Integral())
        h_data.Scale(1./h_data.Integral())
        max_y = max([h_gg.GetMaximum(), h_jj.GetMaximum(),
                     h_data.GetMaximum()])
        h_data.GetYaxis().SetRangeUser(0., max_y*1.1)

        # cosmetic setup
        h_data.SetLineColor(1)
        h_gg.SetLineColor(2)
        h_jj.SetLineColor(4)


        h_data.Draw()
        h_gg.Draw("same")
        h_jj.Draw("same")

        legend = ROOT.myLegend(0.6, 0.6, 0.8, 0.8)
        legend.AddEntry(h_data, "data", "L")
        legend.AddEntry(h_gg, "#gamma", "L")
        legend.AddEntry(h_jj, "jet", "L")
        legend.Draw()
        ROOT.myText(0.6, 0.85, 1, self.analysis)
        canvas.SaveAs(self.analysis+"_"+out_name+".pdf")


if __name__ == "__main__":
    handle = HistHandler()
    GG_FILENAME = "gg_template.root"
    JJ_FIELNAME = "jj_template.root"
    DATA_FILENAME = "data_template.root"
    handle.process(GG_FILENAME, JJ_FIELNAME, DATA_FILENAME)
