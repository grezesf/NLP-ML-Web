# script to plot the age of question against question score

# try to fit f1 function
f1(x) = a1*x**2 + a2*x + a3
a1 = 0
a2 = 0
a3 = 0
fit f1(x) "../results/age-score.dat" via a1,a2,a3
plot "../results/age-score.dat", f1(x)