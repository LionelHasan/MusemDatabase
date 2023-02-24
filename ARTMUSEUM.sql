DROP DATABASE IF EXISTS ARTSMUSEUM;
CREATE DATABASE ARTSMUSEUM; 
USE ARTSMUSEUM;


DROP TABLE IF EXISTS COLLECTIONS;
CREATE TABLE COLLECTIONS (
	CNAME					varchar(30) not null,
	CURRENT_CONTACT_PERSON 	varchar(30),
    PHONE					varchar(30),
    ADDRESS					varchar(30),
    CDESCRIPTION			varchar(30),
    CTYPE					varchar(30),
    
    primary key (CNAME)
);

INSERT INTO COLLECTIONS (CNAME, CURRENT_CONTACT_PERSON, PHONE, ADDRESS, CDESCRIPTION, CTYPE)
VALUES
('Picasso','Yoda','403-923-2000','1200 Fifth Avenue', 'Picasso Art', 'Museum'),
('Royal', 'Charles', '403-200-1020', 'Building 1200 Yodi Land', 'Royal Art', 'Personal'),
('NA', 'James', '403-100-0002', 'Art Institute of Chicago, NY', 'American found art', 'Museum'),
('French', 'Bond', '403-777-2992','Museum of Fine Arts, Boston', 'French Pieces', 'Museum'),
('Old', 'Paolo', '403-721-2392','National Museum of Recovery', 'Ancient War Artifacts', 'Museum'),
('Greek', 'Ja', '403-123-1222','Louvre Museum', 'Greek Antiquities', 'Museum');


DROP TABLE IF EXISTS ART_OBJECT;
CREATE TABLE ART_OBJECT (
	ID_NO					integer	not null,
	EPOCH					varchar(30),
	ART_DESCRIPTION			varchar(100),
    TITLE					varchar(100),
    YEAR_MADE				varchar(30),
    CULTURE_OR_COUNTRY		varchar(30),
    COLLECTION_NAME			varchar(30),
    
	primary key (ID_NO),
    constraint COLLECTNAME_ART foreign key (COLLECTION_NAME) references COLLECTIONS (CNAME) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO ART_OBJECT (ID_NO, EPOCH, ART_DESCRIPTION, TITLE, YEAR_MADE, CULTURE_OR_COUNTRY, COLLECTION_NAME)
VALUES
('002', 'Renaissance', 'Represents reality', "Trompe I'Oeil Still Life with Flower Garland and Curtain", '1658', 'Dutch', 'Royal'),
('837', 'Renissance', 'Represents music', "Still Life with Violin", '1912', 'French', 'French'),
('920', 'Modern', 'Represents shallow space', "Violin and Grapes", '1912', 'French', 'French'),
('571', 'Ancient', 'Represents a failing society', "The Scallop Shell", '1912', 'French', 'French'),
('431', 'Ancient', 'Represents Life', "Birth and Rebirth and Rebirth", '2019', 'American', 'NA'),
('020', 'Ancient', 'Candlestick holder used in the 1500s', "Angel Bearing Candlestick", '1524', 'French', 'French'),
('721', 'Modern', 'Represents cutlery', "The Absinthe Glass", '1914', 'Spanish', 'Picasso'),
('241', 'Modern', 'Represents survival', "Glass and Die", '1914', 'Spanish', 'Picasso'),
('833', 'Modern', 'Represents a broken picnic', "The Bottle of Banyuls", '1914', 'Spanish', 'Picasso'),
('202', 'Modern', 'Wood work', "Bowl", '1500', 'First Nations', 'NA'),
('183', 'Ancient', 'Pottery', "Face Jug", '1867', 'American', 'NA'),
('004', 'Renissance', 'Represents battle', "Field Armor of King Henry VIII of England", '1544', 'England', 'Royal'),
('287', 'Renissance', 'Represents battle', "Armor Garniture of KIng Henry VIII of England", '1527', 'England', 'Royal'),
('661', 'Ancient', 'Wedding Feast', "Les Noces de Cana", '1500', 'Italian', 'Old'),
('442', 'Ancient', 'Religious Statue', "La Vierge de Calvaire", '1600', 'Netherlands', 'Old'),
('092', 'Imperial Rome', 'Statue of son of Clemenès, Asthenian', "Statue: Marcellus", '1207', 'Rome', 'Greek');


DROP TABLE IF EXISTS BORROWED;
CREATE TABLE BORROWED (
	BORROW_ID_NO		integer not null,
	DATE_RETURNED		varchar(10),
	DATE_BORROWED		varchar(10),
    COLLECTION_NAME			varchar(30),
    
    primary key (BORROW_ID_NO),
    constraint BORROWID foreign key (BORROW_ID_NO) references ART_OBJECT (ID_NO) ON DELETE CASCADE ON UPDATE CASCADE,
    constraint COLLECTNAME_BORROW foreign key (COLLECTION_NAME) references COLLECTIONS (CNAME) ON DELETE CASCADE ON UPDATE CASCADE
    );
    
    insert into BORROWED (BORROW_ID_NO, DATE_RETURNED, DATE_BORROWED, COLLECTION_NAME)
    VALUES 
    ('002', '2020-11-11', '2021-12-12','Royal'),
    ('837', '2011-08-11', '2015-07-12','French'),
    ('920', '2012-03-11', '2019-02-26','French'),
    ('661', '2011-09-22', '2019-03-12','Old'),
    ('442', '2020-06-01', '2022-02-02','Old'),
    ('092', '2002-12-22', '2020-02-22','Greek');
 


DROP TABLE IF EXISTS PERMANENT_COLLECTION;
CREATE TABLE PERMANENT_COLLECTION (
	PERM_ID_NO		integer not null,
    BSTATUS			varchar(30),
    COST			integer,
    DATE_ACQUIRED	varchar(10),
    
    primary key (PERM_ID_NO),
    constraint PERMID foreign key (PERM_ID_NO) references ART_OBJECT (ID_NO) ON DELETE CASCADE ON UPDATE CASCADE
    );
    
    
insert into PERMANENT_COLLECTION (PERM_ID_NO, BSTATUS, COST, DATE_ACQUIRED)
VALUES
('571','Stored','101000','2008-9-9'),
('431','Stored','50001','2008-9-9'),
('020','Display','25034','2008-9-9'),
('721','Display','52880','2008-9-9'),
('241','Stored','51110','2008-9-9'),
('833','Display','512310','2008-9-9'),
('202','Stored','303213','2008-9-9'),
('183','Display','603123','2008-9-9'),
('004','Display','20','2008-9-9'),
('287','Display','1000','2008-9-9');


DROP TABLE IF EXISTS PAINTING;
CREATE TABLE PAINTING (
    PAINT_ID_NO         integer not null,
    PAINT_STYLE         varchar(30),
    MATERIAL            varchar(30),
    PAINT_TYPE          varchar(30),

    primary key (PAINT_ID_NO),
    constraint PAINTID foreign key (PAINT_ID_NO) references ART_OBJECT (ID_NO) ON DELETE CASCADE ON UPDATE CASCADE
    );

insert into PAINTING (PAINT_ID_NO, PAINT_STYLE, MATERIAL, PAINT_TYPE)
VALUES
('002', 'Baroque', 'Canvas', 'Oil'),
('837', 'Cubism', 'Paper', 'Charcoal'),
('920', 'Analytic Cubism', 'Canvas', 'Oil'),
('571', 'Futuristic', 'Canvas', 'Enamel'),
('431', 'Rebirth', 'Panel', 'Charcoal Pastel'),
('661', 'Religious', 'Paper', 'Oil');

DROP TABLE IF EXISTS STATUE;
CREATE TABLE STATUE (
    STAT_ID_NO          integer not null,
    STAT_STYLE          varchar(50),
    STAT_WEIGHT         integer,
    STAT_HEIGHT         integer,
    STAT_MATERIAL       varchar(40),

    primary key (STAT_ID_NO),
    constraint STATID foreign key (STAT_ID_NO) references ART_OBJECT (ID_NO) ON DELETE CASCADE ON UPDATE CASCADE
    );

insert into STATUE (STAT_ID_NO, STAT_STYLE, STAT_WEIGHT, STAT_HEIGHT, STAT_MATERIAL)
VALUES
('004', 'Armor', '50', '184.2', 'Steel'),
('287', 'Armor', '62', '185.4', 'Steel/Gold'),
('442', 'Figurine of Religion', '32', '118', 'feuillum wood - oak');

DROP TABLE IF EXISTS SCULPTURE;
CREATE TABLE SCULPTURE (
    SCUL_ID_NO      integer not null,
    SCUL_STYLE      varchar(30),
    SCUL_WEIGHT     integer,
    SCUL_HEIGHT     integer,
    SCUL_MATERIAL   varchar(30),

    primary key (SCUL_ID_NO),
    constraint SCULPTID foreign key (SCUL_ID_NO) references ART_OBJECT (ID_NO) ON DELETE CASCADE ON UPDATE CASCADE
    );

insert into SCULPTURE (SCUL_ID_NO, SCUL_STYLE, SCUL_WEIGHT, SCUL_HEIGHT, SCUL_MATERIAL)
VALUES
('020', 'Angel','103','391.3','Bronze'),
('721', 'Classic Pontarlier', '15', '22.5', 'Painted bronze'),
('241', 'Minimalism', '30', '23.5', 'Wood'),
('092', 'Nude', '351', '180', 'Marble');


DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST (
    ARTIST_NAME             varchar(50) not null DEFAULT 'unknown',
    EPOCH                   varchar(50),
    ORIGIN_COUNTRY          varchar(50),
    DATE_BORN               varchar(10),
    DATE_DIED               varchar(10),
    MAIN_STYLE              varchar(30),
    ARTIST_DESCRIPTION      varchar(100),

    primary key (ARTIST_NAME)
    );

insert into ARTIST (ARTIST_NAME, EPOCH, ORIGIN_COUNTRY, DATE_BORN, DATE_DIED, MAIN_STYLE, ARTIST_DESCRIPTION)
VALUES ('Robert Pruitt', 'Renaissance', 'USA', '1975-3-2', null , 'Figurative Drawings', 'Visual Artist'),
('Pablo Picasso', 'Renaissance', 'Spain', '1881-10-25', '1973-04-08', 'Paintings', 'Known for pioneering cubism'),
('Georges Braque', 'Ancient', 'France', '1882-05-13', '1963-08-31', 'Painting', 'Known for his role in the development of cubism'),
('Adriaen van der Spelt', 'Ancient', 'Netherlands', '1630-04-01', '1673-07-01', 'Painting', 'Known for his flower paintings'),
('Benedetto da Rovezzano', 'Ancient', 'Italy', '1474-09-22', '1552-03-21', 'Architect','Known for his sculptures'),
('Juan Gris', 'Modern', 'France', '1887-03-23', '1927-05-11', 'Innovative', 'Known for his distinctive work'),
('Nori', 'Futurisitic', 'Canada', '1450-09-01', '1550-09-02', 'Wood Art','Known for multi-ranging art'),
('Damian Luck', 'Renissance', 'England', '1870-01-02', '1890-03-22', 'Sculpture', 'Known for his creations of armor'),
('Paolo Veronese', 'Ancient', 'Italy', '1600-02-11', '1623-02-11', 'Paintings', 'Known for his art work based on Christianity'),
('Joe Harris', 'Ancient Religion', 'Paris', '1524-04-22', '1555-02-01', 'Sculpting', 'Built multiple statues during World War II'),
('Bob Ross', 'Imperial Rome', 'Rome', '1197-02-11', '1210-11-11', 'Nude Sculptures', 'Sculpted the Greek Gods');

Drop TABLE IF EXISTS EXHIBITION;
CREATE TABLE EXHIBITION(
	EXHIBITION_NAME			varchar(100)	not null,
	START_DATE				varchar(10)	not null,
	END_DATE			    varchar(10),
	PRIMARY KEY (EXHIBITION_NAME)
);
INSERT INTO EXHIBITION
VALUES ('The Tudors','1970-12-23','2024-02-11'), 
("Cubism and the Trompe I'Oeil Tradition", '2022-08-20', '2023-01-22'), 
("Hear Me Now", '2022-09-09','2023-02-05'),
('Department of Recovery', '2022-09-01', '2023-07-25'),
('Department of Greek Antiquities','2010-01-12', '2022-12-22'),
('UNKNOWN', 'UNKNOWN', 'UNKNOWN');


Drop TABLE IF EXISTS SHOWN_DURING;
CREATE TABLE SHOWN_DURING(
	EXHIBITION_NAME			varchar(100)	not null,
	ART_ID_NO				INT 		not null,
	PRIMARY KEY (EXHIBITION_NAME,Art_ID_NO),
	constraint EXHIBNAME FOREIGN KEY(Exhibition_Name) REFERENCES EXHIBITION(EXHIBITION_NAME) ON DELETE CASCADE ON UPDATE CASCADE,
	constraint EXHIBID FOREIGN KEY(ART_ID_NO) REFERENCES ART_OBJECT(ID_NO) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO SHOWN_DURING
VALUES ('The Tudors', '002'),
('The Tudors', '837'),
("Cubism and the Trompe I'Oeil Tradition", '571'),
("Cubism and the Trompe I'Oeil Tradition", '920'),
("Hear Me Now", '431'),
("Hear Me Now", '020'),
('The Tudors', '721'),
('The Tudors','241'),
('The Tudors','833'),
('Hear Me Now', '202'),
('The Tudors', '183'),
("Cubism and the Trompe I'Oeil Tradition",'004'),
("Cubism and the Trompe I'Oeil Tradition",'287'),
('Department of Recovery', '661'),
('Department of Recovery','442'),
('Department of Greek Antiquities', '092');
            


Drop TABLE IF EXISTS OTHER;
CREATE TABLE OTHER(
	OTHER_ID				INT			not null,
	OTHER_TYPE				varchar(30)	not null,
	OTHER_STYLE				varchar(30)	not null,
	PRIMARY KEY (OTHER_ID),
	constraint OTHERID FOREIGN KEY(OTHER_ID) REFERENCES ART_OBJECT(ID_NO) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO OTHER
VALUES ('183', 'Face Jug', 'Pottery'), 
('202', 'Whittling', 'Modern'),
('833', 'Print', 'Collages');
            

Drop TABLE IF EXISTS CREATED_BY;
CREATE TABLE CREATED_BY(
	ARTIST_NAME				varchar(50) not null DEFAULT 'unknown',
	ART_ID_NO				INT			not null,
	PRIMARY KEY (ARTIST_NAME, ART_ID_NO),
	constraint CREATENAME FOREIGN KEY(ARTIST_NAME) REFERENCES ARTIST(ARTIST_NAME) ON DELETE CASCADE ON UPDATE CASCADE,
	constraint CREATEID FOREIGN KEY(ART_ID_NO) REFERENCES ART_OBJECT(ID_NO) ON DELETE CASCADE ON UPDATE CASCADE	
);
INSERT INTO CREATED_BY
VALUES 
('Adriaen van der Spelt', '002'),
('Georges Braque', '837'),
('Pablo Picasso', '920'),
('Pablo Picasso', '571'),
('Robert Pruitt', '431'),
('Benedetto da Rovezzano','020'),
('Pablo Picasso','721'),
('Pablo Picasso','241'),
('Juan Gris','833'),
('Nori','202'),
('Nori', '183'),
('Damian Luck', '004'),
('Damian Luck', '287'),
('Paolo Veronese','661'),
('Joe Harris', '442'),
('Bob Ross', '092');


DROP ROLE IF EXISTS database_guest@localhost;
CREATE ROLE database_guest@localhost;
GRANT Select ON ARTSMUSEUM.* TO database_guest@localhost;
DROP USER IF EXISTS guest@localhost;
flush privileges;
CREATE USER guest@localhost;
GRANT database_guest@localhost TO guest@localhost;
SET DEFAULT ROLE ALL TO guest@localhost;

DROP ROLE IF EXISTS database_data_entry@localhost;
CREATE ROLE database_data_entry@localhost;
GRANT Select, CREATE, DELETE, DROP, ALTER, EXECUTE, INSERT, TRIGGER, UPDATE, CREATE VIEW ON ARTSMUSEUM.* TO database_data_entry@localhost;
DROP USER IF EXISTS data_entry@localhost;
flush privileges;
CREATE USER data_entry@localhost identified WITH mysql_native_password BY 'dataentrypass';
GRANT database_data_entry@localhost TO data_entry@localhost;
SET DEFAULT ROLE ALL TO data_entry@localhost;

DROP ROLE IF EXISTS database_admin@localhost;
CREATE ROLE database_admin@localhost;
GRANT ALL privileges ON ARTSMUSEUM.* TO database_admin@localhost;
DROP USER IF EXISTS db_admin@localhost;
flush privileges;
CREATE USER db_admin@localhost IDENTIFIED WITH mysql_native_password BY 'adminpass';
GRANT database_admin@localhost TO db_admin@localhost;
SET DEFAULT ROLE ALL TO db_admin@localhost;