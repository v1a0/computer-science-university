# Aggregation


## Count the number of facilities

```sql
SELECT COUNT(name) FROM cd.facilities;
```

```sql
SELECT COUNT(DISTINCT name) FROM cd.facilities;
```



## Count the number of expensive facilities

> Produce a count of the number of facilities that have a cost to guests of 10 or more.

```sql
SELECT COUNT(fac.facid) 
FROM cd.facilities AS fac 
WHERE fac.guestcost >= 10
```


## Count the number of recommendations each member makes

> Produce a count of the number of recommendations each member has made. Order by member ID.


```sql
SELECT столбцы
FROM таблица
[WHERE условие_фильтрации_строк]
[GROUP BY столбцы_для_группировки]
[HAVING условие_фильтрации_групп]
[ORDER BY столбцы_для_сортировки]
```

```sql
SELECT recommendedby, COUNT(*)
FROM cd.members
WHERE recommendedby IS NOT NULL
GROUP BY recommendedby
ORDER BY recommendedby;
```


## List the total slots booked per facility

> Produce a list of the total number of slots booked per facility. For now, just produce an output table consisting of facility id and slots, sorted by facility id.

```sql
SELECT facid, SUM(slots) AS "Total Slots"
FROM cd.bookings
GROUP BY facid
ORDER BY facid
```


## List the total slots booked per facility in a given month

> Produce a list of the total number of slots booked per facility in the month of September 2012. Produce an output table consisting of facility id and slots, sorted by the number of slots.


```sql
SELECT facid, SUM(slots) AS "Total Slots"
FROM cd.bookings
WHERE starttime >= '09-01-2012' AND starttime < '10-01-2012'
GROUP BY facid
ORDER BY "Total Slots"
```

```sql
select facid, sum(slots)  as  "Total Slots"  
    from cd.bookings 
    where starttime >=  '2012-09-01'  
    and starttime <  '2012-10-01'  
    group  by facid 
order  by sum(slots);
```



## List the total slots booked per facility per month

> Produce a list of the total number of slots booked per facility per month in the year of 2012. Produce an output table consisting of facility id and slots, sorted by the id and month.


```sql
SELECT facid, EXTRACT(MONTH FROM starttime) AS "month", SUM(slots) AS "Total Slots"
FROM cd.bookings
WHERE EXTRACT(YEAR FROM starttime) = '2012'
GROUP BY facid, "month"
```



## Find the count of members who have made at least one booking

> Find the total number of members (including guests) who have made at least one booking.


```sql
SELECT COUNT(DISTINCT memid)
FROM cd.bookings ;
```



## List facilities with more than 1000 slots booked

> Produce a list of facilities with more than 1000 slots booked. Produce an output table consisting of facility id and slots, sorted by facility id.

```sql
SELECT facid, SUM(slots) AS "Total Slots"
FROM cd.bookings
GROUP BY facid
HAVING SUM(slots) > 1000
ORDER BY facid;
```


## Find the total revenue of each facility 

> Produce a list of facilities along with their total revenue. The output table should consist of facility name and revenue, sorted by revenue. Remember that there's a different cost for guests and members!

```sql
SELECT 
	fac.name,
	SUM(
	  CASE 
	  	WHEN bk.memid = 0
	  		THEN fac.guestcost * bk.slots
	  	ELSE fac.membercost * bk.slots
	  END
	) AS "revenue"
FROM cd.facilities AS fac
LEFT JOIN cd.bookings bk
ON bk.facid = fac.facid
GROUP BY fac.name
ORDER BY "revenue"
```