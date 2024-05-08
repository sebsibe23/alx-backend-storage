-- Ranks the country origins of bands, ordered by a number of (non-unique) fans.
SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;
