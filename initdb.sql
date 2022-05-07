-- initialize database

create table cat (
    name text unique not null,
    image_url text
);

insert into cat (name, image_url)
values 
("Lil Bub", ""),
("Grumpy Cat", "")
;

