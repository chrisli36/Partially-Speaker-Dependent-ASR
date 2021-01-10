set samples 1000
set xrange [0.000000:1.000000]
set autoscale y
set size 0.78, 1.0
set nogrid
set ylabel 'Counts'
set xlabel 'Confidence Measure'
set title  'Confidence scores for exp/tri3/decode_dev/score_10/ctm_39phn.filt'
plot 'exp/tri3/decode_dev/score_10/ctm_39phn.filt.hist.dat' using 1:2 '%lf%lf' title 'All Conf.' with lines, \
     'exp/tri3/decode_dev/score_10/ctm_39phn.filt.hist.dat' using 1:2 '%lf%*s%lf' title 'Correct Conf.' with lines, \
     'exp/tri3/decode_dev/score_10/ctm_39phn.filt.hist.dat' using 1:2 '%lf%*s%*s%lf' title 'Incorrect Conf.' with lines
set size 1.0, 1.0
