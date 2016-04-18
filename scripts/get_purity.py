#!/usr/bin/env python

import ROOT
import AtlasStyle
from ROOT import RooArgSet, RooArgList, RooFit

if not hasattr(ROOT, "myLegend"):
    ROOT.gROOT.LoadMacro("/Users/xju/Documents/Programs/hzzws/scripts/loader.c")

ROOT.gROOT.SetBatch(True)
class HistHandler:
    def __init__(self):
        print "HistHandler create"
        self.OBS_NAME = "obs"
        self.WEIGHT_NAME = "weight"
        self.analysis = "EK"
        self.OUTPUT_NAME = "ws_"+self.analysis+".root"
        self.COMBINE_PDF_NAME = "combPdf"

    def make_dataset(self, hist):
        if not hist:
            return None
        nbins = hist.GetNbinsX()
        obs = self.ws.var(self.OBS_NAME)
        weight = self.ws.var(self.WEIGHT_NAME)
        dataset = ROOT.RooDataSet("dataset_"+hist.GetName(), "data",
                                  RooArgSet(obs, weight), 
                                  RooFit.WeightVar(weight)
                                 )
        for ibin in range(1, nbins+1):
            x_val = hist.GetBinCenter(ibin)
            y_val = hist.GetBinContent(ibin)
            weight.setVal(y_val)
            obs.setVal(x_val)
            dataset.add(RooArgSet(obs,weight), y_val)
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
        self.ws = ROOT.RooWorkspace("combined", "combined")
        leading_gamma_pdf = self.make_histpdf(leading_gamma)
        leading_jet_pdf = self.make_histpdf(leading_jet)
        subleading_gamma_pdf = self.make_histpdf(subleading_gamma)
        subleading_jet_pdf = self.make_histpdf(subleading_jet)

        gg_events = ROOT.RooRealVar("gg_events", "gg", 0, 1E7)
        gj_events = ROOT.RooRealVar("gj_events", "gj", 0, 1E7)
        jg_events = ROOT.RooRealVar("jg_events", "jg", 0, 1E7)
        jj_events = ROOT.RooRealVar("jj_events", "jj", 0, 1E7)
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
        combined_pdf = ROOT.RooSimultaneous(self.COMBINE_PDF_NAME,
                                            self.COMBINE_PDF_NAME, categories)
        combined_pdf.addPdf(combined_leading_pdf, "leading")
        combined_pdf.addPdf(combined_subleading_pdf, "subleading")
        getattr(self.ws, 'import')(combined_pdf, RooFit.RecycleConflictNodes())

        # build RooDataSet
        obs = self.ws.var(self.OBS_NAME)
        weight = self.ws.var(self.WEIGHT_NAME)
        if not weight:
            weight = ROOT.RooRealVar(self.WEIGHT_NAME, self.WEIGHT_NAME, 0, 1E6)
            getattr(self.ws,'import')(weight)
        dataset_leading = self.make_dataset(data_leading)
        dataset_subleading = self.make_dataset(data_subleading)
        dataset = ROOT.RooDataSet(
            "obsData", "data",
            RooArgSet(obs, weight),
            RooFit.Index(categories),
            RooFit.Import("leading", dataset_leading),
            RooFit.Import("subleading", dataset_subleading),
            RooFit.WeightVar(weight)
        )
        getattr(self.ws, 'import')(dataset, RooFit.RecycleConflictNodes())

        self.ws.writeToFile(self.OUTPUT_NAME)

    def get_1D_hists(self, hist_2d):
        """
        get projection for EKEI (1-4), EKHI (5-8)
        HKEI (9-12), HKHI (13-16), EK(17-20), HK(21-24)
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
        elif self.analysis == "EK":
            Y_START = 17
            Y_END = 20
        elif self.analysis == "HK":
            Y_START = 21
            Y_END = 24
        else:
            Y_START = 17
            Y_END = 20

        h1 = hist_2d.ProjectionX(hist_2d.GetName()+"_px", Y_START, Y_END)
        return h1

    def get_hists(self, file_name, DO_2D=False):
        """ """
        fin = ROOT.TFile.Open(file_name, "read")
        if DO_2D:
            LEADING_2D_HIST_NAME = "h_leading_etcone40_2D"
            SUBLEADING_2D_HIST_NAME = "h_subleading_etcone40_2D"
            h2d_leading = fin.Get(LEADING_2D_HIST_NAME)
            h2d_subleading = fin.Get(SUBLEADING_2D_HIST_NAME)
            h1d_leading = self.get_1D_hists(h2d_leading)
            h1d_subleading = self.get_1D_hists(h2d_subleading)
            if not h2d_leading or not h2d_subleading:
                print "cannot find hist in", file_name
        else:
            h1d_leading = fin.Get("leading_jet")
            h1d_subleading = fin.Get("subleading_jet")

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
        self.gg_leading, self.gg_subleading = self.get_hists(fgg_name, True)
        self.jj_leading, self.jj_subleading = self.get_hists(fjj_name)
        data_leading, data_subleading = self.get_hists(fdata_name)

        # compare pythia, Sherpa, bkg and data
        pythia_file_name = "gg_template_pythia.root"
        gg_pythia_leading, gg_pythia_subleading = self.get_hists(pythia_file_name, True)
        generator_leading = {
            "data": data_leading,
            "pythia":gg_pythia_leading,
            "sherpa":self.gg_leading,
            "bkg template":self.jj_leading,
        }
        generator_subleading = {
            "data": data_subleading,
            "pythia":gg_pythia_subleading,
            "sherpa":self.gg_subleading,
            "bkg template":self.jj_subleading,
        }
        self.compare_hists(generator_leading, "leading_gg")
        self.compare_hists(generator_subleading, "subleading_gg")

        self.get_combined_ws(self.gg_leading, self.gg_subleading,
                             self.jj_leading, self.jj_subleading,
                             data_leading, data_subleading)

        self.fit_workspace()

        self.get_results()

    def compare_hists(self, hist_dict, out_name):
        """
        compare the two templates with the data
        They are scaled to unit
        """
        canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
        # rebin histograms for comparison only!
        # scale all histograms to unit
        num_rebin = 1
        for name, hist in hist_dict.iteritems():
            if hist is None: continue
            hist.Rebin(num_rebin)
            if name == "sherpa":
                hist.Scale(3.2)

        max_y = max([x.GetMaximum() for x in hist_dict.itervalues()])

        # start to plot histgorams
        num_count = 0
        color_list = [2, 4, ROOT.kGreen+1, ROOT.kOrange+6, ROOT.kViolet-3]
        legend = ROOT.myLegend(0.6, 0.6, 0.8, 0.8)
        X_TITLE = "E_{T}^{iso} - 0.022 #times E_{T} [GeV]"
        for name, hist in hist_dict.iteritems():
            if hist is None: continue
            hist.SetLineColor(color_list[num_count])
            hist.SetLineWidth(2)
            hist.SetMarkerSize(0)
            if num_count == 0:
                hist.GetYaxis().SetRangeUser(0., max_y*1.1)
                hist.GetXaxis().SetTitle(X_TITLE)
                hist.Draw("HIST")
            else:
                hist.Draw("same HIST")
            legend.AddEntry(hist, name, "L")
            num_count += 1
        legend.Draw()
        ROOT.myText(0.6, 0.85, 1, self.analysis)
        canvas.SaveAs(self.analysis+"_"+out_name+".pdf")

    def fit_workspace(self): 
        """
        Take the data and pdf from the workspace and 
        perform the fitting
        """
        if not self.ws:
            f_in = ROOT.TFile.Open(self.OUTPUT_NAME)
            ws = f_in.Get("combined")
        else:
            ws = self.ws
        pdf = ws.obj(self.COMBINE_PDF_NAME)
        data = ws.data("obsData")
        pdf.fitTo(
            data, RooFit.Extended(True),
            RooFit.Minimizer("Minuit2", ROOT.Math.MinimizerOptions.DefaultMinimizerAlgo())
        )
        obs = ws.var("obs")
        self.plot_pdf_data(pdf, obs, data)

    @staticmethod
    def plot_pdf_data(pdf, obs, data):
        """
        plot individual components
        """
        category = pdf.indexCat()
        cat_iter = ROOT.TIter(category.typeIterator())
        obj = cat_iter()
        data_list = data.split(category, True)
        while obj:
            color = 2
            ch_name = obj.GetName()
            ch_pdf = pdf.getPdf(ch_name)
            ch_pdf.Print()
            frame = obs.frame()
            ch_data = data_list.At(obj.getVal())
            # print expected and observed events
            exp_events = ch_pdf.expectedEvents(RooArgSet(obs))
            obs_events = ch_data.sumEntries()
            print "In ", ch_name, exp_events, obs_events
            # plot pdf and data
            ch_pdf.plotOn(
                frame,
                RooFit.LineWidth(2),
                RooFit.LineColor(color),
                RooFit.Normalization(exp_events, ROOT.RooAbsReal.NumEvent),
            )
            color += 1
            # plot individual components in pdf
            ch_pdf_pdf_list = ch_pdf.pdfList()
            ch_pdf_coeff_list = ch_pdf.coefList()
            for ilist in range(ch_pdf_pdf_list.getSize()):
                pdf_ = ch_pdf_pdf_list.at(ilist)
                norm_ = ch_pdf_coeff_list.at(ilist)
                pdf_.plotOn(
                    frame, RooFit.LineWidth(2),
                    RooFit.LineColor(color),
                    RooFit.LineStyle(2),
                    RooFit.Normalization(norm_.getVal(), ROOT.RooAbsReal.NumEvent),
                )
                color += 1
            ch_data.plotOn(frame, RooFit.LineWidth(2),
                           RooFit.LineColor(1),
                           RooFit.DrawOption("ep")
                          )
            canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
            frame.Draw()
            canvas.SaveAs(ch_name+"_overlay.pdf")
            obj = cat_iter()
            color += 1

    def get_results(self, cut_value):
       pass 

if __name__ == "__main__":
    GG_FILENAME = "gg_template_sherpa.root"
    JJ_FIELNAME = "jj_template.root"
    DATA_FILENAME = "data_template.root"
    handle = HistHandler()
    handle.process(GG_FILENAME, JJ_FIELNAME, DATA_FILENAME)
    handle.fit_workspace()
