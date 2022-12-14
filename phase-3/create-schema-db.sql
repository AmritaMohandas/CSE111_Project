-- SQLite
CREATE TABLE books (
    b_bookID decimal(9,0) not null,
    b_title varchar(100),
    b_firstpublished decimal(4,0) not null,
    b_type char(15) not null
);
CREATE TABLE authors (
    a_authorID decimal(9,0) not null,
    a_name varchar(50),
    a_condition char(8) not null
);
CREATE TABLE booksauthors (
    ba_bookID decimal(9,0) not null,
    ba_authorID decimal(9,0) not null
);
CREATE TABLE genres (
    g_genreID decimal(3,0) not null,
    g_name varchar(30)
);
CREATE TABLE booksgenres (
    bg_bookID decimal(9,0) not null,
    bg_genreID decimal(3,0) not null
);
CREATE TABLE publishers (
    p_publisherID decimal(3,0) not null,
    p_name varchar(50)
);
CREATE TABLE bookspublishers (
    bp_bookID decimal(9,0) not null,
    bp_publisherID decimal(3,0) not null,
    bp_isbn decimal(15,0) not null,
    bp_formatID decimal(1,0) not null,
    bp_publishyear decimal(4,0) not null
);
CREATE TABLE format (
    f_formatID decimal(1,0) not null,
    f_name char(10) not null
);
CREATE TABLE users (
    u_userID INTEGER PRIMARY KEY AUTOINCREMENT,
    u_firstname char(15) not null,
    u_lastname char(15) not null,
    u_username char(15) not null,
    u_email varchar(20),
    u_password varchar(15),
    u_category char(15) not null
);
CREATE TABLE readingstatus (
    rs_bookID decimal(9,0) not null,
    rs_userID decimal(9,0) not null,
    rs_readStatus char(20) not null
);
CREATE TABLE ratings (
    r_ratingID decimal(9,0) not null,
    r_bookID decimal(9,0) not null,
    r_userID decimal(9,0) not null,
    r_ratingValue decimal(1,0) not null
);

-- CREATE TABLE region (
--     r_regionkey decimal(2,0) not null,
--     r_name char(25) not null,
--     r_comment varchar(152)
-- );
-- CREATE TABLE nation (
--     n_nationkey decimal(3,0) not null,
--     n_name char(25) not null,
--     n_regionkey decimal(2,0) not null,
--     n_comment varchar(152)
-- );
-- CREATE TABLE part (
--     p_partkey decimal(10,0) not null,
--     p_name varchar(55) not null,
--     p_mfgr char(25) not null,
--     p_brand char(10) not null,
--     p_type varchar(25) not null,
--     p_size decimal(2,0) not null,
--     p_container char(10) not null,
--     p_retailprice decimal(6,2) not null,
--     p_comment varchar(23) not null
-- );
-- CREATE TABLE supplier (
--     s_suppkey decimal(8,0) not null,
--     s_name char(25) not null,
--     s_address varchar(40) not null,
--     s_nationkey decimal(3,0) not null,
--     s_phone char(15) not null,
--     s_acctbal decimal(7,2) not null,
--     s_comment varchar(101) not null
-- );
-- CREATE TABLE partsupp (
--     ps_partkey decimal(10,0) not null,
--     ps_suppkey decimal(8,0) not null,
--     ps_availqty decimal(5,0) not null,
--     ps_supplycost decimal(6,2) not null,
--     ps_comment varchar(199) not null
-- );
-- CREATE TABLE customer (
--     c_custkey decimal(9,0) not null,
--     c_name varchar(25) not null,
--     c_address varchar(40) not null,
--     c_nationkey decimal(3,0) not null,
--     c_phone char(15) not null,
--     c_acctbal decimal(7,2) not null,
--     c_mktsegment char(10) not null,
--     c_comment varchar(117) not null
-- );
-- CREATE TABLE orders (
--     o_orderkey decimal(12,0) not null,
--     o_custkey decimal(9,0) not null,
--     o_orderstatus char(1) not null,
--     o_totalprice decimal(8,2) not null,
--     o_orderdate date not null,
--     o_orderpriority char(15) not null,
--     o_clerk char(15) not null,
--     o_shippriority decimal(1,0) not null,
--     o_comment varchar(79) not null
-- );
-- CREATE TABLE lineitem (
--     l_orderkey decimal(12,0) not null,
--     l_partkey decimal(10,0) not null,
--     l_suppkey decimal(8,0) not null,
--     l_linenumber decimal(1,0) not null,
--     l_quantity decimal(2,0) not null,
--     l_extendedprice decimal(8,2) not null,
--     l_discount decimal(3,2) not null,
--     l_tax decimal(3,2) not null,
--     l_returnflag char(1) not null,
--     l_linestatus char(1) not null,
--     l_shipdate date not null,
--     l_commitdate date not null,
--     l_receiptdate date not null,
--     l_shipinstruct char(25) not null,
--     l_shipmode char(10) not null,
--     l_comment varchar(44) not null
-- );