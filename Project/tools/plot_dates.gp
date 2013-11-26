# script to plot the age of question against question score

f1(x) = a*x + b
a = 0
b = 0
fit f1(x) "../results/ages-scores.dat" via a,b
plot "../results/ages-scores.dat", f1(x)