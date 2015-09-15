#!/usr/bin/python

from ROOT import TGraph
import array

def create_tgraph(data, name, x_title, y_title, minimum=None, data_x=-1):
    #        xdata = list(xrange(len(data)))
    xdata = data_x
    if data_x == -1:
        xdata = []
        for i in range(len(data)):
            xdata.append(minimum + i)
    x = array.array('d', xdata)
    y = array.array('d', data)
    gr = TGraph(len(x), x, y)
    # gr.SetDirectory(0)
    gr.SetTitle(name)
    gr.SetLineColor(4)
    gr.SetMarkerColor(2)
    gr.SetMarkerSize(1.5)
    gr.SetMarkerStyle(34)
    gr.GetXaxis().SetTitle(x_title)
    gr.GetYaxis().SetTitle(y_title)
    gr.GetYaxis().SetTitleOffset(1.4)
    gr.SetDrawOption('AP')
    gr.SetLineWidth(2)
    return gr

wbc_scan=[0,0,0,0,0,0,0,0,0,0,1,20,98,8,0,0]
min_wbc = 90
graph = create_tgraph(wbc_scan, "wbc scan", "wbc", "evt/trig [%]", min_wbc)
# graph.Draw("AP")
# raw_input()
# exit()
print "pxarCore =>> wbcScan\n"

print "wbc\tyield\n"
print "090\t 0%"
print "091\t 0%"
print "092\t 0%"
print "093\t 0%"
print "094\t 0%"
print "095\t 0%"
print "096\t 0%"
print "097\t 0%"
print "098\t 0%"
print "099\t 0%"
print "100\t 2%"
print "101\t20%"
print "102\t98%"
print "103\t 8%"
print "104\t 0%"
print "105\t 0%"

print "\nROC STATISTICS:"
print "wbc\troc0\troc1\troc2\troc3"
print "100\t0\t2\t0\t0"
print "101\t6\t12\t10\t4"
print "102\t60\t92\t96\t56"
print "103\t2\t6\t6\t0"
print "104\t0\t0\t0\t0"

print "\nTRIGGER PHASE:"
trigger_phase = [0,0,0,89,890,21,0,0,0,0]
for i in range(len(trigger_phase)):
    if trigger_phase[i]:
        print i, '\t', trigger_phase[i] / 20 * '|', "{0:2.1f}%".format( trigger_phase[i] / float(10))
