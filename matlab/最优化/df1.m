%目标函数的梯度
%df1.m
function df=df1(x)
B = 1520; %人字架跨距
T = 2.5; %钢管厚度
df=[2*pi*T*(B^2/4 + x(2)^2)^(1/2);(2*pi*T*x(1)*x(2))/(B^2/4 + x(2)^2)^(1/2)];