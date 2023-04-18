insert into authors_2 select * from authors where Id % 2 = 0;
insert into authors_4 select * from authors where Id % 4 = 0;
insert into publication_2 select * from publication where Id % 2 = 0;
insert into publication_4 select * from publication where Id % 4 = 0;
insert into publish_2 select * from publish where Id % 2 = 0;
insert into publish_4 select * from publish where Id % 4 = 0;