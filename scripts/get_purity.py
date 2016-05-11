#!/usr/bin/env python

import ROOT
import AtlasStyle
from ROOT import RooArgSet, RooArgList, RooFit

if not hasattr(ROOT, "myLegend"):
    ROOT.gROOT.LoadMacro("/afs/cern.ch/user/x/xju/work/h4l/h4lcode/hzzws/scripts/loader.c")

ROOT.gROOT.SetBatch(True)
class HistHandler:
    def __init__(self):
        print "HistHandler create"
        self.OBS_NAME = "obs"
        self.WEIGHT_NAME = "weight"
        self.analysis = "spin2"
        self.OUTPUT_NAME = "ws_"+self.analysis+".root"
        self.COMBINE_PDF_NAME = "combPdf"
        self.ISO_CUT = 2.45
        self.X_TITLE = "E_{T}^{iso} - 0.022 #times E_{T} [GeV]"
        self.iso_hist_name = "h_leading_iso_massbin" # without DD correction
        #self.iso_hist_name = "h_leading_isoDD_massbin"  # with DD correction


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
        print "number of entries: ", hist.GetEntries(), hist.Integral()
        for ibin in range(1, nbins+1):
            x_val = hist.GetBinCenter(ibin)
            y_val = hist.GetBinContent(ibin)
            y_err = hist.GetBinError(ibin);
            weight.setVal(y_val)
            obs.setVal(x_val)
            dataset.add(RooArgSet(obs,weight), y_val, y_err)
        print "dataSet: ", dataset.sumEntries()
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
            obs.setBins(nbins);
            obs.Print()
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

        gg_events = ROOT.RooRealVar("gg_events", "gg", 0, 1E5)
        gj_events = ROOT.RooRealVar("gj_events", "gj", 0, 1E5)
        jg_events = ROOT.RooRealVar("jg_events", "jg", 0, 1E5)
        jj_events = ROOT.RooRealVar("jj_events", "jj", 0, 1E5)
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

    def get_hists(self, file_name, hist_name, DO_2D=False, start=1, end=2):
        """ """
        fin = ROOT.TFile.Open(file_name, "read")
        if DO_2D:
            h2d_leading = fin.Get(hist_name)
            h2d_subleading = fin.Get(hist_name.replace("leading","subleading"))
            if not h2d_leading or not h2d_subleading:
                print "cannot find hist in", file_name
                return None
            h1d_leading = h2d_leading.ProjectionX(
                h2d_leading.GetName()+"_px"+str(start)+"_"+str(end),
                start, end)
            h1d_subleading = h2d_subleading.ProjectionX(
                h2d_subleading.GetName()+"_px"+str(start)+"_"+str(end),
                start, end)
        else:
            h1d_leading = fin.Get(hist_name)
            h1d_subleading = fin.Get(hist_name.replace("leading", "subleading"))

        if not h1d_leading or not h1d_subleading:
            print "cannot find projection"
            return None
        h1d_leading.SetDirectory(0)
        h1d_subleading.SetDirectory(0)
        fin.Close()
        h1d_leading.SetName("leading_"+file_name.replace(".root",""))
        h1d_subleading.SetName("subleading_"+file_name.replace(".root",""))
        return (h1d_leading, h1d_subleading)

    def process(self, fgg_name, fjj_name, fdata_name):
        """
            main function to process the three files
        """
        self.gg_leading, self.gg_subleading = self.get_hists(
            fgg_name, self.iso_hist_name, True, 1, 5
        )
        self.jj_leading, self.jj_subleading = self.get_hists(
            fjj_name, "h_leading_iso_massbin", True, 1, 5
        )
        data_leading, data_subleading = self.get_hists(
            fdata_name, "h_leading_iso_massbin", True, 1, 5
        )
        #data_leading.Sumw2()
        #data_subleading.Sumw2()

        # check the distributions
        component_leading = {
            "data": data_leading,
            "#gamma": self.gg_leading,
            "jet": self.jj_leading
        }
        component_subleading = {
            "data": data_subleading,
            "#gamma": self.gg_subleading,
            "jet": self.jj_subleading
        }
        self.compare_hists(component_leading, "leading", "leading")
        self.compare_hists(component_subleading, "subleading", "subleading")

        self.get_combined_ws(self.gg_leading, self.gg_subleading,
                             self.jj_leading, self.jj_subleading,
                             data_leading, data_subleading)
        self.fit_workspace()

        self.get_results()

    def compare_hists(self, hist_dict_org, out_name, title):
        """
        compare the two templates with the data
        They are scaled to unit
        """
        canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
        # make copys of input histograms
        hist_dict = {}
        for name, hist in hist_dict_org.iteritems():
            hist_dict[name] = hist.Clone(hist.GetName()+"_cp")

        # rebin histograms for comparison only!
        # scale all histograms to unit
        num_rebin = 1
        for name, hist in hist_dict.iteritems():
            if hist is None:
                print name,"has empty hist",hist.GetName()
                continue
            hist.Rebin(num_rebin)
            if hist.Integral() != 0:
                hist.Scale(1./hist.Integral())
            else:
                print hist.GetName(),"in ",name,"is empty!"

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
        ROOT.myText(0.6, 0.88, 1, self.analysis)
        ROOT.myText(0.6, 0.83, 1, title)
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
            RooFit.Minimizer("Minuit2", ROOT.Math.MinimizerOptions.DefaultMinimizerAlgo()),
            RooFit.SumW2Error(True),
        )
        obs = ws.var("obs")
        self.plot_pdf_data(pdf, obs, data, self.X_TITLE)

    @staticmethod
    def plot_pdf_data(pdf, obs, data, xtitle):
        """
        plot individual components
        """
        category = pdf.indexCat()
        cat_iter = ROOT.TIter(category.typeIterator())
        obj = cat_iter()
        data_list = data.split(category, True)
        while obj:
            legend = ROOT.myLegend(0.6, 0.6, 0.8, 0.9)
            color = 2
            ch_name = obj.GetName()
            ch_pdf = pdf.getPdf(ch_name)
            ch_pdf.Print()
            frame = obs.frame(obs.getBins())
            ch_data = data_list.At(obj.getVal())
            # print expected and observed events
            exp_events = ch_pdf.expectedEvents(RooArgSet(obs))
            obs_events = ch_data.sumEntries()
            print "In ", ch_name, exp_events, obs_events
            # plot data
            index_obj = 0
            ch_data.plotOn(frame, RooFit.LineWidth(2),
                           RooFit.LineColor(1),
                           RooFit.MarkerSize(1.00),
                           RooFit.DrawOption("EP")
                          )
            legend.AddEntry(frame.getObject(index_obj), "data", "EP")
            index_obj += 1
            # plot pdf
            ch_pdf.plotOn(
                frame,
                RooFit.LineWidth(2),
                RooFit.LineColor(color),
                RooFit.Normalization(exp_events, ROOT.RooAbsReal.NumEvent),
            )
            legend.AddEntry(frame.getObject(index_obj), "total", "L")
            color += 1
            # plot individual components in pdf
            ch_pdf_pdf_list = ch_pdf.pdfList()
            ch_pdf_coeff_list = ch_pdf.coefList()
            index_obj += 1
            for ilist in range(ch_pdf_pdf_list.getSize()):
                pdf_ = ch_pdf_pdf_list.at(ilist)
                norm_ = ch_pdf_coeff_list.at(ilist)
                pdf_.plotOn(
                    frame, RooFit.LineWidth(2),
                    RooFit.LineColor(color),
                    RooFit.LineStyle(2),
                    RooFit.Normalization(norm_.getVal(), ROOT.RooAbsReal.NumEvent),
                )
                print "\t ", norm_.GetName(), norm_.getVal(), round(norm_.getVal()*100/exp_events,3)
                legend.AddEntry(frame.getObject(index_obj),
                                norm_.GetName().replace("_events",""),
                                "L")
                index_obj += 1
                color += 1
            canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
            frame.Draw()
            frame.GetXaxis().SetTitle(xtitle)
            legend.Draw()
            canvas.SaveAs(ch_name+"_overlay.pdf")
            obj = cat_iter()
            color += 1

    def get_eff(self, hist):
        cut_bin = hist.FindBin(self.ISO_CUT)
        num_bins = hist.GetNbinsX()
        total_= hist.Integral(1, num_bins)
        eff = hist.Integral(1, cut_bin)/total_
        return  eff

    def get_results(self):
        print "Calo Iso cut: ", self.ISO_CUT
        eff_gamma_leading = self.get_eff(self.gg_leading)
        eff_gamma_subleading = self.get_eff(self.gg_subleading)
        eff_jet_leading = self.get_eff(self.jj_leading)
        eff_jet_subleading = self.get_eff(self.jj_subleading)
        num_gg = self.ws.var("gg_events").getVal()
        num_gj = self.ws.var("gj_events").getVal()
        num_jg = self.ws.var("jg_events").getVal()
        num_jj = self.ws.var("jj_events").getVal()
        print "efficiency of #gamma: {:.3f} {:.3f}".format(
            eff_gamma_leading, eff_gamma_subleading)
        print "efficiency of jet: {:.3f} {:.3f}".format(
            eff_jet_leading, eff_jet_subleading)
        num_gg_sig = num_gg*eff_gamma_leading*eff_gamma_subleading
        num_gj_sig = num_gj*eff_gamma_leading*eff_jet_subleading
        num_jg_sig = num_jg*eff_jet_leading*eff_gamma_subleading
        num_jj_sig = num_jj*eff_jet_leading*eff_jet_subleading
        total_sig = num_gg_sig+num_gj_sig+num_jg_sig+num_jj_sig
        print "In SR:"
        print "\t gg: ", round(num_gg_sig,3), round(100*num_gg_sig/total_sig,1), "%"
        print "\t gj: ", round(num_gj_sig,3), round(100*num_gj_sig/total_sig,1), "%"
        print "\t jg: ", round(num_jg_sig,3), round(100*num_jg_sig/total_sig,1), "%"
        print "\t jj: ", round(num_jj_sig,3), round(100*num_jj_sig/total_sig,1), "%"


    def compare(self, file_dicts):
        mass_range = [
            "160_250GeV",
            "250_400GeV",
            "400_650GeV",
            "650_1000GeV",
            "1000_GeV",
            "eta_0_0.6",
            "eta_0.6_1.37",
            "eta_1.52_1.81",
            "eta_1.81_2.37",
        ]
        for imass in range(1, len(mass_range)+1):
            title_ = mass_range[imass-1]
            print "dealing with mass: ", title_
            hist_leading_dict = {}
            hist_subleading_dict = {}
            for name, file_name in file_dicts.iteritems():
                hist_name = self.iso_hist_name
                if "Data" in name or "Bkg" in name :
                    hist_name = "h_leading_iso_massbin"
                leading, subleading = self.get_hists(file_name, hist_name,
                                                     True, imass, imass)
                hist_leading_dict[name] = leading
                hist_subleading_dict[name] = subleading
            self.compare_hists(hist_leading_dict, "leading_"+title_, title_)
            self.compare_hists(hist_subleading_dict, "subleading_"+title_, title_)

if __name__ == "__main__":
    GG_SHERPA_FILENAME = "gg_sherpa.root"
    GG_PYTHIA_FILENAME = "gg_pythia.root"
    JJ_FIELNAME = "jets_data.root"
    #DATA_FILENAME = "data.root"
    DATA_FILENAME = "pseudodata.root"
    cmp_dict = {
        "Sherpa": GG_SHERPA_FILENAME,
        "Pythia": GG_PYTHIA_FILENAME,
        "Bkg Template": JJ_FIELNAME,
        "Data":  DATA_FILENAME
    }
    handle = HistHandler()
    handle.ISO_CUT = 7.
    handle.compare(cmp_dict)
    handle.process(GG_SHERPA_FILENAME, JJ_FIELNAME, DATA_FILENAME)
    #handle.process(GG_PYTHIA_FILENAME, JJ_FIELNAME, DATA_FILENAME)
