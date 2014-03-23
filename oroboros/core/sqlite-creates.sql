/* Oroboros - SQLite db structure */

/* Info */
create table Info (
	version integer not null
);/*End*/


/* Aspects */
create table Aspects (
	_idx integer primary key,
	name varchar not null unique, -- aspect name
	angle numeric not null unique check (angle between 0 and 180), -- angle
	ranking integer not null check (ranking > -1),
	bool_use integer not null check (bool_use in (0, 1)), -- for new filters
	default_orb numeric not null check (default_orb >= 0), -- for new filters
	color varchar not null check (rgxp('^[0-9]{1,3},[0-9]{1,3},[0-9]{1,3}$', color) = 1),
	glyph varchar not null,
	comment text not null default ''
);/*End*/

/* AspectsInsertTrigger */
-- Cascade aspects inserts to filters
create trigger AspectsInsertTrigger after insert on Aspects for each row
	begin
		-- Every aspect must appear in every aspects filter set
		insert into _AspectsFilters (filter_idx, aspect_idx, bool_use)
			select _idx, new._idx, new.bool_use from AspectsFilters order by name;
		-- Every aspect must appear in every orbs filter set
		insert into _OrbsFilters (filter_idx, aspect_idx, orb)
			select _idx, new._idx, new.default_orb from OrbsFilters order by name;
	end;/*End*/

/* AspectsUpdateTrigger */
-- Cascade aspects id update to filters
create trigger AspectsUpdateTrigger after update of _idx on Aspects for each row
	begin
		update _AspectsFilters set aspect_idx = new._idx where aspect_idx = old._idx;
		update _OrbsFilters set aspect_idx = new._idx where aspect_idx = old._idx;
	end;/*End*/

/* AspectsDeleteTrigger */
-- Cascade aspects delete on filters
create trigger AspectsDeleteTrigger after delete on Aspects for each row
	begin
		delete from _AspectsFilters where aspect_idx = old._idx;
		delete from _OrbsFilters where aspect_idx = old._idx;
	end;/*End*/



/* AspectsFilters */
create table AspectsFilters (
	_idx integer primary key, -- referenced by Filters.aspects and MidPointsFilters.aspects
	name varchar(250) default '<?>' unique,
	comment text not null default ''
);/*End*/

/* _AspectsFilters */
create table _AspectsFilters (
	filter_idx integer not null, -- references AspectsFilters._idx,
	aspect_idx integer not null, -- references Aspects._idx,
	bool_use integer not null default 0 check (bool_use in (0, 1)),
	primary key (filter_idx, aspect_idx)
);/*End*/

/* AspectsFiltersInsertTrigger */
-- Cascade aspects filters inserts to sub table
create trigger AspectsFiltersInsertTrigger after insert on AspectsFilters for each row
	begin
		-- Insert default values for each aspect
		insert into _AspectsFilters (filter_idx, aspect_idx, bool_use)
			select new._idx, _idx, bool_use from Aspects;
	end;/*End*/

/* AspectsFiltersUpdateTrigger */
-- Cascade aspects filters id update to sub table and Filters
create trigger AspectsFiltersUpdateTrigger after update of _idx on AspectsFilters for each row
	begin
		update _AspectsFilters set filter_idx = new._idx where filter_idx = old._idx;
		update Filters set aspects = new._idx where aspects = old._idx;
		update MidPointsFilters set aspects = new._idx where aspects = old._idx;
	end;/*End*/

/* AspectsFiltersDeleteTrigger */
-- Casade aspects filters deletes to sub table, if not referenced by Filters or MidPointsFilters
create trigger AspectsFiltersDeleteTrigger before delete on AspectsFilters for each row
	begin
		select raise (rollback, 'Error: delete on AspectsFilters violates foreign key constraint.')
			where (select aspects from Filters where aspects = old._idx) is not null;
		select raise (rollback, 'Error: delete on AspectsFilters violates foreign key constraint.')
			where (select aspects from MidPointsFilters where aspects = old._idx) is not null;
		delete from _AspectsFilters where filter_idx = old._idx;
	end;/*End*/

/* _AspectsFiltersUpdateTrigger */
-- Check aspects filters id exists
create trigger _AspectsFiltersUpdateTrigger before update of filter_idx on _AspectsFilters for each row
	begin
		select raise (rollback, 'Error: update on _AspectsFilters violates foreign key constraint.')
			where (select _idx from AspectsFilters where _idx = new.filter_idx) is null;
	end;/*End*/



/* OrbsFilters */
create table OrbsFilters (
	_idx integer primary key, -- referenced by Filters.orbs and MidPointsFilters.orbs
	name varchar(250) default '<?>' unique,
	comment text not null default ''
);/*End*/

/* _OrbsFilters */
create table _OrbsFilters (
	filter_idx integer not null, -- references OrbsFilters._idx,
	aspect_idx integer not null, -- references Aspects._idx,
	orb numeric not null default 0 check (orb >= 0),
	primary key (filter_idx, aspect_idx)
);/*End*/

/* OrbsFiltersInsertTrigger */
-- Cascade orbs filters inserts to sub table
create trigger OrbsFiltersInsertTrigger after insert on OrbsFilters for each row
	begin
		-- Insert default values for each aspect
		insert into _OrbsFilters (filter_idx, aspect_idx, orb)
			select new._idx, _idx, default_orb from Aspects;
	end;/*End*/

/* OrbsFiltersUpdateTrigger */
-- Cascade orbs filters id update to sub table and Filters
create trigger OrbsFiltersUpdateTrigger after update of _idx on OrbsFilters for each row
	begin
		update _OrbsFilters set filter_idx = new._idx where filter_idx = old._idx;
		update Filters set orbs = new._idx where orbs = old._idx;
		update MidPointsFilters set orbs = new._idx where orbs = old._idx;
	end;/*End*/

/* OrbsFiltersDeleteTrigger */
-- Cascade orbs filters deletes to sub table, if not referenced by Filters
create trigger OrbsFiltersDeleteTrigger before delete on OrbsFilters for each row
	begin
		select raise (rollback, 'Error: delete on OrbsFilters violates foreign key constraint.')
			where (select orbs from Filters where orbs = old._idx) is not null;
		select raise (rollback, 'Error: delete on OrbsFilters violates foreign key constraint.')
			where (select orbs from MidPointsFilters where orbs = old._idx) is not null;
		delete from _OrbsFilters where filter_idx = old._idx;
	end;/*End*/

/* _OrbsFilters_Update_Trigger */
-- Check orbs filter id exists
create trigger _OrbsFiltersUpdateTrigger before update of filter_idx on _OrbsFilters for each row
	begin
		select raise (rollback, 'Error: update on _OrbsFilters violates foreign key constraint.')
			where (select _idx from OrbsFilters where _idx = new.filter_idx) is null;
	end;/*End*/



/* Planets */
create table Planets (
	_idx integer primary key,
	num integer not null unique, -- Body/asteroid number as defined in swephexp.h, or another...
	-- from 0 to 39 : Default bodies + lunar nodes, Lilith + Default asteroids: Ceres, Pallas, Juno, Vesta.
	-- from 40 to 58: Uranian + Fictitious bodies
	-- from 1000 to 9999: fixed stars.
	-- from 10000 : Asteroids.
	-- or negative values for other bodies :
	-- -1 = SE_ECL_NUT : Dont use here.
	-- from -2 to -99 : Bodies based on built-ins planets (Priapus, south nodes).
	-- from -100 to -199 : Houses cusps.
	-- from -200 to -299 : Bodies whose position is based on houses cusps only.
	-- from -300 to -? : "Parts" and other subtilities, based on houses cusps and planets.
	name varchar not null unique,
	family integer not null check (family between -1 and 6), -- planet family (for gui):
	-- family 0 = traditional planet (sun->pluto, default asteroids, nodes, etc)
	-- family 1 = uranian & fictitious bodies
	-- family 2 = fixed stars
	-- family 3 = additional asteroids
	-- family 4 = houses (and those based on them only)
	-- family 5 = parts
	ranking integer not null check (ranking > -1), -- ranking
	bool_use integer not null default 0 check (bool_use in (0, 1)), -- Wether this body is displayed by default or not
	bool_aspect integer not null default 0 check (bool_aspect in (0, 1)), -- Wether body is aspected by default or not
	orb_mod varchar not null default '0' check (rgxp('^[+-]?[0-9]+\.?[0-9]*[%]?$', orb_mod) = 1), -- orb added or removed by default, in % or degrees
	glyph varchar not null default 'image.png',
	comment text not null default ''
);/*End*/



/* PlanetsFilters */
create table PlanetsFilters (
	_idx integer primary key, -- referenced by Filters.planets
	name varchar(250) default '<?>' unique,
	comment text not null default ''
);/*End*/

/* _PlanetsFilters */
create table _PlanetsFilters (
	filter_idx integer not null, -- references PlanetsFilters._idx,
	planet_idx integer not null, -- references Planets._idx,
	bool_use integer not null default 0 check (bool_use in (0, 1)),
	primary key (filter_idx, planet_idx)
);/*End*/

/* PlanetsFiltersInsertTrigger */
-- Cascade planets filters inserts to subtable
create trigger PlanetsFiltersInsertTrigger after insert on PlanetsFilters for each row
	begin
		-- Insert default values for each planet
		insert into _PlanetsFilters (filter_idx, planet_idx, bool_use)
			select new._idx, _idx, bool_use from Planets;
	end;/*End*/

/* planetsFiltersUpdateTrigger */
-- Cascade planets filters id update to sub table and Filters
create trigger PlanetsFiltersUpdateTrigger after update of _idx on PlanetsFilters for each row
	begin
		update _PlanetsFilters set filter_idx = new._idx where filter_idx = old._idx;
		update Filters set planets = new._idx where planets = old._idx;
		update MidPointsFilters set planets = new._idx where planets = old._idx;
	end;/*End*/

/* PlanetsFiltersDeleteTrigger */
-- Cascade planets filters deletes to sub table, if not referenced by Filters
create trigger PlanetsFiltersDeleteTrigger before delete on PlanetsFilters for each row
	begin
		select raise (rollback, 'Error: delete on PlanetsFilters violates foreign key constraint.')
			where (select planets from Filters where planets = old._idx) is not null;
		select raise (rollback, 'Error: delete on PlanetsFilters violates foreign key constraint.')
			where (select planets from MidPointsFilters where planets = old._idx) is not null;
		delete from _PlanetsFilters where filter_idx = old._idx;
	end;/*End*/

/* _PlanetsFiltersUpdateTrigger */
-- Check planets filter id exists
create trigger _PlanetsFiltersUpdateTrigger before update of filter_idx on _PlanetsFilters for each row
	begin
		select raise (rollback, 'Error: update on _PlanetsFilters violates foreign key constraint.')
			where (select _idx from PlanetsFilters where _idx = new.filter_idx) is null;
	end;/*End*/



/* AspectsRestrictions */
create table AspectsRestrictions (
	_idx integer primary key, -- referenced by Filters.asprestr
	name varchar(250) default '<?>' unique,
	comment text not null default ''
);/*End*/

/* _AspectsRestrictions */
create table _AspectsRestrictions (
	filter_idx integer not null, -- references AspectsRestrictions._idx,
	planet_idx integer not null, -- references Planets._idx,
	bool_asp integer not null default 0 check (bool_asp in (0, 1)),
	primary key (filter_idx, planet_idx)
);/*End*/

/* AspectsRestrictionsInsertTrigger */
-- Cascade aspects restrictions filters to sub table
create trigger AspectsRestrictionsInsertTrigger after insert on AspectsRestrictions for each row
	begin
		-- Insert default values for each planet
		insert into _AspectsRestrictions (filter_idx, planet_idx, bool_asp)
			select new._idx, _idx, bool_aspect from Planets;
	end;/*End*/

/* AspectsRestrictionsUpdateTrigger */
-- Cascade aspects restrictionss filters id updates to subtable and Filters
create trigger AspectsRestrictionsUpdateTrigger after update of _idx on AspectsRestrictions for each row
	begin
		update _AspectsRestrictions set filter_idx = new._idx where filter_idx = old._idx;
		update Filters set asprestr = new._idx where asprestr = old._idx;
		update MidpointsFilters set asprestr = new._idx where asprestr = old._idx;
	end;/*End*/

/* AspectsRestrictionsDeleteTrigger */
-- Cascade aspects restrictionss filters deletes, if not referenced by Filters
create trigger AspectsRestrictionsDeleteTrigger before delete on AspectsRestrictions for each row
	begin
		select raise (rollback, 'Error: delete on AspectsRestrictions violates foreign key constraint.')
			where (select asprestr from Filters where asprestr = old._idx) is not null;
		select raise (rollback, 'Error: delete on AspectsRestrictions violates foreign key constraint.')
			where (select asprestr from MidPointsFilters where asprestr = old._idx) is not null;
		delete from _AspectsRestrictions where filter_idx = old._idx;
	end;/*End*/

/* _AspectsRestrictionsUpdateTrigger */
-- Check aspects restrictionss filter id exists
create trigger _AspectsRestrictionsUpdateTrigger before update of filter_idx on _AspectsRestrictions for each row
	begin
		select raise (rollback, 'Error: update on _AspectsRestrictions violates foreign key constraint.')
			where (select _idx from AspectsRestrictions where _idx = new.filter_idx) is null;
	end;/*End*/



/* OrbsRestrictions */
create table OrbsRestrictions (
	_idx integer primary key, -- referenced by Filters.orbrestr
	name varchar(250) default '<?>' unique,
	comment text not null default ''
);/*End*/

/* _OrbsRestrictions */
create table _OrbsRestrictions (
	filter_idx integer not null, -- references OrbsRestrictions._idx,
	planet_idx integer not null, -- references Planets._idx,
	orb_mod varchar(15) not null default '0',
	primary key (filter_idx, planet_idx)
);/*End*/

/* OrbsRestrictionsInsertTrigger */
-- Cascade orbs restrictions filters inserts to sub table
create trigger OrbsRestrictionsInsertTrigger after insert on OrbsRestrictions for each row
	begin
		-- Insert default values for each planet
		insert into _OrbsRestrictions (filter_idx, planet_idx, orb_mod)
			select new._idx, _idx, orb_mod from Planets;
	end;/*End*/

/* OrbsRestrictionsUpdateTrigger */
-- Cascade orbs restrictions filters id update to subtable and Filters
create trigger OrbsRestrictions after update of _idx on OrbsRestrictions for each row
	begin
		update _OrbsRestrictions set filter_idx = new._idx where filter_idx = old._idx;
		update Filters set orbrestr = new._idx where orbrestr = old._idx;
		update MidPointsFilters set orbrestr = new._idx where orbrestr = old._idx;
	end;/*End*/

/* OrbsRestrictionsDeleteTrigger */
-- Cascade orbs restrictions filters deletes, if not referenced by Filters
create trigger OrbsRestrictionsDeleteTrigger before delete on OrbsRestrictions for each row
	begin
		select raise (rollback, 'Error: delete on OrbsRestrictions violates foreign key constraint.')
			where (select orbrestr from Filters where orbrestr = old._idx) is not null;
		select raise (rollback, 'Error: delete on OrbsRestrictions violates foreign key constraint.')
			where (select orbrestr from MidPointsFilters where orbrestr = old._idx) is not null;
		delete from _OrbsRestrictions where filter_idx = old._idx;
	end;/*End*/

/* _OrbsRestrictionsUpdateTrigger */
-- Check orbs-filter id exists
create trigger _OrbsRestrictionsUpdateTrigger before update of filter_idx on _OrbsRestrictions for each row
	begin
		select raise (rollback ,'Error: update on _OrbsRestrictions violates foreign key constraint.')
			where (select _idx from OrbsRestrictions where _idx = new.filter_idx) is null;
	end;/*End*/





/* MidPointsFilters */
create table MidPointsFilters (
	_idx integer primary key,
	name varchar not null default '<?>' unique,
	planets integer not null, -- references PlanetsFilters._idx
	aspects integer not null, -- references AspectsFilters._idx
	orbs integer not null, -- references OrbsFilters._idx
	asprestr integer not null, -- references AspectsRestrictions._idx
	orbrestr integer not null, -- references OrbsRestrictions._idx
	comment text not null default ''
);/*End*/

/* MidPointsFiltersInsertTrigger */
-- check filters exist
create trigger MidPointsFiltersInsertTrigger before insert on MidPointsFilters for each row
	begin
		select raise (rollback, 'Error: insert on MidPointsFilters.planets violates foreign key constraint.')
			where (select _idx from PlanetsFilters where _idx = new.planets) is null;
		select raise (rollback, 'Error: insert on MidPointsFilters.aspects violates foreign key constraint.')
			where (select _idx from AspectsFilters where _idx = new.aspects) is null;
		select raise (rollback, 'Error: insert on MidPointsFilters.orbs violates foreign key constraint.')
			where (select _idx from OrbsFilters where _idx = new.orbs) is null;
		select raise (rollback, 'Error: insert on MidPointsFilters.asprestr violates foreign key constraint.')
			where (select _idx from AspectsRestrictions where _idx = new.asprestr) is null;
		select raise (rollback, 'Error: insert on MidPointsFilters.orbrestr violates foreign key constraint.')
			where (select _idx from OrbsRestrictions where _idx = new.orbrestr) is null;
	end;/*End*/

/* MidPointsFiltersUpdatePlanetsTrigger */
-- check planets-filter exists
create trigger MidPointsFiltersUpdatePlanetsTrigger before update of planets on MidPointsFilters for each row
	begin
		select raise (rollback, 'Error: update on MidPointsFilters.planets violates foreign key constraint.')
			where (select _idx from PlanetsFilters where _idx = new.planets) is null;
	end;/*End*/

/* MidPointsFiltersUpdateAspectsTrigger */
-- check aspects-filter exists
create trigger MidPointsFiltersUpdateAspectsTrigger before update of aspects on MidPointsFilters for each row
	begin
		select raise (rollback, 'Error: update on MidPointsFilters.aspects violates foreign key constraint.')
			where (select _idx from AspectsFilters where _idx = new.aspects) is null;
	end;/*End*/

/* MidPointsFiltersUpdateOrbsTrigger */
-- check orbs-filter exists
create trigger MidPointsFiltersUpdateOrbsTrigger before update of orbs on MidPointsFilters for each row
	begin
		select raise (rollback, 'Error: update on MidPointsFilters.orbs violates foreign key constraint.')
			where (select _idx from OrbsFilters where _idx = new.orbs) is null;
	end;/*End*/

/* MidPointsFiltersUpdateAspectsRestrictionsTrigger */
-- check asprestr-filter exists
create trigger MidPointsFiltersUpdateAspectsRestrictionsTrigger before update of asprestr on MidPointsFilters for each row
	begin
		select raise (rollback, 'Error: update on MidPointsFilters.asprestr violates foreign key constraint.')
			where (select _idx from AspectsRestrictions where _idx = new.asprestr) is null;
	end;/*End*/

/* MidPointsFiltersUpdateOrbsRestrictionsTrigger */
-- check orbrestr-filter exists
create trigger MidPointsFiltersUpdateOrbsRestrictionsTrigger before update of orbrestr on MidPointsFilters for each row
	begin
		select raise (rollback, 'Error: update on MidPointsFilters.orbrestr violates foreign key constraint.')
			where (select _idx from OrbsRestrictions where _idx = new.orbrestr) is null;
	end;/*End*/

/* MidPointsFiltersDeleteTrigger */
create trigger MidPointsFiltersDeleteTrigger before delete on MidPointsFilters for each row
	begin
		select raise (rollback, 'Error: delete on MidPointsFilters violates foreign key constraint.')
			where (select midpoints from Filters where _idx = (select dft_filter from Config)) = old._idx;
	end;/*End*/





/* Filters */
create table Filters (
	_idx integer primary key,
	name varchar not null unique default '<?>',
	bg_color varchar not null default 'black' check (bg_color in ('black', 'white')),
	ephe_type varchar not null default 'swiss' check (ephe_type in ('swiss','jpl','moshier')),
	ephe_path varchar not null default '/usr/local/share/swisseph',  -- path to ephe dir/file
	hsys varchar not null default 'P', -- house system
	sid_mode integer not null default -1 check (sid_mode between -1 and 255), -- sidereal mode: -1=tropical, 0+=sidereal mode
	sid_t0 numeric not null default 0, -- user's sidereal mode reference date
	sid_ayan_t0 numeric not null default 0, -- user's sidereal initial ayanamsa
	true_pos integer not null default 0 check (true_pos in (0, 1)), -- true/apparent positions
	xcentric varchar not null default 'geo' check (xcentric in ('geo','topo','helio','bary')),
	calc_midp integer not null default 0 check (calc_midp in (0, 1)), -- calculate midpoints
	draw_midp integer not null default 0 check (draw_midp in (0, 1)), -- draw midpoints
	-- Filters:
	planets integer not null, -- references PlanetsFilters._idx,
	aspects integer not null, -- references AspectsFilters,_idx,
	orbs integer not null, -- references OrbsFilters._idx,
	asprestr integer not null, -- references AspectsRestrictions._idx,
	orbrestr integer not null, -- references OrbsRestrictions._idx
	midpoints integer not null, -- references MidPointsFilters._idx
	comment text not null default ''
);/*End*/

/* FiltersInsertTrigger */
-- check filters exist
create trigger FiltersInsertTrigger before insert on Filters for each row
	begin
		select raise (rollback, 'Error: insert on Filters.planets violates foreign key constraint.')
			where (select _idx from PlanetsFilters where _idx = new.planets) is null;
		select raise (rollback, 'Error: insert on Filters.aspects violates foreign key constraint.')
			where (select _idx from AspectsFilters where _idx = new.aspects) is null;
		select raise (rollback, 'Error: insert on Filters.orbs violates foreign key constraint.')
			where (select _idx from OrbsFilters where _idx = new.orbs) is null;
		select raise (rollback, 'Error: insert on Filters.asprestr violates foreign key constraint.')
			where (select _idx from AspectsRestrictions where _idx = new.asprestr) is null;
		select raise (rollback, 'Error: insert on Filters.orbrestr violates foreign key constraint.')
			where (select _idx from OrbsRestrictions where _idx = new.orbrestr) is null;
		select raise (rollback, 'Error: insert on Filters.midpoints violates foreign key constraint.')
			where (select _idx from MidPointsFilters where _idx = new.midpoints) is null;
	end;/*End*/

/* FiltersUpdatePlanetsTrigger */
-- check planets-filter exists
create trigger FiltersUpdatePlanetsTrigger before update of planets on Filters for each row
	begin
		select raise (rollback, 'Error: update on Filters.planets violates foreign key constraint.')
			where (select _idx from PlanetsFilters where _idx = new.planets) is null;
	end;/*End*/

/* FiltersUpdateAspectsTrigger */
-- check aspects-filter exists
create trigger FiltersUpdateAspectsTrigger before update of aspects on Filters for each row
	begin
		select raise (rollback, 'Error: update on Filters.aspects violates foreign key constraint.')
			where (select _idx from AspectsFilters where _idx = new.aspects) is null;
	end;/*End*/

/* FiltersUpdateOrbsTrigger */
-- check orbs-filter exists
create trigger FiltersUpdateOrbsTrigger before update of orbs on Filters for each row
	begin
		select raise (rollback, 'Error: update on Filters.orbs violates foreign key constraint.')
			where (select _idx from OrbsFilters where _idx = new.orbs) is null;
	end;/*End*/

/* FiltersUpdateAspectsRestrictionsTrigger */
-- check asprestr-filter exists
create trigger FiltersUpdateAspectsRestrictionsTrigger before update of asprestr on Filters for each row
	begin
		select raise (rollback, 'Error: update on Filters.asprestr violates foreign key constraint.')
			where (select _idx from AspectsRestrictions where _idx = new.asprestr) is null;
	end;/*End*/

/* FiltersUpdateOrbsRestrictionsTrigger */
-- check orbrestr-filter exists
create trigger FiltersUpdateOrbsRestrictionsTrigger before update of orbrestr on Filters for each row
	begin
		select raise (rollback, 'Error: update on Filters.orbrestr violates foreign key constraint.')
			where (select _idx from OrbsRestrictions where _idx = new.orbrestr) is null;
	end;/*End*/

/* FiltersUpdateMidPointsTrigger */
-- check midpoints filter exists
create trigger FiltersUpdateMidPointsTrigger before update of midpoints on Filters for each row
	begin
		select raise (rollback, 'Error: update on Filters.midpoints violates foreign key constraint.')
			where (select _idx from MidPointsFilters where _idx = new.midpoints) is null;
	end;/*End*/

/* FiltersDeleteTrigger */
create trigger FiltersDeleteTrigger before delete on Filters for each row
	begin
		select raise (rollback, 'Error: delete on Filters violates foreign key constraint.')
			where (select dft_filter from Config) == old._idx;
	end;/*End*/




/* Config */
create table Config (
	username varchar not null default 'John Smith', -- user's name
	usermail varchar not null default 'johnsmith@nsa.gov', -- user's mail
	language varchar not null default '', -- language
	atlas_db varchar not null default '~/.oroboros/atlas.db', -- path to atlas db
	charts_dir varchar not null default '~', -- charts directory
	use_docutils integer not null default 0 check (use_docutils in (0, 1)), -- use docutils
	use_hg integer not null default 0 check (use_hg in (0, 1)), -- synch. with distant hg repo
	hg_repo varchar not null default 'http://hg.atarax.org/public', -- distant hg repository
	hg_user varchar not null default 'anonymous', -- hg username
	hg_pswd varchar not null default 'password', -- hg password
	-- defaults for new charts and here/now-chart:
	dft_name varchar not null default 'Here-Now',
	dft_location varchar not null default 'Lausanne',
	dft_country varchar not null default 'Switzerland',
	dft_zoneinfo varchar not null default 'Europe/Zurich',
	dft_timezone varchar not null default 'UTC+1',
	dft_latitude varchar not null default '46:N:32:0',
	dft_longitude varchar not null default '6:E:40:0',
	dft_altitude integer not null default 400 check (dft_altitude >= 0),
	dft_comment varchar not null default '',
	dft_filter integer not null --references Filters._idx
);/*End*/

/* ConfigInsertTrigger */
create trigger ConfigInsertTrigger before insert on Config for each row
	begin
		select raise (rollback, 'Error: unable to insert config.')
			where (select count(username) from Config) != 0;
		select raise (rollback, 'Error: insert on Config violates foreign key constraint.')
			where (select _idx from Filters where _idx = new.dft_filter) is null;
	end;/*End*/

/* ConfigUpdateTrigger */
create trigger ConfigUpdateTrigger before update of dft_filter on Config for each row
	begin
		select raise (rollback, 'Error: update on Config.dft_filter violates foreign key constraint.')
			where (select _idx from Filters where _idx = new.dft_filter) is null;
	end;/*End*/

/* ConfigDeleteTrigger */
create trigger ConfigDeleteTrigger before delete on Config for each row
	begin
		select raise (rollback, 'Error: unable to delete config.') where 1;
	end;



/* End. */
