program ackerman; 
uses CRT;
var
    m: integer;
    n: integer;

function ackerman(m:integer;n:integer):LongInt;
begin
    
    if m=0 then
    begin
        ackerman:=n + 1;
    end;
    
    if n = 0 then
    begin
        ackerman:=ackerman(m-1,1);
    end;

    if m > 0 then
    begin
        if n > 0 then
        begin
            ackerman:=ackerman(m-1,ackerman(m,n-1));
        end;
    end;

end;

begin
    m:=0;
    n:=0;
    writeln('- - - Funcion Ackerman - - -');
    writeln('Inserte m');
    read(m);
    writeln('Ingrese n');
    read(n);
	writeln('El valor ackerman es:', ackerman(m,n));

ReadKey();
end.
