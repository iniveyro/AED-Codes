program ej211;
uses crt;

var
	sec: text;
	v: char;
	cont: integer;

Procedure ARR(VAR sec_local: text);
	begin
		assign(sec_local, 'datos_secuencia.txt');

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
	while not eof (sec) do
	begin

		if v = 'A' then
			cont:=cont+1;
		
		read(sec,v);
	
	end;
	writeln('La cantidad de A que hay es de: ', cont);
	close(sec);
end.