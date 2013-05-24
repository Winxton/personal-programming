
select count(*) from (
SELECT term from frequency
WHERE docid = '10398_txt_earn'
AND count = 1
UNION
SELECT term from frequency
WHERE docid='925_txt_trade' 
AND count =1);
