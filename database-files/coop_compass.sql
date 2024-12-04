DROP SCHEMA IF EXISTS `coop_compass` ;
CREATE DATABASE IF NOT EXISTS `coop_compass`;
USE `coop_compass`;

DROP TABLE IF EXISTS `flaggedReview`;
DROP TABLE IF EXISTS `review`;
DROP TABLE IF EXISTS `sentJobListings`;
DROP TABLE IF EXISTS `favoriteJobListings`;
DROP TABLE IF EXISTS `jobListing`;
DROP TABLE IF EXISTS `company`;
DROP TABLE IF EXISTS `recruiter`;
DROP TABLE IF EXISTS `admin`;
DROP TABLE IF EXISTS `student`;
DROP TABLE IF EXISTS `advisor`;
DROP TABLE IF EXISTS `deletedJobListings`;


CREATE TABLE IF NOT EXISTS `admin`
(
    `adminId`     VARCHAR(255) PRIMARY KEY DEFAULT (UUID()),
    `name`        VARCHAR(255) NOT NULL,
    `email`       VARCHAR(255) NOT NULL,
    `phoneNumber` BIGINT
);

CREATE TABLE IF NOT EXISTS `advisor`
(
    `advisorId`   VARCHAR(255) PRIMARY KEY DEFAULT (UUID()),
    `name`        VARCHAR(255) NOT NULL,
    `email`       VARCHAR(255) NOT NULL,
    `phoneNumber` BIGINT
);

CREATE TABLE IF NOT EXISTS `student`
(
    `studentId`   VARCHAR(255) PRIMARY KEY DEFAULT (UUID()),
    `advisorId`   VARCHAR(255) REFERENCES `advisor` (`advisorId`),
    `name`        VARCHAR(255) NOT NULL,
    `email`       VARCHAR(255) NOT NULL,
    `phoneNumber` BIGINT
);

CREATE TABLE IF NOT EXISTS `recruiter`
(
    `recruiterId` VARCHAR(255) PRIMARY KEY DEFAULT (UUID()),
    `name`        VARCHAR(255) NOT NULL,
    `email`       VARCHAR(255) NOT NULL,
    `phoneNumber` BIGINT
);

CREATE TABLE IF NOT EXISTS `company`
(
    `companyId`      VARCHAR(255) PRIMARY KEY,
    `adminCreatedId` VARCHAR(255) NOT NULL REFERENCES `admin` (`adminId`),
    `name`           VARCHAR(255) NOT NULL,
    `headline`       VARCHAR(255),
    `description`    TEXT,
    `websiteLink`    VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS `jobListing`
(
    `jobListingId` VARCHAR(255) PRIMARY KEY DEFAULT (UUID()),
    `recruiterId`  VARCHAR(255) NOT NULL REFERENCES `recruiter` (`recruiterId`),
    `companyId`    VARCHAR(255) NOT NULL REFERENCES `company` (`companyId`),
    `jobTitle`     VARCHAR(255) NOT NULL,
    `description`  TEXT,
    `startDate`    DATE,
    `endDate`      DATE,
    `hourlyWage`   INT,
    `skills`       TEXT,
    `location`     VARCHAR(255),
    `deleted`      BOOLEAN DEFAULT false,
    `datePosted`   TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS `review`
(
    `reviewId`        VARCHAR(255) PRIMARY KEY DEFAULT (UUID()),
    `jobListingId`    VARCHAR(255) NOT NULL REFERENCES `jobListing` (`jobListingId`),
    `studentId`       VARCHAR(255) NOT NULL REFERENCES `student` (`studentId`),
    `anonymous`       BOOLEAN DEFAULT true,
    `description`     TEXT,
    `jobSatisfaction` INT CHECK (`jobSatisfaction` BETWEEN 1 AND 5),
    `hourlyWage`      INT,
    `deleted`         BOOLEAN DEFAULT false,
    `datePosted`      TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS `favoriteJobListings`
(
    `studentId`    VARCHAR(255) NOT NULL REFERENCES `student` (`studentId`),
    `jobListingId` VARCHAR(255) NOT NULL REFERENCES `jobListing` (`jobListingId`),
    PRIMARY KEY (`studentId`, `jobListingId`)
);

CREATE TABLE IF NOT EXISTS `flaggedReview`
(
    `reviewId`        VARCHAR(255) NOT NULL REFERENCES `review` (`reviewId`),
    `flaggedById`     VARCHAR(255) NOT NULL REFERENCES `recruiter` (`recruiterId`),
    `reason`          TEXT         NOT NULL,
    `dateFlagged`     TIMESTAMP DEFAULT CURRENT_TIMESTAMP    NOT NULL,
    PRIMARY KEY (`reviewId`, `flaggedById`)
);

CREATE TABLE IF NOT EXISTS `sentJobListings`
(
    `jobListingId`     VARCHAR(255) NOT NULL REFERENCES `jobListing` (`jobListingId`),
    `studentId`        VARCHAR(255) NOT NULL REFERENCES `student` (`studentId`),
    `advisorId`        VARCHAR(255) NOT NULL REFERENCES `advisor` (`advisorId`),
    PRIMARY KEY (`jobListingId`, `studentId`, `advisorId`)
);

insert into `admin` (`adminId`, `name`, `email`, `phoneNumber`) values 
('1', 'Sam', 'lmizzi0@senate.gov', 5628527288),
('2', 'Jorie', 'jyuryichev1@amazon.co.jp', 1039806271),
('3', 'Inglis', 'icockerill2@rakuten.co.jp', 9903030009),
('4', 'Arleyne', 'ahelder3@cdc.gov', 6654685293),
('5', 'Jordain', 'jeixenberger4@psu.edu', 6492932409),
('6', 'Felita', 'ffowley5@opensource.org', 6982304075),
('7', 'Candi', 'cryde6@auda.org.au', 2183635205),
('8', 'Fey', 'fbernuzzi7@purevolume.com', 7468015888),
('9', 'Dari', 'dpatrone8@nytimes.com', 3704172970),
('10', 'Paolina', 'pdymocke9@chicagotribune.com', 5709425554);

insert into `advisor` (`advisorId`, `name`, `email`, `phoneNumber`) values 
('1', 'Rachel', 'aeplate0@ehow.com', 1097505450),
('2', 'Johannah', 'jpolin1@mtv.com', 6429056148),
('3', 'Clarance', 'ccaselick2@rambler.ru', 9756653194),
('4', 'Cheslie', 'cnorley3@barnesandnoble.com', 9869398550),
('5', 'Jeannie', 'jdanford4@theglobeandmail.com', 2093779799),
('6', 'Annie', 'ajennemann5@telegraph.co.uk', 1904086200),
('7', 'Tome', 'treavell6@weebly.com', 1609609756),
('8', 'Kristian', 'kjurkowski7@microsoft.com', 6843489383),
('9', 'Leona', 'lgwioneth8@usda.gov', 8054821240),
('10', 'Neall', 'ndeason9@mozilla.com', 7924372720);

insert into `student` (`studentId`, `advisorId`, `name`, `email`, `phoneNumber`) values 
('100', '1', 'Aaryan Jain', 'aaryanjain1203@gmail.com', 1234567890),
('101', '1', 'Alice Johnson', 'alice.johnson@example.com', 1234567890),
('102', '2', 'Bob Smith', 'bob.smith@example.com', 2345678901),
('103', '3', 'Charlie Brown', 'charlie.brown@example.com', 3456789012),
('104', '4', 'David Clark', 'david.clark@example.com', 4567890123),
('105', '5', 'Emma Davis', 'emma.davis@example.com', 5678901234),
('106', '6', 'Fiona White', 'fiona.white@example.com', 6789012345),
('107', '7', 'George King', 'george.king@example.com', 7890123456),
('108', '8', 'Hannah Lee', 'hannah.lee@example.com', 8901234567),
('109', '9', 'Isaac Turner', 'isaac.turner@example.com', 9012345678),
('110', '10', 'Julia Adams', 'julia.adams@example.com', 1123456789),
('111', '1', 'Kevin Carter', 'kevin.carter@example.com', 2234567890),
('112', '2', 'Laura Nelson', 'laura.nelson@example.com', 3345678901),
('113', '3', 'Michael Scott', 'michael.scott@example.com', 4456789012),
('114', '4', 'Nancy Harris', 'nancy.harris@example.com', 5567890123),
('115', '5', 'Oliver Wright', 'oliver.wright@example.com', 6678901234),
('116', '6', 'Patricia Walker', 'patricia.walker@example.com', 7789012345),
('117', '7', 'Quinn Hughes', 'quinn.hughes@example.com', 8890123456),
('118', '8', 'Rachel Brooks', 'rachel.brooks@example.com', 9901234567),
('119', '9', 'Samuel Price', 'samuel.price@example.com', 1012345678),
('120', '10', 'Tina Bell', 'tina.bell@example.com', 2023456789),
('121', '1', 'Uma Hill', 'uma.hill@example.com', 3034567890),
('122', '2', 'Victor Green', 'victor.green@example.com', 4045678901),
('123', '3', 'Wendy Cox', 'wendy.cox@example.com', 5056789012),
('124', '4', 'Xander Reed', 'xander.reed@example.com', 6067890123),
('125', '5', 'Yvonne Cook', 'yvonne.cook@example.com', 7078901234),
('126', '6', 'Zachary Morgan', 'zachary.morgan@example.com', 8089012345),
('127', '7', 'Abby Foster', 'abby.foster@example.com', 9090123456),
('128', '8', 'Ben Lopez', 'ben.lopez@example.com', 1101234567),
('129', '9', 'Cathy Perry', 'cathy.perry@example.com', 2203456789),
('130', '10', 'Derek Ramirez', 'derek.ramirez@example.com', 3304567890);

insert into `recruiter` (`recruiterId`, `name`, `email`, `phoneNumber`) values 
('0', 'Quandale', 'quandale@gmail.com', 1234567890),
('1', 'Emmaline', 'eklus0@shareasale.com', 9736374111),
('2', 'Fayina', 'fandrin1@businessinsider.com', 8536196206),
('3', 'Benedikta', 'blantaph2@cloudflare.com', 6132895977),
('4', 'Ailyn', 'aguice3@discovery.com', 3019310702),
('5', 'Yvonne', 'yzeal4@mail.ru', 7651916989),
('6', 'Llywellyn', 'lbockings5@a8.net', 7751281688),
('7', 'Heinrick', 'hmesser6@adobe.com', 6701469297),
('8', 'Bernadette', 'bsnoddy7@soundcloud.com', 5401635649),
('9', 'Paulie', 'ppuvia8@geocities.jp', 2686690835),
('10', 'Herman', 'hveazey9@comcast.net', 4263349666);

insert into `company` (`companyId`, `adminCreatedId`, `name`, `headline`, `description`, `websiteLink`) values
('1', '1', 'Dablist', 'Chronic iridocyclitis, left eye', 'Chronic iridocyclitis, left eye', 'http://cnbc.com'),
('2', '2', 'Cogilith', 'Chorioamnionitis, first trimester, fetus 5', 'Chorioamnionitis, first trimester, fetus 5', 'http://ibm.com'),
('3', '3', 'Shufflester', 'Superficial injury of other parts of head', 'Superficial injury of other parts of head', 'http://gnu.org'),
('4', '4', 'Realcube', 'Underdosing of local anesthetics, sequela', 'Underdosing of local anesthetics, sequela', 'https://accuweather.com'),
('5', '5', 'Divanoodle', 'Other specified injury of dorsal vein of foot', 'Other specified injury of dorsal vein of foot', 'https://bluehost.com'),
('6', '6', 'Tazzy', 'Oth fracture of base of skull, init for clos fx', 'Other fracture of base of skull, initial encounter for closed fracture', 'https://yandex.ru'),
('7', '7', 'Photobean', 'Oth disrd of bone density and structure, left forearm', 'Other specified disorders of bone density and structure, left forearm', 'http://networksolutions.com'),
('8', '8', 'Twitterwire', 'Angioplasty status', 'Angioplasty status', 'http://tmall.com'),
('9', '9', 'Babblestorm', 'Follicular lymphoma grade IIIb, intrathoracic lymph nodes', 'Follicular lymphoma grade IIIb, intrathoracic lymph nodes', 'https://mac.com'),
('10', '10', 'JumpXS', 'Disp fx of cuboid bone of left foot, subs for fx w malunion', 'Displaced fracture of cuboid bone of left foot, subsequent encounter for fracture with malunion', 'https://umich.edu'),
('11', '1', 'Skivee', 'Nondisp fx of lateral condyle of r femr, 7thJ', 'Nondisplaced fracture of lateral condyle of right femur, subsequent encounter for open fracture type IIIA, IIIB, or IIIC with delayed healing', 'http://independent.co.uk'),
('12', '2', 'Divape', 'Nondisp fx of hook pro of hamate bone, unsp wrist, sequela', 'Nondisplaced fracture of hook process of hamate [unciform] bone, unspecified wrist, sequela', 'http://businessinsider.com'),
('13', '3', 'Ainyx', 'Unspecified open wound of right eyelid and periocular area', 'Unspecified open wound of right eyelid and periocular area', 'http://chronoengine.com'),
('14', '4', 'Realfire', 'Anterior spinal artery compression syndromes, site unsp', 'Anterior spinal artery compression syndromes, site unspecified', 'https://lycos.com'),
('15', '5', 'Feedbug', 'Disp fx of shaft of metacarpal bone, subs for fx w nonunion', 'Displaced fracture of shaft of other metacarpal bone, subsequent encounter for fracture with nonunion', 'https://posterous.com'),
('16', '6', 'Yodoo', 'Salter-Harris Type III physeal fracture of right calcaneus', 'Salter-Harris Type III physeal fracture of right calcaneus', 'https://surveymonkey.com'),
('17', '7', 'Buzzdog', 'Postpartum thyroiditis', 'Postpartum thyroiditis', 'http://flickr.com'),
('18', '8', 'Mydeo', 'Scombroid fish poisoning', 'Scombroid fish poisoning', 'http://linkedin.com'),
('19', '9', 'Edgeclub', 'Unsp fx upper end of right ulna, init for opn fx type I/2', 'Unspecified fracture of upper end of right ulna, initial encounter for open fracture type I or II', 'https://ustream.tv'),
('20', '10', 'Thoughtblab', 'Myotonic chondrodystrophy', 'Myotonic chondrodystrophy', 'http://deliciousdays.com');

insert into `jobListing` (`jobListingId`, `recruiterId`, `companyId`, `jobTitle`, `description`, `startDate`, `endDate`, `hourlyWage`, `skills`, `location`, `deleted`, `datePosted`) values 
('job_1', '1', '11', 'Marketing Manager', 'Marketing Manager role at Skivee, focusing on Supply Chain Management.', '2024-11-25', '2025-09-03', 43, 'Marketing Strategies, SEO', 'Miami, FL', False, '2024-11-25T05:17:41.948983'),
('job_2', '4', '5', 'Marketing Manager', 'Marketing Manager role at Divanoodle, focusing on Supply Chain Management.', '2024-11-25', '2025-06-26', 28, 'Python, SQL, Tableau', 'San Francisco, CA', False, '2024-11-25T05:17:41.949003'),
('job_3', '0', '8', 'Graphic Designer', 'Graphic Designer role at Twitterwire, focusing on Recruitment.', '2024-11-25', '2025-11-25', 30, 'Supply Chain Management', 'Los Angeles, CA', False, '2024-11-25T05:17:41.949020'),
('job_4', '8', '20', 'Financial Analyst', 'Financial Analyst role at Thoughtblab, focusing on Financial Modeling.', '2024-11-25', '2025-03-24', 35, 'Customer Relationship Management', 'Miami, FL', False, '2024-11-25T05:17:41.949037'),
('job_5', '4', '16', 'Data Analyst', 'Data Analyst role at Yodoo, focusing on Recruitment.', '2024-11-25', '2025-06-11', 44, 'Python, SQL, Tableau', 'Miami, FL', True, '2024-11-25T05:17:41.949047'),
('job_6', '5', '11', 'Software Engineer', 'Software Engineer role at Skivee, focusing on Customer Relationship Management.', '2024-11-25', '2025-04-16', 49, 'Marketing Strategies, SEO', 'Boston, MA', True, '2024-11-25T05:17:41.949056'),
('job_7', '6', '12', 'Operations Manager', 'Operations Manager role at Divape, focusing on Supply Chain Management.', '2024-11-25', '2025-08-11', 29, 'Project Management, Agile', 'Chicago, IL', False, '2024-11-25T05:17:41.949065'),
('job_8', '7', '5', 'Graphic Designer', 'Graphic Designer role at Divanoodle, focusing on Adobe Photoshop.', '2024-11-25', '2025-10-08', 42, 'Customer Relationship Management', 'Denver, CO', False, '2024-11-25T05:17:41.949078'),
('job_9', '6', '4', 'Project Coordinator', 'Project Coordinator role at Realcube, focusing on Supply Chain Management.', '2024-11-25', '2025-11-15', 39, 'Project Management, Agile', 'Boston, MA', False, '2024-11-25T05:17:41.949088'),
('job_10', '3', '19', 'Financial Analyst', 'Financial Analyst role at Edgeclub, focusing on Supply Chain Management.', '2024-11-25', '2025-06-19', 36, 'Financial Modeling, Excel', 'Los Angeles, CA', False, '2024-11-25T05:17:41.949097'),
('job_11', '6', '6', 'Data Analyst', 'Data Analyst role at Tazzy, focusing on Marketing Strategies.', '2024-11-25', '2025-08-05', 27, 'Financial Modeling, Excel', 'Austin, TX', True, '2024-11-25T05:17:41.949106'),
('job_12', '8', '14', 'HR Specialist', 'HR Specialist role at Realfire, focusing on Python.', '2024-11-25', '2025-09-30', 25, 'Recruitment, Payroll', 'Miami, FL', False, '2024-11-25T05:17:41.949115'),
('job_13', '8', '16', 'Project Coordinator', 'Project Coordinator role at Yodoo, focusing on Adobe Photoshop.', '2024-11-25', '2025-09-21', 40, 'Marketing Strategies, SEO', 'Seattle, WA', False, '2024-11-25T05:17:41.949124'),
('job_14', '8', '13', 'Data Analyst', 'Data Analyst role at Ainyx, focusing on Project Management.', '2024-11-25', '2025-10-04', 48, 'Adobe Photoshop, Illustrator', 'New York, NY', False, '2024-11-25T05:17:41.949132'),
('job_15', '1', '2', 'Sales Executive', 'Sales Executive role at Cogilith, focusing on UI/UX Design.', '2024-11-25', '2025-03-08', 37, 'Recruitment, Payroll', 'Seattle, WA', True, '2024-11-25T05:17:41.949141'),
('job_16', '8', '17', 'Software Engineer', 'Software Engineer role at Buzzdog, focusing on Marketing Strategies.', '2024-11-25', '2025-05-26', 15, 'Adobe Photoshop, Illustrator', 'Austin, TX', False, '2024-11-25T05:17:41.949150'),
('job_17', '2', '20', 'Sales Executive', 'Sales Executive role at Thoughtblab, focusing on Recruitment.', '2024-11-25', '2025-09-23', 29, 'Recruitment, Payroll', 'Chicago, IL', False, '2024-11-25T05:17:41.949158'),
('job_18', '5', '17', 'Sales Executive', 'Sales Executive role at Buzzdog, focusing on Financial Modeling.', '2024-11-25', '2025-10-27', 16, 'UI/UX Design, Figma', 'Los Angeles, CA', False, '2024-11-25T05:17:41.949174'),
('job_19', '6', '5', 'Financial Analyst', 'Financial Analyst role at Divanoodle, focusing on UI/UX Design.', '2024-11-25', '2025-05-13', 29, 'Adobe Photoshop, Illustrator', 'Seattle, WA', False, '2024-11-25T05:17:41.949183'),
('job_20', '3', '2', 'Project Coordinator', 'Project Coordinator role at Cogilith, focusing on Java.', '2024-11-25', '2025-04-01', 41, 'Java, Spring Boot', 'New York, NY', False, '2024-11-25T05:17:41.949193'),
('job_21', '5', '7', 'Project Coordinator', 'Project Coordinator role at Photobean, focusing on Project Management.', '2024-11-25', '2025-06-04', 48, 'Java, Spring Boot', 'San Francisco, CA', False, '2024-11-25T05:17:41.949210'),
('job_22', '4', '10', 'Product Designer', 'Product Designer role at JumpXS, focusing on Python.', '2024-11-25', '2025-03-07', 45, 'Customer Relationship Management', 'New York, NY', False, '2024-11-25T05:17:41.949224'),
('job_23', '8', '10', 'Data Analyst', 'Data Analyst role at JumpXS, focusing on Python.', '2024-11-25', '2025-09-19', 30, 'Java, Spring Boot', 'New York, NY', False, '2024-11-25T05:17:41.949238'),
('job_24', '4', '13', 'Project Coordinator', 'Project Coordinator role at Ainyx, focusing on Adobe Photoshop.', '2024-11-25', '2025-06-16', 48, 'Customer Relationship Management', 'Atlanta, GA', False, '2024-11-25T05:17:41.949252'),
('job_25', '3', '14', 'Product Designer', 'Product Designer role at Realfire, focusing on Financial Modeling.', '2024-11-25', '2025-05-22', 41, 'Financial Modeling, Excel', 'Miami, FL', False, '2024-11-25T05:17:41.949262'),
('job_26', '4', '9', 'Operations Manager', 'Operations Manager role at Babblestorm, focusing on Recruitment.', '2024-11-25', '2025-09-07', 33, 'Java, Spring Boot', 'Boston, MA', False, '2024-11-25T05:17:41.949270'),
('job_27', '0', '8', 'Operations Manager', 'Operations Manager role at Twitterwire, focusing on Adobe Photoshop.', '2024-11-25', '2025-11-11', 50, 'UI/UX Design, Figma', 'San Francisco, CA', False, '2024-11-25T05:17:41.949278'),
('job_28', '1', '5', 'HR Specialist', 'HR Specialist role at Divanoodle, focusing on UI/UX Design.', '2024-11-25', '2025-08-07', 19, 'Financial Modeling, Excel', 'Atlanta, GA', False, '2024-11-25T05:17:41.949286'),
('job_29', '2', '11', 'Marketing Manager', 'Marketing Manager role at Skivee, focusing on Python.', '2024-11-25', '2025-10-03', 16, 'Java, Spring Boot', 'Boston, MA', False, '2024-11-25T05:17:41.949294'),
('job_30', '7', '9', 'Graphic Designer', 'Graphic Designer role at Babblestorm, focusing on Recruitment.', '2024-11-25', '2025-09-09', 36, 'Marketing Strategies, SEO', 'Miami, FL', False, '2024-11-25T05:17:41.949304'),
('job_31', '0', '8', 'Marketing Manager', 'Marketing Manager role at Twitterwire, focusing on UI/UX Design.', '2024-11-25', '2025-08-31', 48, 'Project Management, Agile', 'New York, NY', False, '2024-11-25T05:17:41.949317'),
('job_32', '5', '15', 'Marketing Manager', 'Marketing Manager role at Feedbug, focusing on Java.', '2024-11-25', '2025-07-09', 34, 'Marketing Strategies, SEO', 'Boston, MA', False, '2024-11-25T05:17:41.949331'),
('job_33', '8', '18', 'Operations Manager', 'Operations Manager role at Mydeo, focusing on Java.', '2024-11-25', '2025-07-08', 37, 'Project Management, Agile', 'Atlanta, GA', False, '2024-11-25T05:17:41.949344'),
('job_34', '4', '13', 'Graphic Designer', 'Graphic Designer role at Ainyx, focusing on Supply Chain Management.', '2024-11-25', '2025-08-27', 35, 'Marketing Strategies, SEO', 'Miami, FL', False, '2024-11-25T05:17:41.949358'),
('job_35', '10', '7', 'HR Specialist', 'HR Specialist role at Photobean, focusing on UI/UX Design.', '2024-11-25', '2025-11-06', 39, 'UI/UX Design, Figma', 'Miami, FL', False, '2024-11-25T05:17:41.949373'),
('job_36', '5', '3', 'Operations Manager', 'Operations Manager role at Shufflester, focusing on UI/UX Design.', '2024-11-25', '2025-11-01', 43, 'Python, SQL, Tableau', 'Austin, TX', False, '2024-11-25T05:17:41.949381'),
('job_37', '5', '1', 'Project Coordinator', 'Project Coordinator role at Dablist, focusing on Java.', '2024-11-25', '2025-05-06', 40, 'Python, SQL, Tableau', 'Miami, FL', False, '2024-11-25T05:17:41.949389'),
('job_38', '9', '5', 'Marketing Manager', 'Marketing Manager role at Divanoodle, focusing on Project Management.', '2024-11-25', '2025-05-31', 50, 'Project Management, Agile', 'Atlanta, GA', False, '2024-11-25T05:17:41.949401'),
('job_39', '5', '2', 'Data Analyst', 'Data Analyst role at Cogilith, focusing on Java.', '2024-11-25', '2025-02-27', 45, 'Python, SQL, Tableau', 'Austin, TX', False, '2024-11-25T05:17:41.949415'),
('job_40', '8', '16', 'Sales Executive', 'Sales Executive role at Yodoo, focusing on Financial Modeling.', '2024-11-25', '2025-11-13', 41, 'Python, SQL, Tableau', 'Seattle, WA', False, '2024-11-25T05:17:41.949425'),
('job_41', '9', '4', 'Marketing Manager', 'Marketing Manager role at Realcube, focusing on Customer Relationship Management.', '2024-11-25', '2025-05-12', 37, 'Python, SQL, Tableau', 'Denver, CO', False, '2024-11-25T05:17:41.949436'),
('job_42', '2', '14', 'Product Designer', 'Product Designer role at Realfire, focusing on Adobe Photoshop.', '2024-11-25', '2025-05-16', 27, 'Project Management, Agile', 'Seattle, WA', False, '2024-11-25T05:17:41.949455'),
('job_43', '10', '3', 'Financial Analyst', 'Financial Analyst role at Shufflester, focusing on UI/UX Design.', '2024-11-25', '2025-09-13', 28, 'Project Management, Agile', 'San Francisco, CA', False, '2024-11-25T05:17:41.949469'),
('job_44', '10', '10', 'Graphic Designer', 'Graphic Designer role at JumpXS, focusing on Python.', '2024-11-25', '2025-10-04', 16, 'Python, SQL, Tableau', 'New York, NY', False, '2024-11-25T05:17:41.949483'),
('job_45', '8', '12', 'Financial Analyst', 'Financial Analyst role at Divape, focusing on Financial Modeling.', '2024-11-25', '2025-04-30', 46, 'Financial Modeling, Excel', 'New York, NY', False, '2024-11-25T05:17:41.949490'),
('job_46', '10', '20', 'Product Designer', 'Product Designer role at Thoughtblab, focusing on Python.', '2024-11-25', '2025-09-14', 50, 'Financial Modeling, Excel', 'Boston, MA', False, '2024-11-25T05:17:41.949498'),
('job_47', '7', '20', 'Data Analyst', 'Data Analyst role at Thoughtblab, focusing on Supply Chain Management.', '2024-11-25', '2025-03-28', 37, 'Supply Chain Management', 'Seattle, WA', False, '2024-11-25T05:17:41.949506'),
('job_48', '2', '12', 'Project Coordinator', 'Project Coordinator role at Divape, focusing on Supply Chain Management.', '2024-11-25', '2025-10-12', 15, 'Adobe Photoshop, Illustrator', 'San Francisco, CA', False, '2024-11-25T05:17:41.949514'),
('job_49', '8', '5', 'Sales Executive', 'Sales Executive role at Divanoodle, focusing on Recruitment.', '2024-11-25', '2025-05-24', 46, 'Financial Modeling, Excel', 'Atlanta, GA', False, '2024-11-25T05:17:41.949522'),
('job_50', '2', '2', 'Data Analyst', 'Data Analyst role at Cogilith, focusing on Customer Relationship Management.', '2024-11-25', '2025-03-08', 17, 'Python, SQL, Tableau', 'San Francisco, CA', False, '2024-11-25T05:17:41.949531');

insert into `review` (`reviewId`, `jobListingId`, `studentId`, `anonymous`, `description`, `jobSatisfaction`, `hourlyWage`, `deleted`, `datePosted`) values 
('review_1', 'job_31', '100', False, 'The tasks were repetitive, but pay was decent.', 1, 27, False, '2024-11-25T05:23:24.598294'),
('review_2', 'job_24', '100', True, 'Supportive team and good work-life balance.', 5, 27, True, '2024-11-25T05:23:24.598308'),
('review_3', 'job_11', '100', False, 'Pay was below industry standard, but good learning opportunities.', 1, 28, False, '2024-11-25T05:23:24.598314'),
('review_4', 'job_13', '100', True, 'Loved the companys culture and the projects.', 4, 22, True, '2024-11-25T05:23:24.598320'),
('review_5', 'job_11', '130', True, 'Supportive team and good work-life balance.', 5, 40, False, '2024-11-25T05:23:24.598326'),
('review_6', 'job_26', '101', False, 'The tasks were repetitive, but pay was decent.', 1, 44, False, '2024-11-25T05:23:24.598332'),
('review_7', 'job_15', '103', False, 'The tasks were repetitive, but pay was decent.', 2, 21, False, '2024-11-25T05:23:24.598337'),
('review_8', 'job_22', '126', False, 'Flexible work hours and a good mentor.', 2, 50, False, '2024-11-25T05:23:24.598347'),
('review_9', 'job_20', '105', False, 'Challenging but rewarding job.', 1, 35, False, '2024-11-25T05:23:24.598354'),
('review_10', 'job_44', '115', False, 'Challenging but rewarding job.', 1, 28, False, '2024-11-25T05:23:24.598360'),
('review_11', 'job_50', '113', True, 'The job was not as described, but the experience was okay.', 2, 22, False, '2024-11-25T05:23:24.598366'),
('review_12', 'job_25', '101', False, 'Pay was below industry standard, but good learning opportunities.', 4, 33, False, '2024-11-25T05:23:24.598372'),
('review_13', 'job_11', '108', False, 'Challenging but rewarding job.', 5, 45, False, '2024-11-25T05:23:24.598377'),
('review_14', 'job_48', '117', False, 'Challenging but rewarding job.', 4, 50, False, '2024-11-25T05:23:24.598383'),
('review_15', 'job_11', '113', True, 'Flexible work hours and a good mentor.', 4, 38, False, '2024-11-25T05:23:24.598389'),
('review_16', 'job_18', '103', True, 'Loved the companys culture and the projects.', 1, 28, False, '2024-11-25T05:23:24.598394'),
('review_17', 'job_38', '108', True, 'Loved the companys culture and the projects.', 1, 31, True, '2024-11-25T05:23:24.598399'),
('review_18', 'job_17', '129', False, 'Great experience, learned a lot!', 5, 29, False, '2024-11-25T05:23:24.598413'),
('review_19', 'job_27', '129', False, 'The tasks were repetitive, but pay was decent.', 5, 43, False, '2024-11-25T05:23:24.598419'),
('review_20', 'job_8', '112', True, 'Tough environment but great for skill development.', 1, 32, False, '2024-11-25T05:23:24.598424'),
('review_21', 'job_42', '106', True, 'High expectations but good rewards.', 5, 44, False, '2024-11-25T05:23:24.598430'),
('review_22', 'job_6', '102', False, 'Loved the companys culture and the projects.', 2, 37, False, '2024-11-25T05:23:24.598435'),
('review_23', 'job_49', '115', True, 'Loved the companys culture and the projects.', 1, 20, False, '2024-11-25T05:23:24.598445'),
('review_24', 'job_8', '127', False, 'Flexible work hours and a good mentor.', 2, 32, False, '2024-11-25T05:23:24.598454'),
('review_25', 'job_14', '123', True, 'Tough environment but great for skill development.', 5, 34, False, '2024-11-25T05:23:24.598463'),
('review_26', 'job_9', '111', False, 'Tough environment but great for skill development.', 1, 33, False, '2024-11-25T05:23:24.598473'),
('review_27', 'job_18', '130', True, 'Tough environment but great for skill development.', 5, 40, True, '2024-11-25T05:23:24.598494'),
('review_28', 'job_27', '108', False, 'Great experience, learned a lot!', 1, 30, False, '2024-11-25T05:23:24.598504'),
('review_29', 'job_43', '101', True, 'Tough environment but great for skill development.', 4, 15, False, '2024-11-25T05:23:24.598513'),
('review_30', 'job_5', '101', False, 'The tasks were repetitive, but pay was decent.', 3, 31, False, '2024-11-25T05:23:24.598524'),
('review_31', 'job_27', '122', False, 'The job was not as described, but the experience was okay.', 4, 42, False, '2024-11-25T05:23:24.598533'),
('review_32', 'job_22', '118', False, 'Great experience, learned a lot!', 4, 22, False, '2024-11-25T05:23:24.598543'),
('review_33', 'job_41', '125', False, 'Great experience, learned a lot!', 3, 19, False, '2024-11-25T05:23:24.598551'),
('review_34', 'job_3', '102', False, 'The job was not as described, but the experience was okay.', 1, 37, False, '2024-11-25T05:23:24.598560'),
('review_35', 'job_20', '101', True, 'Loved the companys culture and the projects.', 1, 22, False, '2024-11-25T05:23:24.598569'),
('review_36', 'job_33', '111', False, 'High expectations but good rewards.', 3, 29, False, '2024-11-25T05:23:24.598578'),
('review_37', 'job_39', '120', True, 'High expectations but good rewards.', 1, 22, False, '2024-11-25T05:23:24.598588'),
('review_38', 'job_27', '125', True, 'Tough environment but great for skill development.', 2, 20, False, '2024-11-25T05:23:24.598595'),
('review_39', 'job_34', '102', False, 'Challenging but rewarding job.', 4, 40, False, '2024-11-25T05:23:24.598600'),
('review_40', 'job_16', '120', False, 'Tough environment but great for skill development.', 4, 21, False, '2024-11-25T05:23:24.598606'),
('review_41', 'job_45', '109', False, 'Tough environment but great for skill development.', 4, 35, False, '2024-11-25T05:23:24.598611'),
('review_42', 'job_31', '103', False, 'Tough environment but great for skill development.', 5, 34, False, '2024-11-25T05:23:24.598617'),
('review_43', 'job_38', '130', True, 'Great experience, learned a lot!', 1, 37, False, '2024-11-25T05:23:24.598623'),
('review_44', 'job_12', '123', True, 'Challenging but rewarding job.', 5, 44, False, '2024-11-25T05:23:24.598628'),
('review_45', 'job_5', '125', False, 'The job was not as described, but the experience was okay.', 5, 21, False, '2024-11-25T05:23:24.598633'),
('review_46', 'job_29', '129', True, 'High expectations but good rewards.', 1, 39, False, '2024-11-25T05:23:24.598638'),
('review_47', 'job_23', '125', True, 'Supportive team and good work-life balance.', 2, 47, False, '2024-11-25T05:23:24.598643'),
('review_48', 'job_25', '115', False, 'Tough environment but great for skill development.', 3, 29, False, '2024-11-25T05:23:24.598648'),
('review_49', 'job_18', '109', True, 'Flexible work hours and a good mentor.', 4, 26, False, '2024-11-25T05:23:24.598653'),
('review_50', 'job_18', '118', False, 'Great experience, learned a lot!', 4, 31, False, '2024-11-25T05:23:24.598658'),
('review_51', 'job_30', '129', True, 'High expectations but good rewards.', 5, 36, False, '2024-11-25T05:23:24.598664'),
('review_52', 'job_43', '110', False, 'The tasks were repetitive, but pay was decent.', 5, 16, False, '2024-11-25T05:23:24.598669'),
('review_53', 'job_25', '103', False, 'Supportive team and good work-life balance.', 2, 15, False, '2024-11-25T05:23:24.598678'),
('review_54', 'job_11', '120', False, 'The tasks were repetitive, but pay was decent.', 2, 46, False, '2024-11-25T05:23:24.599151'),
('review_55', 'job_22', '121', True, 'Great experience, learned a lot!', 4, 34, False, '2024-11-25T05:23:24.599189'),
('review_56', 'job_21', '116', True, 'The job was not as described, but the experience was okay.', 5, 21, False, '2024-11-25T05:23:24.599199'),
('review_57', 'job_45', '102', False, 'Pay was below industry standard, but good learning opportunities.', 1, 49, False, '2024-11-25T05:23:24.599208'),
('review_58', 'job_30', '127', False, 'Loved the companys culture and the projects.', 1, 47, False, '2024-11-25T05:23:24.599217'),
('review_59', 'job_21', '126', False, 'The tasks were repetitive, but pay was decent.', 5, 36, False, '2024-11-25T05:23:24.599238'),
('review_60', 'job_14', '115', True, 'Flexible work hours and a good mentor.', 4, 48, False, '2024-11-25T05:23:24.599252'),
('review_61', 'job_44', '103', True, 'Supportive team and good work-life balance.', 1, 43, False, '2024-11-25T05:23:24.599264'),
('review_62', 'job_25', '124', False, 'Loved the companys culture and the projects.', 4, 38, False, '2024-11-25T05:23:24.599274'),
('review_63', 'job_49', '115', True, 'High expectations but good rewards.', 5, 39, False, '2024-11-25T05:23:24.599285'),
('review_64', 'job_30', '117', False, 'Flexible work hours and a good mentor.', 4, 20, False, '2024-11-25T05:23:24.599316'),
('review_65', 'job_37', '116', False, 'Pay was below industry standard, but good learning opportunities.', 4, 44, False, '2024-11-25T05:23:24.599327'),
('review_66', 'job_2', '130', True, 'High expectations but good rewards.', 5, 47, False, '2024-11-25T05:23:24.599339'),
('review_67', 'job_33', '123', False, 'High expectations but good rewards.', 2, 19, False, '2024-11-25T05:23:24.599349'),
('review_68', 'job_38', '113', False, 'Loved the companys culture and the projects.', 3, 40, False, '2024-11-25T05:23:24.599359'),
('review_69', 'job_22', '111', True, 'Great experience, learned a lot!', 1, 40, False, '2024-11-25T05:23:24.599370'),
('review_70', 'job_3', '122', False, 'The job was not as described, but the experience was okay.', 5, 23, False, '2024-11-25T05:23:24.599380'),
('review_71', 'job_41', '121', True, 'Loved the companys culture and the projects.', 1, 29, False, '2024-11-25T05:23:24.599390'),
('review_72', 'job_24', '126', True, 'Challenging but rewarding job.', 4, 16, False, '2024-11-25T05:23:24.599401'),
('review_73', 'job_27', '121', True, 'Loved the companys culture and the projects.', 3, 19, False, '2024-11-25T05:23:24.599414'),
('review_74', 'job_13', '128', False, 'Supportive team and good work-life balance.', 4, 40, False, '2024-11-25T05:23:24.599424'),
('review_75', 'job_6', '113', True, 'Great experience, learned a lot!', 1, 43, False, '2024-11-25T05:23:24.599434'),
('review_76', 'job_18', '105', True, 'Pay was below industry standard, but good learning opportunities.', 1, 19, False, '2024-11-25T05:23:24.599457'),
('review_77', 'job_15', '102', False, 'Tough environment but great for skill development.', 5, 38, False, '2024-11-25T05:23:24.599469'),
('review_78', 'job_34', '107', True, 'Challenging but rewarding job.', 2, 28, False, '2024-11-25T05:23:24.599479'),
('review_79', 'job_46', '130', False, 'Great experience, learned a lot!', 5, 19, False, '2024-11-25T05:23:24.599490'),
('review_80', 'job_46', '123', False, 'Supportive team and good work-life balance.', 5, 48, False, '2024-11-25T05:23:24.599499'),
('review_81', 'job_25', '123', True, 'The tasks were repetitive, but pay was decent.', 1, 19, False, '2024-11-25T05:23:24.599509'),
('review_82', 'job_49', '102', False, 'The tasks were repetitive, but pay was decent.', 3, 26, False, '2024-11-25T05:23:24.599519'),
('review_83', 'job_37', '101', False, 'Loved the companys culture and the projects.', 5, 23, False, '2024-11-25T05:23:24.599529'),
('review_84', 'job_44', '108', True, 'Supportive team and good work-life balance.', 5, 50, False, '2024-11-25T05:23:24.599539'),
('review_85', 'job_45', '104', True, 'Great experience, learned a lot!', 3, 21, False, '2024-11-25T05:23:24.599561'),
('review_86', 'job_15', '111', True, 'Loved the companys culture and the projects.', 2, 44, False, '2024-11-25T05:23:24.599572'),
('review_87', 'job_16', '126', False, 'Tough environment but great for skill development.', 5, 45, False, '2024-11-25T05:23:24.599582'),
('review_88', 'job_32', '104', False, 'The job was not as described, but the experience was okay.', 5, 16, False, '2024-11-25T05:23:24.599592'),
('review_89', 'job_23', '124', False, 'High expectations but good rewards.', 1, 45, False, '2024-11-25T05:23:24.599602'),
('review_90', 'job_6', '115', False, 'Flexible work hours and a good mentor.', 4, 21, False, '2024-11-25T05:23:24.599612'),
('review_91', 'job_1', '112', False, 'Pay was below industry standard, but good learning opportunities.', 1, 45, False, '2024-11-25T05:23:24.599627'),
('review_92', 'job_14', '112', False, 'The tasks were repetitive, but pay was decent.', 5, 17, False, '2024-11-25T05:23:24.599647'),
('review_93', 'job_24', '126', False, 'Supportive team and good work-life balance.', 2, 42, False, '2024-11-25T05:23:24.599655'),
('review_94', 'job_24', '111', False, 'Tough environment but great for skill development.', 1, 31, False, '2024-11-25T05:23:24.599667'),
('review_95', 'job_30', '108', True, 'Flexible work hours and a good mentor.', 5, 37, False, '2024-11-25T05:23:24.599677'),
('review_96', 'job_18', '111', True, 'Pay was below industry standard, but good learning opportunities.', 3, 50, False, '2024-11-25T05:23:24.599687'),
('review_97', 'job_20', '114', False, 'Flexible work hours and a good mentor.', 4, 17, False, '2024-11-25T05:23:24.599698'),
('review_98', 'job_10', '110', False, 'Loved the companys culture and the projects.', 4, 28, False, '2024-11-25T05:23:24.599707'),
('review_99', 'job_3', '116', False, 'Pay was below industry standard, but good learning opportunities.', 5, 27, False, '2024-11-25T05:23:24.599717'),
('review_100', 'job_40', '130', False, 'Pay was below industry standard, but good learning opportunities.', 1, 36, False, '2024-11-25T05:23:24.599728');

INSERT INTO `favoriteJobListings` (`studentId`, `jobListingId`)
VALUES ('100', 'job_1'),
       ('100', 'job_2');

INSERT INTO `sentJobListings` (`jobListingId`, `studentId`, `advisorId`)
VALUES ('job_1', '100', '1'),
        ('job_2', '100', '1'),
        ('job_3', '100', '1'),
        ('job_3', '101', '1'),
        ('job_4', '101', '1'),
        ('job_3', '111', '1'),
        ('job_3', '121', '1');

INSERT INTO `flaggedReview` (`reviewId`, `flaggedById`, `reason`, `dateFlagged`)
VALUES ('review_4', '0', 'Inappropriate language', '2024-11-25T05:23:24.599768'),
       ('review_5', '0', 'Inappropriate language', '2024-11-25T05:23:24.599778');
