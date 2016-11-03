
CREATE TABLE talent(
    ID char(50) primary key,
    name TEXT not null,
    first_name char(50),
    last_name  char(50),
    cell_phone char(200),
    email char(200) not null,
    birth_year INTEGER,
    birth_date TEXT,
    self_skill_desc TEXT,
    desc TEXT
);

INSERT INTO talent values("1","radzebra","","","","redZebra@gmail.com",2011,"","master","first user for all");

CREATE TABLE tag(
    ID char(50) primary key,
    desc TEXT not null
);

INSERT INTO tag values("P0001","java");
INSERT INTO tag values("P0002","python");
INSERT INTO tag values("P0003","perl");
INSERT INTO tag values("A0001","Grid computing");
INSERT INTO tag values("A0002","Cloud computing");

CREATE TABLE talent_tag(
    talent_ID char(50),
    tag_ID char(50),
    FOREIGN KEY(talent_ID) REFERENCES talent(ID),
    FOREIGN KEY(tag_ID) REFERENCES tag(ID)
);

INSERT INTO talent_tag values("1","P0001");
INSERT INTO talent_tag values("1","P0002");
INSERT INTO talent_tag values("1","A0002");

CREATE TABLE contact(
    talent_ID char(50),
    method char(100),
    desc TEXT,
    FOREIGN KEY(talent_ID) REFERENCES talent(ID)
);

CREATE TABLE talent_story(
    talent_ID char(50),
    story_ID char(50),
    confident_level_ID char(10),
    type_ID char(10), 
    start_date char(20),
    end_date char(20),
    desc TEXT,
    PRIMARY KEY(talent_ID, story_ID),
    FOREIGN KEY(talent_ID) REFERENCES talent(ID),
    FOREIGN KEY(type_ID) REFERENCES type(ID),
    FOREIGN KEY(confident_level_ID) REFERENCES confident_leve(ID)
);

CREATE TABLE endorsement(
    ID char(50) primary key,
    talent_ID char(50),
    story_ID char(50),
    endorser_ID char(50),
    endorser_comment TEXT,
    desc TEXT 
);

CREATE TABLE confident_level(
    ID char(10) primary key,
    endorser_ID char(50),
    level integer,
    desc TEXT
);

CREATE TABLE type(
    ID char(10) primary key,
    desc TEXT
);

