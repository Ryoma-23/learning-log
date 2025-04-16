/*SELECT * FROM countries;*/
/*問題：各グループの中でFIFAランクが最も高い国と低い国のランキング番号を表示してください。*/
SELECT group_name AS グループ, MIN(ranking) AS ランキング最上位, MAX(ranking) AS ランキング最下位
FROM countries
GROUP BY group_name;

/*問題：全ゴールキーパーの平均身長、平均体重を表示してください*/
SELECT AVG(height), AVG(weight)
FROM players
WHERE position = 'GK';

/*問題：各国の平均身長を高い方から順に表示してください。ただし、FROM句はcountriesテーブルとしてください。*/
SELECT c.name, AVG(p.height)
FROM countries c
JOIN players p ON c.id = p.country_id
GROUP BY c.name
ORDER BY AVG(p.height) DESC;

/*問題：各国の平均身長を高い方から順に表示してください。ただし、FROM句はplayersテーブルとして、テーブル結合を使わず副問合せを用いてください。*/
SELECT (SELECT c.name FROM countries c WHERE c.id = p.country_id), AVG(p.height)
FROM players p
GROUP BY p.country_id
ORDER BY AVG(p.height) DESC;

/*問題：キックオフ日時と対戦国の国名をキックオフ日時の早いものから順に表示してください。*/
SELECT p.kickoff AS キックオフ時間, c1.name AS 対戦国１, c2.name AS 対戦国２
FROM pairings p
LEFT JOIN countries c1 ON p.my_country_id = c1.id
LEFT JOIN countries c2 ON p.enemy_country_id = c2.id
ORDER BY kickoff;

/*問題：すべての選手を対象として選手ごとの得点ランキングを表示してください。（SELECT句で副問合せを使うこと）*/
SELECT p.name, p.position, p.club, (SELECT COUNT(id) FROM goals g WHERE g.player_id = p.id) AS ゴール数
FROM players p
ORDER BY ゴール数 DESC;