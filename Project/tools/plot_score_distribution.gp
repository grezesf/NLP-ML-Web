#script to plot the distribution of scores against the counts for that score.

# try to fit f1 function
f1(x) = a/(b+(c+x)**2)
a = 10000
b = 10
c = -1
fit [0:1000] f1(x) "../results/score-distribution.dat" via a,b,c
set boxwidth 0.5
set style fill solid
plot "../results/score-distribution.dat" with boxes