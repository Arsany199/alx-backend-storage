-- lists all bands with Glam rock as their main style
SELECT band_name,
       2022 - SUBSTRING_INDEX(formed, '-', -1) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
