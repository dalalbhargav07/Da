a.
	select 
		
		distinct tr.trip_headsign
	from 
	trips tr
	join stopTimes sti on (tr.trip_id = sti.trip_id)
	join stops st on (sti.stop_id = st.stop_id)
	where 
	st.name_stop =  ' Ferry Stop - Alderney';

	Time taken : 0.062 sec

b.
	select 
	
		distinct tr.trip_headsign
	from 
	trips tr
	join stopTimes sti on (tr.trip_id = sti.trip_id)
	where 
	sti.arrival_time between '20:57:00' and '20:57:00';
	
	Time taken : 0.281 sec

c. 
	select 
		sti.*
	from 
	trips tr
	join stopTimes sti on (tr.trip_id = sti.trip_id)
	join stops st on (sti.stop_id = st.stop_id)
	where 
	tr.trip_headsign =  'FERRY TO HALIFAX'
	and tr.route_id = 'FerD-116';

	Time taken : 0.109 sec

d.
	select 

		st.stop_id,
		count(sti.trip_id) AS coun
	from 
	trips tr
	join stopTimes sti on (tr.trip_id = sti.trip_id)
	join stops st on (sti.stop_id = st.stop_id)
	group by 
		st.stop_id
	order by 2 desc limit 3;
	
	Time taken : 1.421 sec
	