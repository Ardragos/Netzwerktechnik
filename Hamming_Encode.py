print("Enter 7 digit Code to encode: ");
x = input();
a = (int(x[0]) + int(x[1]) + int(x[2]))%2;
print(a);
b = (int(x[3]) + int(x[4]) + int(x[5]))%2;
print(b);
c = (int(x[0]) + int(x[1]) + int(x[3]) + int(x[4]) + int(x[6]))%2;
print(c);
d = (int(x[0]) + int(x[2]) + int(x[3]) + int(x[5]) + int(x[6]))%2;
print(d);
print(x[0] + x[1] + x[2] + str(a) + x[3] + x[4] + x[5] + str(b) + x[6] + str(c) + str(d));
#	  0      1      2      3   4      5      6      7   8      9   10