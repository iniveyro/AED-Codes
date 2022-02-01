program recurInverso;
uses CRT;

var
	num: integer;

function Inverso(a:integer):integer;
begin
	if (a<10) then
		Inverso:= a
	else
		Inverso:= (a mod 10)*10 + Inverso(a div 10);
end;

begin

	write ('Ingrese un numero a invertir: ');
	readln(num);

	write('El numero inverso es: ', Inverso(num));
end.