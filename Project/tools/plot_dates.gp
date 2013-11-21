# script to plot the age of question against question score

f1(x) = a*x + b
a = 0
b = 0
fit f1(x) "../results/ages-score.dat" via a,b
plot "../results/ages-score.dat", f1(x)