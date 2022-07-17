create table units
(
    unit_id serial
        constraint units_pk
            primary key,
    name    text,
    symbol  text,
    enable  boolean
);

INSERT INTO units (unit_id, name, symbol, enable) VALUES (1,'testing', 't-800', true);