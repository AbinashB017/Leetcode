
Select max(num) as num
from(
    SELECT num
FROM MyNumbers
GROUP BY num
HAVING COUNT(*) = 1
) t;
