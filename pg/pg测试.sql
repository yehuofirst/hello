CREATE TABLESPACE action_sdb  LOCATION '/home/eos/sdb'

                      List of tablespaces
         Name         |  Owner   |          Location           
----------------------+----------+-----------------------------
 eosio_space_actions  | postgres | /home/eos/sdb/eosio_actions
 eosio_space_transfer | postgres | /home/eos/eosio_transfer
 pg_default           | postgres | 
 pg_global            | postgres | 


select count(*) from pg_stat_activity;
select oid,datname from pg_database where datname = 'postgres';

select relname,relfilenode from pg_class where relname='test';

查看所有数据库大小
select pg_database.datname, pg_database_size(pg_database.datname) AS size from pg_database; 


pg_dump -h 127.0.0.1 -p 5432 -U postgres -W -F c -b -v -f omnidata.backup omnidata


pg_restore -j4 -Fc -h 127.0.0.1 -d omnidata -U postgres -p 5432 omnidata.backup


pg_dump -h 127.0.0.1 -p 5432 -U postgres -W -F c -b -v -f omnidata.backup omnidata


pg_restore -j4 -c -h 127.0.0.1 -d omnidata -U postgres -p 5432 omnidata.backup



pg_dump -h 192.168.1.179 -p 5432 -U postgres -W -F c -b -v -f /home/eos/action.sql -t actions -n eosio_log_201809 eosio


pg_restore -j4 -Fc -h 192.168.1.211 -d loadtest -U postgres -p 5432 -f /home/eos/action.sql

psql -h 192.168.1.211 -d loadtest -U postgres -p 5432 -f /home/eos/action.sql


psql -h 192.168.1.211 -d loadtest -U postgres -p 5432 -f /home/eos/block.sql

pg_dump -h 192.168.1.179 -p 5432 -U postgres -W -F c -b -v -f /home/eos/action.sql -t eosio_log_201809.actions*  eosio


----insert非常慢
pg_dump -h 192.168.1.179 -p 5432 -U postgres --inserts   -a -f /home/eos/block.sql -t eosio_log_201809.block_info  eosio
psql -h 192.168.1.211 -d loadtest -U postgres -p 5432 -f /home/eos/block.sql

-----copy非常快20秒2G,备份快还原也快
pg_dump -h 192.168.1.179 -p 5432 -U postgres  -a -f /home/eos/action.sql -t eosio_log_201809.actions_20180901  eosio
psql -h 192.168.1.211 -d bbbb -U postgres -p 5432 -f /home/eos/action.sql

导copy语句
/home/eos/pyeosloop/actions_worker --max_tasks=500 --lock=actions_all --zmq_topic=actions_all --event_whitelist=actoins --start_hash=01cde2307f58115df6b837ba19963156c597acec442d96b1eab07ce5d0b0e2d8  --logging=./config/logging/logging_01.ini --upsert_log=0  --zmq_rep_url=tcp://192.168.1.213:5552

pg外部表
1.安装fdw扩展
create extension postgres_fdw;
2.创建远程server
create server server_remote179 
FOREIGN data wrapper postgres_fdw 
OPTIONS(host '192.168.1.179', port '5432', dbname 'eosio');
3.创建用户匹配信息
create user mapping for postgres server server_remote179 options(user 'postgres',password 'postgres');
4.创建外部表
CREATE FOREIGN TABLE "eosio_log_201809"."actions_wai" (
  "createtime" timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updatetime" timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "_id" varchar(32) COLLATE "pg_catalog"."default" NOT NULL,
  "global_sequence" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "blocknum" int8 NOT NULL,
  "txid" varchar(64) COLLATE "pg_catalog"."default" NOT NULL,
  "act_digest" varchar(64) COLLATE "pg_catalog"."default" NOT NULL,
  "timestamp" timestamp(6) NOT NULL,
  "blockhash" varchar(64) COLLATE "pg_catalog"."default" NOT NULL,
  "account" varchar(16) COLLATE "pg_catalog"."default" NOT NULL,
  "name" varchar(16) COLLATE "pg_catalog"."default" NOT NULL,
  "data" jsonb NOT NULL,
  "status" varchar(16) COLLATE "pg_catalog"."default" NOT NULL,
  "receiver_account" varchar(16)[] COLLATE "pg_catalog"."default" NOT NULL,
  "date" timestamp(6) NOT NULL
)
server server_remote179 options (table_name 'actions')
;

