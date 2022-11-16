X = -1 : 0.1 : 1;
Y = 0.5*X.^2;

figure(1);
p = plot(X,Y,'-b');
ax= gca;
ax.FontSize = 15;
axis square
xlabel('d-y')
ylabel('Loss score')
ax.XLim = [-1 1];
box on
grid on

Y1 = -log(X);
Y2 = -log(1-X);

figure(2);
cla
plot(X,Y1,'-b');
hold on
plot(X,Y2,'-r');
ax= gca;
ax.FontSize = 15;
axis square
xlabel('y')
ylabel('Loss score')
ax.XLim = [0 1];
box on
grid on
legend({'d=1 : E=-ln(y)', 'd=0 : E=-ln(1-y)'}, 'Location', 'north')