#!/usr/bin/env python

import ROOT

def main( input_file = "./data/new_sys.root", analysis_tag = "Nominal_8TeV", 
         with_geo = True):
    meas_name = "meas_"+analysis_tag
    meas = ROOT.RooStats.HistFactory.Measurement(meas_name, meas_name)
    meas.SetOutputFilePrefix('./results/'+analysis_tag)
    meas.SetExportOnly(True)
    meas.SetPOI("xs")

    #create a channel
    chan = ROOT.RooStats.HistFactory.Channel("chan_"+analysis_tag)
    chan.SetStatErrorConfig(0.001, "Poisson")
    chan.SetData("bkg_nominal", input_file)

    #add sample
    #signal = ROOT.RooStats.HistFactory.Sample("signal", "bkg_total_gg_full",
    #                                          input_file)
    #signal.AddOverallSys("sys_signal", 0.95, 1.05)
    #chan.AddSample(signal)

    bkg = ROOT.RooStats.HistFactory.Sample("bkg_nominal", "bkg_nominal", input_file)
    bkg.ActivateStatError()
    bkg.AddHistoSys("bkg_purity","purity_sys_down", input_file, "",
                    "purity_sys_up", input_file, "")
    bkg.AddHistoSys("bkg_irreducible","irreducible_sys_down", input_file, "",
                    "irreducible_sys_up", input_file, "")
    bkg.AddHistoSys("bkg_reducible","reducible_sys_down", input_file, "",
                    "reducible_sys_up", input_file, "")
    if with_geo:
        bkg.AddHistoSys("geo","geo_sys_down", input_file, "",
                    "geo_sys_up", input_file, "")
    chan.AddSample(bkg)
    #end a channel
    
    #finish a channel
    meas.AddChannel(chan)
    meas.CollectHistograms()
    meas.PrintTree()
    meas.PrintXML("xml", meas.GetOutputFilePrefix())

if __name__ == "__main__":
    # main()  ## for 8 TeV

    #tag = "HKHI"
    #main("hists_input_"+tag+".root", tag+"_13TeV", False)

    tag = "EKHI"
    main("hists_input_"+tag+".root", tag+"_13TeV", False)

