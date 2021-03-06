CREATE TABLE matters (matterId INTEGER PRIMARY KEY NOT NULL,matterName VARCHAR(50),requestingClientId INTEGER,matterDescription VARCHAR(255),priorityId INTEGER,timeNeeded INTEGER, timeLogged INTEGER, isBillable TINYINT,deadline INTEGER)
CREATE TABLE tasks (taskId INTEGER PRIMARY KEY NOT NULL,matterId INTEGER,taskName VARCHAR(50),taskAssigneeId INTEGER,taskStatusId INTEGER,timeLogged INTEGER,timeNeeded INTEGER,priorityId INTEGER,specialisationNeededId INTEGER)
CREATE TABLE users (userid INTEGER PRIMARY KEY NOT NULL,username VARCHAR(50),passwordHash VARCHAR(500),timeCreated INTEGER)
CREATE TABLE userssecuritygroups (entryid INTEGER PRIMARY KEY NOT NULL,userid INTEGER,groupId INTEGER)
CREATE TABLE securitygroups (groupid INTEGER PRIMARY KEY NOT NULL,groupname VARCHAR(50))
CREATE TABLE groupspermissions (entryid INTEGER PRIMARY KEY NOT NULL,groupid INTEGER,permissionname VARCHAR(50),permissionvalue TINYINT)
CREATE TABLE clients (clientid INTEGER PRIMARY KEY NOT NULL,clientname VARCHAR(50),clientBasePriority INTEGER)