# Write your MySQL query statement below
select w1.Id from Weather w1
inner join Weather w2 on w1.Temperature > w2.Temperature and DATEDIFF(w1.RecordDate, w2.RecordDate) = 1;