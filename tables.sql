CREATE DATABASE magicwm

USE magicwm

CREATE TABLE matters (
    matterId INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    matterName VARCHAR(50),
    requestingClientId INTEGER,
    priorityId INTEGER,
    timeNeeded INTEGER, --time in minutes
    timeLogged INTEGER, --in minutes
    isBillable TINYINT,
    deadline INTEGER --store epoch timestmp
)

CREATE TABLE tasks (
    taskId INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    matterId INTEGER,
    taskName VARCHAR(50),
    taskAssigneeId INTEGER,
    taskStatusId INTEGER,
    timeLogged INTEGER,
    timeNeeded INTEGER,
    priorityId INTEGER,
    specialisationNeededId INTEGER
)

CREATE TABLE users (
    userid INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    username VARCHAR(50),
    passwordHash VARCHAR(500),
    timeCreated INTEGER
)

CREATE TABLE userssecuritygroups (
    entryid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    userid INT,
    groupId INT
)

CREATE TABLE securitygroups (
    groupid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	groupname VARCHAR(50)
)

CREATE TABLE groupspermissions (
    entryid INT PRIMARY KEY AUTOINCRMENT NOT NULL,
	groupid INT,
	permissionname VARCHAR(50),
	permissionvalue TINYINT --might be bool/tinyint
)

CREATE TABLE clients (
    clientid INT PRIMARY KEY AUTOINCRMENT NOT NULL,
    clientname VARCHAR(50),
    clientBasePriority INT
)