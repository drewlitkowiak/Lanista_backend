create database if not exists lanista;
use lanista;

create table if not exists videos (
	video_id INT NOT NULL UNIQUE,
	creator INT NOT NULL,
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
		DEFAULT CURRENT_TIMESTAMP,
        
	INDEX (creator, age_restriction, genre, availability),
    
	PRIMARY KEY (video_id)
);

INSERT INTO videos(video_id, creator, age_restriction, genre, title,
                    runtime, advertisement, comments_enabled, stream,
                    availability, upload_date, meta_change, data_change)
			VALUES(0, 0, 0, 0, "example-0",
			0, 0, true, false,
            0, 0, default, default),
		(1, 0, 0, 0, "example-1",
		0, 0, true, false,
		0, 0, default, default);
            
            
SELECT * FROM videos;