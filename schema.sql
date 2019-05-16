create table Users(uid serial primary key, first_name varchar(20), last_name varchar(30), phone char(10), email varchar(50), password varchar(20));

create table ContactList(uid integer references Users(uid), cid integer references Users(uid),
primary key(uid, cid));

create table Message(mid serial primary key, image varchar(255), text varchar(140),
date char(10), uid integer references Users(uid), gid integer references ChatGroup(gid), 
oid integer references Message(mid));

create table Likes(uid integer references Users(uid), mid integer references Message(mid),
date char(10),  primary key(uid, mid));

create table Dislikes(uid integer references User(suid), mid integer references Message(mid),
date char(10), primary key(uid, mid));

create table ChatGroup(gid serial primary key, gname varchar(20), uid integer references Users(uid));

create table isMember(uid integer references Users(uid), gid integer references ChatGroup(gid),
primary key(uid, gid));

create table Hashtag(hid serial primary key, tag varchar(20));

create table Tagged(hid integer references Hashtag(hid), mid integer references Message(mid),
primary key(hid, mid));
