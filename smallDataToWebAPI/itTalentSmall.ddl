
CREATE TABLE talent(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
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

INSERT INTO talent values(1,"radzebra","","","","redZebra@gmail.com",2011,"","master","first user for all");

CREATE TABLE tag(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    desc TEXT not null
);

INSERT INTO tag values(1,"java");
INSERT INTO tag values(2,"python");
INSERT INTO tag values(3,"perl");
INSERT INTO tag values(4,"Grid computing");
INSERT INTO tag values(5,"Cloud computing");

CREATE TABLE talent_tag(
    talent_ID INTEGER ,
    tag_ID INTEGER ,
    FOREIGN KEY(talent_ID) REFERENCES talent(ID),
    FOREIGN KEY(tag_ID) REFERENCES tag(ID)
    PRIMARY KEY(talent_ID, tag_ID)
);


