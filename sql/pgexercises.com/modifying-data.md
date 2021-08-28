# Modifying data

![basic-sql-schema.png](..\..\img\basic-sql-schema.png)


## Insert

> The club is adding a new facility - a spa. We need to add it into the facilities table. Use the following values: facid: 9, Name: 'Spa', membercost: 20, guestcost: 30, initialoutlay: 100000, monthlymaintenance: 800.


```sql
INSERT INTO cd.facilities 
VALUES (9, 'Spa', 20, 30, 100000, 800);
```

```sql
insert  into cd.facilities
(facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)  
values  (9,  'Spa',  20,  30,  100000,  800);
```


## Insert 2

> In the previous exercise, you learned how to add a facility. Now you're going to add multiple facilities in one command. Use the following values:
> facid: 9, Name: 'Spa', membercost: 20, guestcost: 30, initialoutlay: 100000, monthlymaintenance: 800.
> facid: 10, Name: 'Squash Court 2', membercost: 3.5, guestcost: 17.5, initialoutlay: 5000, monthlymaintenance: 80.

```sql
INSERT INTO cd.facilities
VALUES 
  (9, 'Spa', 20, 30, 100000, 800),
  (10, 'Squash Court 2', 3.5, 17.5, 5000, 80);
```

```sql
insert  into cd.facilities 
(facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)  
values  (9,  'Spa',  20,  30,  100000,  800),  (10,  'Squash Court 2',  3.5,  17.5,  5000,  80);
```

```sql
insert  into cd.facilities
(facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)  
SELECT  9,  'Spa',  20,  30,  100000,  800  
    UNION  ALL  SELECT  10,  'Squash Court 2',  3.5,  17.5,  5000,  80;
```


## Insert 3

> Let's try adding the spa to the facilities table again. This time, though, we want to automatically generate the value for the next facid, rather than specifying it as a constant. Use the following values for everything else: Name: 'Spa', membercost: 20, guestcost: 30, initialoutlay: 100000, monthlymaintenance: 800.

```sql
INSERT INTO cd.facilities
(facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
SELECT MAX(fac.facid) + 1, 'Spa', 20, 30, 100000, 800
FROM cd.facilities as fac
```

```sql
insert  into cd.facilities 
(facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)  
select 
    (select max(facid) from cd.facilities) + 1,
    'Spa',  
    20,  
    30,  
    100000,  
    800;
```


## Update

> We made a mistake when entering the data for the second tennis court. The initial outlay was 10000 rather than 8000: you need to alter the data to fix the error.


```sql
UPDATE cd.facilities 
SET initialoutlay=10000
WHERE name = 'Tennis Court 2';
```

```sql
update cd.facilities
set initialoutlay =  10000
where facid =  1;
```


> for all records
```sql
update cd.facilities
set initialoutlay =  10000;
```



## Update multiple

> We want to increase the price of the tennis courts for both members and guests. Update the costs to be 6 for members, and 30 for guests.


```sql
UPDATE cd.facilities
SET 
	membercost = 6,
	guestcost = 30
WHERE
	name LIKE '%Tennis Court%';
```

```sql
update cd.facilities
set membercost =  6, guestcost =  30  
where facid in  (0,1);
```



## Update calculated

> We want to alter the price of the second tennis court so that it costs 10% more than the first one. Try to do this without using constant values for the prices, so that we can reuse the statement if we want to.


```sql
UPDATE cd.facilities 
SET membercost=(
  SELECT membercost
  FROM cd.facilities
  WHERE name = 'Tennis Court 1'
  ) * 1.1,
  guestcost=(
  SELECT guestcost
  FROM cd.facilities
  WHERE name = 'Tennis Court 1'
  ) * 1.1
WHERE name = 'Tennis Court 2';
```

```sql
update cd.facilities facs 
set 
    membercost =  (select membercost *  1.1  from cd.facilities where facid =  0), 
    guestcost =  (select guestcost *  1.1  from cd.facilities where facid =  0)  
where facs.facid =  1;
```


## Delete

> As part of a clearout of our database, we want to delete all bookings from the cd.bookings table. How can we accomplish this?

```sql
DELETE FROM cd.bookings;
```

```sql
TRUNCATE cd.bookings;
```


## Вelete wh

> We want to remove member 37, who has never made a booking, from our database. How can we achieve that?

```sql
DELETE 
FROM cd.members mem
WHERE mem.memid = 37;
```



## Delete wh2

> In our previous exercises, we deleted a specific member who had never made a booking. How can we make that more general, to delete all members who have never made a booking?

```sql
DELETE 
FROM cd.members mem
WHERE (
  SELECT COUNT(bk.memid)
  FROM cd.bookings bk
  WHERE bk.memid = mem.memid
  ) = 0
```

```sql
delete  
from cd.members 
where memid not in (select memid from cd.bookings);
```

```sql
DELETE 
FROM cd.members mem
WHERE NOT EXISTS (
    SELECT 1 
    FROM cd.bookings 
    WHERE memid = mem.memid
)
```



