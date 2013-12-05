# script to plot the age of question against average question score for that age

# try to fit f1 function
f1(x) = a1*x**2 + a2*x + a3
a1 = 1
a2 = 1
a3 = 1
fit [0:1300] f1(x) "../results/age-average-score.dat" via a1,a2,a3
plot "../results/age-average-score.dat", f1(x)