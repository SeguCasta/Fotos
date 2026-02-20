/*
CREATE TABLE dbo.CopiaFicheros (
    Id              INT IDENTITY PRIMARY KEY,
    RutaOrigen      NVARCHAR(500) NOT NULL,
    NombreFichero   NVARCHAR(255) NOT NULL,
    RutaDestino     NVARCHAR(500) NOT NULL,
    Copiado         BIT NOT NULL DEFAULT 0,
    FechaCopia      DATETIME NULL,
    Error           NVARCHAR(1000) NULL
);

*/
--Insert into CopiaFicheros
-- 'C:\Users\seguc\OneDrive\Pictures\Galería de Samsung\DCIM\Camera'
select f1.ruta as RutaOrigen, f1.nombre as NombreFichero, 'C:\Users\seguc\OneDrive\Pictures\Galería de Samsung' as RutaDestino, 0, '01/01/1999',NULL
from FotosDCIM f1
where
1=1

and ruta not like '%Galería de Samsung%'

and ruta not like '%pictures\NO_Galeria%'

--and ruta not like '%pictures\Albunes%'


and not exists (
	select nombre 
	from fotosdcim
	where ruta<>f1.ruta and nombre = f1.nombre
	)

and ruta like 'C:\Users\seguc\OneDrive\Pictures\Albunes%'
order by ruta, Nombre

/*
select * from CopiaFicheros
*/

