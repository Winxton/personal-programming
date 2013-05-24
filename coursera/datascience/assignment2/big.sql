select count(*) from (
SELECT docid, sum(count) from frequency
group by docid
having sum(count) > 300
);