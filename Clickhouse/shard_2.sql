--commented command to access in conteiner where should insert command below - todo in terminal, without python typing
--docker exec -it clickhouse-node3 bash
--clickhouse-client
CREATE DATABASE shard;
CREATE DATABASE replica;
CREATE TABLE shard.film_view (id UUID, user UUID, film UUID, progress_time Int64) Engine=ReplicatedMergeTree('/clickhouse/tables/shard2/film_view', 'replica_1') PARTITION BY film ORDER BY id;
CREATE TABLE replica.film_view (id UUID, user UUID, film UUID, progress_time Int64) Engine=ReplicatedMergeTree('/clickhouse/tables/shard1/film_view', 'replica_2') PARTITION BY film ORDER BY id;
CREATE TABLE default.film_view (id UUID, user UUID, film UUID, progress_time Int64) ENGINE = Distributed('company_cluster', '', film_view, rand());