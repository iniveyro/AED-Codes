program FARMACIA; 
uses CRT;
var
    sec,sal: file of char;
    v: char;
    cont1,cont3,i,resg1,resg2:integer;
    resguardo:integer;
    bandera:boolean;
function enterosT(k:char):integer;
begin
    case k of
        '0': enterosT:=0;
        '1': enterosT:=1;
        '2': enterosT:=2;
        '3': enterosT:=3;
        '4': enterosT:=4;
        '5': enterosT:=5;
        '6': enterosT:=6;
        '7': enterosT:=7;
        '8': enterosT:=8;
        '9': enterosT:=9;
    end;
end; 
function mes(k:integer):string;
begin
	case k of 
	 1: mes:= 'enero';
	 2: mes:= 'febrero';
	 3: mes:= 'marzo';
	 4: mes:= 'abril';
	 5: mes:= 'mayo';
	 6: mes:= 'junio';
	 7: mes:= 'julio';
	 8: mes:= 'agosto';
	 9: mes:= 'septiembre';
	 10: mes:= 'ocutubre';
	 11: mes:= 'noviembre';
	 12: mes:= 'diciembre';
    end;
end; 
begin
    cont1:=0;
    cont3:=0;
    i:=0;
    resg1:=0;
    resg2:=0;
    resguardo:=0;
    bandera:=true;
    assign(sec, 'codigo2.dat');
    {$I-}
    reset(sec);
    {$I+}
    if IOResult <> 0 then
        halt(2);
    assign(sal, 'salida.dat'); 
    rewrite(sal);
    read(sec, v);
    //while v <>'%' do     //R 05052019codigo1#   
    while not EOF(sec) do              
    begin
        if bandera then
        begin
            bandera:=false;
            if v ='R' then
            begin
                for i:=1 to 3 do
                begin
                    read(sec,v);
                    write(sal,v);                   
                end;              //R050 52019codigo1#  
                resg2:=enterosT(v)*10;
                read(sec,v);
                write(sal,v);
                resg2:=resg2+enterosT(v);    //R0505 2019codigo1#
                read(sec,v);
                while v<>'#' do
                begin
                    write(sal,v);
                    read(sec,v);
                end;     //R05052019codigo1#    
                write(sal,'-');   
            end
            else
            begin
                for i:=1 to 3 do
                    read(sec,v);
		        resg2:=enterosT(v)*10;              
		        read(sec,v);
		        resg2:=resg1+enterosT(v);
                while v<>'#' do
                    read(sec,v); 
            end;    //R05052019codigo1#   
            read(sec,v);     //R05052019codigo1#C 2345#50#10+ 
            write('*');
            while v<>'#' do
            begin
                write(v);
                read(sec,v);            
            end;     //R05052019codigo1#C2345# 50#10+ 
            write('-');
            read(sec,v);
            while v<>'#' do
            begin
                write(v);
                read(sec,v);            
            end;     //R05052019codigo1#C2345# 50#10+ 
            writeln('.');
            cont1:=1; 
            while v<>'+' do
               read(sec,v); 
            read(sec,v);
        end; //R05052019codigo1#C2345#50#10+ 
        if v='R' then
        begin
            for i:=1 to 3 do
            begin
                read(sec,v);
                write(sal,v);
            end; //R050 52019codigo1#C2345#50#10+ 
            resg1:=enterosT(v)*10;
            read(sec,v);
            write(sal,v);
            resg1:=resg2+enterosT(v);
            read(sec,v); //R05052 019codigo1#C2345# 50#10+ 
            while v<>'#' do
            begin
                write(sal,v);
                read(sec,v);
            end; //R05052019codigo1# C2345#50#10+
            write(sal,'-'); 
        end
        else
        begin
            for i:=1 to 3 do
                read(sec,v); //R050 52019codigo1#C2345#50#10+ 
            resg1:=enterosT(v)*10;
            read(sec,v);
            resg1:=resg1+enterosT(v);
            while v<>'#' do
                read(sec,v); 
        end; //R05052019codigo1# C2345#50#10+
        read(sec,v);
        write('*');
        while v<>'#' do
        begin
            write(v);
            read(sec,v); 
        end; //R05052019codigo1#C2345# 50#10+ 
        write('-');
        read(sec,v);
        while v<>'#' do
        begin
            write(v);
            read(sec,v); 
        end; //R05052019codigo1#C2345# 50#10+ 
        writeln('.');
        while v<>'+' do
            read(sec,v);  //R05052019codigo1#C2345#50#10+  
    	if resg1=resg2 then
        begin
		    cont1:=cont1+1;
        end
	    else
        begin
            if resg1<>resg2 then
            begin
                if cont1>cont3 then
                begin
                    cont3:=cont1;
                    resguardo:=resg2;
                end;
                resg2:=resg1;
                cont1:=1;
            end;
        end;
        read(sec,v); //R05052019codigo1#C2345#50#10+&  
    end;
    if cont1>cont3 then
    begin;
        resguardo:=resg1;
        cont3:=cont1;
        writeln('el mes en el que mas remedios ingresaron es ');
        write(mes(resguardo));
        write(',el cual tuvo un total de remedios ingresados de: ');
        write(cont3);
    end;
    if cont1<cont3 then
    begin;
        writeln('el mes en el que mas remedios ingresaron es ');
        write(mes(resguardo));
        write(',el cual tuvo un total de remedios ingresados de: ');
        write(cont3); 
    end;
    if cont3=0 then
        write('secuencia bacia');
    close(sec);
    close(sal);
end.	

