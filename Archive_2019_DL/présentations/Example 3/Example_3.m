N = 300;
a = 0.2;
b = 0;

X = zeros(N,1);
Y = zeros(N,1);
X1 = [];
Y1 = [];
X2 = [];
Y2 = [];

for n = 1 : N
    
    Theta = rand(1)*10*pi;
    l = rand(1);
    p = rand(1);
    r = a*Theta+b;
    
    if l < 0.5 && p < 0.99
        
        dx = rand(1)-0.5;
        dy = rand(1)-0.5;
        X(n) = (r+dx)*cos(r);
        Y(n) = (r+dy)*sin(r);
        X1 = cat(1, X1, X(n));
        Y1 = cat(1, Y1, Y(n));
        
    elseif l < 0.5 && p >= 0.99
        dx = rand(1)-0.5;
        dy = rand(1)-0.5;
        X(n) = (r+dx)*cos(r);
        Y(n) = (r+dy)*sin(r);
        X2 = cat(1, X2, X(n));
        Y2 = cat(1, Y2, Y(n));
    else 
        dx = rand(1)-0.5;
        dy = rand(1)-0.5;
        X(n) = -(r+dx)*cos(r);
        Y(n) = -(r+dy)*sin(r);
        X2 = cat(1, X2, X(n));
        Y2 = cat(1, Y2, Y(n));
    end
end


figure(1);
p = plot(X,Y,'ok', 'MarkerFaceColor', [0.8 0.8 0.8]);
ax= gca;
ax.FontSize = 15;
p.MarkerSize = 10;
axis square
xlabel('X')
ylabel('Y')
ax.XLim = [-8 8];
ax.YLim = [-8 8];


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

ax= gca;
ax.FontSize = 15;
ax.XLim = [-8 8];
ax.YLim = [-8 8];
axis square
xlabel('X')
ylabel('Y')
box on
