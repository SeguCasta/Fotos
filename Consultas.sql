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
--and nombre='IMG-20161212-WA0001.jpg                                                                             '
--and ruta='C:\Users\seguc\OneDrive\Pictures\Albunes\Pueblo'
and ruta='C:\Users\seguc\OneDrive\Pictures\Galería de Samsung\Pueblo'

select count(*)
from fotosdcim
where ruta='C:\Users\seguc\OneDrive\Pictures\Albunes\Pueblo                                                                                                                                                                                                           '

select count(*)
from fotosdcim
where ruta='C:\Users\seguc\OneDrive\Pictures\Galería de Samsung\Pueblo                                                                                                                                                                                                '

