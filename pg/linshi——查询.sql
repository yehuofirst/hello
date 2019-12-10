SELECT bnum, bhash, actions_jsonb(actions) actions FROM lua_block_actions WHERE bnum >= 25202384 and bnum <= 25202401

SELECT bnum, bhash, actions_jsonb(actions) actions FROM lua_block_actions WHERE bnum >= 25202301 and bnum <= 25202382


SELECT bnum, bhash, actions_jsonb(actions) actions FROM lua_block_actions WHERE bnum >= 25202383 and bnum <= 25202383


SELECT t1.bnum, t1.a FROM (SELECT bnum, count(bnum) a FROM t_actions WHERE bnum >= 10000000 and bnum < 20000000 GROUP BY bnum) as t1 WHERE t1.a > 1;

16928196----16928321

DELETE from t_actions_2000w WHERE bnum >= 18000001 and bnum <= 19000000

DELETE from t_actions_2000w WHERE bnum >= 18000001 and bnum <= 18100000

DELETE from t_actions_2000w WHERE bnum >= 18100001 and bnum <= 18200000

DELETE from t_actions_2000w WHERE bnum >= 18200001 and bnum <= 18300000
DELETE from t_actions_2000w WHERE bnum >= 18300001 and bnum <= 18400000;
DELETE from t_actions_2000w WHERE bnum >= 18400001 and bnum <= 18500000;
DELETE from t_actions_2000w WHERE bnum >= 18500001 and bnum <= 18600000;
DELETE from t_actions_2000w WHERE bnum >= 18600001 and bnum <= 18700000;
DELETE from t_actions_2000w WHERE bnum >= 18700001 and bnum <= 18800000;
DELETE from t_actions_2000w WHERE bnum >= 18800001 and bnum <= 18900000;
DELETE from t_actions_2000w WHERE bnum >= 18900001 and bnum <= 19000000;
