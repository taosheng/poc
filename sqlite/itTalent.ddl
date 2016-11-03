CREATE TABLE talent(
    ID char(50) primary key,
    name TEXT not null,
    first_name char(50),
    last_name  char(50),
    cell_phone TEXT,
    email TEXT,
    birth_year INTEGER,
    birth_date TEXT,
    self_skill_desc,
    desc TEXT,
);

CREATE TABLE talent_history(
    talent_ID char(50),
    history_ID char(50),
    confident_level_ID char(10),
    desc TEXT,
    PRIMARY KEY(talent_ID, history_ID),
    FOREIGN KEY(talent_ID) REFERENCES talent(ID),
    FOREIGN KEY(confident_level_ID) REFERENCES confident_leve(ID)
);

CREATE TABLE confident_level(
    ID char(10) primary key,
    desc TEXT
);

CREATE TABLE skill(
    ID char(10) primary key,
    short_desc char(100),
    desc TEXT
);

INSERT INTO skill values("P001","programming expert","expert level of at least one computing language");
INSERT INTO skill values("P002","java master","java programming master!");
INSERT INTO skill values("P003","python master","python programming master!");
INSERT INTO skill values("S001","software design","know how to design a software");
INSERT INTO skill values("X001","manager","know how to lead a team");
