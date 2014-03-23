/* Oroboros - SQLite inserts */

/* Info */
insert into Info (version) values (20080712);/*End*/


/* Aspects */
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (0, 'Conjunction', 1, 1, 10, '255,255,0', 'conjunction.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (180, 'Opposition', 2, 1, 10, '0,0,255', 'opposition.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (120, 'Trine', 3, 1, 8, '0,255,0', 'trine.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (90, 'Square', 4, 1, 8, '255,0,0', 'square.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (60, 'Sextile', 5, 1, 4, '0,255,255', 'sextile.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (150, 'Quincunx', 6, 0, 4, '255,0,192', 'quincunx.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (135, 'SesquiSquare', 7, 0, 2, '192,128,0', 'sesquisquare.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (45, 'SemiSquare', 8, 0, 2, '192,128,0', 'semisquare.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (30, 'SemiSextile', 9, 0, 2, '255,0,192', 'semisextile.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (22.5, 'SquiSquare', 10, 0, 1, '192,128,0', 'squisquare.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (15, 'SquiSextile', 11, 0, 1, '192,128,0', 'squisextile.png');/*End*/

insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (72, 'Quintile', 12, 0, 1, '0,128,255', 'quintile.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (144, 'BiQuintile', 13, 0, 1, '0,128,255', 'biquintile.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (36, 'SemiQuintile', 14, 0, 1, '0,128,255', 'semiquintile.png');/*End*/

insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (40, 'Novile', 15, 0, 0.5, '255,128,0', 'novile.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (80, 'BiNovile', 16, 0, 0.5, '255,128,0', 'binovile.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (160, 'QuadriNovile', 17, 0, 0.5, '255,128,0', 'quatronovile.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (20, 'SemiNovile', 18, 0, 0.5, '255,128,0', 'seminovile.png');/*End*/

insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (51.428571428571431, 'Septile', 19, 0, 0.5, '128,128,128', 'septile.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (102.85714285714286, 'BiSeptile', 20, 0, 0.5, '128,128,128', 'biseptile.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (154.28571428571428, 'TriSeptile', 21, 0, 0.5, '128,128,128', 'triseptile.png');/*End*/

insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (32.727272727272727, 'Undecile', 22, 0, 0.5, '0,128,128', 'undecile.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (65.454545454545453, 'BiUndecile', 23, 0, 0.5, '0,128,128', 'biundecile.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (98.181818181818187, 'TriUndecile', 24, 0, 0.5, '0,128,128', 'triundecile.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (130.90909090909091, 'QuadUndecile', 25, 0, 0.5, '0,128,128', 'quadundecile.png');/*End*/
insert into Aspects (angle, name, ranking, bool_use, default_orb, color, glyph)
values (163.63636363636363, 'QuinUndecile', 26, 0, 0.5, '0,128,128', 'quinundecile.png');/*End*/


/* AspectsFilters */
insert into AspectsFilters (name, comment)
values ('<Aspects Filter 1>', 'Example Aspects Filter.');/*End*/


/* OrbsFilters */
insert into OrbsFilters (name, comment)
values ('<Orbs Filter 1>', 'Example Orbs Filter.');/*End*/


/* Planets*/
-- ***** Real Bodies
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (0, 'Sun', 0, 0, 1, 1, 'sun.png');/*End*/ -- Sun
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (1, 'Moon', 0, 1, 1, 1, 'moon.png');/*End*/ -- Moon
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (2, 'Mercury', 0, 2, 1, 1, 'mercury.png');/*End*/ -- Mercury
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (3, 'Venus', 0, 3, 1, 1, 'venus.png');/*End*/ -- Venus
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (4, 'Mars', 0, 4, 1, 1, 'mars.png');/*End*/ -- Mars
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (5, 'Jupiter', 0, 5, 1, 1, 'jupiter.png');/*End*/ -- Jupiter
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (6, 'Saturn', 0, 6, 1, 1, 'saturn.png');/*End*/ -- Saturn
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (7, 'Uranus', 0, 7, 1, 1, 'uranus.png');/*End*/ -- Uranus
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (8, 'Neptune', 0, 8, 1, 1, 'neptune.png');/*End*/ -- Neptune
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (9, 'Pluto', 0, 9, 1, 1, 'pluto.png');/*End*/ -- Pluto
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (14, 'Earth', 0, 10, 0, 0, 'earth.png');/*End*/ -- Earth
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (15, 'Chiron', 0, 11, 0, 0, 'chiron.png');/*End*/ -- Chiron
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (16, 'Pholus', 0, 12, 0, 0, 'pholus.png');/*End*/ -- Pholus
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (17, 'Ceres', 0, 13, 0, 0, 'ceres.png');/*End*/ -- Ceres
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (18, 'Pallas', 0, 14, 0, 0, 'pallas.png');/*End*/ -- Pallas
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (19, 'Juno', 0, 15, 0, 0, 'juno.png');/*End*/ -- Juno
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (20, 'Vesta', 0, 16, 0, 0, 'vesta.png');/*End*/ -- Vesta

-- ***** Lunar nodes, Lilith/Priapus
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (10, 'Rahu (mean)', 0, 17, 0, 0, 'north_lunar_node.png');/*End*/ -- North lunar node (mean)
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (11, 'Rahu (true)', 0, 18, 0, 0, 'north_lunar_node.png');/*End*/ -- North lunar node (true)
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-2, 'Ketu (mean)', 0, 19, 0, 0, 'south_lunar_node.png');/*End*/ -- South lunar node (mean)
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-3, 'Ketu (true)', 0, 20, 0, 0, 'south_lunar_node.png');/*End*/ -- South lunar node (true)
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (12, 'Lilith (mean)', 0, 21, 0, 0, 'lilith.png');/*End*/ -- Mean Lunar Apogee
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (13, 'Lilith (true)', 0, 22, 0, 0, 'lilith.png');/*End*/ -- Osculating Lunar Apogee
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-4, 'Priapus (mean)', 0, 23, 0, 0, 'priapus.png');/*End*/ -- Priapus (mean)
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-5, 'Priapus (true)', 0, 24, 0, 0, 'priapus.png');/*End*/ -- Priapus (true)

-- ***** Hamburg/Uranian "planets"
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (40, 'Cupido', 1, 25, 0, 0, 'cupido.png');/*End*/ -- Cupido
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (41, 'Hades', 1, 26, 0, 0, 'hades.png');/*End*/ -- Hades
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (42, 'Zeus', 1, 27, 0, 0, 'zeus.png');/*End*/ -- Zeus
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (43, 'Kronos', 1, 28, 0, 0, 'kronos.png');/*End*/ -- Kronos
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (44, 'Apollon', 1, 29, 0, 0, 'apollon.png');/*End*/ -- Apollon
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (45, 'Admetos', 1, 30, 0, 0, 'admetos.png');/*End*/ -- Admetos
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (46, 'Vulkanus', 1, 31, 0, 0, 'vulkanus.png');/*End*/ -- Vulkanus
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (47, 'Poseidon', 1, 32, 0, 0, 'poseidon.png');/*End*/ -- Poseidon

-- ***** Other fictitious bodies
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (48, 'Isis', 1, 33, 0, 0, 'isis.png');/*End*/ -- Isis
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (49, 'Nibiru', 1, 34, 0, 0, 'nibiru.png');/*End*/ -- Nibiru
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (50, 'Harrington', 1, 35, 0, 0, 'harrington.png');/*End*/ -- Harrington
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (51, 'Neptune (Leverrier)', 1, 36, 0, 0, 'neptune_leverrier.png');/*End*/ -- Neptune Leverrier
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (52, 'Neptune (Adams)', 1, 37, 0, 0, 'neptune_adams.png');/*End*/ -- Neptune Adams
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (53, 'Pluto (Lowell)', 1, 38, 0, 0, 'pluto_lowell.png');/*End*/ -- Pluto Lowell
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (54, 'Pluto (Pickering)', 1, 39, 0, 0, 'pluto_pickering.png');/*End*/ -- Pluto Pickering
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (55, 'Vulcan', 1, 40, 0, 0, 'vulcan.png');/*End*/ -- Vulcan
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (56, 'White Moon', 1, 41, 0, 0, 'white_moon.png');/*End*/ -- White Moon
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (57, 'Proserpina', 1, 42, 0, 0, 'proserpina.png');/*End*/ -- Proserpina
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (58, 'Waldemath', 1, 43, 0, 0, 'waldemath.png');/*End*/ -- Waldemath

-- ***** Houses cusps ( -100 <= num <= -199 ) related to swe_houses()
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-100, 'Cusp 01', 4, 50, 0, 1, 'house_01.png');/*End*/ -- House cusp I (Asc)
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-101, 'Cusp 02', 4, 51, 0, 1, 'house_02.png');/*End*/ -- House cusp II
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-102, 'Cusp 03', 4, 52, 0, 1, 'house_03.png');/*End*/ -- House cusp III
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-103, 'Cusp 04', 4, 53, 0, 1, 'house_04.png');/*End*/ -- House cusp IV (FC)
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-104, 'Cusp 05', 4, 54, 0, 1, 'house_05.png');/*End*/ -- House cusp V
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-105, 'Cusp 06', 4, 55, 0, 1, 'house_06.png');/*End*/ -- House cusp VI
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-106, 'Cusp 07', 4, 56, 0, 1, 'house_07.png');/*End*/ -- House cusp VII (Des)
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-107, 'Cusp 08', 4, 57, 0, 1, 'house_08.png');/*End*/ -- House cusp VIII
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-108, 'Cusp 09', 4, 58, 0, 1, 'house_09.png');/*End*/ -- House cusp IX
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-109, 'Cusp 10', 4, 59, 0, 1, 'house_10.png');/*End*/ -- House cusp X (MC)
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-110, 'Cusp 11', 4, 60, 0, 1, 'house_11.png');/*End*/ -- House cusp XI
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-111, 'Cusp 12', 4, 61, 0, 1, 'house_12.png');/*End*/ -- House cusp XII
/* Gauquelin sectors */
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-112, 'Sector 01', 4, 62, 0, 1, 'gauquelin_01.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-113, 'Sector 02', 4, 63, 0, 1, 'gauquelin_02.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-114, 'Sector 03', 4, 64, 0, 1, 'gauquelin_03.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-115, 'Sector 04', 4, 65, 0, 1, 'gauquelin_04.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-116, 'Sector 05', 4, 66, 0, 1, 'gauquelin_05.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-117, 'Sector 06', 4, 67, 0, 1, 'gauquelin_06.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-118, 'Sector 07', 4, 68, 0, 1, 'gauquelin_07.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-119, 'Sector 08', 4, 69, 0, 1, 'gauquelin_08.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-120, 'Sector 09', 4, 70, 0, 1, 'gauquelin_09.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-121, 'Sector 10', 4, 71, 0, 1, 'gauquelin_10.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-122, 'Sector 11', 4, 72, 0, 1, 'gauquelin_11.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-123, 'Sector 12', 4, 73, 0, 1, 'gauquelin_12.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-124, 'Sector 13', 4, 74, 0, 1, 'gauquelin_13.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-125, 'Sector 14', 4, 75, 0, 1, 'gauquelin_14.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-126, 'Sector 15', 4, 76, 0, 1, 'gauquelin_15.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-127, 'Sector 16', 4, 77, 0, 1, 'gauquelin_16.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-128, 'Sector 17', 4, 78, 0, 1, 'gauquelin_17.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-129, 'Sector 18', 4, 79, 0, 1, 'gauquelin_18.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-130, 'Sector 19', 4, 80, 0, 1, 'gauquelin_19.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-131, 'Sector 20', 4, 81, 0, 1, 'gauquelin_20.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-132, 'Sector 21', 4, 82, 0, 1, 'gauquelin_21.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-133, 'Sector 22', 4, 83, 0, 1, 'gauquelin_22.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-134, 'Sector 23', 4, 84, 0, 1, 'gauquelin_23.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-135, 'Sector 24', 4, 85, 0, 1, 'gauquelin_24.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-136, 'Sector 25', 4, 86, 0, 1, 'gauquelin_25.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-137, 'Sector 26', 4, 87, 0, 1, 'gauquelin_26.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-138, 'Sector 27', 4, 88, 0, 1, 'gauquelin_27.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-139, 'Sector 28', 4, 89, 0, 1, 'gauquelin_28.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-140, 'Sector 29', 4, 90, 0, 1, 'gauquelin_29.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-141, 'Sector 30', 4, 91, 0, 1, 'gauquelin_30.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-142, 'Sector 31', 4, 92, 0, 1, 'gauquelin_31.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-143, 'Sector 32', 4, 93, 0, 1, 'gauquelin_32.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-144, 'Sector 33', 4, 94, 0, 1, 'gauquelin_33.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-145, 'Sector 34', 4, 95, 0, 1, 'gauquelin_34.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-146, 'Sector 35', 4, 96, 0, 1, 'gauquelin_35.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-147, 'Sector 36', 4, 97, 0, 1, 'gauquelin_36.png');/*End*/

/* Asc, Mc, etc */
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-148, 'Asc', 4, 100, 1, 1, 'asc.png');/*End*/ -- Asc
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-149, 'Mc', 4, 101, 1, 1, 'mc.png');/*End*/ -- Mc
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-150, 'Armc', 4, 104, 0, 1, 'armc.png');/*End*/ -- ARMC
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-151, 'Vertex', 4, 105, 0, 1, 'vertex.png');/*End*/ -- Vertex
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-152, 'Equatorial Ascendant', 4, 106, 0, 1, 'equasc.png');/*End*/ -- Equatorial ascendant
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-153, 'Co-ascendant (Koch)', 4, 107, 0, 1, 'coasc1.png');/*End*/ -- Co-Ascendant (Koch)
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-154, 'Co-ascendant (Munkasey)', 4, 108, 0, 1, 'coasc2.png');/*End*/ -- Co-Ascendant (Munkasey)
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-155, 'Polar Ascendant (Munkasey)', 4, 109, 0, 1, 'poasc.png');/*End*/ -- Polar Ascendant (Munkasey)
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
-- Additional values:
values (-156, 'Dsc', 4, 102, 0, 1, 'dsc.png');/*End*/ -- Dsc
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-157, 'Ic', 4, 103, 0, 1, 'ic.png');/*End*/ -- Ic

-- ***** Parts ( -300 <= num )
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-300, 'Part of Fortune (Rudhyar)', 5, 200, 0, 0, 'part_fortune.png');/*End*/ -- Part of Fortune

-- ***** Fixed Stars
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1000, 'Aldebaran', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1001, 'Algol', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1002, 'Antares', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1003, 'Regulus', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1004, 'Sirius', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1005, 'Spica', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1006, 'Gal. Center', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1007, 'Great Attractor', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1008, 'Virgo Cluster', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1009, 'Andromeda Galaxy', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1010, 'Praesepe Cluster', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1011, 'Deneb', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1012, 'Rigel', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1013, 'Mira', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1014, 'Ain', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Andromeda **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1015, 'Alpheratz', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1016, 'Mirach', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1017, 'Almaak', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Aquila **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1018, 'Altair', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1019, 'Alshain', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1020, 'Tarazed', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1021, 'Deneb Okab', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1022, 'Dheneb', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1023, 'Al Thalimaim', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Aquarius **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1024, 'Sadalmelek', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1025, 'Sadalsuud', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1026, 'Sadalachbia', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1027, 'Skat', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1028, 'Albali', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1029, 'Ancha', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1030, 'Situla', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1031, 'Seat', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Ara **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1032, 'Ara', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Aries **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1033, 'Hamal', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1034, 'Sheratan', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1035, 'Mesarthim', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1036, 'Botein', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Auriga **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1037, 'Capella', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1038, 'Menkalinan', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1039, 'Prijipati', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1040, 'Maaz', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1041, 'Al Anz', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1042, 'Haedi', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1043, 'Hoedus II', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1044, 'Hasseleh', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1045, 'Al Khabdhilinan', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Bootes **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1046, 'Arcturus', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1047, 'Nekkar', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1048, 'Seginus', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1049, 'Haris', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1050, 'Princeps', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1051, 'Izar', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1052, 'Mufrid', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1053, 'Asellus Primus', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1054, 'Asellus Secundus', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1055, 'Asellus Tertius', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1056, 'Alkalurops', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1057, 'Ceginus', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1058, 'Merga', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Caelum **
-- ** Camelopardalis **
-- ** Capricornus **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1059, 'Giedi Prima', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1060, 'Giedi Secunda', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1061, 'Dabih', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1062, 'Nashira', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1063, 'Deneb Algedi', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1064, 'Castra', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1065, 'Armus', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1066, 'Dorsum', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1067, 'Alshat', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1068, 'Oculus', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1069, 'Bos', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Carina **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1070, 'Canopus', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1071, 'Miaplacidus', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1072, 'Avior', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1073, 'Foramen', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1074, 'Scutulum', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Cassiopeia **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1075, 'Schedar', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1076, 'Caph', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1077, 'Tsih', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
--insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
--values (-1078, 'Ruchbah', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1079, 'Segin', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1080, 'Achird', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1081, 'Marfak', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Centaurus **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1082, 'Rigel Kentaurus', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1083, 'Hadar', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1084, 'Muhlifain', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1085, 'Menkent', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1086, 'Ke Kwan', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1087, 'Proxima Cent.', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Cepheus **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1088, 'Alderamin', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1089, 'Alphirk', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1090, 'Alrai', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1091, 'Kurhah', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1092, 'Erakis', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1093, 'The Garnet Star', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1094, 'Kurdah', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1095, 'Al Kalb al Rai', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Cetus **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1096, 'Menkar', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1097, 'Diphda', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1098, 'Kaffaljidhma', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1099, 'Baten Kaitos', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1100, 'Deneb Algenubi', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1101, 'Deneb Kaitos', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
--insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
--values (-1102, 'Menkar', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Chameleon **
-- ** Circinus **
-- ** Canis Major **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1103, 'Mirzam', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1104, 'Muliphein', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1105, 'Wezen', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1106, 'Adara', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1107, 'Furud', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1108, 'Aludra', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Canis Minor **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1109, 'Procyon', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1110, 'Gomeisa', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Cancer **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1112, 'Acubens', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1113, 'Al Tarf', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1114, 'Asellus Borealis', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1115, 'Tegmen', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Columba **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1116, 'Phact', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1117, 'Wazn', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1118, 'Tsze', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Coma Berenices **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1119, 'Diadem', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1120, 'Aldafirah', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1121, 'Kissin', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Corona Borealis **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1122, 'Alphecca', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1123, 'Nusakan', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1124, 'The Blaze Star', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Crater **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1125, 'Alkes', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1126, 'Alsharasif', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1127, 'Labrum', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Crux **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1128, 'Acrux', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1129, 'Mimosa', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1130, 'Gacrux', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Corvus **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1131, 'Alchiba', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1132, 'Kraz', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1133, 'Gienah', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1134, 'Algorab', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1135, 'Minkar', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Canis Venatici **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1136, 'Cor Caroli', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1137, 'Asterion', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Cygnus **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1138, 'Albireo', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1139, 'Sador', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1140, 'Gienah Cygni', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1141, 'Azelfafage', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
--insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
--values (-1142, 'Ruchbah', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Delphinus **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1143, 'Sualocin', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1144, 'Rotanev', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1145, 'Deneb Dulphim', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Dorado **
-- ** Draco **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1146, 'Thuban', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1147, 'Rastaban', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1148, 'Eltanin', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1149, 'Nodus II', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1150, 'Tyl', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1151, 'Nodus I', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1152, 'Edasich', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1153, 'Giansar', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1154, 'Arrakis', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1155, 'Kuma', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1156, 'Grumium', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1157, 'Alsafi', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1158, 'Dziban', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1159, 'Alathfar', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Equuleus **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1160, 'Kitalpha', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Eridanus **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1161, 'Achernar', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1162, 'Cursa', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1163, 'Zaurak', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1164, 'Rana', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1165, 'Azha', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1166, 'Acamar', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1167, 'Zibal', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1168, 'Beid', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1169, 'Keid', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1170, 'Angetenar', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1171, 'Theemin', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1172, 'Sceptrum', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Fornax **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1173, 'Fornacis', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Gemini **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1174, 'Castor', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1175, 'Pollux', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1176, 'Alhena', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1177, 'Wasat', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1178, 'Mebsuta', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1179, 'Mekbuda', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1180, 'Propus', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1181, 'Tejat', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1182, 'Alzirr', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Grus **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1183, 'Alnair', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1184, 'Al Dhanab', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Hercules **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1185, 'Ras Algethi', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1186, 'Kornephoros', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1187, 'Sarin', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1188, 'Marsik', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1189, 'Masym', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1190, 'Kajam', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1191, 'Apex', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Horologium **
-- ** Hydra **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1192, 'Alphard', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1193, 'Cor Hydrae', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1194, 'Al Minliar al Shuja', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1195, 'Ukdah', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1196, 'Minchir', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Hydrus **
-- ** Indus **
-- ** Lacerta **
-- ** Leo **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1197, 'Denebola', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1198, 'Algieba', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1199, 'Dhur', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1200, 'Zosma', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1201, 'Ras Elased Australis', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1202, 'Adhafera', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
--insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
--values (-1203, 'Algieba', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1204, 'Tse Tseng', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1205, 'Alminhar', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1206, 'Alterf', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1207, 'Ras Elased Borealis', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1208, 'Subra', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1209, 'Coxa', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1210, 'Chertan', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Lepus **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1211, 'Arneb', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1212, 'Nihal', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Libra **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1213, 'Zugen Elgenubi', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1214, 'Zuben Eshmali', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1215, 'Zuben Elakrab', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1216, 'Zuben Elakribi', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1217, 'Zuben Hakrabi', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1218, 'Brachium', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Leo Minor **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1219, 'Praecipua', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Lupus **
-- ** Lynx **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1220, 'Alsciaukat', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1221, 'Mabsuthat', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Lyra **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1222, 'Vega', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1223, 'Sheliak', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1224, 'Sulaphat', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1225, 'Aladfar', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
--insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
--values (-1226, 'Alathfar', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Mensa **
-- ** Microscopium **
-- ** Monoceros **
-- ** Musca **
-- ** Norma **
-- ** Octans **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1227, 'Polaris Australis', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Ophiucus **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1228, 'Rasalhague', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1229, 'Celbalrai', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1230, 'Yed Prior', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1231, 'Yed Posterior', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1232, 'Han', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1233, 'Sabik', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1234, 'Marfik', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1235, 'Sinistra', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1236, "Barnard's star", 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Orion **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1237, 'Betelgeuse', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1238, 'Bellatrix', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1239, 'Mintaka', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1240, 'Alnilam', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1241, 'Alnitak', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1242, 'Hatsya', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1243, 'Saiph', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1244, 'Heka', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1245, 'Tabit', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1246, 'Thabit', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Pavo **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1247, 'Peacock', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Phoenix **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1248, 'Ankaa', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Pegasus **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1249, 'Markab', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1250, 'Scheat', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1251, 'Algenib', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1252, 'Enif', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1253, 'Homam', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1254, 'Matar', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1255, 'Biham', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1256, 'Sadalbari', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1257, 'Kerb', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1258, 'Salm', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Perseus **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1259, 'Mirfak', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1261, 'Atik', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1262, 'Miram', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1263, 'Misam', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1264, 'Menkib', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
--insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
--values (-1265, 'Atik', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1266, 'Gorgona Secunda', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1267, 'Gorgona Tertia', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1268, 'Gorgona Quarta', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Pictor **
-- ** Piscis Austrinus **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1269, 'Fomalhaut', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Pisces **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1270, 'Alrischa', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1271, 'Fum Alsamakah', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1272, 'Al Pherg', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Puppis **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1273, 'Naos', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1274, 'Asmidiske', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Pyxis **
-- ** Reticulum **
-- ** Sculptor **
-- ** Scorpius **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1275, 'Akrab', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1276, 'Dschubba', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1277, 'Sargas', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1278, 'Shaula', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1279, 'Jabbah', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1280, 'Grafias', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1281, 'Alniyat', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1282, 'Lesath', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1283, 'Jabhat al Akrab', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Scutum **
-- ** Serpens **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1284, 'Unukalhai', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1285, 'Chow', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1286, 'Alya', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Sextans **
-- ** Sagitta **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1287, 'Sham', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Sagittarius **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1288, 'Rukbat', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1289, 'Arkab Prior', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1290, 'Arkab Posterior', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1291, 'Alnasl', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1292, 'Kaus Medis', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1293, 'Kaus Australis', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1294, 'Ascella', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1295, 'Kaus Borealis', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1296, 'Polis', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1297, 'Ain al Rami', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1298, 'Manubrium', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1299, 'Albaldah', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1300, 'Nunki', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1301, 'Terebellium', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Taurus **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1302, 'Elnath', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1303, 'Hyadum I', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1304, 'Hyadum II', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1305, 'Al Hecka', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1306, 'Alcyone', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1307, 'Caleano', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1308, 'Electra', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1309, 'Taygeta', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1310, 'Maia', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1311, 'Asterope', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1312, 'Sterope I', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1313, 'Sterope II', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1314, 'Merope', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1315, 'Atlas', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Telescopium **
-- ** Triangulum Australe **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1316, 'Atria', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Triangulum **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1317, 'Ras Mutallah', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Tucana **
-- ** Ursa Major **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1318, 'Dubhe', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1319, 'Merak', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1320, 'Phecda', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1321, 'Megrez', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1322, 'Alioth', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1323, 'Mizar', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1324, 'Alkaid', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1325, 'Al Haud', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1326, 'Talitha Borealis', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1327, 'Talitha Australis', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1328, 'Tania Borealis', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1329, 'Tania Australis', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1330, 'Alula Borealis', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1331, 'Alula Australis', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1332, 'Muscida', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1333, 'El Kophrah', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1334, 'Alcor', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1335, 'Saidak', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Ursa Minor **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1336, 'Polaris', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1337, 'Kochab', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1338, 'Pherkad', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1339, 'Yildun', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1340, 'Pherkad Minor', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Vela **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1341, 'Suhail al Muhlif', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1342, 'Markeb', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1343, 'Alsuhail', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1344, 'Suhail', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1345, 'Tseen Ke', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Virgo **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1346, 'Zavijava', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1347, 'Alaraph', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1348, 'Porrima', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1349, 'Auva', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1350, 'Vindemiatrix', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1351, 'Heze', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1352, 'Zaniah', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1353, 'Syrma', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1354, 'Khambalia', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1355, 'Rijl al Awwa', 2, 1000, 0, 0, 'fixedstar.png');/*End*/
-- ** Volans **
-- ** Vulpecula **
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (-1356, 'Anser', 2, 1000, 0, 0, 'fixedstar.png');/*End*/


-- ***** Asteroids (num > 10000)
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (146199, 'Eris', 3, 146199, 0, 0, 'eris.png' );/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (17066, 'Nessus', 3, 17066, 0, 0, 'nessus.png' );/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (60000, 'Quaoar', 3, 60000, 0, 0, 'quaoar.png' );/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (100377, 'Sedna', 3, 100377, 0, 0, 'sedna.png' );/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (30000, 'Varuna', 3, 30000, 0, 0, 'varuna.png' );/*End*/
insert into Planets (num, name, family, ranking, bool_use, bool_aspect, glyph)
values (10128, 'Nemesis', 3, 10128, 0, 0, 'asteroid.png' );/*End*/


/* PlanetsFilters */
insert into PlanetsFilters (name, comment)
values ('<Planets Filter 1>', 'Example planets filter.');/*End*/

/* AspectsRestrictions */
insert into AspectsRestrictions (name, comment)
values ('<Aspects Restrictions 1>', 'Example aspects restrictions.');/*End*/

/* OrbsRestrictions */
insert into OrbsRestrictions (name, comment)
values ('<Orbs Restrictions 1>', 'Example orbs restrictions.');/*End*/

/* MidPointsFilters */
insert into MidPointsFilters (name, planets, aspects, orbs, asprestr, orbrestr, comment)
values ('<Mid-Points Filter 1>', 1, 1, 1, 1, 1, 'Example mid-points filter.');/*End*/


/* Filters */
insert into Filters (name, planets, aspects, orbs, asprestr, orbrestr, midpoints)
values ('<Default Filters Set>', 1, 1, 1, 1, 1, 1);/*End*/


/* Config */
insert into Config (dft_filter) values (1);


/* End. */
