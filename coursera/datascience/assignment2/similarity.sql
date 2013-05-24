/*
select sum(t1.count * t2.count) --, sum(t1.count*t2.count)
FROM
( select * from frequency where docid = '10080_txt_crude' ) t1
JOIN
( select * from frequency where docid = '17035_txt_earn' ) t2
ON t1.term = t2.term
GROUP BY t1.docid, t2.docid;
*/

select A.docid, B.docid, sum(A.count * B.count)
FROM frequency A, frequency B
WHERE A.term = B.term AND A.docid < B.docid
GROUP BY A.docid, B.docid;