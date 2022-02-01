program recurExisteNum;
uses CRT;

type
	arreglo = array [1..10] of integer;


var
	num: integer;
	i: integer;
	arr: arreglo;

function ExisteNum(arr:arreglo;i:integer;num:integer):integer;
begin
	if (num=arr[i]) then
		ExisteNum:= 1
	else
		if (i<11) then
			ExisteNum:= ExisteNum(arr,i+1,num)
		else
			ExisteNum:= 0;
end;

begin
	for i:=1 to 10 do
	begin
		writeln('[CARGA] Ingrese un numero: ');
		readln(arr[i]);
	end;

	i:=1;
	writeln('Ingrese un numero para saber su existencia: ');
	readln(num);
	if (ExisteNum(arr,i,num)=1) then
		writeln('EL NUMERO EXISTE')
	else
		writeln('EL NUMERO NO EXISTE');

end.