/*
select count(*)
from FotosDCIM

select top 1000 *
from FotosDCIM

select Nombre, iSize, count(*)
from FotosDCIM
group by Nombre, iSize
having count(*) > 1

select * 
from FotosDCIM
where 
1=1
--and nombre = '20170818_085516~3.jpg'                                                                              '                                                                                 %'
and ruta='C:\Users\seguc\OneDrive\Pictures\Albunes\Pueblo'
--and ruta='C:\Users\seguc\OneDrive\Pictures\Galería de Samsung\Pueblo'

select count(*)
from fotosdcim
where ruta='C:\Users\seguc\OneDrive\Pictures\Albunes\Pueblo                                                                                                                                                                                                           '

select count(*)
from fotosdcim
where ruta='C:\Users\seguc\OneDrive\Pictures\Galería de Samsung\Pueblo                                                                                                                                                                                                '
*/

/* marcar fotos fuera de galeria de samsung que estan Si/No en galeria de Samsung
*/

select f1.id, f1.ruta, f1.nombre
from FotosDCIM f1
where
1=1

and ruta not like '%Galería de Samsung%'

and ruta not like '%pictures\ursula%'
and ruta not like '%pictures\escaneos%'
and ruta not like '%pictures\mis escaneos%'
and ruta not like '%pictures\my scans%'
and ruta not like '%pictures\libros%'
and not exists (
	select nombre 
	from fotosdcim
	where ruta<>f1.ruta and nombre = f1.nombre
	)

and ruta='C:\Users\seguc\OneDrive\Pictures\Álbum de cámara'
order by ruta, Nombre