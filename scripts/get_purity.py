#!/usr/bin/env python

import ROOT

class HistHandler:
    def __init__(self):
        print "HistHandler create"
        self.OBS_NAME = "obs"
        self.ws = ROOT.RooWorkspace("combined", "combined")
        self.OUTPUT_NAME = "ws_test.root"
        self.out_file = ROOT.TFile.Open(self.OUTPUT_NAME, "recreate")

    def make_histpdf(self, hist):
        obs = self.ws.var(self.OBS_NAME)
        if not obs:
            nbins = hist.GetNbinsX()
            low = hist.GetBinLowEdge(1)
            high = hist.GetBinLowEdge(nbins+1)
            obs = ROOT.RooRealVar(self.OBS_NAME, self.OBS_NAME, low, high)
            getattr(self.ws, 'import')(obs)

        obs_list = ROOT.RooArgList(obs)
        histdata = ROOT.RooDataHist("histdata_"+hist.GetName(),
                                    "data_hist",
                                    obs_list, hist)
        INTERPOLATE_ORDER = 2
        pdf_name = "histpdf_"+hist.GetName()
        histpdf = ROOT.RooHistPdf(pdf_name, pdf_name,
                                  obs_list, histdata,
                                  INTERPOLATE_ORDER)
        getattr(self.ws, 'import')(histpdf)
        return self.ws.obj(pdf_name)

    def get_combined_ws(self,
                        leading_gamma, subleading_gamma,
                        leading_jet, subleading_jet,
                        leading_data, subleading_data):
        leading_gamma_pdf = self.make_histpdf(leading_gamma)
        leading_jet_pdf = self.make_histpdf(leading_jet)
        leading_data_pdf = self.make_histpdf(leading_data)
        subleading_gamma_pdf = self.make_histpdf(subleading_gamma)
        subleading_jet_pdf = self.make_histpdf(subleading_jet)
        subleading_data_pdf = self.make_histpdf(subleading_data)
        gg_events = ROOT.RooRealVar("gg_events", "gg", 0, 1E4)
        gj_events = ROOT.RooRealVar("gj_events", "gj", 0, 1E4)
        jg_events = ROOT.RooRealVar("jg_events", "jg", 0, 1E4)
        jj_events = ROOT.RooRealVar("jj_events", "jj", 0, 1E4)
        LEADING_PDF_NAME = "combined_leading"
        combined_leading_pdf = ROOT.RooAddPdf(LEADING_PDF_NAME,
                                              LEADING_PDF_NAME,
                                              ROOT.RooArgList(leading_gamma_pdf,
                                                              leading_gamma_pdf,
                                                              leading_jet_pdf,
                                                              leading_jet_pdf),
                                              ROOT.RooArgList(gg_events,
                                                              gj_events,
                                                              jg_events,
                                                              jj_events)
                                             )
        SUBLEADING_PDF_NAME = "combined_subleading"
        combined_subleading_pdf = ROOT.RooAddPdf(SUBLEADING_PDF_NAME,
                                                 SUBLEADING_PDF_NAME,
                                                 ROOT.RooArgList(subleading_gamma_pdf,
                                                                 subleading_jet_pdf,
                                                                 subleading_gamma_pdf,
                                                                 subleading_jet_pdf),
                                                 ROOT.RooArgList(gg_events,
                                                                 gj_events,
                                                                 jg_events,
                                                                 jj_events)
                                                )
        categories = ROOT.RooCategory("channelCat", "channelCat")
        pdf_map = {"leading": combined_leading_pdf,
                   "subleading": combined_subleading_pdf
                  }
        categories.defineType("leading", 0)
        categories.defineType("subleading", 1)
        COMBINE_PDF_NAME = "combined"
        combined_pdf = ROOT.RooSimultaneous(COMBINE_PDF_NAME, COMBINE_PDF_NAME,
                                            pdf_map, categories)
        getattr(self.ws, 'import')(combined_pdf)
        self.ws.writeToFile(self.OUTPUT_NAME)

    def get_1D_hists(self, hist_2d):
        Y_START = 1
        Y_END = 4
        h1 = hist_2d.ProjectionX(hist_2d.GetName()+"_px", Y_START, Y_END)
        return h1

    def get_hists(self, file_name):
        """ """
        fin = ROOT.TFile.Open(file_name, "read")
        LEADING_2D_HIST_NAME = "h_leading_etcone40_2D"
        SUBLEADING_2D_HIST_NAME = "h_subleading_etcone40_2D"
        h2d_leading = fin.Get(LEADING_2D_HIST_NAME)
        h2d_subleading = fin.Get(SUBLEADING_2D_HIST_NAME)
        h1d_leading = self.get_1D_hists(h2d_leading)
        h1d_subleading = self.get_1D_hists(h2d_subleading)
        return (h1d_leading, h1d_subleading)

    def process(self, fgg_name, fjj_name, fdata_name):
        """
            main function to process the three files
        """
        gg_leading, gg_subleading = self.get_hists(fgg_name)
        jj_leading, jj_subleading = self.get_hists(fjj_name)
        data_leading, data_subleading = self.get_hists(fdata_name)
        self.get_combined_ws(gg_leading, gg_subleading,
                             jj_leading, jj_subleading,
                             data_leading, data_subleading)

    def compare_hists():
        pass

if __name__ == "__main__":
    handle = HistHandler()
    GG_FILENAME = ""
    JJ_FIELNAME = ""
    DATA_FILENAME = ""
    handle.process(GG_FILENAME, JJ_FIELNAME, DATA_FILENAME)
