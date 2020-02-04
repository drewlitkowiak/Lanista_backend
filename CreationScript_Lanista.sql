create database if not exists lanista;
use lanista;

create table if not exists videos (
	creator INT NOT NULL,
    link INT NOT NULL,
    age_restriction INT,
    genre INT NOT NULL,
    title VARCHAR(255),
    runtime INT NOT NULL,
    advertisement INT NOT NULL,
    comments_enabled BOOL NOT NULL,
    stream BOOL NOT NULL,
    availability INT NOT NULL,
    upload_date INT NOT NULL,
    meta_change TIMESTAMP NOT NULL 
		DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    data_change TIMESTAMP NOT NULL
		DEFAULT CURRENT_TIMESTAMP
);
