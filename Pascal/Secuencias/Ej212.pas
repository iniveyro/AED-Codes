program ej212;
uses crt;

var
	sec: text;
	v: char;
	cont: integer;

function Consonantes(v:char):boolean;
begin
	case v of
		'A': Consonantes:= False;
		'E': Consonantes:= False;
		'I': Consonantes:= False;
		'O': Consonantes:= False;
		'U': Consonantes:= False;
		' ': Consonantes:= False;
	else
		Consonantes:= True;
	end;
end;

Procedure ARR(VAR sec_local: text);
	begin
		assign(sec_local, 'datosEj212.txt');

		//Control de acciones sobre el archivo
		{$I-}				
			reset(sec_local);				
		{$I+}

		//Verifico estado de la accion ejecutada
	  	if IOResult <> 0 then	  			  			
		      	writeln('No se pudo abrir el archivo... ERROR');	  			    
	end;

begin
	
	cont:=0;
	ARR(sec);
	read(sec,v);
	while (v <> 'Z') do
	begin

		if Consonantes(v) = True then
			cont:=cont+1;
		read(sec,v);
	
	end;
	writeln('La cantidad de consonates que hay es de: ', cont);
	close(sec);
end.