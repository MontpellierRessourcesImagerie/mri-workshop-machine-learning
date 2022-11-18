clear all
close all
clc

X = -10 : 0.1 : 10;
Y = zeros(size(X));

%Y = 1./(1+exp(-X));
% Y = tanh(X);

for n = 1 : length(X)
    if X(n)<0
        Y(n) = 0.05*X(n);
    else
        Y(n) = X(n);
    end
end

plot(X,Y,'-b','LineWidth', 2)
xlabel('x')
ylabel('\phi (x)')
axis square
grid on
ax = gca;
ax.FontSize = 15;