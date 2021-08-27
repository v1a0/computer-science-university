# Joins ans Subqueries (Solutions)

![basic-sql-schema.png](..\..\img\basic-sql-schema.png)



## Simple join

> How can you produce a list of the start times for bookings by members named 'David Farrell'?

```sql
SELECT starttime 
FROM cd.bookings 
WHERE memid = (
  SELECT memid
  FROM cd.members
  WHERE
  	surname = 'Farrell'
	AND
	firstname = 'David'
  LIMIT 1
  );
```

```sql
SELECT bks.starttime 
FROM cd.bookings bks INNER JOIN cd.members mems
ON mems.memid = bks.memid 
WHERE 
    mems.firstname='David' AND mems.surname='Farrell';
```

```sql
SELECT starttime
FROM cd.bookings INNER JOIN cd.members
    ON cd.members.memid = cd.bookings.memid
WHERE
	cd.members.firstname = 'David'
    AND
    cd.members.surname = 'Farrell'
```

```sql
SELECT starttime 
FROM cd.bookings bk, cd.members mem
WHERE
	bk.memid = mem.memid
	AND
	mem.firstname = 'David'
	AND
	mem.surname = 'Farrell';
```


##  Simple join 2

> How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'? Return a list of start time and facility name pairings, ordered by the time.

```sql
SELECT bk.starttime AS start, fa.name AS name
FROM 
cd.bookings as bk INNER JOIN cd.facilities as fa
ON bk.facid = fa.facid
WHERE 
	fa.name LIKE '%Tennis Court%'
	AND
	'2012-09-21' <= bk.starttime
	AND
	bk.starttime < '2012-09-22'

ORDER BY bk.starttime
```


```sql
SELECT bks.starttime AS  start, facs.name AS name 
FROM cd.facilities facs INNER JOIN cd.bookings bks
ON facs.facid = bks.facid
WHERE 
    facs.name IN ('Tennis Court 2','Tennis Court 1') 
    AND
    bks.starttime >=  '2012-09-21' 
    AND
    bks.starttime <  '2012-09-22' 
ORDER BY bks.starttime;
```



## Self

> How can you output a list of all members who have recommended another member? Ensure that there are no duplicates in the list, and that results are ordered by (surname, firstname).


```sql
SELECT DISTINCT m1.firstname, m1.surname
FROM cd.members as m1 INNER JOIN cd.members as m2 
ON m1.memid = m2.recommendedby
ORDER BY m1.surname, m1.firstname
```


```sql
select  distinct recs.firstname as firstname, recs.surname as surname
from cd.members mems inner join cd.members recs 
on recs.memid = mems.recommendedby 
order by surname, firstname;
```


## Self 2

> How can you output a list of all members, including the individual who recommended them (if any)? Ensure that results are ordered by (surname, firstname).


```sql
SELECT mem.firstname memfname, mem.surname memsname, rec.firstname recfname, rec.surname recsname
FROM cd.members as mem LEFT OUTER JOIN cd.members as rec
ON rec.memid = mem.recommendedby
ORDER BY memsname, memfname
```

```sql
select mems.firstname as memfname, mems.surname as memsname, recs.firstname as recfname, recs.surname as recsname
from cd.members mems left  outer  join cd.members recs
on recs.memid = mems.recommendedby
order by memsname, memfname;
```



##  Three join

> How can you produce a list of all members who have used a tennis court? Include in your output the name of the court, and the name of the member formatted as a single column. Ensure no duplicate data, and order by the member name followed by the facility name.


```sql
SELECT DISTINCT mem.firstname || ' ' || mem.surname as member, fac.name as facility
FROM cd.bookings bk INNER JOIN cd.facilities fac
ON fac.facid = bk.facid AND fac.name LIKE '%Tennis Court%'
INNER JOIN cd.members mem
ON bk.memid = mem.memid
ORDER BY member, facility
```

```sql
select distinct mems.firstname ||  ' '  || mems.surname as member, facs.name as facility
from cd.members mems inner join cd.bookings bks
on mems.memid = bks.memid 
inner join cd.facilities facs
on bks.facid = facs.facid
where facs.name in  ('Tennis Court 2','Tennis Court 1') 
order by member, facility
```


##  Three join 2

> How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30? Remember that guests have different costs to members (the listed costs are per half-hour 'slot'), and the guest user is always ID 0. Include in your output the name of the facility, the name of the member formatted as a single column, and the cost. Order by descending cost, and do not use any subqueries.

```sql
SELECT * FROM (
  SELECT 
	mem.firstname || ' ' || mem.surname member,
	fac.name facility,
	CASE
		WHEN mem.memid = 0
			THEN fac.guestcost * bk.slots
		ELSE fac.membercost * bk.slots
	END as cost
	
	FROM cd.bookings bk
	INNER JOIN cd.facilities fac
	ON fac.facid = bk.facid 
		AND 
		bk.starttime > '2012-09-14' 
		AND
		bk.starttime <= '2012-09-15'
	LEFT JOIN cd.members mem
	ON bk.memid = mem.memid
	ORDER BY cost DESC

) res WHERE res.cost > 30
```

```sql
select mems.firstname ||  ' '  || mems.surname as member, facs.name as facility,  case  when mems.memid =  0  then bks.slots*facs.guestcost else bks.slots*facs.membercost end  as cost
from cd.members mems inner join cd.bookings bks
on mems.memid = bks.memid 
inner join cd.facilities facs 
on bks.facid = facs.facid 
where bks.starttime >=  '2012-09-14' 
    and 
    bks.starttime <  '2012-09-15' 
    and  (  
        (mems.memid = 0 and bks.slots*facs.guestcost > 30)  
        or  
        (mems.memid != 0 and bks.slots*facs.membercost > 30)
    )
order by cost desc;
```