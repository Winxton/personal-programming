/*
create view query
AS
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count ;
*/

select max(sim) from (
select newFreq.docid, frequency.docid, sum (frequency.count * newFreq.count) as sim from newFreq, frequency
where newFreq.term = frequency.term and newFreq.docid='q'
group by newFreq.docid, frequency.docid
);