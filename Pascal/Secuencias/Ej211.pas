program ej211;
uses crt;

var
	sec: string[10];
	v: char;
	pos: integer;
	cont: integer;

begin
	pos:=0;
	sec:= 'AAAeeAee*';
	v:= sec[pos];
	cont:=0;
	while v <> '*' do
	begin

		if v = 'A' then
			cont:=cont+1;
		
		pos:=pos+1;
		v:= sec[pos];
	
	end;
	writeln('La cantidad de A que hay es de: ', cont);
end.