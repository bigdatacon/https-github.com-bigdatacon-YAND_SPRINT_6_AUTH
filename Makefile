build:
	docker network create movies_network || true
	docker-compose up -d --build
	docker-compose -f ./auth_api/docker-compose.yml up -d --build

up:
	docker network create movies_network || true
	docker-compose up -d
	docker-compose -f ./auth_api/docker-compose.yml up -d

down:
	docker-compose down --remove-orphans
	docker-compose -f ./auth_api/docker-compose.yml down --remove-orphans
	docker network rm movies_network

stop:
	docker-compose stop
	docker-compose -f ./auth_api/docker-compose.yml stop



# superuser:
# 	docker-compose exec auth_flask flask user create admin admin@localhost 123
#
# logs:
# 	docker-compose logs
#
# up-tests:
# 	docker-compose -f ./tests/functional/docker-compose.yml up --build -d
# 	docker-compose -f ./tests/functional/docker-compose.yml exec auth_flask flask user create admin admin@localhost 123
# 	docker-compose -f ./tests/functional/docker-compose.yml exec auth_flask pytest .
#
# run-tests:
# 	docker-compose -f ./tests/functional/docker-compose.yml exec auth_flask pytest .
#
# down-tests:
# 	docker-compose -f ./tests/functional/docker-compose.yml down --remove-orphans
#
# logs-tests:
# 	docker-compose -f ./tests/functional/docker-compose.yml logs