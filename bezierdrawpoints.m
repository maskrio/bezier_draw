function bezierdrawpoints(P)
    n = size(P, 1);

    figure;
    hold on;
    axis equal;

    t = 0:0.02:1;

    for k = 1:n
        x1 = P(k,1); y1 = P(k,2);
        x2 = P(k,3); y2 = P(k,4);
        x3 = P(k,5); y3 = P(k,6);
        x4 = P(k,7); y4 = P(k,8);

        x = [x1; x2; x3; x4];
        y = [y1; y2; y3; y4];

        % plot([x(1) x(2)],[y(1) y(2)],'r:',x(2),y(2),'rs');
        % plot([x(3) x(4)],[y(3) y(4)],'r:',x(3),y(3),'rs');
        % plot(x(1),y(1),'bo',x(4),y(4),'bo');
        bx=3*(x(2)-x(1)); by=3*(y(2)-y(1)); % spline equations ...
        cx=3*(x(3)-x(2))-bx;cy=3*(y(3)-y(2))-by;
        dx=x(4)-x(1)-bx-cx;dy=y(4)-y(1)-by-cy;
        xp=x(1)+t.*(bx+t.*(cx+t*dx)); % Horner's method
        yp=y(1)+t.*(by+t.*(cy+t*dy));

        plot(xp, yp, 'b-');
    end

    hold off;
end
