#coding:utf-8
import torndb

db = torndb.Connection(
    host="127.0.0.1:3306", 
    database="chatroom",
    user="root",
    password="123456"
    )

create_table = """

DROP TABLE IF EXISTS user;
CREATE TABLE user (
	`id` INT (11) NOT NULL AUTO_INCREMENT,
	`username` VARCHAR (255) NOT NULL,
	`password` VARCHAR (255) NOT NULL,
	`sex` bit (1) DEFAULT 1,
	`registed` datetime,
	`usertype` bit (1) DEFAULT 1,
	`phone` VARCHAR (255),
	PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS room;
CREATE TABLE room (
	`id` INT (11) NOT NULL AUTO_INCREMENT,
	`roomname` VARCHAR (255) NOT NULL,
	`created_time` datetime,
	`owner_id` INT (11) NOT NULL,
	PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS message;
CREATE TABLE message (
	`id` INT (11) NOT NULL AUTO_INCREMENT,
	`roomid` INT (11) NOT NULL,
	`msg` VARCHAR (500) NOT NULL,
	`userid` INT (11) NOT NULL,
	`have_read` tinyint(1) DEFAULT 0,
	`created_time` datetime,
	`type` tinyint(1) DEFAULT 0,
	PRIMARY KEY (`id`)
);

"""

if __name__ == '__main__':
    try:
        db.execute(create_table)
        print "ok"
    except Exception as err:
        print(err)


