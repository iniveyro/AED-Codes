program ej212;
uses crt;

var
	sec: text;
	sal: text;
	v: char;

Procedure Crear(VAR sec_local: text);
begin
	assign(sec_local, 'salEj213.txt');

	//Control de acciones sobre el archivo
	{$I-}				
		rewrite(sec_local);				
	{$I+}
	//Verifico estado de la accion ejecutada
  	if IOResult <> 0 then	  			  			
      	writeln('No se pudo abrir el archivo... ERROR');	  			    
end;



Procedure ARR(VAR sec_local: text);
begin
	assign(sec_local, 'datosEj213.txt');

	//Control de acciones sobre el archivo
	{$I-}				
		reset(sec_local);				
	{$I+}
	//Verifico estado de la accion ejecutada
  	if IOResult <> 0 then	  			  			
      	writeln('No se pudo abrir el archivo... ERROR');	  			    
end;

begin

	ARR(sec);
	Crear(sal);
	read(sec,v);

	while not eof(sec) do
	begin
		if v = '$' then
			read(sec,v)
		else
		begin
			write(v);
			write(sal,v);
			read(sec,v);
		end;
	end;
	
	close(sec);
	close(sal);
end.