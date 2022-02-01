program recurFMax;
uses CRT;

type
	arreglo = array [1..10] of integer;

var
	max: integer;
	i: integer;
	arr: arreglo;

function FMax(arr:arreglo;i:integer;max:integer):integer;
begin
	if (i=10) then
		FMax:= max
	else
		begin
		if (max < arr[i]) then
			begin
			max:= arr[i];
			FMax:= FMax(arr,i+1,max);
			end;
		end;
		else
			FMax:= FMax(arr,i+1,max);
end;

begin
	for i:=1 to 10 do
	begin
		writeln('[CARGA] Ingrese un numero: ');
		readln(arr[i]);
	end;
	i:=1;
	writeln('Ingrese un numero para saber su existencia: ', FMax(arr,i,max));
end.