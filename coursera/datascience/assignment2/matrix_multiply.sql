select val from (
select A.row_num as crow, B.col_num as ccol, sum(A.value*B.value) as val from A,B
where A.col_num = B.row_num
group by A.row_num, B.col_num
) where crow = 2 and ccol = 3;