N = 1;
a = 1;
b = 0.2;

x = rand(N,1);
X = x*1.8-0.9;
y = rand(N,1);
Y = y*1.8-0.9;

figure(1);
p = plot(X,Y,'ok', 'MarkerFaceColor', [0.8 0.8 0.8]);
ax= gca;
ax.FontSize = 15;
p.MarkerSize = 10;
axis square
xlabel('X')
ylabel('Y')
ax.XLim = [-1 1];
ax.YLim = [-1 1];

X1 = [];
Y1 = [];
X2 = [];
Y2 = [];

for n = 1 : N
    if Y(n) > a*X(n)+b
        X1 = cat(1, X1, X(n));
        Y1 = cat(1, Y1, Y(n));
    else
        X2 = cat(1, X2, X(n));
        Y2 = cat(1, Y2, Y(n));
    end
end

X_sep = [-0.9,0.9];
Y_sep = a*X_sep+b;

figure(2);
cla
if ~isempty(X1)
    p1 = plot(X1,Y1,'or', 'MarkerFaceColor', [1 0.1 0]);
    p1.MarkerSize = 10;
end
hold on
if ~isempty(X2)
    p2 = plot(X2,Y2,'ob', 'MarkerFaceColor', [0 0.1 1]);
    p2.MarkerSize = 10;
end
plot(X_sep,Y_sep, '--k', 'LineWidth', 2)

ax= gca;
ax.FontSize = 15;
ax.XLim = [-1 1];
ax.YLim = [-1 1];
axis square
xlabel('X')
ylabel('Y')
box on


