SELECT count(*) FROM stock;
DELETE FROM stock;
INSERT INTO stock
(
	s_cod,
	s_name,
	s_price,
	in_date
)
VALUES
(
	'',
	'',
	'',
	'',
)

SELECT s_code, s_name, s_price, in_date 
FROM stock
WHERE s_name = 'LG';


SELECT s_code, s_name, s_price 
FROM stock 
where s_code = '000020';

SELECT distinct_stock_oldpythonpython s_name
FROM stock; 

SELECT COUNT(s000040)
FROM stock_sync_0121; 

SELECT * FROM COLS WHERE TABLE_NAME = 'stock_sync_0121';
SHOW COLUMNS FROM stock_sync_0121;
SELECT COLUMN_NAME FROM _stock_old
WHERE TABLE_NAME = 'stock_sync_0121';

SELECT COLUMN_NAME
  FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_SCHEMA = '_stock_old' AND TABLE_NAME = 'stock_sync_0121'
  AND column_NAME != 'in_time';


SELECT s000020, s000040 FROM stock_sync_0121;
SELECT s000020, s000040, s000050, s000060, s000070, s000075, s000080, s000087, s000100, s000105
            FROM stock_sync_0121;



