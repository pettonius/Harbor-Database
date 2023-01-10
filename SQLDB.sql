CREATE TABLE Is_Stored (
	Shipment_Id varchar DEFAULT '000000' NOT NULL,
	SA_Id varchar DEFAULT '0000' NOT NULL,
	StartDate datetime NOT NULL,
	EndDate datetime NOT NULL,
	StoreConditions text DEFAULT NULL,
	PRIMARY KEY (Shipment_Id,SA_Id)
	
);

INSERT INTO "Is_Stored" VALUES ('100011','2001','1984-02-11 00:00:00','1984-02-13 00:00:00',NULL),('200022','2012','1981-05-20 10:07:10','1981-05-29 10:07:10',NULL),('330032','2003','2000-07-15 11:01:01','2000-07-30 06:03:15',NULL),('456201','2011','2007-03-30 21:15:03','2007-04-05 00:00:00',NULL),('753103','2005','2002-02-11 20:00:00','2002-02-19 21:00:00',NULL),('907336','2016','2012-08-01 16:00:00','2012-08-13 16:59:00',NULL),('702345','2007','1960-01-31 22:00:00','1960-02-01 00:00:00',NULL),('992643','2003','2015-09-01 12:00:00','2015-09-07 12:50:00',NULL),('854200','2009','2015-09-01 12:50:00','2015-09-07 12:00:00',NULL),('542103','2010','2010-11-25 21:43:35','2010-12-09 22:00:00',NULL);

CREATE TABLE Cargo (
	Shipment_Id varchar DEFAULT '000000' NOT NULL,
	Type string NOT NULL,
	ShipmentMethod string NOT NULL,
	BulkWeight float DEFAULT NULL,
	ContNumber integer DEFAULT NULL,
	IsFragile boolean DEFAULT FALSE,
	IsDangerous boolean DEFAULT FALSE,
	Special_Care text DEFAULT NULL,
	PRIMARY KEY (Shipment_Id)	
);

INSERT INTO "Cargo" VALUES ('100011','wood','bulk',500,NULL,FALSE,FALSE,NULL),('200022','package','container',NULL,100,TRUE,FALSE,NULL),('330032','oil','container',NULL,500,FALSE,TRUE,NULL),('456201','aluminum','bulk',1000,NULL,FALSE,FALSE,NULL),('753103','potatoes','bulk',700,NULL,FALSE,FALSE,NULL),('907336','wood','bulk',3500,NULL,FALSE,FALSE,NULL),('702345','sand','bulk',3200,NULL,FALSE,FALSE,NULL),('992643','oil','container',NULL,400,FALSE,TRUE,NULL),('854200','package','container',NULL,200,TRUE,FALSE,NULL),('542103','potatoes','container',NULL,600,TRUE,FALSE,NULL);

CREATE TABLE Station (
	Station_Id varchar DEFAULT '000' NOT NULL,
	MinimumLength float,
	MaximumLength float,
	MinimumWidth float,
	MaximumWidth float,
	PRIMARY KEY (Station_Id)
);

INSERT INTO "Station" VALUES ('501',200,250,20,30),('402',300,350,30,40),('303',250,400,35,45),('444',100,150,15,20),('115',200,250,20,30),('926',400,500,40,50),('37',500,550,60,70),('88',300,400,30,35),('654',200,250,20,25),('2',100,200,20,30);

CREATE TABLE Arrival (
	Station_Id varchar DEFAULT '000' NOT NULL,
	Shipment_Id varchar DEFAULT '000' NOT NULL,
	Ship_Id varchar DEFAULT '00000000' NOT NULL,
	Port_Id varchar DEFAULT '000' NOT NULL,
	ExpDateTime datetime NOT NULL,
	ActualDateTime datetime NOT NULL,
	PRIMARY KEY (Station_Id,Shipment_Id,Ship_Id,Port_Id)
);	

INSERT INTO "Arrival" VALUES ('501','100011','13452795','234','1984-02-10 22:00:00','1984-02-10 22:15:00'),('402','200022','12934712','214','1981-05-20 07:00:00','1981-05-20 07:30:45'),('303','330032','42093845','138','2000-07-15 10:30:00','2000-07-15 10:45:00'),('444','456201','22993811','017','2007-03-30 19:45:00','2007-03-30 20:00:00'),('115','753103','79823450','025','2002-02-11 19:00:00','2002-02-11 19:05:00'),('926','907336','10965432','111','2012-08-01 15:20:00','2012-08-01 15:00:00'),('37','702345','09563104','050','1960-01-31 20:30:00','1960-01-31 20:50:00'),('88','992643','1000000','201','2015-09-01 10:45:00','2015-09-01 10:45:00'),('654','854200','00452304','408','2015-09-01 12:30:00','2015-09-01 12:45:00'),('2','542103','98352912','312','2010-11-25 21:00:00','2010-11-25 21:00:00');

CREATE TABLE Port (
	Port_Id varchar DEFAULT '000' NOT NULL,
	Country string1,
	City string,
	PRIMARY KEY (Port_Id)
);

INSERT INTO "Port" VALUES ('234','China','Shangai'),('214','Italy','Milan'),('138','United Kingdom','London'),('017','Greece','Athens'),('025','Spain','Valencia'),('111','Turkey','Istanbul'),('050','Norway','Alesund'),('201','Egypt','Cairo'),('408','India','Gujarat'),('312','Japan','Fukuoka');

CREATE TABLE Departure (
	Station_Id varchar DEFAULT '000' NOT NULL,
	Shipment_Id varchar DEFAULT '000' NOT NULL,
	Ship_Id varchar DEFAULT '00000000' NOT NULL,
	Port_Id varchar DEFAULT '000' NOT NULL,
	ExpDateTime datetime NOT NULL,
	ActualDateTime datetime NOT NULL,
	PRIMARY KEY (Station_Id,Shipment_Id,Ship_Id,Port_Id)
);

INSERT INTO "Departure" VALUES ('501','100011','13452795','234','1984-02-10 23:00:00','1984-02-10 23:15:00'),('402','200022','12934712','214','1981-05-20 08:00:00','1981-05-20 08:10:00'),('303','330032','42093845','138','2000-07-15 11:30:00','2000-07-15 11:30:00'),('444','456201','22993811','017','2007-03-30 20:30:00','2007-03-30 20:20:00'),('115','753103','79823450','025','2002-02-11 20:00:00','2002-02-11 20:50:00'),('926','907336','10965432','111','2012-08-01 15:50:00','2012-08-01 16:00:00'),('37','702345','09563104','050','1960-01-31 21:10:00','1960-01-31 21:20:00'),('88','992643','1000000','201','2015-09-01 12:00:00','2015-09-01 11:45:00'),('654','854200','00452304','408','2015-09-01 13:30:00','2015-09-01 13:45:00'),('2','542103','98352912','312','2010-11-25 22:00:00','2010-11-25 22:05:00');


CREATE TABLE StorageArea (
	StorageArea_Id varchar DEFAULT '0000' NOT NULL,
	MerchandiseType string,
	Location string,
	PRIMARY KEY (StorageArea_Id)
);

INSERT INTO "StorageArea" VALUES ('2001','wood','Section A'),('2002','wood','Section B'),('2003','wood','Section C'),('2004','aluminum','Section D'),('2005','aluminum','Section A'),('2006','sand','Section B'),('2007','sand','Section C'),('2008','sand','Section A'),('2009','potatoes','Section B'),('2010','potatoes','Section C'),('2011','oil','Section A'),('2012','oil','Section B'),('2013','package','Section C'),('2014','package','Section A'),('2015','package','Section B'),('2016','potatoes','Section C'),('2017','potatoes','Section A'),('2018','potatoes','Section B'),('2019','oil','Section C'),('2020','package','Section D');

CREATE TABLE Warehouse (
	StorageArea_Id varchar DEFAULT '0000' NOT NULL,
	TotalCpacity float,
	FreeCpacity float,
	PRIMARY KEY (StorageArea_Id),
	FOREIGN KEY (StorageArea_Id) REFERENCES StorageArea(StorageArea_Id)
				ON DELETE SET DEFAULT ON UPDATE CASCADE
	
);

INSERT INTO "Warehouse" VALUES ('2001',80000,2000),('2002',90000,90000),('2003',75000,20000),('2004',60000,0),('2005',55000,0),('2006',12000,8000),('2007',50000,1000),('2008',1000000,500000),('2009',200000,0),('2010',720000,620000);

CREATE TABLE ContainerYard (
	StorageArea_Id varchar DEFAULT '0000' NOT NULL,
	TotalContainerSpace integer,
	FreeContainerSpace integer,
	PRIMARY KEY (StorageArea_Id),
	FOREIGN KEY (StorageArea_Id) REFERENCES StorageArea(StorageArea_Id)
				ON DELETE SET DEFAULT ON UPDATE CASCADE
);

INSERT INTO "ContainerYard" VALUES ('2011',1000,0),('2012',9000,9000),('2013',10000,1000),('2014',20000,250),('2015',5000,4550),('2016',1600,500),('2017',3000,1000),('2018',25000,20500),('2019',4500,1000),('2020',18000,9000);

CREATE TABLE Ship (
	Ship_Id varchar DEFAULT '00000000' NOT NULL,
	ShipName string NOT NULL,
	Length float,
	Width float,
	Weight integer,
	ConstructionDate date,
	Owner string DEFAULT NULL,
	PRIMARY KEY (Ship_Id)
);

INSERT INTO "Ship" VALUES ('13452795','Diana',400,60,200000,'1932-02-13','MSC'),('12934712','Barzan',450,60,195000,'1999-01-21','Yang Ming Marine Transport Corporation'),('42093845','Pegasus',200,35,80000,'2005-05-09','ONE'),('22993811','Ever Golden',400,60,200000,'2009-07-12','Evergreen'),('79823450','Oceania',380,70,180000,'2000-11-09','MSC'),('10965432','Triumph',150,21,75000,'1942-03-03','MSC'),('09563104','COSCO',400,60,200000,'1984-02-13','COSCO'),('10000000','OOCL',240,50,110000,'1993-12-20','Teekay'),('00452304','Madrid Maersk',101,16,40000,'1920-06-01','Ap Moller-Maersk'),('98352912','OPAL FORTUNE',180,30,110000,'2017-03-21','CMA CGM Group');










