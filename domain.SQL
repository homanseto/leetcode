-- =====================================================================
-- 1. Create and Populate Table: d_access_times_day_code
-- =====================================================================

-- Create table structure
CREATE TABLE d_access_times_day_code (
    id SERIAL PRIMARY KEY,
    code VARCHAR(10) NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL
);

-- Insert data from dAccessTimesDayCode.geojson
INSERT INTO d_access_times_day_code (id, code, description) VALUES
(1, 'MON', 'Every Monday'), [cite: 1]
(2, 'TUE', 'Every Tuesday'), [cite: 1]
(3, 'WED', 'Every Wednesday'), [cite: 1]
(4, 'THU', 'Every Thursday'), [cite: 1]
(5, 'FRI', 'Every Friday'), [cite: 1]
(6, 'SAT', 'Every Saturday'), [cite: 1]
(7, 'SUN', 'Every Sunday'), [cite: 2]
(8, 'ED', 'Everyday (Monday - Sunday)'), [cite: 1]
(9, 'WD', 'All Weekday (Monday - Friday)'), [cite: 1]
(10, 'WE', 'All Weekend (Saturday - Sunday)'), [cite: 1]
(11, 'PH', 'All Public Holiday'), [cite: 1]
(12, 'EPH', 'Eve of all Public Holiday'); [cite: 1]

-- Reset the serial sequence to prevent conflicts on future manual inserts
SELECT setval(pg_get_serial_sequence('d_access_times_day_code', 'id'), COALESCE(MAX(id), 1)) FROM d_access_times_day_code;


-- =====================================================================
-- 2. Create and Populate Table: d_access_times_type
-- =====================================================================

-- Create table structure
CREATE TABLE d_access_times_type (
    id SERIAL PRIMARY KEY,
    code VARCHAR(10) NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL
);

-- Insert data from dAccessTimesType.geojson
INSERT INTO d_access_times_type (id, code, description) VALUES
(1, 'OPEN', 'Opening Hours'), [cite: 3]
(2, 'CLOSE', 'Closing Hours'); -- Fixed the typo "Closeing Hours" from the source file 

-- Reset the serial sequence
SELECT setval(pg_get_serial_sequence('d_access_times_type', 'id'), COALESCE(MAX(id), 1)) FROM d_access_times_type;


-- =====================================================================
-- 1. Create and Populate Table: d_direction
-- =====================================================================
CREATE TABLE d_direction (
    id SERIAL PRIMARY KEY,
    code INTEGER NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL
);

INSERT INTO d_direction (id, code, description) VALUES
(1, 1, 'One Way Forward'),
(2, -1, 'One Way Backward'),
(3, 0, 'Both Ways');

SELECT setval(pg_get_serial_sequence('d_direction', 'id'), COALESCE(MAX(id), 1)) FROM d_direction;


-- =====================================================================
-- 2. Create and Populate Table: d_floor_unit_data_source
-- =====================================================================
CREATE TABLE d_floor_unit_data_source (
    id SERIAL PRIMARY KEY,
    code INTEGER NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL
);

INSERT INTO d_floor_unit_data_source (id, code, description) VALUES
(1, 1, 'iB1000'),
(2, 2, '3DSpatialData'),
(3, 3, 'DAP'),
(4, 4, 'MMS'),
(5, 5, 'TD'),
(6, 6, 'AFCD'),
(7, 7, 'HyD'),
(8, 8, 'AsBuilt'),
(9, 9, 'Proposal'),
(10, 10, 'FieldChecking'),
(11, 11, 'Estimation'),
(12, 12, 'Other');

SELECT setval(pg_get_serial_sequence('d_floor_unit_data_source', 'id'), COALESCE(MAX(id), 1)) FROM d_floor_unit_data_source;


-- =====================================================================
-- 3. Create and Populate Table: d_floor_unit_level_source
-- =====================================================================
CREATE TABLE d_floor_unit_level_source (
    id SERIAL PRIMARY KEY,
    code INTEGER NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL
);

INSERT INTO d_floor_unit_level_source (id, code, description) VALUES
(1, 1, 'iB1000'),
(2, 2, '3DSpatialData'),
(3, 3, 'Photo'),
(4, 4, 'MMS'),
(5, 5, 'LiDAR'),
(6, 6, 'TD'),
(7, 7, 'AsBuilt'),
(8, 8, 'Proposal'),
(9, 9, 'FieldChecking'),
(10, 10, 'Estimation'),
(11, 11, 'Other');

SELECT setval(pg_get_serial_sequence('d_floor_unit_level_source', 'id'), COALESCE(MAX(id), 1)) FROM d_floor_unit_level_source;


-- =====================================================================
-- 4. Create and Populate Table: d_obstacles_type
-- =====================================================================
CREATE TABLE d_obstacles_type (
    id SERIAL PRIMARY KEY,
    code INTEGER NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL
);

INSERT INTO d_obstacles_type (id, code, description) VALUES
(1, 1, 'Accessible'),
(2, 2, 'BridgePier'),
(3, 3, 'BusStop'),
(4, 4, 'FireHydrant'),
(5, 5, 'LightPole'),
(6, 6, 'RoadSign'),
(7, 7, 'TrafficLight'),
(8, 8, 'TrafficSign'),
(9, 9, 'SignPole'),
(10, 10, 'Bollard'),
(11, 11, 'Tree'),
(12, 12, 'ElectricBox'),
(13, 13, 'ParkingMeter');

SELECT setval(pg_get_serial_sequence('d_obstacles_type', 'id'), COALESCE(MAX(id), 1)) FROM d_obstacles_type;


-- =====================================================================
-- 5. Create and Populate Table: d_ped_cover
-- =====================================================================
CREATE TABLE d_ped_cover (
    id SERIAL PRIMARY KEY,
    code INTEGER NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL
);

INSERT INTO d_ped_cover (id, code, description) VALUES
(1, 1, 'Covered'),
(2, 2, 'NonCovered'),
(3, 3, 'Unclassified');

SELECT setval(pg_get_serial_sequence('d_ped_cover', 'id'), COALESCE(MAX(id), 1)) FROM d_ped_cover;


-- =====================================================================
-- 6. Create and Populate Table: d_ped_crossing_feature
-- =====================================================================
CREATE TABLE d_ped_crossing_feature (
    id SERIAL PRIMARY KEY,
    code INTEGER NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL
);

INSERT INTO d_ped_crossing_feature (id, code, description) VALUES
(1, 1, 'Road'),
(2, 2, 'Tramway'),
(3, 3, 'LightRail'),
(4, 4, 'BicycleTrack'),
(5, 5, 'PublicTransportInterchange');

SELECT setval(pg_get_serial_sequence('d_ped_crossing_feature', 'id'), COALESCE(MAX(id), 1)) FROM d_ped_crossing_feature;


-- =====================================================================
-- 7. Create and Populate Table: d_ped_data_source
-- =====================================================================
CREATE TABLE d_ped_data_source (
    id SERIAL PRIMARY KEY,
    code INTEGER NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL
);

INSERT INTO d_ped_data_source (id, code, description) VALUES
(1, 1, 'iB1000'),
(2, 2, '3DSpatialData'),
(3, 3, 'DAP'),
(4, 4, 'MMS'),
(5, 5, 'TD'),
(6, 6, 'AFCD'),
(7, 7, 'HyD'),
(8, 8, 'AsBuilt'),
(9, 9, 'Proposal'),
(10, 10, 'FieldChecking'),
(11, 11, 'Estimation'),
(12, 12, 'Other');

SELECT setval(pg_get_serial_sequence('d_ped_data_source', 'id'), COALESCE(MAX(id), 1)) FROM d_ped_data_source;


-- =====================================================================
-- 8. Create and Populate Table: d_ped_enabled
-- =====================================================================
CREATE TABLE d_ped_enabled (
    id SERIAL PRIMARY KEY,
    code INTEGER NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL
);

INSERT INTO d_ped_enabled (id, code, description) VALUES
(1, 1, 'True'),
(2, 2, 'False');

SELECT setval(pg_get_serial_sequence('d_ped_enabled', 'id'), COALESCE(MAX(id), 1)) FROM d_ped_enabled;


-- =====================================================================
-- 9. Create and Populate Table: d_ped_feature_type
-- =====================================================================
CREATE TABLE d_ped_feature_type (
    id SERIAL PRIMARY KEY,
    code INTEGER NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL
);

INSERT INTO d_ped_feature_type (id, code, description) VALUES
(1, 1, 'Footway'),
(2, 2, 'Footbridge'),
(3, 4, 'Subway'),
(4, 5, 'Service Lane'),
(5, 6, 'Traffic Island'),
(6, 7, 'RunIn'),
(7, 8, 'Escalator'),
(8, 9, 'Travelator'),
(9, 10, 'Lift'),
(10, 11, 'Ramp'),
(11, 12, 'Staircase'),
(12, 13, 'Stairlift'),
(13, 14, 'Other'),
(14, 15, 'M_Footway'),
(15, 16, 'M_Escalator'),
(16, 17, 'M_Travelator'),
(17, 18, 'M_Lift'),
(18, 19, 'M_Ramp'),
(19, 20, 'M_Staircase'),
(20, 21, 'M_Stairlift'),
(21, 22, 'M_Others'),
(22, 23, 'Generalized Walkway inside Park'),
(23, 24, 'Footpath'),
(24, 25, 'Village'),
(25, 26, 'Track'),
(26, 30, 'Crossing - Signalized'),
(27, 31, 'Crossing - Zebra'),
(28, 32, 'Crossing - Cautionary'),
(29, 33, 'Crossing - Others');

SELECT setval(pg_get_serial_sequence('d_ped_feature_type', 'id'), COALESCE(MAX(id), 1)) FROM d_ped_feature_type;


-- =====================================================================
-- 10. Create and Populate Table: d_site_type
-- =====================================================================
CREATE TABLE d_site_type (
    id SERIAL PRIMARY KEY,
    code INTEGER NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL
);

INSERT INTO d_site_type (id, code, description) VALUES
(1, 1, 'Farm'),
(2, 2, 'Accommodation'),
(3, 3, 'Commerce'),
(4, 4, 'EducationAndTraining'),
(5, 5, 'HealthAndMedicalService'),
(6, 6, 'Leisure,CultureAndSports'),
(7, 7, 'Organization'),
(8, 8, 'PublicAndSocialService'),
(9, 9, 'Religion'),
(10, 10, 'TouristAttraction'),
(11, 11, 'Military'),
(12, 12, 'Industry'),
(13, 13, 'WorksArea'),
(14, 14, 'Transportation'),
(15, 15, 'Utilities');

SELECT setval(pg_get_serial_sequence('d_site_type', 'id'), COALESCE(MAX(id), 1)) FROM d_site_type;