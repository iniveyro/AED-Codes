program recursividadparcial;
uses CRT;

var
	x:longint;

function Deteccion(n:longint):boolean;
begin
	if (n>=0) then
	begin
		if (n = 1) then
			Deteccion:= true
		else
			Deteccion:= false;

		Deteccion:= Deteccion (n mod 100) and Deteccion (n div 100);
end;

begin
	writeln('Ingrese el numero en binario');
	readln(x);
	if (Deteccion(x) = true) then
	writeln ('Tiene una cantidad de 1 impares');

	ReadKey();

end.