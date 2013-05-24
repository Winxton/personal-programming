
select count(*) from
( select * from frequency where term = 'transactions' ) t1
join
( select * from frequency where term = 'world') t2
on t1.docid = t2.docid;


