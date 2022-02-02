program recurImpares;
uses CRT;

var
	num: integer;
	
function Impares(n:integer):integer;
begin
    if (n < 10) then
        if (n mod 2 <> 0) then
            Impares:= n
        else
            Impares:= 0
    else    
        Impares:= Impares(n mod 10) + Impares(n div 10);
end;

begin
	
	writeln('Ingrese un numero para saber su existencia: ');
	readln(num);
	
    writeln ('La suma de los digitos Impares es: ', Impares(num));
end.