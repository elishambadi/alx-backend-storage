-- Select recently formed bands as from 2022
SELECT band_name, (2022 - formed) AS lifespan
FROM metal_bands
WHERE split LIKE '%Glam Rock%'
ORDER BY lifespan DESC;
