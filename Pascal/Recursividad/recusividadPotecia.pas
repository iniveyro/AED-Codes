program recursividadPotencia;
uses CRT;

var
	base: integer;
	exponente: integer;

function Potencia(a:integer;b:integer):integer;
begin
	if (b=1) then
		Potencia:= a
	else
		Potencia:= a * Potencia(a,b-1);
end;

begin
	write('Ingrese la base: ');
	readln(base);
	write ('Ingrese el exponente: ');
	readln(exponente);

	write('Su resultado es: ', Potencia(base,exponente));
end.